(function () {
  // Click-to-play YouTube previews (_partials/youtube-lite.html). The preview
  // is a link until this runs; one video plays at a time.
  var playing = null;

  function stop(fig) {
    var frame = fig.querySelector('.yt__frame');
    if (frame) frame.replaceWith(fig._preview);
    fig.classList.remove('is-playing');
    fig._note.textContent = fig._idleNote;
  }

  function play(fig) {
    if (playing && playing !== fig) stop(playing);
    var frame = document.createElement('iframe');
    frame.className = 'yt__frame';
    frame.src = 'https://www.youtube-nocookie.com/embed/' +
      encodeURIComponent(fig.getAttribute('data-youtube')) + '?autoplay=1';
    frame.title = fig.getAttribute('data-title');
    frame.allow = 'autoplay; encrypted-media; picture-in-picture';
    frame.allowFullscreen = true;
    fig._preview.replaceWith(frame);
    fig.classList.add('is-playing');
    fig._note.textContent = 'Now playing';
    playing = fig;
  }

  [].forEach.call(document.querySelectorAll('.yt'), function (fig) {
    var link = fig.querySelector('.yt__box');
    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = link.className;
    btn.setAttribute('aria-label', link.getAttribute('aria-label'));
    while (link.firstChild) btn.appendChild(link.firstChild);
    link.replaceWith(btn);
    fig._preview = btn;
    fig._note = fig.querySelector('.yt__note');
    fig._idleNote = fig._note.textContent;
    btn.addEventListener('click', function () { play(fig); });
  });
})();
