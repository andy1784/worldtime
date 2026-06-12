/**
 * World Time Sync - Embeddable Clock Widget
 * 
 * Usage:
 *   <div id="wts-widget"></div>
 *   <script src="https://worldtimessync.com/widget.js" 
 *           data-timezone="America/New_York" 
 *           data-theme="dark"
 *           data-size="medium">
 *   </script>
 * 
 * Options:
 *   data-timezone  - IANA timezone (default: America/New_York)
 *   data-theme     - "dark" or "light" (default: dark)
 *   data-size      - "small", "medium", "large" (default: medium)
 *   data-show-date - "true" or "false" (default: true)
 *   data-bg        - Custom background color (optional)
 *   data-text      - Custom text color (optional)
 */

(function() {
    'use strict';

    // Find the script tag that loaded this widget
    var scripts = document.querySelectorAll('script[src*="worldtimessync.com/widget.js"]');
    if (!scripts.length) {
        console.error('[World Time Sync] Unable to find widget script tag');
        return;
    }
    
    var config = {};
    try {
        // Parse data attributes from the last script tag
        var script = scripts[scripts.length - 1];
        config.timezone = script.getAttribute('data-timezone') || 'America/New_York';
        config.theme = script.getAttribute('data-theme') || 'dark';
        config.size = script.getAttribute('data-size') || 'medium';
        config.showDate = script.getAttribute('data-show-date') !== 'false';
        config.backgroundColor = script.getAttribute('data-bg') || '';
        config.textColor = script.getAttribute('data-text') || '';
        config.targetId = script.getAttribute('data-target') || '';
    } catch(e) {
        console.error('[World Time Sync] Error parsing config:', e);
    }

    // Widget URL builder
    var baseUrl = 'https://worldtimessync.com';
    var params = [];
    params.push('tz=' + encodeURIComponent(config.timezone));
    params.push('theme=' + encodeURIComponent(config.theme));
    params.push('size=' + encodeURIComponent(config.size));
    params.push('date=' + (config.showDate ? '1' : '0'));
    if (config.backgroundColor) params.push('bg=' + encodeURIComponent(config.backgroundColor));
    if (config.textColor) params.push('text=' + encodeURIComponent(config.textColor));
    
    var widgetUrl = baseUrl + '/widget-embed.html?' + params.join('&');

    // Size presets
    var sizes = {
        small: { width: '220px', height: '120px' },
        medium: { width: '300px', height: '160px' },
        large: { width: '420px', height: '220px' }
    };
    var dims = sizes[config.size] || sizes.medium;

    // Find target container
    var container = null;
    if (config.targetId) {
        container = document.getElementById(config.targetId);
    }
    
    // If no target specified, insert before the script tag
    if (!container) {
        // Create a placeholder before the script tag
        container = document.createElement('div');
        container.id = 'wts-widget-' + Math.random().toString(36).substr(2, 9);
        if (script && script.parentNode) {
            document.currentScript = script;
            script.parentNode.insertBefore(container, script);
        } else {
            // Fallback: append to body
            document.body.appendChild(container);
        }
    }

    // Create iframe
    var iframe = document.createElement('iframe');
    iframe.src = widgetUrl;
    iframe.style.width = dims.width;
    iframe.style.height = dims.height;
    iframe.style.border = 'none';
    iframe.style.borderRadius = '12px';
    iframe.style.overflow = 'hidden';
    iframe.setAttribute('frameborder', '0');
    iframe.setAttribute('scrolling', 'no');
    iframe.setAttribute('title', 'World Time Sync Clock');
    iframe.setAttribute('loading', 'lazy');

    // Widget container styling
    container.style.display = 'inline-block';
    container.style.position = 'relative';

    // Clear container and add iframe
    container.innerHTML = '';
    container.appendChild(iframe);

    // Add attribution link (required by our terms)
    var attr = document.createElement('a');
    attr.href = baseUrl + '/time/' + slugify(config.timezone);
    attr.target = '_blank';
    attr.rel = 'noopener noreferrer';
    attr.style.cssText = 'display:block;text-align:right;font-size:10px;color:rgba(128,128,128,0.5);text-decoration:none;margin-top:2px;font-family:system-ui,sans-serif;';
    attr.textContent = 'World Time Sync';
    container.appendChild(attr);

    function slugify(tz) {
        var parts = tz.split('/');
        var city = parts[parts.length - 1].toLowerCase().replace(/[^a-z0-9]+/g, '-');
        return city.replace(/^-|-$/g, '');
    }

    // Handle iframe resize messages
    window.addEventListener('message', function(e) {
        if (e.origin !== baseUrl) return;
        if (e.data && e.data.type === 'wts-resize' && e.data.height) {
            iframe.style.height = e.data.height + 'px';
        }
    });
})();
