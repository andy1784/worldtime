#!/usr/bin/env python3
"""
Generate Lighthouse CI config and GitHub Action workflow.
"""
from pathlib import Path

BASE = Path('/home/kaliuser/worldtime')

# Lighthouse CI config
lighthouserc = """module.exports = {
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
"""

# GitHub Action workflow
github_workflow = """name: Lighthouse CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  workflow_dispatch:

jobs:
  lighthouse:
    runs-on: ubuntu-latest
    timeout-minutes: 30
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci || npm install
        working-directory: .

      - name: Build (if needed)
        run: npm run build 2>/dev/null || echo "No build script, serving static files"

      - name: Start local server
        run: |
          npx serve . -p 3000 &
          sleep 5
        working-directory: .

      - name: Run Lighthouse CI
        uses: treosh/lighthouse-ci-action@v11
        with:
          urls: |
            http://localhost:3000/
            http://localhost:3000/time/london
            http://localhost:3000/country/australia
            http://localhost:3000/blog/30-minute-time-zone-offsets
            http://localhost:3000/time-zones/est
            http://localhost:3000/world-clock
          budgetPath: ./lighthouse-budget.json
          configPath: ./lighthouserc.js
          uploadArtifacts: true

      - name: Upload Lighthouse reports
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: lighthouse-reports
          path: .lighthouseci/
          retention-days: 30

      - name: Comment PR with results
        if: github.event_name == 'pull_request'
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            const path = require('path');
            
            // Find the latest Lighthouse report
            const reportDir = '.lighthouseci';
            if (fs.existsSync(reportDir)) {
              const files = fs.readdirSync(reportDir);
              const jsonFiles = files.filter(f => f.endsWith('.json'));
              
              if (jsonFiles.length > 0) {
                const latestReport = jsonFiles.sort().pop();
                const report = JSON.parse(fs.readFileSync(path.join(reportDir, latestReport), 'utf8'));
                
                // Extract key metrics
                const categories = report.categories || {};
                const audits = report.audits || {};
                
                const perf = categories.performance?.score ? Math.round(categories.performance.score * 100) : 'N/A';
                const a11y = categories.accessibility?.score ? Math.round(categories.accessibility.score * 100) : 'N/A';
                const bp = categories['best-practices']?.score ? Math.round(categories['best-practices'].score * 100) : 'N/A';
                const seo = categories.seo?.score ? Math.round(categories.seo.score * 100) : 'N/A';
                
                const lcp = audits['largest-contentful-paint']?.displayValue || 'N/A';
                const fid = audits['max-potential-fid']?.displayValue || 'N/A';
                const cls = audits['cumulative-layout-shift']?.displayValue || 'N/A';
                const tbt = audits['total-blocking-time']?.displayValue || 'N/A';
                
                const comment = `## 🚀 Lighthouse CI Results
                
| Metric | Score |
|--------|-------|
| Performance | ${perf} |
| Accessibility | ${a11y} |
| Best Practices | ${bp} |
| SEO | ${seo} |
                
| Core Web Vitals | Value |
|----------------|-------|
| LCP | ${lcp} |
| FID | ${fid} |
| CLS | ${cls} |
| TBT | ${tbt} |

*Full reports uploaded as workflow artifacts.*`;
                
                github.rest.issues.createComment({
                  issue_number: context.issue.number,
                  owner: context.repo.owner,
                  repo: context.repo.repo,
                  body: comment
                });
              }
            }
"""

# Lighthouse budget file
budget = """{
  "ci": {
    "assert": {
      "assertions": {
        "categories:performance": ["error", { "minScore": 0.9 }],
        "categories:accessibility": ["error", { "minScore": 0.9 }],
        "categories:best-practices": ["error", { "minScore": 0.9 }],
        "categories:seo": ["error", { "minScore": 0.9 }],
        "first-contentful-paint": ["error", { "maxNumericValue": 2500 }],
        "largest-contentful-paint": ["error", { "maxNumericValue": 2500 }],
        "cumulative-layout-shift": ["error", { "maxNumericValue": 0.1 }],
        "total-blocking-time": ["error", { "maxNumericValue": 200 }],
        "max-potential-fid": ["warn", { "maxNumericValue": 300 }]
      }
    }
  }
}
"""

def main():
    # Write lighthouserc.js
    (BASE / 'lighthouserc.js').write_text(lighthouserc)
    print("Created lighthouserc.js")
    
    # Write lighthouse-budget.json
    (BASE / 'lighthouse-budget.json').write_text(budget)
    print("Created lighthouse-budget.json")
    
    # Create .github/workflows directory
    workflows_dir = BASE / '.github' / 'workflows'
    workflows_dir.mkdir(parents=True, exist_ok=True)
    
    # Write workflow
    (workflows_dir / 'lighthouse-ci.yml').write_text(github_workflow)
    print("Created .github/workflows/lighthouse-ci.yml")
    
    print("\nDone! Add these files to git and push to enable Lighthouse CI.")

if __name__ == '__main__':
    main()