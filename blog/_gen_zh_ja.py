#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Localized blog posts: ZH and JA translations for the 5 new posts."""
import sys
sys.path.insert(0, '/home/kaliuser/worldtime/blog')
from _gen_i18n import make_i18n_post

DATE_DISPLAY = {'zh': '2026年7月8日', 'ja': '2026年7月8日'}

# =====================================================================
# 1. time-difference-los-angeles-london
# =====================================================================
ZH_1 = (
'<p>如果你在洛杉矶和伦敦之间工作，你会遇到英语世界中最常见的工作时差之一：冬季相差 8 小时，夏季相差 7 小时。洛杉矶的上午通话落在伦敦的傍晚，反之亦然。下面告诉你如何理清头绪。</p>',
'<h2>时区概览</h2>',
'<h3>洛杉矶（PST/PDT）</h3>',
'<p>洛杉矶使用太平洋时间：冬季为 PST（UTC−8），夏季美国夏令时为 PDT（UTC−7），夏令时从 3 月第二个星期日到 11 月第一个星期日。</p>',
'<h3>伦敦（GMT/BST）</h3>',
'<p>伦敦冬季使用 GMT（UTC+0），夏季英国夏令时为 BST（UTC+1），从 3 月最后一个星期日到 10 月最后一个星期日。</p>',
'<h2>时差</h2>',
'<p><strong>冬季（均为标准时间）：</strong>伦敦比洛杉矶早 8 小时。</p>',
'<p><strong>夏季（均为夏令时）：</strong>伦敦比洛杉矶早 7 小时。</p>',
'<p><strong>尴尬的几周：</strong>由于美国和英国切换日期不同，每年春秋季约两周内，只有一方切换时，时差为 7 或 8 小时。</p>',
'<h2>换算公式</h2>',
'<p><strong>伦敦时间 = 洛杉矶时间 + 8 小时（冬季）或 + 7 小时（夏季）</strong></p>',
'<h2>快速换算表（洛杉矶 PST → 伦敦 GMT）</h2>',
'<table><thead><tr><th>洛杉矶</th><th>伦敦</th></tr></thead><tbody>'
'<tr><td>7:00</td><td>15:00</td></tr>'
'<tr><td>9:00</td><td>17:00</td></tr>'
'<tr><td>12:00</td><td>20:00</td></tr>'
'<tr><td>15:00</td><td>23:00</td></tr>'
'<tr><td>18:00</td><td>次日 2:00</td></tr>'
'<tr><td>21:00</td><td>次日 5:00</td></tr>'
'</tbody></table>',
'<div class="converter-widget">'
'    <h2>时区转换器</h2>'
'    <div class="converter-row"><label for="from-time">洛杉矶时间：</label><input type="time" id="from-time" value="09:00"></div>'
'    <div class="converter-row"><label for="dst">季节：</label>'
'      <select id="dst"><option value="8">冬季（PST/GMT）— 伦敦 +8 小时</option><option value="7" selected>夏季（PDT/BST）— 伦敦 +7 小时</option></select></div>'
'    <div class="converter-row"><label for="to-time">伦敦时间：</label><input type="time" id="to-time" readonly></div>'
'</div>',
"<script>document.addEventListener('DOMContentLoaded', function() {var f=document.getElementById('from-time'), d=document.getElementById('dst'), t=document.getElementById('to-time');function cv(){ if(!f.value) return; var p=f.value.split(':').map(Number); var m=p[0]*60+p[1]+parseInt(d.value)*60; while(m<0)m+=1440; while(m>=1440)m-=1440; t.value=String(Math.floor(m/60)).padStart(2,'0')+':'+String(m%60).padStart(2,'0'); }f.addEventListener('input', cv); d.addEventListener('change', cv); cv();});</script>",
'<h2>常见用途</h2>',
'<ul>'
'<li>好莱坞与英国之间的娱乐和科技业务</li>'
'<li>洛杉矶团队中与伦敦相关方协作的远程工程师</li>'
'<li>横跨大西洋的家庭视频通话</li>'
'<li>追看英国剧集首播或美国直播</li>'
'</ul>',
'<h2>常见问题</h2>',
'<div class="faq-section">'
'<div class="faq-item"><h3>洛杉矶和伦敦的时差是多少？</h3><p>冬季 8 小时，夏季 7 小时。伦敦始终更早。</p></div>'
'<div class="faq-item"><h3>为什么相差一小时？</h3><p>两国都实行夏令时，但切换日期不同，因此时差在 7 到 8 小时之间浮动。</p></div>'
'<div class="faq-item"><h3>如果洛杉矶是上午 9 点，伦敦是几点？</h3><p>冬季 GMT 17:00，或夏季 BST 16:00。</p></div>'
'<div class="faq-item"><h3>开会的最佳时间？</h3><p>洛杉矶上午 8–10 点 = 伦敦下午 16–18 点（冬季）或 15–17 点（夏季）。</p></div>'
'<div class="faq-item"><h3>洛杉矶使用 GMT 吗？</h3><p>不使用。洛杉矶使用太平洋时间，比伦敦晚 8/7 小时。</p></div>'
'</div>',
'<p>用我们的<a href="/">世界时钟</a>查看实时时间，并用<a href="/meeting-planner.html">会议规划器</a>安排跨大西洋通话。</p>'
)

JA_1 = (
'<p>ロサンゼルスとロンドン間で働く場合、英語圏で最も大きな時差の一つに直面します。冬は 8 時間、夏は 7 時間の差です。ロサンゼルスの朝の電話はロンドンの夕方に当たり、その逆も同様です。どう整理するか見ていきましょう。</p>',
'<h2>タイムゾーン概要</h2>',
'<h3>ロサンゼルス（PST/PDT）</h3>',
'<p>ロサンゼルスは太平洋時間です。冬は PST（UTC−8）、米国の夏時間は PDT（UTC−7）で、3 月第 2 日曜日から 11 月第 1 日曜日までです。</p>',
'<h3>ロンドン（GMT/BST）</h3>',
'<p>ロンドンは冬は GMT（UTC+0）、英国の夏時間は BST（UTC+1）で、3 月最終日曜日から 10 月最終日曜日までです。</p>',
'<h2>時差</h2>',
'<p><strong>冬（両方標準時）：</strong>ロンドンはロサンゼルスより 8 時間進んでいます。</p>',
'<p><strong>夏（両方夏時間）：</strong>ロンドンはロサンゼルスより 7 時間進んでいます。</p>',
'<p><strong>微妙な週：</strong>米国と英国は切り替え日が異なるため、春秋の約 2 週間はどちらか一方だけが切り替わり、差が 7 または 8 時間になります。</p>',
'<h2>換算式</h2>',
'<p><strong>ロンドン時間 = ロサンゼルス時間 + 8 時間（冬）または + 7 時間（夏）</strong></p>',
'<h2>早見換算表（ロサンゼルス PST → ロンドン GMT）</h2>',
'<table><thead><tr><th>ロサンゼルス</th><th>ロンドン</th></tr></thead><tbody>'
'<tr><td>7:00</td><td>15:00</td></tr>'
'<tr><td>9:00</td><td>17:00</td></tr>'
'<tr><td>12:00</td><td>20:00</td></tr>'
'<tr><td>15:00</td><td>23:00</td></tr>'
'<tr><td>18:00</td><td>翌日 2:00</td></tr>'
'<tr><td>21:00</td><td>翌日 5:00</td></tr>'
'</tbody></table>',
'<div class="converter-widget">'
'    <h2>タイムゾーン変換ツール</h2>'
'    <div class="converter-row"><label for="from-time">ロサンゼルス時間：</label><input type="time" id="from-time" value="09:00"></div>'
'    <div class="converter-row"><label for="dst">季節：</label>'
'      <select id="dst"><option value="8">冬（PST/GMT）— ロンドン +8 時間</option><option value="7" selected>夏（PDT/BST）— ロンドン +7 時間</option></select></div>'
'    <div class="converter-row"><label for="to-time">ロンドン時間：</label><input type="time" id="to-time" readonly></div>'
'</div>',
"<script>document.addEventListener('DOMContentLoaded', function() {var f=document.getElementById('from-time'), d=document.getElementById('dst'), t=document.getElementById('to-time');function cv(){ if(!f.value) return; var p=f.value.split(':').map(Number); var m=p[0]*60+p[1]+parseInt(d.value)*60; while(m<0)m+=1440; while(m>=1440)m-=1440; t.value=String(Math.floor(m/60)).padStart(2,'0')+':'+String(m%60).padStart(2,'0'); }f.addEventListener('input', cv); d.addEventListener('change', cv); cv();});</script>",
'<h2>主な用途</h2>',
'<ul>'
'<li>ハリウッドと英国間のエンタメ・テック取引</li>'
'<li>ロサンゼルスのチームでロンドンの関係者と協業するリモートエンジニア</li>'
'<li>大西洋をまたぐ家族のビデオ通話</li>'
'<li>英国ドラマの初回放送や米国ライブ配信を視聴</li>'
'</ul>',
'<h2>よくある質問</h2>',
'<div class="faq-section">'
'<div class="faq-item"><h3>ロサンゼルスとロンドンの時差は？</h3><p>冬は 8 時間、夏は 7 時間。ロンドンが常に先です。</p></div>'
'<div class="faq-item"><h3>なぜ 1 時間ずれるの？</h3><p>両国とも夏時間がありますが切り替え日が異なるため、差は 7〜8 時間の間を動きます。</p></div>'
'<div class="faq-item"><h3>ロサンゼルスが午前 9 時ならロンドンは？</h3><p>冬は GMT 17:00、夏は BST 16:00 です。</p></div>'
'<div class="faq-item"><h3>会議のベスト時間？</h3><p>ロサンゼルス午前 8–10 時 = ロンドン午後 16–18 時（冬）または 15–17 時（夏）。</p></div>'
'<div class="faq-item"><h3>ロサンゼルスは GMT を使う？</h3><p>いいえ。太平洋時間で、ロンドンより 8/7 時間遅れます。</p></div>'
'</div>',
'<p>リアルタイムの時刻は<a href="/">世界時計</a>で確認し、<a href="/meeting-planner.html">会議プランナー</a>で大西洋をまたぐ通話を予定してください。</p>'
)

# ----- 2. time-difference-new-york-sydney -----
ZH_2 = (
'<p>纽约和悉尼是主要商业城市中相距最远的组合之一：时差为 14 至 16 小时，而且因为季节相反，两者的夏令时期几乎不重叠。这让安排变得像解谜，但可解。</p>',
'<h2>时区概览</h2>',
'<h3>纽约（EST/EDT）</h3>',
'<p>纽约使用东部时间：冬季为 EST（UTC−5），美国夏令时为 EDT（UTC−4），从 3 月第二个星期日到 11 月第一个星期日。</p>',
'<h3>悉尼（AEST/AEDT）</h3>',
'<p>悉尼冬季为 AEST（UTC+10），澳大利亚夏令时为 AEDT（UTC+11），从 10 月第一个星期日到 4 月第一个星期日。</p>',
'<h2>时差</h2>',
'<p><strong>澳大利亚夏季 / 美国冬季：</strong>悉尼比纽约早 16 小时。</p>',
'<p><strong>澳大利亚冬季 / 美国夏季：</strong>悉尼比纽约早 14 小时。</p>',
'<p><strong>重叠周：</strong>只有一方切换的短暂期间，时差为 15 小时。</p>',
'<h2>换算公式</h2>',
'<p><strong>悉尼时间 = 纽约时间 + 16 小时（美国冬季）或 + 14 小时（美国夏季）</strong></p>',
'<h2>快速换算表（纽约 EST → 悉尼 AEDT，美国冬季）</h2>',
'<table><thead><tr><th>纽约</th><th>悉尼</th></tr></thead><tbody>'
'<tr><td>7:00</td><td>当日 23:00</td></tr>'
'<tr><td>9:00</td><td>次日 1:00</td></tr>'
'<tr><td>12:00</td><td>次日 4:00</td></tr>'
'<tr><td>17:00</td><td>次日 9:00</td></tr>'
'<tr><td>20:00</td><td>次日 12:00</td></tr>'
'<tr><td>23:00</td><td>次日 15:00</td></tr>'
'</tbody></table>',
'<h2>常见用途</h2>',
'<ul>'
'<li>美国与澳大利亚之间的商务、金融和搬迁</li>'
'<li>协调横跨太平洋的远程团队</li>'
'<li>东海岸与悉尼之间的家庭通话</li>'
'<li>跨越国际日期变更线关注美国体育或澳洲新闻</li>'
'</ul>',
'<h2>常见问题</h2>',
'<div class="faq-section">'
'<div class="faq-item"><h3>纽约和悉尼的时差是多少？</h3><p>随季节为 14 至 16 小时；悉尼遥遥领先。</p></div>'
'<div class="faq-item"><h3>为什么这么大？</h3><p>两座城市位于地球两端，且夏令时落在一年中的相反半年。</p></div>'
'<div class="faq-item"><h3>如果纽约是上午 9 点，悉尼是几点？</h3><p>次日 1:00（美国冬季，AEDT）或当日 23:00（美国夏季，AEST）。</p></div>'
'<div class="faq-item"><h3>通话的最佳重叠？</h3><p>纽约上午 7–9 点 = 悉尼 23:00–1:00（困难）；许多团队只交换异步备忘。</p></div>'
'<div class="faq-item"><h3>悉尼会调时间吗？</h3><p>会，夏季为 AEDT，但日程与纽约相反。</p></div>'
'</div>',
'<p>使用我们的<a href="/">世界时钟</a>查看实时时间，并用<a href="/meeting-planner.html">会议规划器</a>寻找任何真正的重叠。</p>'
)

JA_2 = (
'<p>ニューヨークとシドニーは、主要なビジネス都市の中で最も離れた組み合わせの一つです。時差は 14〜16 時間で、季節が逆なため両者の夏時間がほとんど重なりません。スケジュールはパズルのようですが、解けます。</p>',
'<h2>タイムゾーン概要</h2>',
'<h3>ニューヨーク（EST/EDT）</h3>',
'<p>ニューヨークは東部時間です。冬は EST（UTC−5）、米国の夏時間は EDT（UTC−4）で、3 月第 2 日曜日から 11 月第 1 日曜日までです。</p>',
'<h3>シドニー（AEST/AEDT）</h3>',
'<p>シドニーは冬は AEST（UTC+10）、オーストラリアの夏時間は AEDT（UTC+11）で、10 月第 1 日曜日から 4 月第 1 日曜日までです。</p>',
'<h2>時差</h2>',
'<p><strong>オーストラリア夏 / 米国冬：</strong>シドニーはニューヨークより 16 時間進んでいます。</p>',
'<p><strong>オーストラリア冬 / 米国夏：</strong>シドニーはニューヨークより 14 時間進んでいます。</p>',
'<p><strong>重複週：</strong>どちらか一方だけが切り替わる短い期間、差は 15 時間です。</p>',
'<h2>換算式</h2>',
'<p><strong>シドニー時間 = ニューヨーク時間 + 16 時間（米国冬）または + 14 時間（米国夏）</strong></p>',
'<h2>早見換算表（ニューヨーク EST → シドニー AEDT、米国冬）</h2>',
'<table><thead><tr><th>ニューヨーク</th><th>シドニー</th></tr></thead><tbody>'
'<tr><td>7:00</td><td>当日 23:00</td></tr>'
'<tr><td>9:00</td><td>翌日 1:00</td></tr>'
'<tr><td>12:00</td><td>翌日 4:00</td></tr>'
'<tr><td>17:00</td><td>翌日 9:00</td></tr>'
'<tr><td>20:00</td><td>翌日 12:00</td></tr>'
'<tr><td>23:00</td><td>翌日 15:00</td></tr>'
'</tbody></table>',
'<h2>主な用途</h2>',
'<ul>'
'<li>米国とオーストラリア間のビジネス、金融、移住</li>'
'<li>太平洋をまたぐリモートチームの調整</li>'
'<li>東海岸とシドニー間の家族通話</li>'
'<li>日付変更線をまたいで米国スポーツや豪州ニュースをチェック</li>'
'</ul>',
'<h2>よくある質問</h2>',
'<div class="faq-section">'
'<div class="faq-item"><h3>ニューヨークとシドニーの時差は？</h3><p>季節により 14〜16 時間。シドニーがずっと先です。</p></div>'
'<div class="faq-item"><h3>なぜこんなに大きい？</h3><p>両都市は地球の反対側にあり、夏時間が年の逆の半分に来るからです。</p></div>'
'<div class="faq-item"><h3>ニューヨークが午前 9 時ならシドニーは？</h3><p>翌日 1:00（米国冬、AEDT）または当日 23:00（米国夏、AEST）です。</p></div>'
'<div class="faq-item"><h3>通話のベスト重複？</h3><p>ニューヨーク午前 7–9 時 = シドニー 23:00–1:00（困難）。非同期メモを交換するチームが多いです。</p></div>'
'<div class="faq-item"><h3>シドニーは時計を変える？</h3><p>はい、夏は AEDT ですが、ニューヨークと逆の日程です。</p></div>'
'</div>',
'<p>リアルタイムの時刻は<a href="/">世界時計</a>で、<a href="/meeting-planner.html">会議プランナー</a>で実際の重複を見つけてください。</p>'
)

# ----- 3. convert-cet-to-est -----
ZH_3 = (
'<p>将中欧时间转换为美国东部时间，是跨大西洋业务、欧洲机构以及任何在柏林、巴黎或马德里与纽约或华盛顿之间通话的人经常需要做的。冬季相差 6 小时，夏季相差 5 小时。</p>',
'<h2>时区概览</h2>',
'<h3>中欧时间（CET）</h3>',
'<p>CET 冬季为 UTC+1，欧洲夏令时为 CEST（UTC+2），从 3 月最后一个星期日到 10 月最后一个星期日。</p>',
'<h3>东部时间（EST/EDT）</h3>',
'<p>美国东部时间冬季为 EST（UTC−5），美国夏令时为 EDT（UTC−4），从 3 月第二个星期日到 11 月第一个星期日。</p>',
'<h2>时差</h2>',
'<p><strong>冬季（均为标准时间）：</strong>CET 比 EST 早 6 小时。</p>',
'<p><strong>夏季（均为夏令时）：</strong>CET 比 EDT 早 6 小时。</p>',
'<p><strong>过渡周：</strong>当只有美国或只有欧洲切换时，短时间内时差为 5 或 7 小时。</p>',
'<h2>换算公式</h2>',
'<p><strong>EST = CET − 6 小时（冬季）/ CET − 6 小时（夏季，均为夏令时）</strong></p>',
'<p>由于两个地区都实行夏令时，6 小时的差距在一年大部分时间保持稳定，只在切换不一致的少数几周变化。</p>',
'<h2>快速换算表（CET → EST）</h2>',
'<table><thead><tr><th>中欧时间</th><th>美国东部时间</th></tr></thead><tbody>'
'<tr><td>9:00</td><td>3:00</td></tr>'
'<tr><td>12:00</td><td>6:00</td></tr>'
'<tr><td>14:00</td><td>8:00</td></tr>'
'<tr><td>17:00</td><td>11:00</td></tr>'
'<tr><td>20:00</td><td>14:00</td></tr>'
'<tr><td>23:00</td><td>17:00</td></tr>'
'</tbody></table>',
'<div class="converter-widget">'
'    <h2>时区转换器</h2>'
'    <div class="converter-row"><label for="from-time">CET/CEST 时间：</label><input type="time" id="from-time" value="14:00"></div>'
'    <div class="converter-row"><label for="to-time">EST/EDT 时间：</label><input type="time" id="to-time" readonly></div>'
'    <div class="converter-note">减去 6 小时（CET→EST）。特定日期请使用我们的<a href="/meeting-planner.html">会议规划器</a>。</div>'
'</div>',
"<script>document.addEventListener('DOMContentLoaded', function() {var f=document.getElementById('from-time'), t=document.getElementById('to-time');function cv(){ if(!f.value) return; var p=f.value.split(':').map(Number); var m=p[0]*60+p[1]-360; while(m<0)m+=1440; while(m>=1440)m-=1440; t.value=String(Math.floor(m/60)).padStart(2,'0')+':'+String(m%60).padStart(2,'0'); }f.addEventListener('input', cv); cv();});</script>",
'<h2>常见用途</h2>',
'<ul>'
'<li>欧盟与美国的商务通话（巴黎、柏林、马德里和纽约）</li>'
'<li>从美国东海岸与欧洲远程同事协调</li>'
'<li>安排跨大西洋的网络研讨会</li>'
'<li>对齐市场开盘和交易</li>'
'</ul>',
'<h2>常见问题</h2>',
'<div class="faq-section">'
'<div class="faq-item"><h3>CET 和 EST 的时差是多少？</h3><p>通常为 6 小时；CET 更早。切换周会短暂变为 5 或 7 小时。</p></div>'
'<div class="faq-item"><h3>哪些城市使用 CET？</h3><p>巴黎、柏林、马德里、罗马、阿姆斯特丹、维也纳以及中欧大部分地区。</p></div>'
'<div class="faq-item"><h3>如果巴黎是 14:00，纽约是几点？</h3><p>冬季 EST 8:00 或夏季 EDT 8:00——仍是 6 小时。</p></div>'
'<div class="faq-item"><h3>6 小时差距全年保持吗？</h3><p>几乎如此。只在欧洲和美国切换日期不同的几周变化。</p></div>'
'<div class="faq-item"><h3>如何将 EST 转换为 CET？</h3><p>给东部时间加 6 小时。</p></div>'
'</div>',
'<p>要实时比较，请打开我们的<a href="/">世界时钟</a>并选择你的城市。</p>'
)

JA_3 = (
'<p>中央ヨーロッパ時間を米国東部時間に変換するのは、大西洋をまたぐビジネス、欧州機関、そしてベルリン・パリ・マドリードとニューヨークやワシントン間で通話する人が常に行います。冬は 6 時間、夏は 5 時間の差です。</p>',
'<h2>タイムゾーン概要</h2>',
'<h3>中央ヨーロッパ時間（CET）</h3>',
'<p>CET は冬は UTC+1、欧州夏時間は CEST（UTC+2）で、3 月最終日曜日から 10 月最終日曜日までです。</p>',
'<h3>東部時間（EST/EDT）</h3>',
'<p>米国東部時間は冬は EST（UTC−5）、米国夏時間は EDT（UTC−4）で、3 月第 2 日曜日から 11 月第 1 日曜日までです。</p>',
'<h2>時差</h2>',
'<p><strong>冬（両方標準時）：</strong>CET は EST より 6 時間進んでいます。</p>',
'<p><strong>夏（両方夏時間）：</strong>CET は EDT より 6 時間進んでいます。</p>',
'<p><strong>移行週：</strong>米国か欧州のどちらかだけが切り替わった時、短時間は差が 5 または 7 時間になります。</p>',
'<h2>換算式</h2>',
'<p><strong>EST = CET − 6 時間（冬）/ CET − 6 時間（夏、両方夏時間）</strong></p>',
'<p>両地域とも夏時間があるため、6 時間の差は年間を通してほぼ維持され、切り替えが一致しない数週間だけ変化します。</p>',
'<h2>早見換算表（CET → EST）</h2>',
'<table><thead><tr><th>中央欧州時間</th><th>米国東部時間</th></tr></thead><tbody>'
'<tr><td>9:00</td><td>3:00</td></tr>'
'<tr><td>12:00</td><td>6:00</td></tr>'
'<tr><td>14:00</td><td>8:00</td></tr>'
'<tr><td>17:00</td><td>11:00</td></tr>'
'<tr><td>20:00</td><td>14:00</td></tr>'
'<tr><td>23:00</td><td>17:00</td></tr>'
'</tbody></table>',
'<div class="converter-widget">'
'    <h2>タイムゾーン変換ツール</h2>'
'    <div class="converter-row"><label for="from-time">CET/CEST 時間：</label><input type="time" id="from-time" value="14:00"></div>'
'    <div class="converter-row"><label for="to-time">EST/EDT 時間：</label><input type="time" id="to-time" readonly></div>'
'    <div class="converter-note">6 時間引く（CET→EST）。特定の日付は<a href="/meeting-planner.html">会議プランナー</a>をご利用ください。</div>'
'</div>',
"<script>document.addEventListener('DOMContentLoaded', function() {var f=document.getElementById('from-time'), t=document.getElementById('to-time');function cv(){ if(!f.value) return; var p=f.value.split(':').map(Number); var m=p[0]*60+p[1]-360; while(m<0)m+=1440; while(m>=1440)m-=1440; t.value=String(Math.floor(m/60)).padStart(2,'0')+':'+String(m%60).padStart(2,'0'); }f.addEventListener('input', cv); cv();});</script>",
'<h2>主な用途</h2>',
'<ul>'
'<li>EU と米国のビジネス通話（パリ、ベルリン、マドリード、ニューヨーク）</li>'
'<li>米国東海岸から欧州のリモート同僚と調整</li>'
'<li>大西洋をまたぐウェビナーを計画</li>'
'<li>市場の始値と取引の調整</li>'
'</ul>',
'<h2>よくある質問</h2>',
'<div class="faq-section">'
'<div class="faq-item"><h3>CET と EST の時差は？</h3><p>通常 6 時間。CET が先です。切り替え週は一時的に 5 または 7 時間になります。</p></div>'
'<div class="faq-item"><h3>どの都市が CET を使う？</h3><p>パリ、ベルリン、マドリード、ローマ、アムステルダム、ウィーン、および中央欧州のほとんど。</p></div>'
'<div class="faq-item"><h3>パリが 14:00 ならニューヨークは？</h3><p>冬は EST 8:00、夏は EDT 8:00——やはり 6 時間です。</p></div>'
'<div class="faq-item"><h3>6 時間の差は一年中維持される？</h3><p>ほぼ。欧州と米国が別の日付で切り替わる数週間だけ変化します。</p></div>'
'<div class="faq-item"><h3>EST を CET に変換するには？</h3><p>東部時間に 6 時間を加えます。</p></div>'
'</div>',
'<p>リアルタイムで比較するには<a href="/">世界時計</a>を開き、都市を選んでください。</p>'
)

# ----- 4. time-difference-dubai-london -----
ZH_4 = (
'<p>迪拜和伦敦是一条热门的商务走廊，而且是最容易处理的之一：时差正好是 4 小时，且从不改变，因为两座城市都不实行夏令时。</p>',
'<h2>时区概览</h2>',
'<h3>迪拜（GST）</h3>',
'<p>迪拜使用海湾标准时间，全年为 UTC+4。阿联酋不实行夏令时。</p>',
'<h3>伦敦（GMT/BST）</h3>',
'<p>伦敦冬季为 GMT（UTC+0），夏季为 BST（UTC+1）。英国实行夏令时。</p>',
'<h2>时差</h2>',
'<p><strong>英国冬季：</strong>迪拜比伦敦早 4 小时。</p>',
'<p><strong>英国夏季：</strong>迪拜比伦敦早 3 小时（因为伦敦切换到 BST）。</p>',
'<p>注意：迪拜自身偏移量不变——时差只因伦敦而变化。</p>',
'<h2>换算公式</h2>',
'<p><strong>迪拜时间 = 伦敦时间 + 4 小时（冬季）或 + 3 小时（夏季）</strong></p>',
'<h2>快速换算表（迪拜 GST → 伦敦）</h2>',
'<table><thead><tr><th>迪拜</th><th>伦敦（GMT，冬季）</th><th>伦敦（BST，夏季）</th></tr></thead><tbody>'
'<tr><td>9:00</td><td>5:00</td><td>6:00</td></tr>'
'<tr><td>12:00</td><td>8:00</td><td>9:00</td></tr>'
'<tr><td>15:00</td><td>11:00</td><td>12:00</td></tr>'
'<tr><td>18:00</td><td>14:00</td><td>15:00</td></tr>'
'<tr><td>21:00</td><td>17:00</td><td>18:00</td></tr>'
'<tr><td>0:00</td><td>20:00</td><td>21:00</td></tr>'
'</tbody></table>',
'<h2>常见用途</h2>',
'<ul>'
'<li>阿联酋与英国之间的金融和贸易</li>'
'<li>经由迪拜枢纽安排航班</li>'
'<li>分布在海湾和伦敦之间的远程团队</li>'
'<li>两个市场的房地产交易</li>'
'</ul>',
'<h2>常见问题</h2>',
'<div class="faq-section">'
'<div class="faq-item"><h3>迪拜和伦敦的时差是多少？</h3><p>英国冬季 4 小时，夏季 3 小时。迪拜不变。</p></div>'
'<div class="faq-item"><h3>迪拜实行夏令时吗？</h3><p>不实行。阿联酋全年保持海湾标准时间（UTC+4）。</p></div>'
'<div class="faq-item"><h3>如果迪拜是 12:00，伦敦是几点？</h3><p>冬季 GMT 8:00 或夏季 BST 9:00。</p></div>'
'<div class="faq-item"><h3>开会的最佳窗口？</h3><p>伦敦 8:00–12:00 = 迪拜 12:00–16:00（冬季）或 11:00–15:00（夏季）。</p></div>'
'<div class="faq-item"><h3>为什么只有一方变动？</h3><p>只有英国实行夏令时；阿联酋保持固定偏移。</p></div>'
'</div>',
'<p>用我们的<a href="/">世界时钟</a>实时查看两座城市，并用<a href="/meeting-planner.html">会议规划器</a>安排。</p>'
)

JA_4 = (
'<p>ドバイとロンドンは人気のビジネス回廊で、最も扱いやすいものの一つです。時差は正確に 4 時間で、どちらの都市も夏時間を採用しないため、一度も変わりません。</p>',
'<h2>タイムゾーン概要</h2>',
'<h3>ドバイ（GST）</h3>',
'<p>ドバイはペルシャ湾標準時で、通年 UTC+4 です。UAE は夏時間を採用していません。</p>',
'<h3>ロンドン（GMT/BST）</h3>',
'<p>ロンドンは冬は GMT（UTC+0）、夏は BST（UTC+1）です。英国は夏時間を採用しています。</p>',
'<h2>時差</h2>',
'<p><strong>英国の冬：</strong>ドバイはロンドンより 4 時間進んでいます。</p>',
'<p><strong>英国の夏：</strong>ドバイはロンドンより 3 時間進んでいます（ロンドンが BST に切り替わるため）。</p>',
'<p>注：ドバイ自体のオフセットは変わりません——時差はロンドンのみで動きます。</p>',
'<h2>換算式</h2>',
'<p><strong>ドバイ時間 = ロンドン時間 + 4 時間（冬）または + 3 時間（夏）</strong></p>',
'<h2>早見換算表（ドバイ GST → ロンドン）</h2>',
'<table><thead><tr><th>ドバイ</th><th>ロンドン（GMT、冬）</th><th>ロンドン（BST、夏）</th></tr></thead><tbody>'
'<tr><td>9:00</td><td>5:00</td><td>6:00</td></tr>'
'<tr><td>12:00</td><td>8:00</td><td>9:00</td></tr>'
'<tr><td>15:00</td><td>11:00</td><td>12:00</td></tr>'
'<tr><td>18:00</td><td>14:00</td><td>15:00</td></tr>'
'<tr><td>21:00</td><td>17:00</td><td>18:00</td></tr>'
'<tr><td>0:00</td><td>20:00</td><td>21:00</td></tr>'
'</tbody></table>',
'<h2>主な用途</h2>',
'<ul>'
'<li>UAE と英国間の金融・貿易</li>'
'<li>ドバイのハブを経由するフライトの手配</li>'
'<li>湾岸とロンドンに分散するリモートチーム</li>'
'<li>両市場での不動産取引</li>'
'</ul>',
'<h2>よくある質問</h2>',
'<div class="faq-section">'
'<div class="faq-item"><h3>ドバイとロンドンの時差は？</h3><p>英国の冬は 4 時間、夏は 3 時間。ドバイは変わりません。</p></div>'
'<div class="faq-item"><h3>ドバイは夏時間を採用する？</h3><p>いいえ。UAE は通年ペルシャ湾標準時（UTC+4）を維持します。</p></div>'
'<div class="faq-item"><h3>ドバイが 12:00 ならロンドンは？</h3><p>冬は GMT 8:00、夏は BST 9:00 です。</p></div>'
'<div class="faq-item"><h3>会議のベスト窓？</h3><p>ロンドン 8:00–12:00 = ドバイ 12:00–16:00（冬）または 11:00–15:00（夏）。</p></div>'
'<div class="faq-item"><h3>なぜ一方だけ動く？</h3><p>夏時間は英国だけで、UAE は固定オフセットを保ちます。</p></div>'
'</div>',
'<p>両都市のリアルタイム時刻は<a href="/">世界時計</a>で確認し、<a href="/meeting-planner.html">会議プランナー</a>で予定を立ててください。</p>'
)

# ----- 5. convert-ist-to-gmt -----
ZH_5 = (
'<p>将印度标准时间（IST）转换为格林尼治标准时间（GMT），是任何在印度与欧洲或非洲之间工作的人经常需要的。要记住的关键点：印度使用半小时偏移 UTC+5:30，且从不改变。正是这半小时让人困惑。</p>',
'<h2>时区概览</h2>',
'<h3>印度标准时间（IST）</h3>',
'<p>IST 全年为 UTC+5:30。印度不实行夏令时，因此偏移量固定。</p>',
'<h3>格林尼治标准时间（GMT）</h3>',
'<p>GMT 冬季为 UTC+0。英国夏季切换到 BST（UTC+1），因此参考点会变动。</p>',
'<h2>时差</h2>',
'<p><strong>英国冬季（GMT）：</strong>印度比 GMT 早 5 小时 30 分钟。</p>',
'<p><strong>英国夏季（BST）：</strong>印度比伦敦早 4 小时 30 分钟。</p>',
'<h2>换算公式</h2>',
'<p><strong>GMT = IST − 5 小时 30 分（冬季）/ IST − 4 小时 30 分（英国夏季）</strong></p>',
'<h2>换算示例</h2>',
'<p><strong>冬季：</strong>15:00 IST → 9:30 GMT</p>',
'<p><strong>夏季：</strong>15:00 IST → 10:30 BST</p>',
'<p>注意半小时。10:00 IST 是 4:30 GMT，而不是 5:00。</p>',
'<h2>快速换算表（IST → GMT）</h2>',
'<table><thead><tr><th>印度（IST）</th><th>伦敦（GMT，冬季）</th><th>伦敦（BST，夏季）</th></tr></thead><tbody>'
'<tr><td>9:00</td><td>3:30</td><td>4:30</td></tr>'
'<tr><td>12:00</td><td>6:30</td><td>7:30</td></tr>'
'<tr><td>15:00</td><td>9:30</td><td>10:30</td></tr>'
'<tr><td>18:00</td><td>12:30</td><td>13:30</td></tr>'
'<tr><td>21:00</td><td>15:30</td><td>16:30</td></tr>'
'<tr><td>0:00</td><td>18:30</td><td>19:30</td></tr>'
'</tbody></table>',
'<div class="converter-widget">'
'    <h2>时区转换器</h2>'
'    <div class="converter-row"><label for="from-time">印度时间：</label><input type="time" id="from-time" value="15:00"></div>'
'    <div class="converter-row"><label for="dst">英国：</label>'
'      <select id="dst"><option value="330">GMT（冬）−5小时30分</option><option value="270" selected>BST（夏）−4小时30分</option></select></div>'
'    <div class="converter-row"><label for="to-time">伦敦时间：</label><input type="time" id="to-time" readonly></div>'
'</div>',
"<script>document.addEventListener('DOMContentLoaded', function() {var f=document.getElementById('from-time'), d=document.getElementById('dst'), t=document.getElementById('to-time');function cv(){ if(!f.value) return; var p=f.value.split(':').map(Number); var m=p[0]*60+p[1]-parseInt(d.value); while(m<0)m+=1440; while(m>=1440)m-=1440; t.value=String(Math.floor(m/60)).padStart(2,'0')+':'+String(m%60).padStart(2,'0'); }f.addEventListener('input', cv); d.addEventListener('change', cv); cv();});</script>",
'<h2>常见用途</h2>',
'<ul>'
'<li>英国与印度之间的外包和 IT 团队协调</li>'
'<li>安排伦敦与班加罗尔、孟买或德里之间的通话</li>'
'<li>从欧洲关注印度交易时段</li>'
'<li>两地之间的家庭和个人通话</li>'
'</ul>',
'<h2>常见问题</h2>',
'<div class="faq-section">'
'<div class="faq-item"><h3>IST 和 GMT 的时差是多少？</h3><p>英国冬季 5 小时 30 分，夏季 4 小时 30 分。</p></div>'
'<div class="faq-item"><h3>为什么是半小时？</h3><p>印度特意使用 UTC+5:30，并全年保持。</p></div>'
'<div class="faq-item"><h3>如果印度是 15:00，伦敦是几点？</h3><p>冬季 GMT 9:30 或夏季 BST 10:30。</p></div>'
'<div class="faq-item"><h3>印度实行夏令时吗？</h3><p>不实行。IST 全年为 UTC+5:30。</p></div>'
'<div class="faq-item"><h3>如何将 GMT 转换为 IST？</h3><p>冬季加 5 小时 30 分，或英国夏季加 4 小时 30 分。</p></div>'
'</div>',
'<p>要按特定日期规划，请使用我们的<a href="/">世界时钟</a>和<a href="/meeting-planner.html">会议规划器</a>。</p>'
)

JA_5 = (
'<p>インド標準時（IST）をグリニッジ標準時（GMT）に変換するのは、インドと欧州やアフリカ間で働く人が常に必要とします。覚えておくべき要点：インドは 30 分のオフセット UTC+5:30 を使い、それは決して変わりません。この 30 分こそが人を惑わせます。</p>',
'<h2>タイムゾーン概要</h2>',
'<h3>インド標準時（IST）</h3>',
'<p>IST は通年 UTC+5:30 です。インドは夏時間を採用していないため、オフセットは固定です。</p>',
'<h3>グリニッジ標準時（GMT）</h3>',
'<p>GMT は冬は UTC+0 です。英国は夏に BST（UTC+1）に切り替わるため、基準点が動きます。</p>',
'<h2>時差</h2>',
'<p><strong>英国の冬（GMT）：</strong>インドは GMT より 5 時間 30 分進んでいます。</p>',
'<p><strong>英国の夏（BST）：</strong>インドはロンドンより 4 時間 30 分進んでいます。</p>',
'<h2>換算式</h2>',
'<p><strong>GMT = IST − 5 時間 30 分（冬）/ IST − 4 時間 30 分（英国夏）</strong></p>',
'<h2>換算例</h2>',
'<p><strong>冬：</strong>15:00 IST → 9:30 GMT</p>',
'<p><strong>夏：</strong>15:00 IST → 10:30 BST</p>',
'<p>30 分に注意。10:00 IST は 4:30 GMT であり、5:00 ではありません。</p>',
'<h2>早見換算表（IST → GMT）</h2>',
'<table><thead><tr><th>インド（IST）</th><th>ロンドン（GMT、冬）</th><th>ロンドン（BST、夏）</th></tr></thead><tbody>'
'<tr><td>9:00</td><td>3:30</td><td>4:30</td></tr>'
'<tr><td>12:00</td><td>6:30</td><td>7:30</td></tr>'
'<tr><td>15:00</td><td>9:30</td><td>10:30</td></tr>'
'<tr><td>18:00</td><td>12:30</td><td>13:30</td></tr>'
'<tr><td>21:00</td><td>15:30</td><td>16:30</td></tr>'
'<tr><td>0:00</td><td>18:30</td><td>19:30</td></tr>'
'</tbody></table>',
'<div class="converter-widget">'
'    <h2>タイムゾーン変換ツール</h2>'
'    <div class="converter-row"><label for="from-time">インド時間：</label><input type="time" id="from-time" value="15:00"></div>'
'    <div class="converter-row"><label for="dst">英国：</label>'
'      <select id="dst"><option value="330">GMT（冬）−5時間30分</option><option value="270" selected>BST（夏）−4時間30分</option></select></div>'
'    <div class="converter-row"><label for="to-time">ロンドン時間：</label><input type="time" id="to-time" readonly></div>'
'</div>',
"<script>document.addEventListener('DOMContentLoaded', function() {var f=document.getElementById('from-time'), d=document.getElementById('dst'), t=document.getElementById('to-time');function cv(){ if(!f.value) return; var p=f.value.split(':').map(Number); var m=p[0]*60+p[1]-parseInt(d.value); while(m<0)m+=1440; while(m>=1440)m-=1440; t.value=String(Math.floor(m/60)).padStart(2,'0')+':'+String(m%60).padStart(2,'0'); }f.addEventListener('input', cv); d.addEventListener('change', cv); cv();});</script>",
'<h2>主な用途</h2>',
'<ul>'
'<li>英国とインド間の外包・IT チーム調整</li>'
'<li>ロンドンとバンガロール、ムンバイ、デリー間の通話を計画</li>'
'<li>欧州からインドの取引時間を追う</li>'
'<li>地域間の家族・個人の通話</li>'
'</ul>',
'<h2>よくある質問</h2>',
'<div class="faq-section">'
'<div class="faq-item"><h3>IST と GMT の時差は？</h3><p>英国の冬は 5 時間 30 分、夏は 4 時間 30 分です。</p></div>'
'<div class="faq-item"><h3>なぜ 30 分？</h3><p>インドは意図的に UTC+5:30 を使い、通年維持しているからです。</p></div>'
'<div class="faq-item"><h3>インドが 15:00 ならロンドンは？</h3><p>冬は GMT 9:30、夏は BST 10:30 です。</p></div>'
'<div class="faq-item"><h3>インドは夏時間を採用する？</h3><p>いいえ。IST は通年 UTC+5:30 です。</p></div>'
'<div class="faq-item"><h3>GMT を IST に変換するには？</h3><p>冬は 5 時間 30 分、英国の夏は 4 時間 30 分を加えます。</p></div>'
'</div>',
'<p>特定の日付で計画するには<a href="/">世界時計</a>と<a href="/meeting-planner.html">会議プランナー</a>をお使いください。</p>'
)

META = {
 'time-difference-los-angeles-london': {
   'zh': ('洛杉矶与伦敦时差：指南与转换工具（2026）| World Time Sync',
     '洛杉矶—伦敦：理清 7–8 小时的时差',
     '了解洛杉矶与伦敦之间 7–8 小时的时差：换算表、夏令时说明与实时转换器。',
     '洛杉矶 伦敦 时差, 洛杉矶伦敦时间换算, PST 转 GMT',
     '洛杉矶与伦敦时差', '时区, 换算, 指南'),
   'ja': ('ロサンゼルスとロンドンの時差：ガイドと変換ツール（2026）| World Time Sync',
     'ロサンゼルス—ロンドン：7〜8 時間の時差を理解する',
     'ロサンゼルスとロンドン間の 7〜8 時間の時差をご紹介。換算表、夏時間、ライブ変換ツール付き。',
     'ロサンゼルス ロンドン 時差, ロサンゼルスロンドン 変換, PST から GMT',
     'ロサンゼルスとロンドンの時差', 'タイムゾーン, 変換, ガイド'),
 },
 'time-difference-new-york-sydney': {
   'zh': ('纽约与悉尼时差：指南与转换工具（2026）| World Time Sync',
     '纽约—悉尼：14–16 小时的太平洋时差',
     '了解纽约与悉尼之间 14–16 小时的时差：换算表、夏令时说明与规划建议。',
     '纽约 悉尼 时差, 纽约悉尼时间换算, EST 转 AEDT',
     '纽约与悉尼时差', '时区, 换算, 指南'),
   'ja': ('ニューヨークとシドニーの時差：ガイドと変換ツール（2026）| World Time Sync',
     'ニューヨーク—シドニー：14〜16 時間の太平洋の差',
     'ニューヨークとシドニー間の 14〜16 時間の時差をご紹介。換算表、夏時間、計画のヒント付き。',
     'ニューヨーク シドニー 時差, ニューヨークシドニー 変換, EST から AEDT',
     'ニューヨークとシドニーの時差', 'タイムゾーン, 変換, ガイド'),
 },
 'convert-cet-to-est': {
   'zh': ('CET 转 EST：时差与换算指南（2026）| World Time Sync',
     'CET 转 EST：稳定的 6 小时跨大西洋时差',
     '用我们的指南、换算表和实时转换器，将中欧时间转换为美国东部时间。',
     'CET 转 EST, CET EST 时差, 中欧时间转东部时间',
     'CET 转 EST', '时区, 换算, 指南'),
   'ja': ('CET を EST に変換：時差とガイド（2026）| World Time Sync',
     'CET を EST に変換：安定した 6 時間の大西洋の差',
     'ガイド・換算表・ライブ変換ツールで中央欧州時間を米国東部時間に変換します。',
     'CET から EST, CET EST 時差, 中央欧州から東部時間',
     'CET を EST に変換', 'タイムゾーン, 変換, ガイド'),
 },
 'time-difference-dubai-london': {
   'zh': ('迪拜与伦敦时差：指南与转换工具（2026）| World Time Sync',
     '迪拜—伦敦：干净的 3–4 小时时差',
     '迪拜与伦敦的时差正好是 3–4 小时，且迪拜一侧从不改变。含换算表、夏令时说明与转换器。',
     '迪拜 伦敦 时差, 迪拜伦敦时间换算, GST 转 GMT',
     '迪拜与伦敦时差', '时区, 换算, 指南'),
   'ja': ('ドバイとロンドンの時差：ガイドと変換ツール（2026）| World Time Sync',
     'ドバイ—ロンドン：きれいな 3〜4 時間の差',
     'ドバイとロンドンの差は正確に 3〜4 時間で、ドバイ側は変わりません。換算表・夏時間・変換ツール付き。',
     'ドバイ ロンドン 時差, ドバイロンドン 変換, GST から GMT',
     'ドバイとロンドンの時差', 'タイムゾーン, 変換, ガイド'),
 },
 'convert-ist-to-gmt': {
   'zh': ('IST 转 GMT：时差与换算指南（2026）| World Time Sync',
     'IST 转 GMT：别忘了半小时',
     '用我们的指南将印度标准时间转换为 GMT。印度全年为 UTC+5:30，请注意半小时。',
     'IST 转 GMT, 印度 GMT 时差, IST GMT 换算',
     'IST 转 GMT', '时区, 换算, 指南'),
   'ja': ('IST を GMT に変換：時差とガイド（2026）| World Time Sync',
     'IST を GMT に変換：30 分をお忘れなく',
     'ガイドでインド標準時を GMT に変換します。インドは通年 UTC+5:30 なので 30 分にご注意を。',
     'IST から GMT, インド GMT 時差, IST GMT 変換',
     'IST を GMT に変換', 'タイムゾーン, 変換, ガイド'),
 },
}

CONTENT = {
 'time-difference-los-angeles-london': {'zh': ZH_1, 'ja': JA_1},
 'time-difference-new-york-sydney': {'zh': ZH_2, 'ja': JA_2},
 'convert-cet-to-est': {'zh': ZH_3, 'ja': JA_3},
 'time-difference-dubai-london': {'zh': ZH_4, 'ja': JA_4},
 'convert-ist-to-gmt': {'zh': ZH_5, 'ja': JA_5},
}

for slug, langs in CONTENT.items():
    for lang in ('zh', 'ja'):
        parts = langs[lang]
        content = ''.join(parts)
        title, h1, desc, kw, bc, tags = META[slug][lang]
        make_i18n_post(slug, lang, lang, title, h1, desc, kw, bc, DATE_DISPLAY[lang], 6, tags, content, [])

print('\nZH + JA localized posts generated.')
