// Folded round-up sections. CSS hides the extra items under html.js, so the
// page never flashes them open; this only opens and closes on request.
(function () {
  var sections = [].slice.call(document.querySelectorAll('.issue-section[data-fold]'));
  if (!sections.length) return;

  function setOpen(sec, open) {
    var btn = sec.querySelector('.issue-more');
    sec.classList.toggle('is-open', open);
    btn.setAttribute('aria-expanded', String(open));
    btn.firstElementChild.textContent = open ? 'Show fewer' : btn.getAttribute('data-more');
  }

  sections.forEach(function (sec) {
    var btn = sec.querySelector('.issue-more');
    btn.addEventListener('click', function () {
      var open = !sec.classList.contains('is-open');
      setOpen(sec, open);
      if (!open) btn.scrollIntoView({ block: 'nearest' });
    });
  });

  // A link to an item hidden in a folded section opens that section first.
  function reveal() {
    var id = decodeURIComponent(location.hash.slice(1));
    var el = id && document.getElementById(id);
    var sec = el && el.closest('.issue-section[data-fold]');
    if (sec && !sec.classList.contains('is-open') && el.closest('.is-extra')) {
      setOpen(sec, true);
      el.scrollIntoView();
    }
  }
  addEventListener('hashchange', reveal);
  reveal();

  // The archive search links to a round-up's link with a text fragment
  // (#:~:text=), which the browser cannot find in a folded section. The
  // directive is hidden from location, but not from the navigation entry.
  var nav = performance.getEntriesByType && performance.getEntriesByType('navigation')[0];
  var text = nav && /:~:text=([^&,]*)/.exec(nav.name);
  if (text) {
    text = decodeURIComponent(text[1]).toLowerCase();
    [].forEach.call(document.querySelectorAll('.issue-section[data-fold] .is-extra'), function (el) {
      if (el.textContent.toLowerCase().indexOf(text) !== -1) setOpen(el.closest('.issue-section'), true);
    });
  }
})();
