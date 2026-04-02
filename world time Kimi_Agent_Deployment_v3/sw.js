// Service Worker for World Time Online - Optimized Version
// Provides offline support, intelligent caching, and performance improvements

const CACHE_NAME = 'worldtime-v2';
const STATIC_ASSETS = [
  './',
  './index.html',
  './assets/index-Dd7au40z.js',
  './assets/index-ufePLcBr.css',
  './favicon.svg',
  './manifest.json'
];

// Cache versioning for invalidation
const CACHE_VERSION = 'v2';
const CACHE_MAX_AGE = 30 * 24 * 60 * 60 * 1000; // 30 days
const API_CACHE_MAX_AGE = 5 * 60 * 1000; // 5 minutes for API

// Install event - cache static assets with improved error handling
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => {
        console.log('[SW] Caching static assets');
        return cache.addAll(STATIC_ASSETS.map(url => 
          new Request(url, { cache: 'reload' })
        ));
      })
      .then(() => {
        console.log('[SW] Static assets cached successfully');
        return self.skipWaiting();
      })
      .catch(err => {
        console.error('[SW] Failed to cache assets:', err);
        // Still skip waiting even if some assets fail
        return self.skipWaiting();
      })
  );
});

// Activate event - clean up old caches and claim clients
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((cacheNames) => {
        return Promise.all(
          cacheNames
            .filter((name) => name !== CACHE_NAME && name.startsWith('worldtime-'))
            .map((name) => {
              console.log('[SW] Deleting old cache:', name);
              return caches.delete(name);
            })
        );
      })
      .then(() => {
        console.log('[SW] Activated and claiming clients');
        return self.clients.claim();
      })
  );
});

// Fetch event - intelligent caching strategies
self.addEventListener('fetch', (event) => {
  const { request } = event;
  const url = new URL(request.url);

  // Skip non-GET requests
  if (request.method !== 'GET') return;

  // Skip chrome-extension and other non-http(s) requests
  if (!url.protocol.startsWith('http')) return;

  // Handle different request types with appropriate strategies
  if (url.hostname.includes('worldtimeapi.org')) {
    // API requests: Network-first with cache fallback
    event.respondWith(handleApiRequest(request));
  } else if (url.origin === location.origin) {
    // Same-origin requests: Cache-first with network fallback
    event.respondWith(handleStaticRequest(request));
  }
  // Cross-origin requests: Let browser handle normally
});

// Network-first strategy for API requests
async function handleApiRequest(request) {
  const cache = await caches.open(CACHE_NAME);
  
  try {
    // Try network first
    const networkResponse = await fetch(request);
    
    if (networkResponse.ok) {
      // Clone and cache successful responses
      const responseClone = networkResponse.clone();
      
      // Add cache headers
      const headers = new Headers(responseClone.headers);
      headers.set('Cache-Control', `max-age=${API_CACHE_MAX_AGE / 1000}`);
      
      const cacheResponse = new Response(responseClone.body, {
        status: responseClone.status,
        statusText: responseClone.statusText,
        headers
      });
      
      cache.put(request, cacheResponse);
      console.log('[SW] API response cached:', request.url);
    }
    
    return networkResponse;
  } catch (error) {
    console.log('[SW] Network failed, trying cache:', request.url);
    
    // Fallback to cache
    const cachedResponse = await cache.match(request);
    if (cachedResponse) {
      // Check if cache is stale
      const cacheTime = await getCacheTime(cachedResponse);
      if (Date.now() - cacheTime < CACHE_MAX_AGE) {
        console.log('[SW] Serving stale API from cache');
        return cachedResponse;
      }
    }
    
    // Return offline fallback if available
    return createOfflineFallback();
  }
}

// Cache-first strategy for static assets
async function handleStaticRequest(request) {
  const cache = await caches.open(CACHE_NAME);
  
  // Try cache first
  const cachedResponse = await cache.match(request);
  if (cachedResponse) {
    // Update cache in background (stale-while-revalidate)
    event.waitUntil(updateCacheInBackground(request));
    console.log('[SW] Serving from cache:', request.url);
    return cachedResponse;
  }
  
  // Fallback to network
  try {
    const networkResponse = await fetch(request);
    if (networkResponse.ok) {
      // Cache the response
      cache.put(request, networkResponse.clone());
      console.log('[SW] Cached from network:', request.url);
    }
    return networkResponse;
  } catch (error) {
    console.error('[SW] Fetch failed:', request.url, error);
    
    // Offline fallback for navigation requests
    if (request.mode === 'navigate') {
      return cache.match('./index.html');
    }
    
    // Return error response
    return new Response('Offline', { status: 503, statusText: 'Service Unavailable' });
  }
}

// Background cache update
async function updateCacheInBackground(request) {
  try {
    const cache = await caches.open(CACHE_NAME);
    const response = await fetch(request);
    if (response.ok) {
      await cache.put(request, response.clone());
      console.log('[SW] Background cache updated:', request.url);
    }
  } catch (error) {
    console.log('[SW] Background update failed:', error);
  }
}

// Get cache timestamp from response
async function getCacheTime(response) {
  const cacheTime = response.headers.get('X-Cache-Time');
  return cacheTime ? parseInt(cacheTime, 10) : Date.now();
}

// Create offline fallback response
function createOfflineFallback() {
  return new Response(
    JSON.stringify({
      error: 'offline',
      message: 'You are currently offline. Please check your connection.',
      cached: true
    }),
    {
      status: 200,
      headers: { 'Content-Type': 'application/json' }
    }
  );
}

// Handle messages from main thread
self.addEventListener('message', (event) => {
  if (event.data && event.data.type === 'SKIP_WAITING') {
    self.skipWaiting();
  }
  
  if (event.data && event.data.type === 'CLEAR_CACHE') {
    event.waitUntil(
      caches.keys().then(names => 
        Promise.all(names.map(name => caches.delete(name)))
      )
    );
  }
  
  if (event.data && event.data.type === 'CACHE_STATUS') {
    event.waitUntil(
      caches.open(CACHE_NAME).then(async cache => {
        const keys = await cache.keys();
        event.source.postMessage({
          type: 'CACHE_STATUS_RESPONSE',
          count: keys.length,
          size: keys.reduce((acc, req) => acc + req.url.length, 0)
        });
      })
    );
  }
});

// Periodic background sync for time updates
self.addEventListener('periodicsync', (event) => {
  if (event.tag === 'sync-time-data') {
    event.waitUntil(syncTimeData());
  }
});

// Sync time data in background
async function syncTimeData() {
  try {
    const cache = await caches.open(CACHE_NAME);
    // Pre-fetch common API endpoints
    const urls = [
      'https://worldtimeapi.org/api/timezone/Europe/London',
      'https://worldtimeapi.org/api/timezone/America/New_York',
      'https://worldtimeapi.org/api/timezone/Asia/Tokyo'
    ];
    
    await Promise.all(urls.map(url => 
      fetch(url).then(res => res.ok && cache.put(url, res.clone()))
    ));
    
    console.log('[SW] Background time data synced');
  } catch (error) {
    console.error('[SW] Background sync failed:', error);
  }
}
