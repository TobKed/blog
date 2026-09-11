(function () {
  var root = document.documentElement;

  // Blocked storage throws on write; the toggle should still flip the page.
  function remember(key, value) {
    try { localStorage.setItem(key, value); } catch (e) {}
  }

  function effectiveTheme() {
    return root.getAttribute('data-theme') ||
      (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  }

  var themeBtn = document.getElementById('theme-toggle');
  if (themeBtn) {
    var syncTheme = function () {
      themeBtn.textContent = effectiveTheme() === 'dark' ? 'Light mode' : 'Dark mode';
    };
    themeBtn.addEventListener('click', function () {
      var next = effectiveTheme() === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      remember('theme', next);
      syncTheme();
    });
    matchMedia('(prefers-color-scheme: dark)').addEventListener('change', syncTheme);
    syncTheme();
  }

  // Buttons that flip a data-* attribute on <html> and remember the choice.
  // The matching restore-on-load lives inline in head.html, before first paint.
  [
    { id: 'photos-toggle', attr: 'data-photos', key: 'photos', on: 'on', off: 'off',
      label: function (v) { return 'Photos ' + v; } },
    { id: 'rail-toggle', attr: 'data-rail', key: 'rail', on: 'below', off: 'side',
      label: function (v) { return v === 'below' ? 'Index below' : 'Index at side'; } },
    { id: 'toc-toggle', attr: 'data-toc', key: 'toc', on: 'side', off: 'inline',
      label: function (v) { return v === 'side' ? 'Contents at side' : 'Contents in post'; } }
  ].forEach(function (t) {
    var btn = document.getElementById(t.id);
    if (!btn) return;
    var sync = function () {
      var v = root.getAttribute(t.attr);
      btn.textContent = t.label(v);
      btn.setAttribute('aria-pressed', String(v === t.on));
    };
    btn.addEventListener('click', function () {
      var next = root.getAttribute(t.attr) === t.on ? t.off : t.on;
      root.setAttribute(t.attr, next);
      remember(t.key, next);
      sync();
    });
    sync();
  });

  // Covers are shipped as data-src when they start hidden, so nothing is
  // downloaded until a reader actually asks for photos. One-way: once promoted
  // the browser has the image, and turning photos off again only hides it.
  function showPhotos() {
    if (root.getAttribute('data-photos') !== 'on') return;
    [].forEach.call(document.querySelectorAll('img[data-src]'), function (img) {
      img.src = img.getAttribute('data-src');
      img.removeAttribute('data-src');
    });
  }
  showPhotos();
  var photosBtn = document.getElementById('photos-toggle');
  if (photosBtn) photosBtn.addEventListener('click', showPhotos);

  // The narrow-screen sidebar. Deliberately not remembered: every page load
  // should open on its own content, which is the point of the bar.
  var menuBtn = document.getElementById('menu-toggle');
  if (menuBtn) {
    menuBtn.addEventListener('click', function () {
      var open = root.getAttribute('data-menu') !== 'open';
      root.setAttribute('data-menu', open ? 'open' : 'closed');
      menuBtn.setAttribute('aria-expanded', String(open));
      menuBtn.firstElementChild.textContent = open ? 'Close' : 'Menu';
      menuBtn.lastElementChild.textContent = open ? '▲' : '▼';
    });
  }

  // Highlight the section the reader is in, as the design's side Contents shows.
  var links = [].slice.call(document.querySelectorAll('.toc--side a'));
  if (links.length) {
    var targets = links.map(function (a) {
      return document.getElementById(decodeURIComponent(a.getAttribute('href').slice(1)));
    });
    var queued = false;
    var spy = function () {
      queued = false;
      var i = 0;
      for (var n = 0; n < targets.length; n++) {
        if (targets[n] && targets[n].getBoundingClientRect().top <= 100) i = n;
      }
      links.forEach(function (a, n) { a.classList.toggle('is-current', n === i); });
    };
    addEventListener('scroll', function () {
      if (queued) return;
      queued = true;
      requestAnimationFrame(spy);
    }, { passive: true });
    spy();
  }

  // The "/" glyph next to the search box advertises this shortcut.
  document.addEventListener('keydown', function (e) {
    var input = document.getElementById('site-search');
    if (e.key !== '/' || !input || /^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement.tagName)) return;
    e.preventDefault();
    input.focus();
  });
})();
