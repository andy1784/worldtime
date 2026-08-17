module.exports = {
  ci: {
    collect: {
      numberOfRuns: 3,
      settings: {
        headless: true,
        preset: 'desktop',
        staticDistDir: './',
      },
      url: [
        'https://worldtimessync.com/',
        'https://worldtimessync.com/time/london',
        'https://worldtimessync.com/country/australia',
        'https://worldtimessync.com/blog/30-minute-time-zone-offsets',
        'https://worldtimessync.com/time-zones/est',
        'https://worldtimessync.com/world-clock',
      ],
    },
    assert: {
      assertions: {
        'categories:performance': ['error', { minScore: 0.9 }],
        'categories:accessibility': ['error', { minScore: 0.9 }],
        'categories:best-practices': ['error', { minScore: 0.9 }],
        'categories:seo': ['error', { minScore: 0.9 }],
        'first-contentful-paint': ['error', { maxNumericValue: 2500 }],
        'largest-contentful-paint': ['error', { maxNumericValue: 2500 }],
        'cumulative-layout-shift': ['error', { maxNumericValue: 0.1 }],
        'total-blocking-time': ['error', { maxNumericValue: 200 }],
        'max-potential-fid': ['warn', { maxNumericValue: 300 }],
        'interactive': ['warn', { maxNumericValue: 3800 }],
        'redirects': ['off', { maxNumericValue: 0 }],
        'render-blocking-resources': ['warn', { maxNumericValue: 500 }],
        'unused-css-rules': ['warn', { maxNumericValue: 50 }],
        'unused-javascript': ['warn', { maxNumericValue: 100 }],
        'modern-image-formats': ['warn', { maxNumericValue: 0 }],
        'offscreen-images': ['warn', { maxNumericValue: 100 }],
        'unminified-css': ['warn', { maxNumericValue: 20 }],
        'unminified-javascript': ['warn', { maxNumericValue: 20 }],
      },
    },
    upload: {
      target: 'temporary-public-storage',
    },
    server: {
      command: 'npx serve . -p 3000',
      port: 3000,
    },
  },
};
