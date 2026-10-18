(function () {
  var root = document.documentElement;
  var darkQuery = matchMedia('(prefers-color-scheme: dark)');

  // Blocked storage throws on write; the toggle should still flip the page.
  function remember(key, value) {
    try { localStorage.setItem(key, value); } catch (e) {}
  }

  function effectiveTheme() {
    return root.getAttribute('data-theme') || (darkQuery.matches ? 'dark' : 'light');
  }

  // .is-dark (first set in head.html) lets CSS pick the sun or moon icon.
  var themeBtn = document.getElementById('theme-toggle');
  function syncTheme() {
    var dark = effectiveTheme() === 'dark';
    root.classList.toggle('is-dark', dark);
    if (!themeBtn) return;
    themeBtn.querySelector('.toggle__label').textContent = dark ? 'Light' : 'Dark';
    themeBtn.title = dark ? 'Switch to light mode' : 'Switch to dark mode';
  }
  if (themeBtn) {
    themeBtn.addEventListener('click', function () {
      var next = effectiveTheme() === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      remember('theme', next);
      syncTheme();
    });
  }
  darkQuery.addEventListener('change', syncTheme);
  syncTheme();

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

  // The header and the phone menu each carry a photos button.
  var photoBtns = [].slice.call(document.querySelectorAll('.js-photos'));
  function syncPhotos() {
    var on = root.getAttribute('data-photos') === 'on';
    photoBtns.forEach(function (b) {
      b.setAttribute('aria-pressed', String(on));
      b.title = on ? 'Hide cover photos' : 'Show cover photos';
    });
  }
  photoBtns.forEach(function (b) {
    b.addEventListener('click', function () {
      var next = root.getAttribute('data-photos') === 'on' ? 'off' : 'on';
      root.setAttribute('data-photos', next);
      remember('photos', next);
      syncPhotos();
      showPhotos();
    });
  });
  syncPhotos();
  showPhotos();

  // The narrow-screen menu. Deliberately not remembered: every page load
  // should open on its own content.
  var menuBtn = document.getElementById('menu-toggle');
  function setMenu(open) {
    root.setAttribute('data-menu', open ? 'open' : 'closed');
    menuBtn.setAttribute('aria-expanded', String(open));
    menuBtn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
  }
  if (menuBtn) {
    menuBtn.addEventListener('click', function () {
      setMenu(root.getAttribute('data-menu') !== 'open');
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && root.getAttribute('data-menu') === 'open') {
        setMenu(false);
        menuBtn.focus();
      }
    });
  }
})();
