#!/usr/bin/env python3
"""
Enhance meeting-planner.html with:
1. Better shareable URLs (already has ?cities=id1,id2)
2. Dynamic Open Graph tags based on selected cities
3. Copy/share button for meeting link
4. Enhanced JSON-LD SoftwareApplication with more detail
5. Twitter Card support
"""

from pathlib import Path
import re

BASE = Path('/home/kaliuser/worldtime')
PLANNER_PATH = BASE / 'meeting-planner.html'

html = PLANNER_PATH.read_text(encoding='utf-8')

# 1. Update the JSON-LD SoftwareApplication to be more detailed
old_json_ld = '''    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "WebApplication",
      "name": "Meeting Planner",
      "description": "Find the best time for meetings across multiple time zones",
      "url": "https://worldtimessync.com/meeting-planner.html",
      "applicationCategory": "UtilityApplication",
      "operatingSystem": "Any",
      "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}
    }
    </script>'''

new_json_ld = '''    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "SoftwareApplication",
      "name": "Meeting Planner",
      "description": "Free meeting planner tool to find the best time for a meeting across multiple time zones. Add cities, see overlapping business hours, and schedule with confidence.",
      "url": "https://worldtimessync.com/meeting-planner.html",
      "applicationCategory": "BusinessApplication",
      "operatingSystem": "Any",
      "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD", "availability": "https://schema.org/InStock"},
      "featureList": [
        "Compare up to 8 cities simultaneously",
        "Visual time zone overlap grid (24-hour view)",
        "Business hours (9-17) and working hours (7-22) highlighting",
        "Best meeting time suggestions with quality scoring",
        "Shareable URLs with pre-selected cities",
        "Google Calendar and ICS export",
        "Email reminder capture"
      ],
      "screenshot": "https://worldtimessync.com/og-image.png",
      "softwareVersion": "2026.1",
      "datePublished": "2026-01-15",
      "author": {"@type": "Organization", "name": "World Time Sync", "url": "https://worldtimessync.com"}
    }
    </script>'''

html = html.replace(old_json_ld, new_json_ld)

# 2. Add dynamic Open Graph meta tags that can be updated by JS
# Find the existing OG tags and enhance them
og_section = '''    <!-- Open Graph -->
    <meta property="og:type" content="website" />
    <meta property="og:url" content="https://worldtimessync.com/meeting-planner" />
    <meta property="og:title" content="Meeting Planner - Find the Best Time Across Time Zones" />
    <meta property="og:description" content="Add cities, see overlapping business hours, and find the perfect meeting time for your global team." />
    <meta property="og:site_name" content="World Time Sync" />'''

enhanced_og = '''    <!-- Open Graph (base - dynamically updated by JS for shared URLs) -->
    <meta property="og:type" content="website" />
    <meta property="og:url" content="https://worldtimessync.com/meeting-planner.html" />
    <meta property="og:title" content="Meeting Planner - Find the Best Time Across Time Zones" />
    <meta property="og:description" content="Add cities, see overlapping business hours, and find the perfect meeting time for your global team." />
    <meta property="og:image" content="https://worldtimessync.com/og-image.png" />
    <meta property="og:site_name" content="World Time Sync" />
    <meta property="og:locale" content="en_US" />'''

html = html.replace(og_section, enhanced_og)

# 3. Add Twitter Card meta tags
twitter_section = '''    <!-- Twitter -->
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="Meeting Planner - Find the Best Time Across Time Zones" />
    <meta name="twitter:description" content="Free tool to find overlapping business hours across multiple time zones." />'''

enhanced_twitter = '''    <!-- Twitter -->
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="Meeting Planner - Find the Best Time Across Time Zones" />
    <meta name="twitter:description" content="Free tool to find overlapping business hours across multiple time zones." />
    <meta name="twitter:image" content="https://worldtimessync.com/og-image.png" />
    <meta name="twitter:site" content="@WorldTimeSync" />'''

html = html.replace(twitter_section, enhanced_twitter)

# 4. Add a share/copy link button in the selected cities area
# Find the renderSelected function and add share button
old_render_selected = '''    function renderSelected() {
        selectedEl.innerHTML = selectedCities.map(c => {
            const tzAbbr = getTimezoneAbbr(c.timezone);
            return '<div class="mp-city-chip">' +
                '<span>' + c.name + '</span>' +
                '<span class="tz-abbr">' + tzAbbr + '</span>' +
                '<span class="remove" data-id="' + c.id + '">&times;</span></div>';
        }).join('');'''

new_render_selected = '''    function renderSelected() {
        selectedEl.innerHTML = selectedCities.map(c => {
            const tzAbbr = getTimezoneAbbr(c.timezone);
            return '<div class="mp-city-chip">' +
                '<span>' + c.name + '</span>' +
                '<span class="tz-abbr">' + tzAbbr + '</span>' +
                '<span class="remove" data-id="' + c.id + '">&times;</span></div>';
        }).join('');

        // Show/hide share button
        const shareBtn = document.getElementById('shareLinkBtn');
        if (shareBtn) {
            shareBtn.style.display = selectedCities.length >= 2 ? 'inline-flex' : 'none';
        }'''

html = html.replace(old_render_selected, new_render_selected)

# 5. Add share button HTML after the selected cities container
old_selected_container = '''            <!-- Selected Cities -->
            <div class="mp-selected" id="selectedCities"></div>
            <button class="mp-add-btn" id="addSelectedBtn" disabled>Add City</button>'''

new_selected_container = '''            <!-- Selected Cities -->
            <div class="mp-selected" id="selectedCities"></div>
            <div class="mp-actions">
                <button class="mp-add-btn" id="addSelectedBtn" disabled>Add City</button>
                <button class="mp-share-btn" id="shareLinkBtn" style="display:none" title="Copy shareable link">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8"/><polyline points="16 6 12 2 8 6"/><line x1="12" y1="2" x2="12" y2="15"/></svg>
                    Copy Link
                </button>
            </div>'''

html = html.replace(old_selected_container, new_selected_container)

# 6. Add share link copy functionality in the script section
# Find the updateURL function and enhance it
old_update_url = '''    function updateURL() {
        if (selectedCities.length >= 2) {
            const ids = selectedCities.map(c => c.id).join(',');
            history.replaceState(null, '', '?cities=' + ids);
        } else {
            history.replaceState(null, '', window.location.pathname);
        }
    }'''

new_update_url = '''    function updateURL() {
        if (selectedCities.length >= 2) {
            const ids = selectedCities.map(c => c.id).join(',');
            history.replaceState(null, '', '?cities=' + ids);
        } else {
            history.replaceState(null, '', window.location.pathname);
        }
        updateShareButton();
    }

    function updateShareButton() {
        const shareBtn = document.getElementById('shareLinkBtn');
        if (shareBtn && selectedCities.length >= 2) {
            const ids = selectedCities.map(c => c.id).join(',');
            shareBtn.dataset.url = window.location.origin + window.location.pathname + '?cities=' + ids;
        }
    }

    // Share button click handler
    document.addEventListener('click', function(e) {
        if (e.target.closest('#shareLinkBtn')) {
            const btn = e.target.closest('#shareLinkBtn');
            const url = btn.dataset.url || window.location.href;
            navigator.clipboard.writeText(url).then(() => {
                const original = btn.innerHTML;
                btn.innerHTML = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Copied!';
                btn.classList.add('copied');
                setTimeout(() => {
                    btn.innerHTML = original;
                    btn.classList.remove('copied');
                }, 2000);
            });
        }
    });'''

html = html.replace(old_update_url, new_update_url)

# 7. Add dynamic OG tag updates when cities are selected
# Find the renderSelected function end and add OG update
old_render_end = '''        selectedEl.querySelectorAll('.remove').forEach(el => {
            el.addEventListener('click', function() {
                removeCity(this.dataset.id);
            });
        });
    }'''

new_render_end = '''        selectedEl.querySelectorAll('.remove').forEach(el => {
            el.addEventListener('click', function() {
                removeCity(this.dataset.id);
            });
        });
        updateShareButton();
        updateOpenGraphTags();
    }

    function updateOpenGraphTags() {
        if (selectedCities.length < 2) return;

        const cityNames = selectedCities.map(c => c.name).join(', ');
        const title = 'Meeting Planner: ' + cityNames;
        const desc = 'Find the best meeting time for ' + cityNames + ' across time zones.';

        // Update OG tags
        document.querySelector('meta[property="og:title"]').setAttribute('content', title);
        document.querySelector('meta[property="og:description"]').setAttribute('content', desc);
        document.querySelector('meta[name="twitter:title"]').setAttribute('content', title);
        document.querySelector('meta[name="twitter:description"]').setAttribute('content', desc);

        // Update canonical URL with cities param
        const ids = selectedCities.map(c => c.id).join(',');
        const canonicalUrl = window.location.origin + window.location.pathname + '?cities=' + ids;
        document.querySelector('link[rel="canonical"]').setAttribute('href', canonicalUrl);
        document.querySelector('meta[property="og:url"]').setAttribute('content', canonicalUrl);
    }'''

html = html.replace(old_render_end, new_render_end)

# 8. Add CSS for the share button
old_css_marker = '/* ============ CALENDAR & LEAD MAGNET ============ */'
new_css = '''    /* Share button styles */
    .mp-actions {
        display: flex;
        gap: 8px;
        flex-wrap: wrap;
    }
    .mp-share-btn {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 8px 16px;
        background: #667eea;
        color: #fff;
        border: none;
        border-radius: 8px;
        font-size: 0.85rem;
        font-weight: 500;
        cursor: pointer;
        transition: background 0.2s;
    }
    .mp-share-btn:hover {
        background: #5568d3;
    }
    .mp-share-btn.copied {
        background: #22c55e;
    }
    .mp-share-btn:focus {
        outline: 2px solid #667eea;
        outline-offset: 2px;
    }

/* ============ CALENDAR & LEAD MAGNET ============ */'''

html = html.replace(old_css_marker, new_css)

# Write back
PLANNER_PATH.write_text(html, encoding='utf-8')
print("Enhanced meeting-planner.html with:")
print("  - Enhanced JSON-LD SoftwareApplication schema")
print("  - Dynamic Open Graph tags")
print("  - Twitter Card support")
print("  - Shareable link copy button")
print("  - Dynamic OG tag updates on city selection")
print("  - Share button CSS")