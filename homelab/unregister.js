// Chirpy loads this when its PWA is disabled. Retire only this site's old
// registrations; other project sites on this origin may use their own workers.
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.getRegistrations().then(registrations => {
    for (const registration of registrations) {
      const scope = new URL(registration.scope).pathname;
      if (scope === '/' || scope === '/homelab/') {
        registration.unregister();
      }
    }
  });
}
