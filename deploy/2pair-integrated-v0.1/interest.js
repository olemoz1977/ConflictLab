(() => {
  'use strict';

  const ENDPOINT = './server/interest_event.php';
  const RELEASE_ID = '2pair-integrated-v0.1';
  const sent = new Set();
  let trainingStarted = false;

  function deviceCategory() {
    const w = Math.min(innerWidth, screen.width || innerWidth);
    if (w < 700) return 'mobile';
    if (w < 1100) return 'tablet';
    return 'desktop';
  }

  function cleanSource(value) {
    const v = String(value || '').trim().toLowerCase().replace(/[^a-z0-9._-]+/g, '_').replace(/^_+|_+$/g, '');
    return (v || 'direct').slice(0, 48);
  }

  function sourceName() {
    const u = new URL(location.href);
    const explicit = u.searchParams.get('src') || u.searchParams.get('utm_source') || u.searchParams.get('source');
    if (explicit) return cleanSource(explicit);

    if (!document.referrer) return 'direct';
    try {
      const host = new URL(document.referrer).hostname.toLowerCase().replace(/^www\./, '');
      if (host === '2rasi.lt') return '2rasi.lt';
      if (host === '2rasi.com') return '2rasi.com';
      if (host === 'instagram.com' || host === 'l.instagram.com') return 'instagram';
      if (host === 'facebook.com' || host === 'l.facebook.com' || host === 'm.facebook.com') return 'facebook';
      if (host === location.hostname.toLowerCase().replace(/^www\./, '')) return 'internal';
      return cleanSource(host);
    } catch {
      return 'other';
    }
  }

  function currentLanguage() {
    return document.documentElement.lang === 'en' ? 'en' : 'lt';
  }

  function emit(event) {
    if (sent.has(event)) return;
    sent.add(event);

    const payload = JSON.stringify({
      releaseId: RELEASE_ID,
      event,
      source: sourceName(),
      language: currentLanguage(),
      deviceCategory: deviceCategory()
    });

    try {
      const blob = new Blob([payload], { type: 'application/json' });
      if (navigator.sendBeacon && navigator.sendBeacon(ENDPOINT, blob)) return;
    } catch {}

    try {
      fetch(ENDPOINT, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: payload,
        keepalive: true,
        credentials: 'same-origin'
      }).catch(() => {});
    } catch {}
  }

  emit('page_open');

  document.addEventListener('click', event => {
    const button = event.target.closest?.('button');
    if (!button) return;
    if (button.classList.contains('visual') || button.classList.contains('ncc') || button.closest('.scale')) return;

    const text = (button.textContent || '').trim();
    if (text === 'Pradėti treniruotę' || text === 'Start practice') {
      trainingStarted = true;
      emit('start_click');
      return;
    }
    if (text === 'Sutinku ir dalyvauju' || text === 'I consent and participate') {
      emit('research_join');
      return;
    }
    if (text === 'Tęsti be duomenų įkėlimo' || text === 'Continue without upload') {
      emit('local_continue');
    }
  });

  const bodyObserver = new MutationObserver(() => {
    if (!trainingStarted || document.body.classList.contains('rapid')) return;
    queueMicrotask(() => {
      if (document.body.classList.contains('rapid')) return;
      const heading = document.querySelector('#app h2')?.textContent?.trim() || '';
      if (heading === 'Dalyvavimas tyrime' || heading === 'Research participation') emit('consent_screen');
    });
  });
  bodyObserver.observe(document.body, { attributes: true, attributeFilter: ['class'] });
})();
