/* World Time Sync — Sunrise/Sunset Calculator */
/* Loaded on city pages to show sunrise/sunset times */
(function(){
    var els = document.querySelectorAll('[data-sunrise-lat]');
    if(!els.length) return;
    function calcSun(lat, d) {
        var start = new Date(d.getFullYear(), 0, 0);
        var dayOfYear = Math.floor((d - start) / 86400000);
        var decl = 0.39795 * Math.sin(0.98563 * (dayOfYear - 81) * Math.PI / 180);
        var latR = lat * Math.PI / 180;
        var cosH = (Math.cos(90.833 * Math.PI / 180) - Math.sin(decl) * Math.sin(latR)) / (Math.cos(decl) * Math.cos(latR));
        if (cosH > 1) return {polarNight: true};
        if (cosH < -1) return {polarDay: true};
        var H = Math.acos(cosH) * 180 / Math.PI;
        var b = (360 / 365) * (dayOfYear - 81) * Math.PI / 180;
        var eqt = 9.87 * Math.sin(2 * b) - 7.53 * Math.cos(b) - 1.5 * Math.sin(b);
        var noonMin = 720 - 4 * (getLon()) - eqt;
        return {rise: noonMin - H * 4, set: noonMin + H * 4, polarNight: false, polarDay: false};
    }
    function getLon() {
        var tz = document.querySelector('[data-sunrise-tz]');
        if(!tz) return 0;
        tz = tz.getAttribute('data-sunrise-tz');
        try {
            var now = new Date();
            var utcStr = now.toLocaleString("en-US", {timeZone: "UTC"});
            var tzStr = now.toLocaleString("en-US", {timeZone: tz});
            return (new Date(tzStr) - new Date(utcStr)) / 3600000 * 15;
        } catch(e) { return 0; }
    }
    function fmtMin(mins) {
        if (mins == null) return "--:--";
        var h = Math.floor(mins / 60) % 24;
        var m = Math.round(mins % 60);
        if (h < 0) h += 24;
        return (h < 10 ? "0" : "") + h + ":" + (m < 10 ? "0" : "") + m;
    }
    function update(el) {
        var lat = parseFloat(el.getAttribute('data-sunrise-lat'));
        var result = calcSun(lat, new Date());
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
        var dayLen = result.set - result.rise;
        var dlH = Math.floor(dayLen / 60);
        var dlM = Math.round(dayLen % 60);
        el.innerHTML = '<div class="sun-item"><span class="sun-icon">🌅</span><span class="sun-label">Sunrise</span><span class="sun-time">' + riseStr + '</span></div>' +
            '<div class="sun-item"><span class="sun-icon">🌇</span><span class="sun-label">Sunset</span><span class="sun-time">' + setStr + '</span></div>' +
            '<div class="sun-item"><span class="sun-icon">☀️</span><span class="sun-label">Daylight</span><span class="sun-time">' + dlH + 'h ' + dlM + 'm</span></div>';
    }
    for (var i = 0; i < els.length; i++) {
        update(els[i]);
        setInterval(function(e){ update(e); }, 60000, els[i]);
    }
})();
