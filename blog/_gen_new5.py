#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 5 new EN blog posts in the existing site style.
Imports templates from /tmp/regen_head.py (extracted WITHOUT the generation loop,
so no side effects on existing posts).
"""
import sys, importlib.util, os
spec = importlib.util.spec_from_file_location("regen_head", "/tmp/regen_head.py")
regen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(regen)
build_head = regen.build_head
ARTICLE_TEMPLATE = regen.ARTICLE_TEMPLATE
TAIL = regen.TAIL
BLOG_DIR = regen.BLOG_DIR

# --- content blocks (same as before) ---
C1 = '''<p>Tokyo and London sit on opposite sides of the business world, and the gap between them is one of the largest you'll routinely manage: 9 hours in winter and 8 in summer. A Tokyo morning is London's late afternoon/evening of the previous day. Here's how to keep calls sane.</p>

<h2>Time Zone Overview</h2>
<h3>Tokyo (JST)</h3>
<p>Tokyo uses Japan Standard Time (JST), which is UTC+9 all year. Japan does not observe daylight saving time, so its offset never changes.</p>
<h3>London (GMT/BST)</h3>
<p>London is GMT (UTC+0) in winter and BST (UTC+1) in summer under the UK daylight saving schedule (late March to late October).</p>

<h2>Time Difference</h2>
<p><strong>London winter:</strong> Tokyo is 9 hours ahead of London.</p>
<p><strong>London summer:</strong> Tokyo is 8 hours ahead of London.</p>
<p>Because Japan has no DST, the only movement comes from London's switch.</p>

<h2>Conversion Formula</h2>
<p><strong>Time in Tokyo = Time in London + 9 hours (winter) or + 8 hours (summer)</strong></p>

<h2>Quick Reference Table (London GMT → Tokyo JST)</h2>
<table><thead><tr><th>London</th><th>Tokyo</th></tr></thead><tbody>
<tr><td>8:00 AM</td><td>5:00 PM</td></tr>
<tr><td>12:00 PM</td><td>9:00 PM</td></tr>
<tr><td>3:00 PM</td><td>12:00 AM (next day)</td></tr>
<tr><td>6:00 PM</td><td>3:00 AM (next day)</td></tr>
<tr><td>9:00 PM</td><td>6:00 AM (next day)</td></tr>
<tr><td>11:59 PM</td><td>8:59 AM (next day)</td></tr>
</tbody></table>

<div class="converter-widget">
    <h2>Time Zone Converter</h2>
    <div class="converter-row"><label for="from-time">Time in London:</label><input type="time" id="from-time" value="09:00"></div>
    <div class="converter-row"><label for="dst">London on:</label>
      <select id="dst"><option value="9">GMT (winter) Tokyo +9h</option><option value="8" selected>BST (summer) Tokyo +8h</option></select></div>
    <div class="converter-row"><label for="to-time">Time in Tokyo:</label><input type="time" id="to-time" readonly></div>
</div>
<script>
document.addEventListener('DOMContentLoaded', function() {
    var f=document.getElementById('from-time'), d=document.getElementById('dst'), t=document.getElementById('to-time');
    function cv(){ if(!f.value) return; var p=f.value.split(':').map(Number); var m=p[0]*60+p[1]+parseInt(d.value)*60; while(m<0)m+=1440; while(m>=1440)m-=1440; t.value=String(Math.floor(m/60)).padStart(2,'0')+':'+String(m%60).padStart(2,'0'); }
    f.addEventListener('input', cv); d.addEventListener('change', cv); cv();
});
</script>

<h2>Common Use Cases</h2>
<ul>
<li>Finance and trading desks linking London and Tokyo markets</li>
<li>Game and software launches coordinated for a global midnight</li>
<li>Remote engineers on a Tokyo team with London stakeholders</li>
<li>Family video calls across the Eurasia gap</li>
</ul>

<h2>Frequently Asked Questions</h2>
<div class="faq-section">
<div class="faq-item"><h3>What is the time difference between Tokyo and London?</h3><p>9 hours in London winter, 8 in summer. Tokyo is always ahead.</p></div>
<div class="faq-item"><h3>Does Tokyo observe DST?</h3><p>No. Japan stays on JST (UTC+9) all year.</p></div>
<div class="faq-item"><h3>If it's 9 AM in London, what time is it in Tokyo?</h3><p>6 PM JST (winter) or 5 PM JST (summer BST).</p></div>
<div class="faq-item"><h3>Best overlap for a meeting?</h3><p>8-10 AM London = 5-7 PM Tokyo (winter). Limited but workable.</p></div>
<div class="faq-item"><h3>Is Tokyo ahead of London?</h3><p>Yes, by 8-9 hours.</p></div>
</div>
<p>Use our <a href="/">world clock</a> and <a href="/meeting-planner.html">meeting planner</a> for live conversion.</p>'''

C2 = '''<p>Singapore and London form a major financial corridor, and it's one of the more predictable ones: Singapore is 8 hours ahead of London in winter and 7 hours ahead in summer. No surprises from Singapore's side — it stays on one offset all year.</p>

<h2>Time Zone Overview</h2>
<h3>Singapore (SGT)</h3>
<p>Singapore uses Singapore Standard Time (SGT), which is UTC+8 year-round. Singapore does not observe daylight saving time.</p>
<h3>London (GMT/BST)</h3>
<p>London is GMT (UTC+0) in winter and BST (UTC+1) in summer.</p>

<h2>Time Difference</h2>
<p><strong>London winter:</strong> Singapore is 8 hours ahead.</p>
<p><strong>London summer:</strong> Singapore is 7 hours ahead.</p>
<p>Singapore's offset is fixed; only London's switch moves the gap.</p>

<h2>Conversion Formula</h2>
<p><strong>Time in Singapore = Time in London + 8 hours (winter) or + 7 hours (summer)</strong></p>

<h2>Quick Reference Table (London GMT → Singapore SGT)</h2>
<table><thead><tr><th>London</th><th>Singapore</th></tr></thead><tbody>
<tr><td>8:00 AM</td><td>4:00 PM</td></tr>
<tr><td>12:00 PM</td><td>8:00 PM</td></tr>
<tr><td>3:00 PM</td><td>11:00 PM</td></tr>
<tr><td>6:00 PM</td><td>2:00 AM (next day)</td></tr>
<tr><td>9:00 PM</td><td>5:00 AM (next day)</td></tr>
<tr><td>11:00 PM</td><td>7:00 AM (next day)</td></tr>
</tbody></table>

<div class="converter-widget">
    <h2>Time Zone Converter</h2>
    <div class="converter-row"><label for="from-time">Time in London:</label><input type="time" id="from-time" value="09:00"></div>
    <div class="converter-row"><label for="dst">London on:</label>
      <select id="dst"><option value="8">GMT (winter) Singapore +8h</option><option value="7" selected>BST (summer) Singapore +7h</option></select></div>
    <div class="converter-row"><label for="to-time">Time in Singapore:</label><input type="time" id="to-time" readonly></div>
</div>
<script>
document.addEventListener('DOMContentLoaded', function() {
    var f=document.getElementById('from-time'), d=document.getElementById('dst'), t=document.getElementById('to-time');
    function cv(){ if(!f.value) return; var p=f.value.split(':').map(Number); var m=p[0]*60+p[1]+parseInt(d.value)*60; while(m<0)m+=1440; while(m>=1440)m-=1440; t.value=String(Math.floor(m/60)).padStart(2,'0')+':'+String(m%60).padStart(2,'0'); }
    f.addEventListener('input', cv); d.addEventListener('change', cv); cv();
});
</script>

<h2>Common Use Cases</h2>
<ul>
<li>UK–Singapore trade, banking, and shipping</li>
<li>Coordinating APAC teams with London HQ</li>
<li>Planning calls between the City and Marina Bay</li>
<li>Following Asian market opens from Europe</li>
</ul>

<h2>Frequently Asked Questions</h2>
<div class="faq-section">
<div class="faq-item"><h3>What is the time difference between Singapore and London?</h3><p>8 hours in London winter, 7 in summer. Singapore is ahead.</p></div>
<div class="faq-item"><h3>Does Singapore observe DST?</h3><p>No. SGT (UTC+8) is constant year-round.</p></div>
<div class="faq-item"><h3>If it's 9 AM in London, what time is it in Singapore?</h3><p>5 PM SGT (winter) or 4 PM SGT (summer BST).</p></div>
<div class="faq-item"><h3>Best overlap for a meeting?</h3><p>9 AM-12 PM London = 5-8 PM Singapore (winter). Comfortable window.</p></div>
<div class="faq-item"><h3>Is Singapore ahead of London?</h3><p>Yes, by 7-8 hours.</p></div>
</div>
<p>Use our <a href="/">world clock</a> and <a href="/meeting-planner.html">meeting planner</a> for live conversion.</p>'''

C3 = '''<p>Tokyo and Sydney are close enough to feel manageable but far enough to trip you up: the gap is just 1 hour in winter and 2 hours in summer, because the two countries handle daylight saving on opposite schedules. Here's the clean breakdown.</p>

<h2>Time Zone Overview</h2>
<h3>Tokyo (JST)</h3>
<p>Tokyo is JST (UTC+9) all year. Japan has no daylight saving time.</p>
<h3>Sydney (AEST/AEDT)</h3>
<p>Sydney is AEST (UTC+10) in winter and AEDT (UTC+11) during Australian daylight saving (first Sunday in October to first Sunday in April).</p>

<h2>Time Difference</h2>
<p><strong>Australian summer / Japan winter:</strong> Sydney is 2 hours ahead of Tokyo.</p>
<p><strong>Australian winter / Japan summer:</strong> Sydney is 1 hour ahead of Tokyo.</p>
<p>Japan never moves; the gap shifts only when Australia switches.</p>

<h2>Conversion Formula</h2>
<p><strong>Time in Sydney = Time in Tokyo + 2 hours (Australia summer) or + 1 hour (Australia winter)</strong></p>

<h2>Quick Reference Table (Tokyo JST → Sydney)</h2>
<table><thead><tr><th>Tokyo</th><th>Sydney (AEDT, Aus summer)</th><th>Sydney (AEST, Aus winter)</th></tr></thead><tbody>
<tr><td>8:00 AM</td><td>10:00 AM</td><td>9:00 AM</td></tr>
<tr><td>12:00 PM</td><td>2:00 PM</td><td>1:00 PM</td></tr>
<tr><td>3:00 PM</td><td>5:00 PM</td><td>4:00 PM</td></tr>
<tr><td>6:00 PM</td><td>8:00 PM</td><td>7:00 PM</td></tr>
<tr><td>9:00 PM</td><td>11:00 PM</td><td>10:00 PM</td></tr>
<tr><td>11:00 PM</td><td>1:00 AM (next day)</td><td>12:00 AM (next day)</td></tr>
</tbody></table>

<div class="converter-widget">
    <h2>Time Zone Converter</h2>
    <div class="converter-row"><label for="from-time">Time in Tokyo:</label><input type="time" id="from-time" value="15:00"></div>
    <div class="converter-row"><label for="dst">Sydney on:</label>
      <select id="dst"><option value="120">AEDT (Aus summer) +2h</option><option value="60" selected>AEST (Aus winter) +1h</option></select></div>
    <div class="converter-row"><label for="to-time">Time in Sydney:</label><input type="time" id="to-time" readonly></div>
</div>
<script>
document.addEventListener('DOMContentLoaded', function() {
    var f=document.getElementById('from-time'), d=document.getElementById('dst'), t=document.getElementById('to-time');
    function cv(){ if(!f.value) return; var p=f.value.split(':').map(Number); var m=p[0]*60+p[1]+parseInt(d.value); while(m<0)m+=1440; while(m>=1440)m-=1440; t.value=String(Math.floor(m/60)).padStart(2,'0')+':'+String(m%60).padStart(2,'0'); }
    f.addEventListener('input', cv); d.addEventListener('change', cv); cv();
});
</script>

<h2>Common Use Cases</h2>
<ul>
<li>Japan–Australia business and tourism</li>
<li>Coordinating creatives and engineers across the Pacific Rim</li>
<li>Sports and esports events spanning both markets</li>
<li>Family calls between Tokyo and Sydney</li>
</ul>

<h2>Frequently Asked Questions</h2>
<div class="faq-section">
<div class="faq-item"><h3>What is the time difference between Tokyo and Sydney?</h3><p>1 hour in Australian winter, 2 in Australian summer. Sydney is ahead.</p></div>
<div class="faq-item"><h3>Does Tokyo observe DST?</h3><p>No. Tokyo stays on JST (UTC+9) all year.</p></div>
<div class="faq-item"><h3>If it's 3 PM in Tokyo, what time is it in Sydney?</h3><p>5 PM AEDT (Aus summer) or 4 PM AEST (Aus winter).</p></div>
<div class="faq-item"><h3>Best overlap for a meeting?</h3><p>9 AM-5 PM Tokyo = 10 AM-7 PM Sydney (summer). Very workable.</p></div>
<div class="faq-item"><h3>Is Sydney ahead of Tokyo?</h3><p>Yes, by 1-2 hours.</p></div>
</div>
<p>Use our <a href="/">world clock</a> and <a href="/meeting-planner.html">meeting planner</a> for live conversion.</p>'''

C4 = '''<p>Converting Greenwich Mean Time (GMT) to Indian Standard Time (IST) is a daily need for anyone bridging Europe/Africa and India. The one thing to remember: India runs on a half-hour offset, UTC+5:30, and never changes it. That half hour is what catches people out.</p>

<h2>Time Zone Overview</h2>
<h3>Greenwich Mean Time (GMT)</h3>
<p>GMT is UTC+0 in winter. The UK switches to BST (UTC+1) in summer, so the reference point shifts.</p>
<h3>Indian Standard Time (IST)</h3>
<p>IST is UTC+5:30 all year. India does not observe daylight saving time, so the offset is fixed.</p>

<h2>Time Difference</h2>
<p><strong>UK winter (GMT):</strong> India is 5 hours 30 minutes ahead of GMT.</p>
<p><strong>UK summer (BST):</strong> India is 4 hours 30 minutes ahead of London.</p>

<h2>Conversion Formula</h2>
<p><strong>IST = GMT + 5 hours 30 minutes (winter) / GMT + 4 hours 30 minutes (UK summer)</strong></p>

<h2>Conversion Examples</h2>
<p><strong>Winter:</strong> 9:00 GMT → 14:30 IST</p>
<p><strong>Summer:</strong> 9:00 BST → 13:30 IST</p>
<p>Watch the half hour. 12:00 GMT is 17:30 IST, not 17:00.</p>

<h2>Quick Reference Table (GMT → IST)</h2>
<table><thead><tr><th>GMT (London winter)</th><th>IST</th><th>BST (London summer)</th><th>IST</th></tr></thead><tbody>
<tr><td>6:00 AM</td><td>11:30 AM</td><td>6:00 AM</td><td>10:30 AM</td></tr>
<tr><td>9:00 AM</td><td>2:30 PM</td><td>9:00 AM</td><td>1:30 PM</td></tr>
<tr><td>12:00 PM</td><td>5:30 PM</td><td>12:00 PM</td><td>4:30 PM</td></tr>
<tr><td>3:00 PM</td><td>8:30 PM</td><td>3:00 PM</td><td>7:30 PM</td></tr>
<tr><td>6:00 PM</td><td>11:30 PM</td><td>6:00 PM</td><td>10:30 PM</td></tr>
<tr><td>9:00 PM</td><td>2:30 AM (next day)</td><td>9:00 PM</td><td>1:30 AM (next day)</td></tr>
</tbody></table>

<div class="converter-widget">
    <h2>Time Zone Converter</h2>
    <div class="converter-row"><label for="from-time">Time in London:</label><input type="time" id="from-time" value="09:00"></div>
    <div class="converter-row"><label for="dst">London on:</label>
      <select id="dst"><option value="330">GMT (winter) IST +5h30m</option><option value="270" selected>BST (summer) IST +4h30m</option></select></div>
    <div class="converter-row"><label for="to-time">Time in India:</label><input type="time" id="to-time" readonly></div>
</div>
<script>
document.addEventListener('DOMContentLoaded', function() {
    var f=document.getElementById('from-time'), d=document.getElementById('dst'), t=document.getElementById('to-time');
    function cv(){ if(!f.value) return; var p=f.value.split(':').map(Number); var m=p[0]*60+p[1]+parseInt(d.value); while(m<0)m+=1440; while(m>=1440)m-=1440; t.value=String(Math.floor(m/60)).padStart(2,'0')+':'+String(m%60).padStart(2,'0'); }
    f.addEventListener('input', cv); d.addEventListener('change', cv); cv();
});
</script>

<h2>Common Use Cases</h2>
<ul>
<li>Outsourcing and IT team coordination between the UK and India</li>
<li>Scheduling calls between London and Bangalore, Mumbai, or Delhi</li>
<li>Tracking Indian market hours from Europe</li>
<li>Family and personal calls across the regions</li>
</ul>

<h2>Frequently Asked Questions</h2>
<div class="faq-section">
<div class="faq-item"><h3>What is the time difference between GMT and IST?</h3><p>5 hours 30 minutes in UK winter, 4 hours 30 minutes in summer.</p></div>
<div class="faq-item"><h3>Why the half hour?</h3><p>India deliberately uses UTC+5:30 and keeps it year-round.</p></div>
<div class="faq-item"><h3>If it's 9 AM GMT, what time is it in India?</h3><p>2:30 PM IST (winter) or 1:30 PM IST (summer BST).</p></div>
<div class="faq-item"><h3>Does India observe DST?</h3><p>No. IST is UTC+5:30 all year.</p></div>
<div class="faq-item"><h3>How do I convert IST to GMT?</h3><p>Subtract 5h30m in winter or 4h30m in UK summer.</p></div>
</div>
<p>Use our <a href="/">world clock</a> and <a href="/meeting-planner.html">meeting planner</a> for date-specific planning.</p>'''

C5 = '''<p>Converting UTC (Coordinated Universal Time) to Eastern Standard Time (EST) is the backbone of scheduling across the Americas. UTC is the neutral reference the entire internet runs on, and EST is UTC−5. Here's the straightforward math.</p>

<h2>Time Zone Overview</h2>
<h3>Coordinated Universal Time (UTC)</h3>
<p>UTC is the primary time standard, UTC+0, with no daylight saving time. Servers, aviation, and global logs all use it.</p>
<h3>Eastern Time (EST/EDT)</h3>
<p>US Eastern Time is EST (UTC−5) in winter and EDT (UTC−4) during US daylight saving (second Sunday in March to first Sunday in November).</p>

<h2>Time Difference</h2>
<p><strong>Winter (EST):</strong> UTC is 5 hours ahead of EST.</p>
<p><strong>Summer (EDT):</strong> UTC is 4 hours ahead of EDT.</p>

<h2>Conversion Formula</h2>
<p><strong>EST = UTC − 5 hours (winter) / UTC − 4 hours (summer)</strong></p>

<h2>Conversion Examples</h2>
<p><strong>Winter:</strong> 14:00 UTC → 9:00 EST</p>
<p><strong>Summer:</strong> 14:00 UTC → 10:00 EDT</p>
<p>When a meeting is "at 18:00 UTC", that's 1:00 PM EST in winter or 2:00 PM EDT in summer.</p>

<h2>Quick Reference Table (UTC → EST/EDT)</h2>
<table><thead><tr><th>UTC</th><th>EST (winter)</th><th>EDT (summer)</th></tr></thead><tbody>
<tr><td>00:00</td><td>7:00 PM (prev day)</td><td>8:00 PM (prev day)</td></tr>
<tr><td>05:00</td><td>12:00 AM</td><td>1:00 AM</td></tr>
<tr><td>10:00</td><td>5:00 AM</td><td>6:00 AM</td></tr>
<tr><td>14:00</td><td>9:00 AM</td><td>10:00 AM</td></tr>
<tr><td>18:00</td><td>1:00 PM</td><td>2:00 PM</td></tr>
<tr><td>22:00</td><td>5:00 PM</td><td>6:00 PM</td></tr>
</tbody></table>

<div class="converter-widget">
    <h2>Time Zone Converter</h2>
    <div class="converter-row"><label for="from-time">Time in UTC:</label><input type="time" id="from-time" value="14:00"></div>
    <div class="converter-row"><label for="dst">US East on:</label>
      <select id="dst"><option value="300">EST (winter) −5h</option><option value="240" selected>EDT (summer) −4h</option></select></div>
    <div class="converter-row"><label for="to-time">Time in Eastern:</label><input type="time" id="to-time" readonly></div>
</div>
<script>
document.addEventListener('DOMContentLoaded', function() {
    var f=document.getElementById('from-time'), d=document.getElementById('dst'), t=document.getElementById('to-time');
    function cv(){ if(!f.value) return; var p=f.value.split(':').map(Number); var m=p[0]*60+p[1]-parseInt(d.value); while(m<0)m+=1440; while(m>=1440)m-=1440; t.value=String(Math.floor(m/60)).padStart(2,'0')+':'+String(m%60).padStart(2,'0'); }
    f.addEventListener('input', cv); d.addEventListener('change', cv); cv();
});
</script>

<h2>Common Use Cases</h2>
<ul>
<li>Reading server logs and API timestamps (always UTC)</li>
<li>Scheduling global product launches on a UTC mark</li>
<li>Converting flight and train times quoted in UTC</li>
<li>Coordinating with US East Coast teams from any UTC-based tool</li>
</ul>

<h2>Frequently Asked Questions</h2>
<div class="faq-section">
<div class="faq-item"><h3>What is the time difference between UTC and EST?</h3><p>UTC is 5 hours ahead of EST in winter, 4 in summer.</p></div>
<div class="faq-item"><h3>Is UTC the same as GMT?</h3><p>They share the same offset (UTC+0), but UTC is the scientific standard; GMT is a time zone.</p></div>
<div class="faq-item"><h3>If it's 14:00 UTC, what time is it in New York?</h3><p>9:00 AM EST (winter) or 10:00 AM EDT (summer).</p></div>
<div class="faq-item"><h3>How do I convert EST to UTC?</h3><p>Add 5 hours in winter or 4 hours in US summer.</p></div>
<div class="faq-item"><h3>Why use UTC at all?</h3><p>It removes ambiguity — no DST, no region, one reference for the whole world.</p></div>
</div>
<p>Use our <a href="/">world clock</a> and <a href="/meeting-planner.html">meeting planner</a> to bridge UTC and local time.</p>'''

META = {
 'time-difference-tokyo-london.html': (
   'Time Difference Between Tokyo and London: Guide & Converter (2026)',
   'What is the Time Difference Between Tokyo and London?',
   'Discover the 8-9 hour gap between Tokyo (JST) and London (GMT/BST). Includes conversion table, DST handling, and an interactive Tokyo-London time zone converter.',
   'time difference Tokyo London, Tokyo to London time, JST to GMT conversion, Tokyo London time zone'),
 'time-difference-singapore-london.html': (
   'Time Difference Between Singapore and London: Guide & Converter (2026)',
   'What is the Time Difference Between Singapore and London?',
   'Find the 7-8 hour gap between Singapore (SGT) and London (GMT/BST). Includes conversion chart, DST info, and a Singapore-London time zone converter.',
   'time difference Singapore London, Singapore to London time, SGT to GMT conversion, Singapore London time zone'),
 'time-difference-tokyo-sydney.html': (
   'Time Difference Between Tokyo and Sydney: Guide & Converter (2026)',
   'What is the Time Difference Between Tokyo and Sydney?',
   'Learn the 1-2 hour gap between Tokyo (JST) and Sydney (AEST/AEDT). Includes conversion table, opposite DST schedules, and Tokyo-Sydney converter.',
   'time difference Tokyo Sydney, Tokyo to Sydney time, JST to AEDT conversion, Tokyo Sydney time zone'),
 'convert-gmt-to-ist.html': (
   'Convert GMT to IST: Time Difference & Conversion Guide (2026)',
   'Convert GMT to IST: Greenwich Mean Time to India Time',
   'Learn how to convert Greenwich Mean Time (GMT) to Indian Standard Time (IST, UTC+5:30) with our step-by-step guide. Includes half-hour offset handling, DST notes, and conversion formula.',
   'convert GMT to IST, GMT to IST time difference, Greenwich to India time, GMT IST converter'),
 'convert-utc-to-est.html': (
   'Convert UTC to EST: Time Difference & Conversion Guide (2026)',
   'Convert UTC to EST: Coordinated Universal Time to Eastern Time',
   'Learn how to convert Coordinated Universal Time (UTC) to Eastern Standard Time (EST, UTC−5) with our step-by-step guide. Includes conversion chart, DST handling, and UTC-EST formula.',
   'convert UTC to EST, UTC to EST time difference, Coordinated Universal to Eastern time, UTC EST converter'),
}

content_map = {
 'time-difference-tokyo-london.html': C1,
 'time-difference-singapore-london.html': C2,
 'time-difference-tokyo-sydney.html': C3,
 'convert-gmt-to-ist.html': C4,
 'convert-utc-to-est.html': C5,
}

created = 0
for slug, (title, h1, desc, kw) in META.items():
    head = build_head(title, desc, kw, slug)
    head = head.replace('{title}', title).replace('{meta_desc}', desc).replace('{keywords}', kw).replace('{slug}', slug)
    article = ARTICLE_TEMPLATE.format(h1=h1, content=content_map[slug])
    full = head + article + TAIL
    (BLOG_DIR / slug).write_text(full, encoding='utf-8')
    created += 1
    print('Wrote', slug)

print(f'Done. {created} posts created.')
