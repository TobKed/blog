// Regression checks for the ups-and-downs theme, run against a built site.
//
//   make preview            # in another shell: builds and serves on :1314
//   node scripts/check_mobile.mjs [baseURL]
//
// Chrome will not size a desktop window below ~900px and DevTools device mode
// is not scriptable, so real phone widths come from CDP device emulation.
// Node's built-in WebSocket (>= 22) talks to Chrome directly - no dependencies.

import { spawn } from 'node:child_process';
import { mkdtempSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

const BASE = (process.argv[2] || 'http://localhost:1314').replace(/\/$/, '');
const PORT = 9444;
const CHROME = process.env.CHROME ||
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';

const profile = mkdtempSync(join(tmpdir(), 'check-mobile-'));
const chrome = spawn(CHROME, [
  '--headless=new', '--disable-gpu', `--remote-debugging-port=${PORT}`,
  '--remote-debugging-address=127.0.0.1', `--user-data-dir=${profile}`, 'about:blank',
], { stdio: 'ignore' });

process.on('exit', () => {
  chrome.kill();
  // Chrome may still be flushing the profile; a leftover temp dir is harmless,
  // and throwing here would replace the real exit code with a crash.
  try { rmSync(profile, { recursive: true, force: true }); } catch {}
});

const failures = [];
const check = (name, ok, detail) => {
  console.log(`${ok ? '  ok  ' : ' FAIL '} ${name}${ok || detail === undefined ? '' : `  (${detail})`}`);
  if (!ok) failures.push(name);
};

async function waitForChrome() {
  for (let i = 0; i < 40; i++) {
    try {
      const r = await fetch(`http://127.0.0.1:${PORT}/json`);
      const targets = await r.json();
      const page = targets.find(t => t.type === 'page');
      if (page) return page;
    } catch {}
    await new Promise(r => setTimeout(r, 250));
  }
  throw new Error('Chrome did not expose a debugging target');
}

async function session(width, height, mobile) {
  const page = await waitForChrome();
  const ws = new WebSocket(page.webSocketDebuggerUrl);
  await new Promise(r => ws.addEventListener('open', r, { once: true }));

  let id = 0;
  const pending = new Map();
  ws.addEventListener('message', ev => {
    const m = JSON.parse(ev.data);
    if (m.id && pending.has(m.id)) {
      const { resolve, reject } = pending.get(m.id);
      pending.delete(m.id);
      m.error ? reject(new Error(JSON.stringify(m.error))) : resolve(m.result);
    }
  });
  const send = (method, params = {}) => new Promise((resolve, reject) => {
    const n = ++id;
    pending.set(n, { resolve, reject });
    ws.send(JSON.stringify({ id: n, method, params }));
  });

  await send('Page.enable');
  await send('Runtime.enable');
  await send('Emulation.setDeviceMetricsOverride',
    { width, height, deviceScaleFactor: mobile ? 3 : 1, mobile });

  return {
    send,
    close: () => ws.close(),
    eval: async expr => (await send('Runtime.evaluate',
      { expression: expr, returnByValue: true, awaitPromise: true })).result.value,
    async go(path) {
      await send('Page.navigate', { url: BASE + path });
      await new Promise(r => setTimeout(r, 1800));
    },
    async tap(selector) {
      const box = await this.eval(
        `(()=>{const e=document.querySelector(${JSON.stringify(selector)});
          if(!e) return null; const r=e.getBoundingClientRect();
          return [Math.round(r.left+r.width/2), Math.round(r.top+r.height/2)];})()`);
      if (!box) throw new Error(`no element ${selector}`);
      for (const type of ['mousePressed', 'mouseReleased']) {
        await send('Input.dispatchMouseEvent',
          { type, x: box[0], y: box[1], button: 'left', clickCount: 1 });
      }
      await new Promise(r => setTimeout(r, 500));
    },
  };
}

const imagesFetched = `performance.getEntriesByType('resource')
  .filter(e => /\\.(png|jpe?g|gif|webp)(\\?|$)/i.test(e.name))
  .filter(e => !/avatar/.test(e.name)).length`;

console.log(`\nchecking ${BASE}\n`);

// ---- phone ----------------------------------------------------------------
{
  const s = await session(390, 844, true);
  console.log('390x844 (phone)');

  await s.go('/');
  check('no horizontal overflow on the index',
    await s.eval('document.documentElement.scrollWidth <= innerWidth'),
    await s.eval('document.documentElement.scrollWidth + " > " + innerWidth'));
  check('covers are not downloaded while photos are hidden',
    await s.eval(`document.documentElement.getAttribute('data-photos') !== 'off' || ${imagesFetched} === 0`),
    `${await s.eval(imagesFetched)} fetched`);
  check('rows collapse to one column',
    await s.eval(`!document.querySelector('.row') ||
      getComputedStyle(document.querySelector('.row')).gridTemplateColumns.split(' ').length === 1`));

  await s.tap('#menu-toggle');
  check('menu opens on tap',
    await s.eval(`document.documentElement.getAttribute('data-menu') === 'open'`));
  check('menu button reports expanded',
    await s.eval(`document.getElementById('menu-toggle').getAttribute('aria-expanded') === 'true'`));
  await s.tap('#menu-toggle');
  check('menu closes again',
    await s.eval(`document.documentElement.getAttribute('data-menu') === 'closed'`));

  await s.go('/2025-january-links/');
  check('post shows the inline Contents, not the side rail',
    await s.eval(`(()=>{const i=document.querySelector('.toc--inline'), d=document.querySelector('.toc--side');
      return !!i && getComputedStyle(i).display !== 'none' && (!d || getComputedStyle(d).display === 'none');})()`));
  check('nothing in the post is wider than the screen',
    await s.eval(`[...document.querySelectorAll('.prose *')]
      .every(e => e.getBoundingClientRect().width <= innerWidth)`));
  s.close();
}

// ---- desktop --------------------------------------------------------------
{
  const s = await session(1280, 820, false);
  console.log('\n1280x820 (desktop)');

  await s.go('/');
  check('sidebar scrolls rather than clipping its own controls',
    await s.eval(`(()=>{const el=document.querySelector('.side');
      return getComputedStyle(el).overflowY === 'auto' || el.scrollHeight <= el.clientHeight;})()`));

  await s.go('/2025-january-links/');
  check('post shows the side Contents',
    await s.eval(`(()=>{const d=document.querySelector('.toc--side');
      return !!d && getComputedStyle(d).display !== 'none';})()`));
  check('no Contents entry is blank',
    await s.eval(`document.querySelectorAll('.toc a[href="#"]').length === 0`),
    `${await s.eval(`document.querySelectorAll('.toc a[href="#"]').length`)} blank`);

  await s.go('/pages/ai-resources/');
  check('a static page still shows its Contents',
    await s.eval(`(()=>{const i=document.querySelector('.toc--inline');
      return !!i && getComputedStyle(i).display !== 'none';})()`));
  check('Contents titles are not double-escaped',
    await s.eval(`![...document.querySelectorAll('.toc a')].some(a => /&(amp|lt|gt);/.test(a.textContent))`));

  await s.go('/tags/');
  check('no taxonomy term lists zero posts',
    await s.eval(`[...document.querySelectorAll('.chip__count')].every(c => c.textContent.trim() !== '0')`),
    `${await s.eval(`[...document.querySelectorAll('.chip__count')].filter(c=>c.textContent.trim()==='0').length`)} empty terms`);

  check('every page links a favicon',
    await s.eval(`!!document.querySelector('link[rel~="icon"]')`));
  s.close();
}

console.log(failures.length
  ? `\n${failures.length} check(s) failed\n`
  : '\nall checks passed\n');
process.exit(failures.length ? 1 : 0);
