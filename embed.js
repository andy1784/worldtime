/**
 * World Time Sync - Embeddable Widget Loader (embed.js)
 * 
 * Modern async widget loader with postMessage auto-resize support.
 * 
 * Usage:
 *   <div id="wts-clock"></div>
 *   <script async src="https://worldtimessync.com/embed.js"></script>
 *   <script>
 *     WorldTimeSync.init({
 *       container: '#wts-clock',
 *       cities: ['new-york', 'london', 'tokyo'],
 *       theme: 'light',
 *       format: '24h',
 *       showSeconds: false,
 *       showTimezone: true
 *     });
 *   </script>
 * 
 * Or with data attributes on script tag:
 *   <script async src="https://worldtimessync.com/embed.js"
 *           data-container="#wts-clock"
 *           data-cities="new-york,london,tokyo"
 *           data-theme="light"
 *           data-format="24h">
 *   </script>
 */

(function() {
    'use strict';

    // Configuration
    var WIDGET_BASE = 'https://worldtimessync.com/widget-embed.html';
    var SCRIPT_SELECTOR = 'script[src*="worldtimessync.com/embed.js"]';
    var DEFAULT_CITIES = ['new-york', 'london', 'tokyo'];
    var MAX_CITIES = 8;

    // City slug to timezone mapping
    var CITY_TIMEZONES = {
        'new-york': 'America/New_York',
        'los-angeles': 'America/Los_Angeles',
        'chicago': 'America/Chicago',
        'denver': 'America/Denver',
        'toronto': 'America/Toronto',
        'vancouver': 'America/Vancouver',
        'mexico-city': 'America/Mexico_City',
        'sao-paulo': 'America/Sao_Paulo',
        'buenos-aires': 'America/Argentina/Buenos_Aires',
        'london': 'Europe/London',
        'paris': 'Europe/Paris',
        'berlin': 'Europe/Berlin',
        'rome': 'Europe/Rome',
        'madrid': 'Europe/Madrid',
        'amsterdam': 'Europe/Amsterdam',
        'stockholm': 'Europe/Stockholm',
        'warsaw': 'Europe/Warsaw',
        'moscow': 'Europe/Moscow',
        'kyiv': 'Europe/Kiev',
        'istanbul': 'Europe/Istanbul',
        'cairo': 'Africa/Cairo',
        'johannesburg': 'Africa/Johannesburg',
        'lagos': 'Africa/Lagos',
        'dubai': 'Asia/Dubai',
        'riyadh': 'Asia/Riyadh',
        'tehran': 'Asia/Tehran',
        'mumbai': 'Asia/Kolkata',
        'delhi': 'Asia/Kolkata',
        'dhaka': 'Asia/Dhaka',
        'karachi': 'Asia/Karachi',
        'shanghai': 'Asia/Shanghai',
        'beijing': 'Asia/Shanghai',
        'hong-kong': 'Asia/Hong_Kong',
        'singapore': 'Asia/Singapore',
        'tokyo': 'Asia/Tokyo',
        'seoul': 'Asia/Seoul',
        'bangkok': 'Asia/Bangkok',
        'jakarta': 'Asia/Jakarta',
        'manila': 'Asia/Manila',
        'sydney': 'Australia/Sydney',
        'melbourne': 'Australia/Melbourne',
        'brisbane': 'Australia/Brisbane',
        'perth': 'Australia/Perth',
        'auckland': 'Pacific/Auckland',
        'utc': 'UTC'
    };

    // Find our script tag
    var scripts = document.querySelectorAll(SCRIPT_SELECTOR);
    if (!scripts.length) {
        console.error('[WorldTimeSync] embed.js: Could not find script tag');
        return;
    }
    var script = scripts[scripts.length - 1];

    // Parse config from data attributes
    var config = {
        container: script.getAttribute('data-container') || '',
        cities: (script.getAttribute('data-cities') || '').split(',').map(function(s) { return s.trim(); }).filter(Boolean),
        theme: script.getAttribute('data-theme') || 'light',
        format: script.getAttribute('data-format') || '24h',
        showSeconds: script.getAttribute('data-seconds') !== 'false',
        showTimezone: script.getAttribute('data-timezone') !== 'false',
        height: parseInt(script.getAttribute('data-height') || '180', 10),
        width: script.getAttribute('data-width') || '100%'
    };

    // Apply defaults
    if (!config.cities.length) config.cities = DEFAULT_CITIES.slice();
    if (config.cities.length > MAX_CITIES) config.cities = config.cities.slice(0, MAX_CITIES);

    // Convert city slugs to timezones for iframe
    var timezones = config.cities.map(function(slug) {
        return CITY_TIMEZONES[slug] || slug; // Allow direct timezone strings too
    });

    // Build iframe URL
    var params = new URLSearchParams();
    params.set('cities', timezones.join(','));
    params.set('theme', config.theme);
    params.set('format', config.format);
    params.set('seconds', config.showSeconds ? '1' : '0');
    params.set('tz', config.showTimezone ? '1' : '0');
    
    var iframeSrc = WIDGET_BASE + '?' + params.toString();

    // Find or create container
    var container = null;
    if (config.container) {
        container = document.querySelector(config.container);
    }
    
    if (!container) {
        // Create container before script tag
        container = document.createElement('div');
        container.id = 'wts-widget-' + Math.random().toString(36).substr(2, 9);
        if (script.parentNode) {
            script.parentNode.insertBefore(container, script);
        } else {
            document.body.appendChild(container);
        }
    }

    // Style container
    container.style.display = 'block';
    container.style.width = config.width;
    container.style.maxWidth = '100%';
    container.style.position = 'relative';

    // Create iframe
    var iframe = document.createElement('iframe');
    iframe.src = iframeSrc;
    iframe.style.width = '100%';
    iframe.style.height = config.height + 'px';
    iframe.style.border = 'none';
    iframe.style.borderRadius = '8px';
    iframe.style.overflow = 'hidden';
    iframe.style.background = 'transparent';
    iframe.setAttribute('frameborder', '0');
    iframe.setAttribute('scrolling', 'no');
    iframe.setAttribute('title', 'World Time Sync Clock');
    iframe.setAttribute('loading', 'lazy');
    iframe.setAttribute('allow', 'clipboard-read; clipboard-write');

    // Clear and append
    container.innerHTML = '';
    container.appendChild(iframe);

    // Add attribution (required)
    var attr = document.createElement('a');
    attr.href = 'https://worldtimessync.com/';
    attr.target = '_blank';
    attr.rel = 'noopener noreferrer';
    attr.style.cssText = 'display:block;text-align:right;font-size:10px;color:rgba(128,128,128,0.6);text-decoration:none;margin-top:4px;font-family:system-ui,sans-serif;';
    attr.textContent = 'World Time Sync';
    container.appendChild(attr);

    // Handle postMessage resize from iframe
    function handleMessage(e) {
        if (e.origin !== 'https://worldtimessync.com') return;
        if (!e.data || e.data.type !== 'wts-resize') return;
        if (e.data.height && typeof e.data.height === 'number') {
            iframe.style.height = e.data.height + 'px';
        }
    }

    if (window.addEventListener) {
        window.addEventListener('message', handleMessage);
    } else if (window.attachEvent) {
        window.attachEvent('onmessage', handleMessage);
    }

    // Public API
    window.WorldTimeSync = {
        init: function(options) {
            // Allow programmatic re-initialization
            if (options) {
                if (options.container) config.container = options.container;
                if (options.cities) config.cities = options.cities.slice(0, MAX_CITIES);
                if (options.theme) config.theme = options.theme;
                if (options.format) config.format = options.format;
                if (typeof options.showSeconds === 'boolean') config.showSeconds = options.showSeconds;
                if (typeof options.showTimezone === 'boolean') config.showTimezone = options.showTimezone;
                if (options.height) config.height = options.height;
                if (options.width) config.width = options.width;
                
                // Rebuild and reload
                timezones = config.cities.map(function(slug) {
                    return CITY_TIMEZONES[slug] || slug;
                });
                params = new URLSearchParams();
                params.set('cities', timezones.join(','));
                params.set('theme', config.theme);
                params.set('format', config.format);
                params.set('seconds', config.showSeconds ? '1' : '0');
                params.set('tz', config.showTimezone ? '1' : '0');
                iframeSrc = WIDGET_BASE + '?' + params.toString();
                iframe.src = iframeSrc;
                
                // Re-find container
                var newContainer = config.container ? document.querySelector(config.container) : container;
                if (newContainer && newContainer !== container) {
                    newContainer.innerHTML = '';
                    newContainer.style.display = 'block';
                    newContainer.style.width = config.width;
                    newContainer.style.maxWidth = '100%';
                    newContainer.style.position = 'relative';
                    
                    var newIframe = iframe.cloneNode(true);
                    newIframe.src = iframeSrc;
                    newIframe.style.height = config.height + 'px';
                    newContainer.appendChild(newIframe);
                    
                    var newAttr = attr.cloneNode(true);
                    newContainer.appendChild(newAttr);
                    
                    container = newContainer;
                    iframe = newIframe;
                } else {
                    iframe.src = iframeSrc;
                }
            }
            return window.WorldTimeSync;
        },
        
        // Update specific config
        setCities: function(cities) {
            return window.WorldTimeSync.init({ cities: cities });
        },
        
        setTheme: function(theme) {
            return window.WorldTimeSync.init({ theme: theme });
        },
        
        destroy: function() {
            if (container && container.parentNode) {
                container.parentNode.removeChild(container);
            }
            if (window.removeEventListener) {
                window.removeEventListener('message', handleMessage);
            } else if (window.detachEvent) {
                window.detachEvent('onmessage', handleMessage);
            }
            delete window.WorldTimeSync;
        }
    };

    // Auto-init if data attributes present
    if (script.hasAttribute('data-container') || script.hasAttribute('data-cities')) {
        // Already initialized via config above
    }

})();