(function () {
  // Archives: kind chips and title search. Hides what does not match, then
  // any group or year left with nothing in it.
  var bar = document.querySelector('.archive__bar');
  if (!bar) return;
  var buttons = [].slice.call(bar.querySelectorAll('[data-filter]'));
  var input = bar.querySelector('input');
  var years = [].slice.call(document.querySelectorAll('.ayear'));
  var kind = '';

  function apply() {
    var q = input.value.trim().toLowerCase();
    years.forEach(function (year) {
      var any = false;
      [].forEach.call(year.querySelectorAll('[data-kind]'), function (el) {
        var show = (!kind || el.getAttribute('data-kind') === kind) &&
          (!q || el.getAttribute('data-title').indexOf(q) !== -1);
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
