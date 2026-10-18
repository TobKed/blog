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
  .filter(e => !/avatar|\\/images\\/youtube\\//.test(e.name)).length`;

console.log(`\nchecking ${BASE}\n`);

const noOverflow = 'document.documentElement.scrollWidth <= innerWidth';
const overflowBy = 'document.documentElement.scrollWidth + " > " + innerWidth';
const visible = sel => `(()=>{const e=document.querySelector(${JSON.stringify(sel)});
  return !!e && getComputedStyle(e).display !== 'none' && e.getBoundingClientRect().height > 0;})()`;
const ROUNDUP = '/2026-september-links/';
// Visible text smaller than min px, outside the selectors allowed to go lower.
const smallText = (min, allow = []) => `[...document.querySelectorAll('body *')].filter(e =>
  [...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim()) && e.getClientRects().length &&
  !e.closest('.toggle__label[style], [hidden]') && !${JSON.stringify(allow)}.some(a => e.matches(a)) &&
  parseFloat(getComputedStyle(e).fontSize) < ${min}).map(e => e.className || e.tagName).slice(0, 5)`;
const ESSAY = '/enum-and-dataclass/';

// ---- phone ----------------------------------------------------------------
{
  const s = await session(390, 844, true);
  console.log('390x844 (phone)');

  for (const path of ['/', ROUNDUP, ESSAY, '/pages/about-me/', '/archives/', '/tags/']) {
    await s.go(path);
    check(`no horizontal overflow on ${path}`, await s.eval(noOverflow), await s.eval(overflowBy));
  }

  await s.go('/');
  check('covers are not downloaded while photos are hidden',
    await s.eval(`document.documentElement.getAttribute('data-photos') !== 'off' || ${imagesFetched} === 0`),
    `${await s.eval(imagesFetched)} fetched`);
  check('main nav is folded behind the menu button', !(await s.eval(visible('.masthead__nav'))));

  await s.tap('#menu-toggle');
  check('menu opens on tap',
    await s.eval(`document.documentElement.getAttribute('data-menu') === 'open'`) &&
    await s.eval(visible('.masthead__nav')));
  check('menu button reports expanded',
    await s.eval(`document.getElementById('menu-toggle').getAttribute('aria-expanded') === 'true'`));
  await s.tap('#menu-toggle');
  check('menu closes again',
    await s.eval(`document.documentElement.getAttribute('data-menu') === 'closed'`));

  await s.go(ROUNDUP);
  check('round-up shows its Contents', await s.eval(visible('.issue-toc')));
  check('tags are at least 44px tall',
    await s.eval(`[...document.querySelectorAll('.issue-tags .chip')].every(c => c.getBoundingClientRect().height >= 44)`));
  for (const path of ['/', ROUNDUP, ESSAY, '/archives/', '/pages/about-me/']) {
    await s.go(path);
    const small = await s.eval(smallText(11, ['.issue-badge']));
    check(`no text below 11px on ${path}`, small.length === 0, small.join(', '));
  }

  await s.go(ESSAY);
  check('nothing in the essay is wider than the screen',
    await s.eval(`[...document.querySelectorAll('.prose > *')]
      .every(e => e.getBoundingClientRect().width <= innerWidth)`));
  s.close();
}

// ---- laptop ---------------------------------------------------------------
{
  const s = await session(1366, 768, false);
  console.log('\n1366x768 (laptop)');
  await s.go('/');
  check('latest post kicker and title are above the fold',
    await s.eval(`['.home-latest .home-kicker', '.home-latest__title'].every(sel =>
      document.querySelector(sel).getBoundingClientRect().bottom <= innerHeight)`));
  s.close();
}

// ---- desktop --------------------------------------------------------------
{
  const s = await session(1280, 820, false);
  console.log('\n1280x820 (desktop)');

  await s.go('/');
  check('masthead shows the nav and no menu button',
    await s.eval(visible('.masthead__nav')) && !(await s.eval(visible('#menu-toggle'))));
  check('current page is underlined, not only coloured',
    await s.eval(`getComputedStyle(document.querySelector('.masthead__nav a.is-active')).textDecorationLine === 'underline'`));
  const photosLabel = `document.querySelector('#photos-toggle .toggle__label').textContent`;
  const before = await s.eval(photosLabel);
  await s.tap('#photos-toggle');
  const after = await s.eval(photosLabel);
  check('photos button states its value', before === 'Photos on' && after === 'Photos off', `${before} -> ${after}`);
  await s.tap('#photos-toggle');
  check('back issues show their date range',
    await s.eval(`/^[A-Z][a-z]{2}( \\d{4})?( – [A-Z][a-z]{2} \\d{4})?$/.test(document.querySelector('.home-back__range').textContent)`));

  await s.go(ROUNDUP);
  check('round-up shows its Contents', await s.eval(visible('.issue-toc')));
  check('no Contents entry is blank',
    await s.eval(`![...document.querySelectorAll('.issue-toc a')].some(a => a.getAttribute('href') === '#' || !a.textContent.trim())`));
  check('a long section is folded',
    await s.eval(`[...document.querySelectorAll('.is-extra')].some(e => getComputedStyle(e).display === 'none')`));
  const foldedCount = `document.querySelector('.issue-section[data-fold] .issue-section__count').textContent`;
  check('a folded section counts what it shows', / of \d+ links?$/.test(await s.eval(foldedCount)), await s.eval(foldedCount));
  await s.eval(`document.querySelector('.issue-more').scrollIntoView({ block: 'center' })`);
  await s.tap('.issue-more');
  check('"Show more" unfolds the section',
    await s.eval(`document.querySelector('.issue-more').getAttribute('aria-expanded') === 'true'`));
  check('an unfolded section counts every link', /^\d+ links?$/.test(await s.eval(foldedCount)), await s.eval(foldedCount));
  check('Contents stays in view while reading',
    await s.eval(`(()=>{const r=document.querySelector('.issue-toc').getBoundingClientRect(); return r.top >= 0 && r.top < innerHeight;})()`));
  check('Contents ends with a 44px "Back to top" link to the header',
    await s.eval(`(()=>{const a=document.querySelector('.issue-toc + .back-top'); return !!a && a.getBoundingClientRect().height >= 44 &&
      !!document.getElementById(a.getAttribute('href').slice(1));})()`));
  const smallDesk = await s.eval(smallText(12));
  check('no text below 12px on the round-up', smallDesk.length === 0, smallDesk.join(', '));

  check('no request reaches YouTube before a video is played',
    await s.eval(`!performance.getEntriesByType('resource').some(e => /youtube|ytimg/.test(new URL(e.name).host))`));
  await s.eval(`document.querySelector('#videos .yt__box').scrollIntoView({ block: 'center' })`);
  await s.tap('#videos .yt__box');
  check('pressing a video preview plays it in place',
    await s.eval(`!!document.querySelector('#videos .yt.is-playing iframe[src*="youtube-nocookie.com/embed/"]')`));
  await s.eval(`document.querySelectorAll('#videos .yt__box')[0].scrollIntoView({ block: 'center' })`);
  await s.tap('#videos .yt__box');
  check('only one video plays at a time',
    await s.eval(`document.querySelectorAll('.yt__frame').length === 1`));

  await s.go(ESSAY);
  check('essay shows "On this page"', await s.eval(visible('.toc')));
  check('"On this page" ends with "Back to top"', await s.eval(visible('.toc + .back-top')));
  check('code blocks carry a Copy button', await s.eval(visible('.code__copy')));

  await s.go('/pages/ai-resources/');
  check('Contents titles are not double-escaped',
    await s.eval(`![...document.querySelectorAll('.toc a')].some(a => /&(amp|lt|gt);/.test(a.textContent))`));

  await s.go('/archives/');
  await s.tap('[data-filter="summary"]');
  check('archive filter narrows the list',
    await s.eval(`(()=>{const shown=[...document.querySelectorAll('li[data-kind]')].filter(e => e.offsetParent);
      return shown.length > 0 && shown.every(e => e.dataset.kind === 'summary');})()`));
  await s.tap('[data-filter=""]');
  check('archive search finds round-ups by a link title',
    await s.eval(`(()=>{const titles=[...document.querySelectorAll('[data-title]')].map(e => e.dataset.title);
      const q=[...document.querySelectorAll('[data-links]')].flatMap(a => a.dataset.links.split('\\n'))
        .find(t => t.length > 12 && !titles.some(x => x.includes(t)));
      const i=document.querySelector('.archive__bar input'); i.value=q; i.dispatchEvent(new Event('input'));
      const shown=[...document.querySelectorAll('[data-kind]')].filter(e => e.offsetParent);
      return shown.length > 0 && shown.every(e => (e.getAttribute('href') || '').includes('#:~:text='));})()`));

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
