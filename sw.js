// Retire the former root-scoped Chirpy worker. Its cached 404s could cover
// other GitHub Pages project sites on this origin.
self.addEventListener('install', event => {
  event.waitUntil(self.skipWaiting());
});

self.addEventListener('activate', event => {
  event.waitUntil((async () => {
    const names = await caches.keys();
    await Promise.all(names.filter(name => name.startsWith('chirpy-')).map(name => caches.delete(name)));
    await self.registration.unregister();
  })());
});
