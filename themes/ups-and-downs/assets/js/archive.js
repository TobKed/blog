(function () {
  // Archives: kind chips and a search over post titles and round-up link
  // titles. Hides what does not match, then any group or year left with
  // nothing in it. A round-up found by one of its links points at that link.
  var bar = document.querySelector('.archive__bar');
  if (!bar) return;
  var buttons = [].slice.call(bar.querySelectorAll('[data-filter]'));
  var input = bar.querySelector('input');
  var years = [].slice.call(document.querySelectorAll('.ayear'));
  var kind = '';

  // Month chips carry data-links; the cover tiles share them by href.
  var links = {};
  [].forEach.call(document.querySelectorAll('[data-links]'), function (a) {
    links[a.getAttribute('href')] = a.getAttribute('data-links').split('\n');
  });

  function fragment(text) {
    // Text fragments treat - , & as syntax, so encode them too.
    return '#:~:text=' + encodeURIComponent(text).replace(/-/g, '%2D');
  }

  function matches(el, q) {
    var href = (el.getAttribute('href') || '').split('#')[0];
    var hit = q && el.getAttribute('data-title').indexOf(q) === -1 &&
      (links[href] || []).filter(function (t) { return t.indexOf(q) !== -1; })[0];
    if (href) el.setAttribute('href', hit ? href + fragment(hit) : href);
    if (hit) el.setAttribute('title', hit); else el.removeAttribute('title');
    return !q || el.getAttribute('data-title').indexOf(q) !== -1 || !!hit;
  }

  function apply() {
    var q = input.value.trim().toLowerCase();
    years.forEach(function (year) {
      var any = false;
      [].forEach.call(year.querySelectorAll('[data-kind]'), function (el) {
        var show = (!kind || el.getAttribute('data-kind') === kind) && matches(el, q);
        el.hidden = !show;
        if (show && !el.hasAttribute('data-next')) any = true;
      });
      [].forEach.call(year.querySelectorAll('[data-group]'), function (g) {
        g.hidden = !g.querySelector('[data-kind]:not([hidden])');
      });
      year.hidden = !any;
    });
  }

  buttons.forEach(function (b) {
    b.addEventListener('click', function () {
      kind = b.getAttribute('data-filter');
      buttons.forEach(function (o) { o.setAttribute('aria-pressed', String(o === b)); });
      apply();
    });
  });
  input.addEventListener('input', apply);
  if (input.value) apply();
})();
