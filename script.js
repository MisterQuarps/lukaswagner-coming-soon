(function () {
  'use strict';
  var reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;

  var header = document.getElementById('header');
  function onScroll() { header.classList.toggle('scrolled', window.scrollY > 24); }
  addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  var targets = document.querySelectorAll('.reveal');
  if (reduced || !('IntersectionObserver' in window)) {
    Array.prototype.forEach.call(targets, function (el) { el.classList.add('in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { threshold: 0.12 });
    Array.prototype.forEach.call(targets, function (el) { io.observe(el); });
  }

  var portals = document.querySelectorAll('.portal');
  var details = document.querySelectorAll('.detail');
  var slot = document.querySelector('.detail-slot');

  function closeDetail(d) {
    d.classList.remove('open');
    var btn = document.getElementById(d.getAttribute('aria-labelledby'));
    if (btn) {
      btn.setAttribute('aria-expanded', 'false');
      var lbl = btn.querySelector('.more');
      if (lbl) lbl.textContent = lbl.dataset.labelOpen;
    }
    if (reduced) { d.hidden = true; return; }
    var done = function () { if (!d.classList.contains('open')) d.hidden = true; d.removeEventListener('transitionend', done); };
    d.addEventListener('transitionend', done);
    setTimeout(done, 700);
  }

  function openDetail(d, btn) {
    d.hidden = false;

    void d.offsetHeight;
    d.classList.add('open');
    btn.setAttribute('aria-expanded', 'true');
    var lbl = btn.querySelector('.more');
    if (lbl) lbl.textContent = lbl.dataset.labelClose;
  }

  Array.prototype.forEach.call(portals, function (btn) {
    btn.addEventListener('click', function () {
      var id = btn.getAttribute('aria-controls');
      var target = document.getElementById(id);
      var wasOpen = btn.getAttribute('aria-expanded') === 'true';
      Array.prototype.forEach.call(details, function (d) {
        if (!d.hidden || d.classList.contains('open')) closeDetail(d);
      });
      if (!wasOpen) {
        openDetail(target, btn);

        if (!reduced && matchMedia('(max-width:680px)').matches) {
          setTimeout(function () {
            slot.scrollIntoView({ behavior: 'smooth', block: 'start' });
          }, 80);
        }
      }
    });
  });

  (function () {
    var rows = document.querySelectorAll('.strip-row');
    if (!rows.length) return;

    Array.prototype.forEach.call(rows, function (row) {

      var parent = row.parentNode;
      var mask = document.createElement('div');
      mask.className = 'strip-mask';
      parent.insertBefore(mask, row);
      mask.appendChild(row);

      function scrollbar() { return row.scrollWidth - row.clientWidth > 4; }
      function syncMask() { mask.style.setProperty('--mask-on', scrollbar() ? '1' : '0'); }
      syncMask();
      addEventListener('resize', syncMask, { passive: true });

      var down = false, startX = 0, startLeft = 0, moved = 0;
      row.addEventListener('pointerdown', function (e) {
        if (e.pointerType === 'touch') return;
        down = true; moved = 0;
        startX = e.clientX; startLeft = row.scrollLeft;
        row.classList.add('is-dragging');
      });
      row.addEventListener('pointermove', function (e) {
        if (!down) return;
        var d = e.clientX - startX;
        moved = Math.abs(d);
        row.scrollLeft = startLeft - d;
      });
      ['pointerup', 'pointerleave', 'pointercancel'].forEach(function (ev) {
        row.addEventListener(ev, function () { down = false; row.classList.remove('is-dragging'); });
      });

      if (reduced) return;

      var dir = 1, px = 0, raf = null, paused = false;
      function step() {
        if (!paused && scrollbar()) {
          px += 0.28 * dir;
          if (Math.abs(px) >= 1) {
            row.scrollLeft += px;
            px = 0;
            if (row.scrollLeft <= 0) dir = 1;
            else if (row.scrollLeft >= row.scrollWidth - row.clientWidth - 1) dir = -1;
          }
        }
        raf = requestAnimationFrame(step);
      }
      function play() { if (raf === null) raf = requestAnimationFrame(step); }
      function stop() { if (raf !== null) { cancelAnimationFrame(raf); raf = null; } }

      ['pointerenter', 'pointerdown', 'focusin', 'touchstart'].forEach(function (ev) {
        row.addEventListener(ev, function () { paused = true; }, { passive: true });
      });
      ['pointerleave', 'focusout', 'touchend'].forEach(function (ev) {
        row.addEventListener(ev, function () { paused = false; }, { passive: true });
      });

      if ('IntersectionObserver' in window) {
        new IntersectionObserver(function (es) {
          es.forEach(function (e) { e.isIntersecting ? play() : stop(); });
        }, { threshold: 0.15 }).observe(row);
      } else { play(); }

      document.addEventListener('visibilitychange', function () {
        document.hidden ? stop() : play();
      });
    });
  })();

  var drawer = document.getElementById('request');
  var backdrop = document.querySelector('.drawer-backdrop');
  var form = document.getElementById('request-form');
  var topicField = document.getElementById('f-topic');
  var errorBox = document.getElementById('form-error');
  var okBox = document.getElementById('form-ok');
  var lastTrigger = null;
  var FOCUSABLE = 'a[href],button:not([disabled]),input:not([disabled]),textarea:not([disabled]),select:not([disabled]),[tabindex]:not([tabindex="-1"])';

  function openDrawer(trigger) {
    lastTrigger = trigger || null;
    var topic = trigger && trigger.dataset.topic ? trigger.dataset.topic : '';
    if (topicField) topicField.value = topic;
    backdrop.hidden = false; drawer.hidden = false;
    void drawer.offsetHeight;
    backdrop.classList.add('open'); drawer.classList.add('open');
    document.body.classList.add('locked');
    var first = drawer.querySelector('input,textarea');
    if (first) first.focus();
  }

  function closeDrawer() {
    backdrop.classList.remove('open'); drawer.classList.remove('open');
    document.body.classList.remove('locked');
    var finish = function () { drawer.hidden = true; backdrop.hidden = true; };
    if (reduced) finish(); else setTimeout(finish, 420);
    if (lastTrigger) { lastTrigger.focus(); lastTrigger = null; }
  }

  document.addEventListener('click', function (e) {
    var open = e.target.closest('[data-request-open]');
    if (open) { e.preventDefault(); openDrawer(open); return; }
    if (e.target.closest('[data-request-close]')) { e.preventDefault(); closeDrawer(); }
  });

  document.addEventListener('keydown', function (e) {
    if (drawer.hidden) return;
    if (e.key === 'Escape') { e.preventDefault(); closeDrawer(); return; }
    if (e.key !== 'Tab') return;
    var items = Array.prototype.filter.call(drawer.querySelectorAll(FOCUSABLE), function (el) {
      return el.offsetParent !== null;
    });
    if (!items.length) return;
    var first = items[0], last = items[items.length - 1];
    if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
    else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
  });

  var LABELS = {
    name: 'Name', email: 'E-Mail', org: 'Unternehmen / Organisation',
    event: 'Veranstaltung', date: 'Termin oder Zeitraum', place: 'Ort',
    audience: 'Publikum und gewünschte Wirkung', count: 'Teilnehmerzahl',
    budget: 'Budgetrahmen', phone: 'Telefon', topic: 'Schwerpunkt'
  };

  function mailtoBauen(fd) {
    var lines = [];
    Object.keys(LABELS).forEach(function (k) {
      var v = (fd.get(k) || '').toString().trim();
      if (k === 'date' && fd.get('date_open')) v = v ? v + ' (noch offen)' : 'noch offen';
      if (k === 'place' && fd.get('place_open')) v = v ? v + ' (noch offen / online)' : 'noch offen / online';
      if (v) lines.push(LABELS[k] + ': ' + v);
    });
    var subject = 'Anfrage KI-Keynote' + (fd.get('org') ? ' – ' + fd.get('org') : '');
    var body = 'Anfrage über die Website\n\n' + lines.join('\n') + '\n';
    return 'mailto:kontakt@lukaswagner.at?subject=' + encodeURIComponent(subject) +
           '&body=' + encodeURIComponent(body);
  }

  if (form) form.addEventListener('submit', function (e) {
    e.preventDefault();
    errorBox.hidden = true;
    okBox.hidden = true;

    var missing = [];
    Array.prototype.forEach.call(form.querySelectorAll('[required]'), function (el) {
      var wrap = el.closest('.field');
      var ok = el.value.trim() !== '' && (el.type !== 'email' || /.+@.+\..+/.test(el.value));
      if (!ok && el.id === 'f-date' && form.querySelector('[name="date_open"]').checked) ok = true;
      if (wrap) wrap.classList.toggle('invalid', !ok);
      if (!ok) missing.push(el);
    });
    if (missing.length) {
      errorBox.textContent = 'Bitte die markierten Pflichtfelder ausfüllen.';
      errorBox.hidden = false;
      missing[0].focus();
      return;
    }

    var fd = new FormData(form);
    var btn = form.querySelector('.drawer-submit');
    var beschriftung = btn.innerHTML;
    btn.setAttribute('aria-busy', 'true');
    btn.textContent = 'Wird gesendet …';

    function zurueck() {
      btn.removeAttribute('aria-busy');
      btn.innerHTML = beschriftung;
    }

    function fallback(grund) {
      zurueck();
      okBox.innerHTML = 'Ihre Anfrage wird in Ihrem E-Mail-Programm geöffnet. ' +
        'Falls sich nichts tut, schreiben Sie bitte direkt an ' +
        '<a href="mailto:kontakt@lukaswagner.at">kontakt@lukaswagner.at</a>.';
      okBox.hidden = false;
      location.href = mailtoBauen(fd);
      if (window.console && grund) console.info('Formular: Fallback auf mailto (' + grund + ')');
    }

    fetch(form.getAttribute('action'), { method: 'POST', body: fd })
      .then(function (r) {
        var typ = r.headers.get('content-type') || '';
        if (typ.indexOf('application/json') === -1) {

          return fallback('keine JSON-Antwort'), null;
        }
        return r.json().then(function (d) { return { status: r.status, daten: d }; });
      })
      .then(function (res) {
        if (!res) return;
        zurueck();
        if (res.daten && res.daten.ok) {
          form.reset();
          Array.prototype.forEach.call(form.querySelectorAll('.field.invalid'),
            function (f) { f.classList.remove('invalid'); });
          okBox.textContent = 'Danke, Ihre Anfrage ist angekommen. ' +
            'Sie bekommen in der Regel innerhalb von zwei Werktagen eine Rückmeldung.';
          okBox.hidden = false;
          okBox.focus && okBox.focus();
        } else {
          errorBox.textContent = (res.daten && res.daten.fehler) ||
            'Der Versand hat nicht geklappt.';
          errorBox.hidden = false;
        }
      })
      .catch(function () { fallback('Netzwerkfehler'); });
  });
})();
