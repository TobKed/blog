// Code-block Copy buttons, the "scroll →" hint on blocks wider than the screen,
// and the current entry in "On this page".
(function () {
    var codes = document.querySelectorAll('.code');

    Array.prototype.forEach.call(codes, function (fig) {
        var btn = fig.querySelector('.code__copy');
        var code = fig.querySelector('pre code') || fig.querySelector('pre');
        if (!btn || !code || !navigator.clipboard) {
            if (btn) btn.hidden = true;
            return;
        }
        btn.addEventListener('click', function () {
            navigator.clipboard.writeText(code.textContent.replace(/\n$/, '')).then(function () {
                btn.textContent = 'Copied';
                setTimeout(function () { btn.textContent = 'Copy'; }, 1500);
            });
        });
    });

    function markWide() {
        Array.prototype.forEach.call(codes, function (fig) {
            var pre = fig.querySelector('pre');
            if (pre) fig.toggleAttribute('data-scroll', pre.scrollWidth > pre.clientWidth + 1);
        });
    }
    if (codes.length) {
        markWide();
        window.addEventListener('resize', markWide);
    }

    var links = document.querySelectorAll('.toc__item');
    if (!links.length) return;
    var byId = {};
    var heads = [];
    Array.prototype.forEach.call(links, function (a) {
        var h = document.getElementById(decodeURIComponent(a.hash.slice(1)));
        if (h) { byId[h.id] = a; heads.push(h); }
    });
    var current = links[0];
    function select(a) {
        if (a === current) return;
        current.classList.remove('is-current');
        a.classList.add('is-current');
        current = a;
        // Keep the phone pill row scrolled to the current pill.
        var row = a.parentNode;
        if (row.scrollWidth > row.clientWidth) {
            row.scrollTo({ left: a.offsetLeft - row.offsetLeft - 20, behavior: 'smooth' });
        }
    }
    // The current section is the last heading that has scrolled past the top third.
    function update() {
        var pick = heads[0];
        for (var i = 0; i < heads.length; i++) {
            if (heads[i].getBoundingClientRect().top < window.innerHeight / 3) pick = heads[i];
            else break;
        }
        if (pick) select(byId[pick.id]);
    }
    var queued = false;
    window.addEventListener('scroll', function () {
        if (queued) return;
        queued = true;
        requestAnimationFrame(function () { queued = false; update(); });
    }, { passive: true });
    update();
})();
