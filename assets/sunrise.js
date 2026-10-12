/* World Time Sync — Sunrise/Sunset Calculator */
/* Loaded on city pages to show sunrise/sunset times */
(function(){
    var els = document.querySelectorAll('[data-sunrise-lat]');
    if(!els.length) return;
    var RAD = Math.PI / 180;
    // Returns the zone's UTC offset in hours at the given instant (default: now).
    function tzOffsetHours(tz, at) {
        var now = at || new Date();
        if (!tz) return -now.getTimezoneOffset() / 60;
        try {
            var utcStr = now.toLocaleString("en-US", {timeZone: "UTC"});
            var tzStr = now.toLocaleString("en-US", {timeZone: tz});
            return (new Date(tzStr) - new Date(utcStr)) / 3600000;
        } catch(e) { return 0; }
    }
    // Returns sunrise/sunset in minutes after local midnight (in the city's time zone).
    function calcSun(lat, lon, offsetH, stdOffsetH, d) {
        var start = new Date(d.getFullYear(), 0, 0);
        var dayOfYear = Math.floor((d - start) / 86400000);
        var decl = Math.asin(0.39795 * Math.sin(0.98563 * (dayOfYear - 81) * RAD));
        var latR = lat * RAD;
        var cosH = (Math.cos(90.833 * RAD) - Math.sin(decl) * Math.sin(latR)) / (Math.cos(decl) * Math.cos(latR));
        if (cosH > 1) return {polarNight: true};
        if (cosH < -1) return {polarDay: true};
        var H = Math.acos(cosH) / RAD;
        var b = (360 / 365) * (dayOfYear - 81) * RAD;
        var eqt = 9.87 * Math.sin(2 * b) - 7.53 * Math.cos(b) - 1.5 * Math.sin(b);
        // Without an explicit longitude, assume the city sits on its standard-time meridian.
        if (isNaN(lon)) lon = stdOffsetH * 15;
        var noonMin = 720 - 4 * lon - eqt + offsetH * 60;
        return {rise: noonMin - H * 4, set: noonMin + H * 4, polarNight: false, polarDay: false};
    }
    function fmtMin(mins) {
        if (mins == null || isNaN(mins)) return "--:--";
        var total = ((Math.round(mins) % 1440) + 1440) % 1440;
        var h = Math.floor(total / 60);
        var m = total % 60;
        return (h < 10 ? "0" : "") + h + ":" + (m < 10 ? "0" : "") + m;
    }
    function update(el) {
        var lat = parseFloat(el.getAttribute('data-sunrise-lat'));
        var lon = parseFloat(el.getAttribute('data-sunrise-lon'));
        var tzEl = el.hasAttribute('data-sunrise-tz') ? el : document.querySelector('[data-sunrise-tz]');
        var tz = tzEl ? tzEl.getAttribute('data-sunrise-tz') : '';
        var now = new Date();
        var offsetH = tzOffsetHours(tz, now);
        var stdOffsetH = Math.min(tzOffsetHours(tz, new Date(now.getFullYear(), 0, 1)), tzOffsetHours(tz, new Date(now.getFullYear(), 6, 1)));
        var result = calcSun(lat, lon, offsetH, stdOffsetH, now);
        if (result.polarNight) {
            el.innerHTML = '<div class="sun-item"><span class="sun-label">Sun does not rise</span><span class="sun-note">Polar night</span></div>';
            return;
        }
        if (result.polarDay) {
            el.innerHTML = '<div class="sun-item"><span class="sun-label">Sun does not set</span><span class="sun-note">Midnight sun</span></div>';
            return;
        }
        var riseStr = fmtMin(result.rise);
        var setStr = fmtMin(result.set);
        var dayLen = Math.round(result.set - result.rise);
        var dlH = Math.floor(dayLen / 60);
        var dlM = dayLen % 60;
        el.innerHTML = '<div class="sun-item"><span class="sun-icon">🌅</span><span class="sun-label">Sunrise</span><span class="sun-time">' + riseStr + '</span></div>' +
            '<div class="sun-item"><span class="sun-icon">🌇</span><span class="sun-label">Sunset</span><span class="sun-time">' + setStr + '</span></div>' +
            '<div class="sun-item"><span class="sun-icon">☀️</span><span class="sun-label">Daylight</span><span class="sun-time">' + dlH + 'h ' + dlM + 'm</span></div>';
    }
    for (var i = 0; i < els.length; i++) {
        update(els[i]);
        setInterval(function(e){ update(e); }, 60000, els[i]);
    }
})();
