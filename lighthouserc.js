module.exports = {
  ci: {
    collect: {
      numberOfRuns: 1,
      startServerCommand: 'npx serve .',
      url: ['https://worldtimessync.com/', 'https://worldtimessync.com/time-zones/est'],
      settings: {
        preset: 'mobile',
        headless: true,
      },
    },
    assert: {
      assertions: {
        'categories:performance': ['error', {minScore: 0.5}],
      },
    },
    upload: {
      target: 'temporary-public-storage',
    },
  },
};
