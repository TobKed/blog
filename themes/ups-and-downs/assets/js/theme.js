(function () {
  var root = document.documentElement;

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
      localStorage.setItem('theme', next);
      syncTheme();
    });
    matchMedia('(prefers-color-scheme: dark)').addEventListener('change', syncTheme);
    syncTheme();
  }

  var photoBtn = document.getElementById('photos-toggle');
  if (photoBtn) {
    var syncPhotos = function () {
      var on = root.getAttribute('data-photos') !== 'off';
      photoBtn.textContent = on ? 'Photos on' : 'Photos off';
      photoBtn.setAttribute('aria-pressed', String(on));
    };
    photoBtn.addEventListener('click', function () {
      var on = root.getAttribute('data-photos') === 'off';
      root.setAttribute('data-photos', on ? 'on' : 'off');
      localStorage.setItem('photos', on ? 'on' : 'off');
      syncPhotos();
    });
    syncPhotos();
  }

  // The "/" glyph next to the search box advertises this shortcut.
  document.addEventListener('keydown', function (e) {
    var input = document.getElementById('site-search');
    if (e.key !== '/' || !input || /^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement.tagName)) return;
    e.preventDefault();
    input.focus();
  });
})();
