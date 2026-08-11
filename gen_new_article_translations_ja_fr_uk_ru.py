#!/usr/bin/env python3
"""Generate ja, fr, uk, ru translations of the new blog post."""
import os
from pathlib import Path

BASE = Path('/home/kaliuser/worldtime')
BLOG_DIR = BASE / 'blog'

CRUMB = {
    'ja': ('ホーム', 'ブログ'),
    'fr': ('Accueil', 'Blog'),
    'uk': ('Головна', 'Блог'),
    'ru': ('Главная', 'Блог'),
}
META_DATE = {
    'ja': '2026年8月10日', 'fr': '10 août 2026', 'uk': '10 лип 2026', 'ru': '10 авг 2026',
}
META_READ = {
    'ja': '読了 8 分', 'fr': '8 min de lecture', 'uk': '8 хв читання', 'ru': '8 мин чтения',
}
SKIP = {'ja': 'メインコンテンツへ移動', 'fr': 'Aller au contenu principal', 'uk': 'Перейти до основного вмісту', 'ru': 'Перейти к основному содержанию'}
LOADING = {'ja': '時刻を読み込み中...', 'fr': "Chargement de l'heure...", 'uk': 'Завантаження часу...', 'ru': 'Загрузка времени...'}

T = {
'time-zone-abbreviations-cheat-sheet': {
 'ja': ('タイムゾーン略語チートシート (2026)',
   '主要なタイムゾーン略語のクイックリファレンス——EST、PST、CET、IST、JST およびその他 50 以上。UTC オフセット、夏時間バリエーション、各略語を使用する都市を含む。',
   'タイムゾーン略語,EST PST CST MST,UTC オフセット チートシート,タイムゾーンコード リスト,タイムゾーン頭字語,夏時間略語',
   'タイムゾーン略語チートシート',
   """<p>フライトの確認で "EST"、会議の招待で "CET"、ログファイルで "IST" を見かける。各略語は UTC からの特定のオフセットを意味するが、夏と冬で異なるものもある。このチートシートでは正確なオフセット、主要都市、夏時間で変わるかどうかを示す。</p>
<h2>北米のタイムゾーン</h2>
<table class="tz-table">
    <thead><tr><th>略語</th><th>正式名称</th><th>UTC オフセット</th><th>夏時間バリエーション</th><th>主要都市</th></tr></thead>
    <tbody>
        <tr><td>EST</td><td>Eastern Standard Time</td><td>UTC-5</td><td>EDT (UTC-4)</td><td>ニューヨーク、トロント、マイアミ、アトランタ</td></tr>
        <tr><td>EDT</td><td>Eastern Daylight Time</td><td>UTC-4</td><td>EST (冬)</td><td>同じ都市、3-11月</td></tr>
        <tr><td>CST</td><td>Central Standard Time</td><td>UTC-6</td><td>CDT (UTC-5)</td><td>シカゴ、ダラス、メキシコシティ、ヒューストン</td></tr>
        <tr><td>CDT</td><td>Central Daylight Time</td><td>UTC-5</td><td>CST (冬)</td><td>同じ都市、3-11月</td></tr>
        <tr><td>MST</td><td>Mountain Standard Time</td><td>UTC-7</td><td>MDT (UTC-6)</td><td>デンバー、フェニックス*、エドモントン、エルパソ</td></tr>
        <tr><td>MDT</td><td>Mountain Daylight Time</td><td>UTC-6</td><td>MST (冬)</td><td>同じ都市 (アリゾナ州を除く)</td></tr>
        <tr><td>PST</td><td>Pacific Standard Time</td><td>UTC-8</td><td>PDT (UTC-7)</td><td>ロサンゼルス、バンクーバー、シアトル、ティフアナ</td></tr>
        <tr><td>PDT</td><td>Pacific Daylight Time</td><td>UTC-7</td><td>PST (冬)</td><td>同じ都市、3-11月</td></tr>
        <tr><td>AKST</td><td>Alaska Standard Time</td><td>UTC-9</td><td>AKDT (UTC-8)</td><td>アンカレッジ、フェアバンクス、ジュノー</td></tr>
        <tr><td>HST</td><td>Hawaii-Aleutian Standard Time</td><td>UTC-10</td><td>夏時間なし</td><td>ホノルル、ヒロ、アダック</td></tr>
    </tbody>
</table>
<p><small>* アリゾナ州 (ナバホ族居留地を除く) は夏時間を実施せず、通年 MST。</small></p>
<h2>大西洋と南米のタイムゾーン</h2>
<table class="tz-table">
    <thead><tr><th>略語</th><th>正式名称</th><th>UTC オフセット</th><th>夏時間バリエーション</th><th>主要都市</th></tr></thead>
    <tbody>
        <tr><td>AST</td><td>Atlantic Standard Time</td><td>UTC-4</td><td>ADT (UTC-3)</td><td>ハリファックス、サンフアン、バミューダ、カラカス</td></tr>
        <tr><td>BRT</td><td>Brasilia Time</td><td>UTC-3</td><td>2019 年以降夏時間なし</td><td>サンパウロ、リオデジャネイロ、ブラジリア</td></tr>
        <tr><td>ART</td><td>Argentina Time</td><td>UTC-3</td><td>2009 年以降夏時間なし</td><td>ブエノスアイレス、コルドバ、ロサリオ</td></tr>
        <tr><td>CLT</td><td>Chile Standard Time</td><td>UTC-4</td><td>CLST (UTC-3)</td><td>サンティアゴ、バルパライソ、コンセプシオン</td></tr>
    </tbody>
</table>
<h2>ヨーロッパとアフリカのタイムゾーン</h2>
<table class="tz-table">
    <thead><tr><th>略語</th><th>正式名称</th><th>UTC オフセット</th><th>夏時間バリエーション</th><th>主要都市</th></tr></thead>
    <tbody>
        <tr><td>GMT</td><td>Greenwich Mean Time</td><td>UTC+0</td><td>BST (UTC+1)</td><td>ロンドン、ダブリン、リスボン (冬)</td></tr>
        <tr><td>BST</td><td>British Summer Time</td><td>UTC+1</td><td>GMT (冬)</td><td>ロンドン、ダブリン、エディンバラ (夏)</td></tr>
        <tr><td>WET</td><td>Western European Time</td><td>UTC+0</td><td>WEST (UTC+1)</td><td>リスボン、カサブランカ、レイキャビク</td></tr>
        <tr><td>CET</td><td>Central European Time</td><td>UTC+1</td><td>CEST (UTC+2)</td><td>パリ、ベルリン、ローマ、マドリード、ワルシャワ</td></tr>
        <tr><td>CEST</td><td>Central European Summer Time</td><td>UTC+2</td><td>CET (冬)</td><td>同じ都市、3-10月</td></tr>
        <tr><td>EET</td><td>Eastern European Time</td><td>UTC+2</td><td>EEST (UTC+3)</td><td>ヘルシンキ、キーウ、ブカレスト、カイロ</td></tr>
        <tr><td>MSK</td><td>Moscow Standard Time</td><td>UTC+3</td><td>2014 年以降夏時間なし</td><td>モスクワ、サンクトペテルブルク、イスタンブール、ミンスク</td></tr>
        <tr><td>SAST</td><td>South Africa Standard Time</td><td>UTC+2</td><td>夏時間なし</td><td>ヨハネスブルグ、ケープタウン、ダーバン</td></tr>
        <tr><td>WAT</td><td>West Africa Time</td><td>UTC+1</td><td>夏時間なし</td><td>ラゴス、キンシャサ、アルジェ</td></tr>
    </tbody>
</table>
<h2>中東と中央アジアのタイムゾーン</h2>
<table class="tz-table">
    <thead><tr><th>略語</th><th>正式名称</th><th>UTC オフセット</th><th>夏時間バリエーション</th><th>主要都市</th></tr></thead>
    <tbody>
        <tr><td>GST</td><td>Gulf Standard Time</td><td>UTC+4</td><td>夏時間なし</td><td>ドバイ、アブダビ、マスカット、ドーハ</td></tr>
        <tr><td>AST</td><td>Arabia Standard Time</td><td>UTC+3</td><td>夏時間なし</td><td>リヤド、ジッダ、クウェートシティ、マナマ</td></tr>
        <tr><td>IRST</td><td>Iran Standard Time</td><td>UTC+3:30</td><td>IRDT (UTC+4:30)</td><td>テヘラン、マシュハド、エスファハーン</td></tr>
        <tr><td>AFT</td><td>Afghanistan Time</td><td>UTC+4:30</td><td>夏時間なし</td><td>カーブル、ヘラート、マザーリシャリーフ</td></tr>
        <tr><td>PKT</td><td>Pakistan Standard Time</td><td>UTC+5</td><td>夏時間なし</td><td>カラチ、ラホール、イスラマバード</td></tr>
    </tbody>
</table>
<h2>南アジアと東南アジアのタイムゾーン</h2>
<table class="tz-table">
    <thead><tr><th>略語</th><th>正式名称</th><th>UTC オフセット</th><th>夏時間バリエーション</th><th>主要都市</th></tr></thead>
    <tbody>
        <tr><td>IST</td><td>India Standard Time</td><td>UTC+5:30</td><td>夏時間なし</td><td>ムンバイ、デリー、バンガロール、コルカタ、チェンナイ</td></tr>
        <tr><td>NPT</td><td>Nepal Time</td><td>UTC+5:45</td><td>夏時間なし</td><td>カトマンズ、ポカラ、ビラトナガル</td></tr>
        <tr><td>BST</td><td>Bangladesh Standard Time</td><td>UTC+6</td><td>夏時間なし</td><td>ダッカ、チッタゴン、シレット</td></tr>
        <tr><td>MMT</td><td>Myanmar Time</td><td>UTC+6:30</td><td>夏時間なし</td><td>ヤンゴン、マンダレー、ネピドー</td></tr>
        <tr><td>ICT</td><td>Indochina Time</td><td>UTC+7</td><td>夏時間なし</td><td>バンコク、ハノイ、ジャカルタ*、プノンペン</td></tr>
        <tr><td>WIB</td><td>Western Indonesian Time</td><td>UTC+7</td><td>夏時間なし</td><td>ジャカルタ、バンドン、スラバヤ</td></tr>
        <tr><td>CST</td><td>China Standard Time</td><td>UTC+8</td><td>夏時間なし</td><td>北京、上海、香港、台北</td></tr>
        <tr><td>SGT</td><td>Singapore Time</td><td>UTC+8</td><td>夏時間なし</td><td>シンガポール、クアラルンプール、マニラ、パース</td></tr>
    </tbody>
</table>
<p><small>* ジャカルタは WIB (UTC+7) を使用し、ICT ではない。</small></p>
<h2>東アジアと太平洋のタイムゾーン</h2>
<table class="tz-table">
    <thead><tr><th>略語</th><th>正式名称</th><th>UTC オフセット</th><th>夏時間バリエーション</th><th>主要都市</th></tr></thead>
    <tbody>
        <tr><td>JST</td><td>Japan Standard Time</td><td>UTC+9</td><td>夏時間なし</td><td>東京、大阪、ソウル*、平壌*</td></tr>
        <tr><td>KST</td><td>Korea Standard Time</td><td>UTC+9</td><td>夏時間なし</td><td>ソウル、釜山、仁川</td></tr>
        <tr><td>AWST</td><td>Australian Western Standard Time</td><td>UTC+8</td><td>夏時間なし</td><td>パース、ブルーム、カラサ</td></tr>
        <tr><td>ACST</td><td>Australian Central Standard Time</td><td>UTC+9:30</td><td>ACDT (UTC+10:30)</td><td>アデレード、ダーウィン、アリススプリングス</td></tr>
        <tr><td>AEST</td><td>Australian Eastern Standard Time</td><td>UTC+10</td><td>AEDT (UTC+11)</td><td>シドニー、メルボルン、ブリスベン*、キャンベラ</td></tr>
        <tr><td>NZST</td><td>New Zealand Standard Time</td><td>UTC+12</td><td>NZDT (UTC+13)</td><td>オークランド、ウェリントン、クライストチャーチ</td></tr>
    </tbody>
</table>
<p><small>* ソウルと平壌は KST を使用し、JST ではない。* ブリスベン (クイーンズランド州) は夏時間を実施しない。</small></p>
<h2>曖昧な略語 — 注意</h2>
<p>文脈によって異なるゾーンを意味する略語がある:</p>
<ul>
    <li><strong>CST</strong> — Central Standard Time (UTC-6, 北米) <em>または</em> China Standard Time (UTC+8) <em>または</em> Cuba Standard Time (UTC-5)</li>
    <li><strong>IST</strong> — India Standard Time (UTC+5:30) <em>または</em> Irish Standard Time (UTC+1, 夏) <em>または</em> Israel Standard Time (UTC+2)</li>
    <li><strong>PST</strong> — Pacific Standard Time (UTC-8) <em>または</em> Philippine Standard Time (UTC+8)</li>
    <li><strong>BST</strong> — British Summer Time (UTC+1) <em>または</em> Bangladesh Standard Time (UTC+6) <em>または</em> Bougainville Standard Time (UTC+11)</li>
    <li><strong>AST</strong> — Atlantic Standard Time (UTC-4) <em>または</em> Arabia Standard Time (UTC+3) <em>または</em> Amazon Standard Time (UTC-4, ブラジル)</li>
</ul>
<p>曖昧なコードを見たら、近くの国名や都市名を確認しよう。正確な変換には <a href="/ja/time-zone-converter.html">タイムゾーンコンバーター</a> を使えば、これらすべてを正しく処理できる。</p>
<h2>クイックリファレンス: 夏時間切り替え日 (典型)</h2>
<ul>
    <li><strong>北米</strong>: 3月第2日曜日 → 11月第1日曜日</li>
    <li><strong>ヨーロッパ</strong>: 3月最終日曜日 → 10月最終日曜日</li>
    <li><strong>オーストラリア (南東)</strong>: 10月第1日曜日 → 4月第1日曜日</li>
    <li><strong>ニュージーランド</strong>: 9月最終日曜日 → 4月第1日曜日</li>
    <li><strong>チリ</strong>: 9月第1日曜日 → 4月第1日曜日</li>
    <li><strong>パラグアイ</strong>: 10月第1日曜日 → 3月最終日曜日</li>
</ul>
<h2>このページをブックマーク、ツールを活用</h2>
<p>50 以上のコードを暗記する必要はない。このページを参照表としてブックマークしよう。特定の日付での正確な変換が必要なとき——特に夏時間の移行週では——<a href="/ja/time-difference.html">時差計算ツール</a> や <a href="/ja/meeting-planner.html">ミーティングプランナー</a> を使おう。IANA タイムゾーンデータベースを使用しているため、すべてのオフセットが最新かつ正確だ。</p>"""),
 'fr': ('Aide-mémoire des abréviations de fuseaux horaires (2026)',
   "Référence rapide pour toutes les abréviations principales de fuseaux horaires — EST, PST, CET, IST, JST et 50 autres. Inclut les décalages UTC, les variantes d'heure d'été et les villes qui utilisent chacune.",
   "abréviations fuseaux horaires, EST PST CST MST, décalages UTC fiche mémoire, liste codes fuseau horaire, acronymes fuseau horaire, abréviations heure d'été",
   'Aide-mémoire des abréviations de fuseaux horaires',
   """<p>Vous voyez "EST" sur une confirmation de vol, "CET" dans une invitation de réunion, "IST" dans un fichier log. Chaque abréviation signifie un décalage UTC précis, mais certaines changent de sens entre l'été et l'hiver. Cette fiche vous donne le décalage exact, les villes principales et si l'heure d'été le modifie.</p>
<h2>Fuseaux Horaires Nord-Américains</h2>
<table class="tz-table">
    <thead><tr><th>Abrév.</th><th>Nom Complet</th><th>Décalage UTC</th><th>Variante Heure d'Été</th><th>Villes Principales</th></tr></thead>
    <tbody>
        <tr><td>EST</td><td>Eastern Standard Time</td><td>UTC-5</td><td>EDT (UTC-4)</td><td>New York, Toronto, Miami, Atlanta</td></tr>
        <tr><td>EDT</td><td>Eastern Daylight Time</td><td>UTC-4</td><td>EST (hiver)</td><td>Mêmes villes, mars-novembre</td></tr>
        <tr><td>CST</td><td>Central Standard Time</td><td>UTC-6</td><td>CDT (UTC-5)</td><td>Chicago, Dallas, Mexico, Houston</td></tr>
        <tr><td>CDT</td><td>Central Daylight Time</td><td>UTC-5</td><td>CST (hiver)</td><td>Mêmes villes, mars-novembre</td></tr>
        <tr><td>MST</td><td>Mountain Standard Time</td><td>UTC-7</td><td>MDT (UTC-6)</td><td>Denver, Phoenix*, Edmonton, El Paso</td></tr>
        <tr><td>MDT</td><td>Mountain Daylight Time</td><td>UTC-6</td><td>MST (hiver)</td><td>Mêmes villes (sauf Arizona)</td></tr>
        <tr><td>PST</td><td>Pacific Standard Time</td><td>UTC-8</td><td>PDT (UTC-7)</td><td>Los Angeles, Vancouver, Seattle, Tijuana</td></tr>
        <tr><td>PDT</td><td>Pacific Daylight Time</td><td>UTC-7</td><td>PST (hiver)</td><td>Mêmes villes, mars-novembre</td></tr>
        <tr><td>AKST</td><td>Alaska Standard Time</td><td>UTC-9</td><td>AKDT (UTC-8)</td><td>Anchorage, Fairbanks, Juneau</td></tr>
        <tr><td>HST</td><td>Hawaii-Aleutian Standard Time</td><td>UTC-10</td><td>Pas d'heure d'été</td><td>Honolulu, Hilo, Adak</td></tr>
    </tbody>
</table>
<p><small>* L'Arizona (sauf réserve Navajo) ne change pas d'heure et reste sur MST toute l'année.</small></p>
<h2>Fuseaux Horaires de l'Atlantique et d'Amérique du Sud</h2>
<table class="tz-table">
    <thead><tr><th>Abrév.</th><th>Nom Complet</th><th>Décalage UTC</th><th>Variante Heure d'Été</th><th>Villes Principales</th></tr></thead>
    <tbody>
        <tr><td>AST</td><td>Atlantic Standard Time</td><td>UTC-4</td><td>ADT (UTC-3)</td><td>Halifax, San Juan, Bermudes, Caracas</td></tr>
        <tr><td>BRT</td><td>Brasilia Time</td><td>UTC-3</td><td>Pas d'heure d'été depuis 2019</td><td>São Paulo, Rio de Janeiro, Brasilia</td></tr>
        <tr><td>ART</td><td>Argentina Time</td><td>UTC-3</td><td>Pas d'heure d'été depuis 2009</td><td>Buenos Aires, Córdoba, Rosario</td></tr>
        <tr><td>CLT</td><td>Chile Standard Time</td><td>UTC-4</td><td>CLST (UTC-3)</td><td>Santiago, Valparaíso, Concepción</td></tr>
    </tbody>
</table>
<h2>Fuseaux Horaires Européens et Africains</h2>
<table class="tz-table">
    <thead><tr><th>Abrév.</th><th>Nom Complet</th><th>Décalage UTC</th><th>Variante Heure d'Été</th><th>Villes Principales</th></tr></thead>
    <tbody>
        <tr><td>GMT</td><td>Greenwich Mean Time</td><td>UTC+0</td><td>BST (UTC+1)</td><td>Londres, Dublin, Lisbonne (hiver)</td></tr>
        <tr><td>BST</td><td>British Summer Time</td><td>UTC+1</td><td>GMT (hiver)</td><td>Londres, Dublin, Édimbourg (été)</td></tr>
        <tr><td>WET</td><td>Western European Time</td><td>UTC+0</td><td>WEST (UTC+1)</td><td>Lisbonne, Casablanca, Reykjavik</td></tr>
        <tr><td>CET</td><td>Central European Time</td><td>UTC+1</td><td>CEST (UTC+2)</td><td>Paris, Berlin, Rome, Madrid, Varsovie</td></tr>
        <tr><td>CEST</td><td>Central European Summer Time</td><td>UTC+2</td><td>CET (hiver)</td><td>Mêmes villes, mars-octobre</td></tr>
        <tr><td>EET</td><td>Eastern European Time</td><td>UTC+2</td><td>EEST (UTC+3)</td><td>Helsinki, Kyiv, Bucarest, Le Caire</td></tr>
        <tr><td>MSK</td><td>Moscow Standard Time</td><td>UTC+3</td><td>Pas d'heure d'été depuis 2014</td><td>Moscou, Saint-Pétersbourg, Istanbul, Minsk</td></tr>
        <tr><td>SAST</td><td>South Africa Standard Time</td><td>UTC+2</td><td>Pas d'heure d'été</td><td>Johannesburg, Le Cap, Durban</td></tr>
        <tr><td>WAT</td><td>West Africa Time</td><td>UTC+1</td><td>Pas d'heure d'été</td><td>Lagos, Kinshasa, Alger</td></tr>
    </tbody>
</table>
<h2>Fuseaux Horaires du Moyen-Orient et d'Asie Centrale</h2>
<table class="tz-table">
    <thead><tr><th>Abrév.</th><th>Nom Complet</th><th>Décalage UTC</th><th>Variante Heure d'Été</th><th>Villes Principales</th></tr></thead>
    <tbody>
        <tr><td>GST</td><td>Gulf Standard Time</td><td>UTC+4</td><td>Pas d'heure d'été</td><td>Dubaï, Abu Dhabi, Mascate, Doha</td></tr>
        <tr><td>AST</td><td>Arabia Standard Time</td><td>UTC+3</td><td>Pas d'heure d'été</td><td>Riyad, Djeddah, Koweït, Manama</td></tr>
        <tr><td>IRST</td><td>Iran Standard Time</td><td>UTC+3:30</td><td>IRDT (UTC+4:30)</td><td>Téhéran, Mashhad, Ispahan</td></tr>
        <tr><td>AFT</td><td>Afghanistan Time</td><td>UTC+4:30</td><td>Pas d'heure d'été</td><td>Kaboul, Héra, Mazâr-e Charîf</td></tr>
        <tr><td>PKT</td><td>Pakistan Standard Time</td><td>UTC+5</td><td>Pas d'heure d'été</td><td>Karachi, Lahore, Islamabad</td></tr>
    </tbody>
</table>
<h2>Fuseaux Horaires d'Asie du Sud et du Sud-Est</h2>
<table class="tz-table">
    <thead><tr><th>Abrév.</th><th>Nom Complet</th><th>Décalage UTC</th><th>Variante Heure d'Été</th><th>Villes Principales</th></tr></thead>
    <tbody>
        <tr><td>IST</td><td>India Standard Time</td><td>UTC+5:30</td><td>Pas d'heure d'été</td><td>Mumbai, Delhi, Bangalore, Kolkata, Chennai</td></tr>
        <tr><td>NPT</td><td>Nepal Time</td><td>UTC+5:45</td><td>Pas d'heure d'été</td><td>Katmandou, Pokhara, Biratnagar</td></tr>
        <tr><td>BST</td><td>Bangladesh Standard Time</td><td>UTC+6</td><td>Pas d'heure d'été</td><td>Dacca, Chittagong, Sylhet</td></tr>
        <tr><td>MMT</td><td>Myanmar Time</td><td>UTC+6:30</td><td>Pas d'heure d'été</td><td>Yangon, Mandalay, Naypyidaw</td></tr>
        <tr><td>ICT</td><td>Indochina Time</td><td>UTC+7</td><td>Pas d'heure d'été</td><td>Bangkok, Hanoï, Jakarta*, Phnom Penh</td></tr>
        <tr><td>WIB</td><td>Western Indonesian Time</td><td>UTC+7</td><td>Pas d'heure d'été</td><td>Jakarta, Bandung, Surabaya</td></tr>
        <tr><td>CST</td><td>China Standard Time</td><td>UTC+8</td><td>Pas d'heure d'été</td><td>Pékin, Shanghai, Hong Kong, Taipei</td></tr>
        <tr><td>SGT</td><td>Singapore Time</td><td>UTC+8</td><td>Pas d'heure d'été</td><td>Singapour, Kuala Lumpur, Manille, Perth</td></tr>
    </tbody>
</table>
<p><small>* Jakarta utilise WIB (UTC+7), pas ICT.</small></p>
<h2>Fuseaux Horaires d'Asie de l'Est et du Pacifique</h2>
<table class="tz-table">
    <thead><tr><th>Abrév.</th><th>Nom Complet</th><th>Décalage UTC</th><th>Variante Heure d'Été</th><th>Villes Principales</th></tr></thead>
    <tbody>
        <tr><td>JST</td><td>Japan Standard Time</td><td>UTC+9</td><td>Pas d'heure d'été</td><td>Tokyo, Osaka, Séoul*, Pyongyang*</td></tr>
        <tr><td>KST</td><td>Korea Standard Time</td><td>UTC+9</td><td>Pas d'heure d'été</td><td>Séoul, Busan, Incheon</td></tr>
        <tr><td>AWST</td><td>Australian Western Standard Time</td><td>UTC+8</td><td>Pas d'heure d'été</td><td>Perth, Broome, Karratha</td></tr>
        <tr><td>ACST</td><td>Australian Central Standard Time</td><td>UTC+9:30</td><td>ACDT (UTC+10:30)</td><td>Adélaïde, Darwin, Alice Springs</td></tr>
        <tr><td>AEST</td><td>Australian Eastern Standard Time</td><td>UTC+10</td><td>AEDT (UTC+11)</td><td>Sydney, Melbourne, Brisbane*, Canberra</td></tr>
        <tr><td>NZST</td><td>New Zealand Standard Time</td><td>UTC+12</td><td>NZDT (UTC+13)</td><td>Auckland, Wellington, Christchurch</td></tr>
    </tbody>
</table>
<p><small>* Séoul et Pyongyang utilisent KST, pas JST. * Brisbane (Queensland) ne change pas d'heure.</small></p>
<h2>Abréviations Ambiguës — Attention</h2>
<p>Certaines abréviations signifient des fuseaux différents selon le contexte:</p>
<ul>
    <li><strong>CST</strong> — Central Standard Time (UTC-6, Amérique du Nord) <em>ou</em> China Standard Time (UTC+8) <em>ou</em> Cuba Standard Time (UTC-5)</li>
    <li><strong>IST</strong> — India Standard Time (UTC+5:30) <em>ou</em> Irish Standard Time (UTC+1, été) <em>ou</em> Israel Standard Time (UTC+2)</li>
    <li><strong>PST</strong> — Pacific Standard Time (UTC-8) <em>ou</em> Philippine Standard Time (UTC+8)</li>
    <li><strong>BST</strong> — British Summer Time (UTC+1) <em>ou</em> Bangladesh Standard Time (UTC+6) <em>ou</em> Bougainville Standard Time (UTC+11)</li>
    <li><strong>AST</strong> — Atlantic Standard Time (UTC-4) <em>ou</em> Arabia Standard Time (UTC+3) <em>ou</em> Amazon Standard Time (UTC-4, Brésil)</li>
</ul>
<p>Quand vous voyez un code ambigu, regardez le pays ou la ville à côté. Pour des conversions exactes, utilisez notre <a href="/fr/time-zone-converter.html">convertisseur de fuseaux horaires</a> qui gère correctement tous ces cas.</p>
<h2>Référence Rapide: Dates de Changement d'Heure d'Été (Typiques)</h2>
<ul>
    <li><strong>Amérique du Nord</strong>: 2e dimanche mars → 1er dimanche novembre</li>
    <li><strong>Europe</strong>: dernier dimanche mars → dernier dimanche octobre</li>
    <li><strong>Australie (sud-est)</strong>: 1er dimanche octobre → 1er dimanche avril</li>
    <li><strong>Nouvelle-Zélande</strong>: dernier dimanche septembre → 1er dimanche avril</li>
    <li><strong>Chili</strong>: 1er dimanche septembre → 1er dimanche avril</li>
    <li><strong>Paraguay</strong>: 1er dimanche octobre → dernier dimanche mars</li>
</ul>
<h2>Marquez Cette Page, Utilisez l'Outil</h2>
<p>Vous n'avez pas besoin de mémoriser 50+ codes. Marquez cette page pour la table de référence. Quand vous avez besoin d'une conversion exacte pour une date spécifique — surtout pendant les semaines de transition d'heure d'été — utilisez notre <a href="/fr/time-difference.html">calculateur de décalage horaire</a> ou <a href="/fr/meeting-planner.html">planificateur de réunion</a>. Ils utilisent la base de données IANA des fuseaux horaires donc chaque décalage est à jour et correct.</p>"""),
 'uk': ('Шпаргалка по скороченням часових поясів (2026)',
   'Швидкий довідник по всіх основних скороченнях часових поясів — EST, PST, CET, IST, JST та 50 інших. Включує UTC-зсуви, варіанти літнього часу й міста, що використовують кожне.',
   'скорочення часових поясів, EST PST CST MST, шпаргалка UTC-зсувів, список кодів часового пояса, акроніми часового пояса, скорочення літнього часу',
   'Шпаргалка по скороченням часових поясів',
   """<p>Ти бачиш "EST" на підтвердженні рейсу, "CET" у запрошенні на зустріч, "IST" у лог-файлі. Кожне скорочення означає конкретний UTC-зсув, але деякі мають інше значення влітку проти зими. Ця шпаргалка дає точний зсув, головні міста й чи змінює літній час його.</p>
<h2>Північноамериканські часові пояси</h2>
<table class="tz-table">
    <thead><tr><th>Скороч.</th><th>Повна назва</th><th>UTC-зсув</th><th>Варіант літнього часу</th><th>Головні міста</th></tr></thead>
    <tbody>
        <tr><td>EST</td><td>Eastern Standard Time</td><td>UTC-5</td><td>EDT (UTC-4)</td><td>Нью-Йорк, Торонто, Маямі, Атланта</td></tr>
        <tr><td>EDT</td><td>Eastern Daylight Time</td><td>UTC-4</td><td>EST (зима)</td><td>Ті самі міста, бер-квіт</td></tr>
        <tr><td>CST</td><td>Central Standard Time</td><td>UTC-6</td><td>CDT (UTC-5)</td><td>Чикаго, Даллас, Мехико, Х'юстон</td></tr>
        <tr><td>CDT</td><td>Central Daylight Time</td><td>UTC-5</td><td>CST (зима)</td><td>Ті самі міста, бер-квіт</td></tr>
        <tr><td>MST</td><td>Mountain Standard Time</td><td>UTC-7</td><td>MDT (UTC-6)</td><td>Денвер, Фенікс*, Едмонтон, Ель-Пасо</td></tr>
        <tr><td>MDT</td><td>Mountain Daylight Time</td><td>UTC-6</td><td>MST (зима)</td><td>Ті самі міста (окрім Аризони)</td></tr>
        <tr><td>PST</td><td>Pacific Standard Time</td><td>UTC-8</td><td>PDT (UTC-7)</td><td>Лос-Анджелес, Ванкувер, Сіетл, Тіхуана</td></tr>
        <tr><td>PDT</td><td>Pacific Daylight Time</td><td>UTC-7</td><td>PST (зима)</td><td>Ті самі міста, бер-квіт</td></tr>
        <tr><td>AKST</td><td>Alaska Standard Time</td><td>UTC-9</td><td>AKDT (UTC-8)</td><td>Анкорідж, Фейрбанкс, Джуно</td></tr>
        <tr><td>HST</td><td>Hawaii-Aleutian Standard Time</td><td>UTC-10</td><td>Немає літнього часу</td><td>Гонолулу, Хіло, Адак</td></tr>
    </tbody>
</table>
<p><small>* Аризона (крім резервації Навахо) не переходить на літній час і залишається на MST цілий рік.</small></p>
<h2>Атлантичні й Південноамериканські часові пояси</h2>
<table class="tz-table">
    <thead><tr><th>Скороч.</th><th>Повна назва</th><th>UTC-зсув</th><th>Варіант літнього часу</th><th>Головні міста</th></tr></thead>
    <tbody>
        <tr><td>AST</td><td>Atlantic Standard Time</td><td>UTC-4</td><td>ADT (UTC-3)</td><td>Галіфакс, Сан-Хуан, Бермуди, Каракас</td></tr>
        <tr><td>BRT</td><td>Brasilia Time</td><td>UTC-3</td><td>Немає літнього часу з 2019</td><td>Сан-Паулу, Ріо-де-Жанейро, Бразилія</td></tr>
        <tr><td>ART</td><td>Argentina Time</td><td>UTC-3</td><td>Немає літнього часу з 2009</td><td>Буенос-Айрес, Кордова, Росаріо</td></tr>
        <tr><td>CLT</td><td>Chile Standard Time</td><td>UTC-4</td><td>CLST (UTC-3)</td><td>Сантьяго, Вальпараїсо, Консепсьйон</td></tr>
    </tbody>
</table>
<h2>Європейські й Африканські часові пояси</h2>
<table class="tz-table">
    <thead><tr><th>Скороч.</th><th>Повна назва</th><th>UTC-зсув</th><th>Варіант літнього часу</th><th>Головні міста</th></tr></thead>
    <tbody>
        <tr><td>GMT</td><td>Greenwich Mean Time</td><td>UTC+0</td><td>BST (UTC+1)</td><td>Лондон, Дублин, Ліссабон (зима)</td></tr>
        <tr><td>BST</td><td>British Summer Time</td><td>UTC+1</td><td>GMT (зима)</td><td>Лондон, Дублин, Единбург (літо)</td></tr>
        <tr><td>WET</td><td>Western European Time</td><td>UTC+0</td><td>WEST (UTC+1)</td><td>Ліссабон, Касабланка, Рейк'явік</td></tr>
        <tr><td>CET</td><td>Central European Time</td><td>UTC+1</td><td>CEST (UTC+2)</td><td>Париж, Берлін, Рим, Мадрид, Варшава</td></tr>
        <tr><td>CEST</td><td>Central European Summer Time</td><td>UTC+2</td><td>CET (зима)</td><td>Ті самі міста, бер-жовт</td></tr>
        <tr><td>EET</td><td>Eastern European Time</td><td>UTC+2</td><td>EEST (UTC+3)</td><td>Гельсінкі, Київ, Бухарест, Каїр</td></tr>
        <tr><td>MSK</td><td>Moscow Standard Time</td><td>UTC+3</td><td>Немає літнього часу з 2014</td><td>Москва, Санкт-Петербург, Стамбул, Мінськ</td></tr>
        <tr><td>SAST</td><td>South Africa Standard Time</td><td>UTC+2</td><td>Немає літнього часу</td><td>Йоганнесбург, Кейптаун, Дурбан</td></tr>
        <tr><td>WAT</td><td>West Africa Time</td><td>UTC+1</td><td>Немає літнього часу</td><td>Лагос, Кіншаса, Альжір</td></tr>
    </tbody>
</table>
<h2>Східні й Центральноазійські часові пояси</h2>
<table class="tz-table">
    <thead><tr><th>Скороч.</th><th>Повна назва</th><th>UTC-зсув</th><th>Варіант літнього часу</th><th>Головні міста</th></tr></thead>
    <tbody>
        <tr><td>GST</td><td>Gulf Standard Time</td><td>UTC+4</td><td>Немає літнього часу</td><td>Дубай, Абу-Дабі, Маскат, Доха</td></tr>
        <tr><td>AST</td><td>Arabia Standard Time</td><td>UTC+3</td><td>Немає літнього часу</td><td>Ріяд, Джидда, Ель-Кувейт, Манама</td></tr>
        <tr><td>IRST</td><td>Iran Standard Time</td><td>UTC+3:30</td><td>IRDT (UTC+4:30)</td><td>Тегеран, Машхад, Ісфаган</td></tr>
        <tr><td>AFT</td><td>Afghanistan Time</td><td>UTC+4:30</td><td>Немає літнього часу</td><td>Кабул, Герат, Мазарі-Шариф</td></tr>
        <tr><td>PKT</td><td>Pakistan Standard Time</td><td>UTC+5</td><td>Немає літнього часу</td><td>Карачі, Лахор, Ісламабад</td></tr>
    </tbody>
</table>
<h2>Південноазійські й Південно-Східноазійські часові пояси</h2>
<table class="tz-table">
    <thead><tr><th>Скороч.</th><th>Повна назва</th><th>UTC-зсув</th><th>Варіант літнього часу</th><th>Головні міста</th></tr></thead>
    <tbody>
        <tr><td>IST</td><td>India Standard Time</td><td>UTC+5:30</td><td>Немає літнього часу</td><td>Мумбаї, Делі, Бангалор, Калкутта, Ченнай</td></tr>
        <tr><td>NPT</td><td>Nepal Time</td><td>UTC+5:45</td><td>Немає літнього часу</td><td>Катманду, Покхара, Біратнагар</td></tr>
        <tr><td>BST</td><td>Bangladesh Standard Time</td><td>UTC+6</td><td>Немає літнього часу</td><td>Дакка, Чіттагонг, Силет</td></tr>
        <tr><td>MMT</td><td>Myanmar Time</td><td>UTC+6:30</td><td>Немає літнього часу</td><td>Янгон, Мандалай, Нейпідо</td></tr>
        <tr><td>ICT</td><td>Indochina Time</td><td>UTC+7</td><td>Немає літнього часу</td><td>Бангкок, Ханої, Джакарта*, Пномпень</td></tr>
        <tr><td>WIB</td><td>Western Indonesian Time</td><td>UTC+7</td><td>Немає літнього часу</td><td>Джакарта, Бандунг, Сурабая</td></tr>
        <tr><td>CST</td><td>China Standard Time</td><td>UTC+8</td><td>Немає літнього часу</td><td>Пекін, Шанхай, Гонконг, Тайбей</td></tr>
        <tr><td>SGT</td><td>Singapore Time</td><td>UTC+8</td><td>Немає літнього часу</td><td>Сінгапур, Куала-Лумпур, Маніла, Перт</td></tr>
    </tbody>
</table>
<p><small>* Джакарта використовує WIB (UTC+7), а не ICT.</small></p>
<h2>Східноазійські й Тихоокеанські часові пояси</h2>
<table class="tz-table">
    <thead><tr><th>Скороч.</th><th>Повна назва</th><th>UTC-зсув</th><th>Варіант літнього часу</th><th>Головні міста</th></tr></thead>
    <tbody>
        <tr><td>JST</td><td>Japan Standard Time</td><td>UTC+9</td><td>Немає літнього часу</td><td>Токіо, Осака, Сеул*, Пхеньян*</td></tr>
        <tr><td>KST</td><td>Korea Standard Time</td><td>UTC+9</td><td>Немає літнього часу</td><td>Сеул, Пусан, Інчхон</td></tr>
        <tr><td>AWST</td><td>Australian Western Standard Time</td><td>UTC+8</td><td>Немає літнього часу</td><td>Перт, Брум, Карратха</td></tr>
        <tr><td>ACST</td><td>Australian Central Standard Time</td><td>UTC+9:30</td><td>ACDT (UTC+10:30)</td><td>Аделаїда, Дарвін, Аліс-Спрінгс</td></tr>
        <tr><td>AEST</td><td>Australian Eastern Standard Time</td><td>UTC+10</td><td>AEDT (UTC+11)</td><td>Сідней, Мельбурн, Брісбен*, Канберра</td></tr>
        <tr><td>NZST</td><td>New Zealand Standard Time</td><td>UTC+12</td><td>NZDT (UTC+13)</td><td>Окленд, Веллінгтон, Крайстчерч</td></tr>
    </tbody>
</table>
<p><small>* Сеул і Пхеньян використовують KST, а не JST. * Брісбен (Квінсленд) не переходить на літній час.</small></p>
<h2>Двозначні скорочення — Увага</h2>
<p>Деякі скорочення залежно від контексту означають різні пояси:</p>
<ul>
    <li><strong>CST</strong> — Central Standard Time (UTC-6, Північна Америка) <em>або</em> China Standard Time (UTC+8) <em>або</em> Cuba Standard Time (UTC-5)</li>
    <li><strong>IST</strong> — India Standard Time (UTC+5:30) <em>або</em> Irish Standard Time (UTC+1, літо) <em>або</em> Israel Standard Time (UTC+2)</li>
    <li><strong>PST</strong> — Pacific Standard Time (UTC-8) <em>або</em> Philippine Standard Time (UTC+8)</li>
    <li><strong>BST</strong> — British Summer Time (UTC+1) <em>або</em> Bangladesh Standard Time (UTC+6) <em>або</em> Bougainville Standard Time (UTC+11)</li>
    <li><strong>AST</strong> — Atlantic Standard Time (UTC-4) <em>або</em> Arabia Standard Time (UTC+3) <em>або</em> Amazon Standard Time (UTC-4, Бразилія)</li>
</ul>
<p>Коли бачиш двозначний код, подивись на країну чи місто поруч. Для точних перерахунків скористайся нашим <a href="/uk/time-zone-converter.html">конвертером часових поясів</a>, який правильно обробляє всі ці випадки.</p>
<h2>Швидкий довідник: Дати переходу на літній час (Типові)</h2>
<ul>
    <li><strong>Північна Америка</strong>: 2-га неділя бер → 1-ша неділя лис</li>
    <li><strong>Європа</strong>: остання неділя бер → остання неділя жов</li>
    <li><strong>Австралія (південний схід)</strong>: 1-ша неділя жов → 1-ша неділя кві</li>
    <li><strong>Нова Зеландія</strong>: остання неділя вер → 1-ша неділя кві</li>
    <li><strong>Чилі</strong>: 1-ша неділя вер → 1-ша неділя кві</li>
    <li><strong>Парагвай</strong>: 1-ша неділя жов → остання неділя бер</li>
</ul>
<h2>Збережи Цю Сторінку, Використовуй Інструмент</h2>
<p>Тобі не потрібно запам'ятовувати 50+ кодів. Збережи цю сторінку як довідкову таблицю. Коли потрібен точний перерахунок для конкретної дати — особливо під час тижнів переходу на літній час — скористайся нашим <a href="/uk/time-difference.html">калькулятором різниці часу</a> або <a href="/uk/meeting-planner.html">планувальником зустрічей</a>. Вони використовують IANA базу часових поясів, тому кожен зсув актуальний і правильний.</p>"""),
 'ru': ('Шпаргалка по аббревиатурам часовых поясов (2026)',
   'Быстрый справочник по всем основным аббревиатурам часовых поясов — EST, PST, CET, IST, JST и 50 других. Включает UTC-смещения, варианты летнего времени и города, использующие каждую.',
   'аббревиатуры часовых поясов, EST PST CST MST, шпаргалка UTC-смещений, список кодов часового пояса, акронимы часового пояса, аббревиатуры летнего времени',
   'Шпаргалка по аббревиатурам часовых поясов',
   """<p>Вы видите "EST" в подтверждении рейса, "CET" в приглашении на встречу, "IST" в файле лога. Каждая аббревиатура означает конкретное смещение от UTC, но некоторые означают разное летом и зимой. Эта шпаргалка дает точное смещение, основные города и меняет ли летнее время её.</p>
<h2>Североамериканские часовые пояса</h2>
<table class="tz-table">
    <thead><tr><th>Аббр.</th><th>Полное название</th><th>UTC-смещ.</th><th>Вариант летнего времени</th><th>Основные города</th></tr></thead>
    <tbody>
        <tr><td>EST</td><td>Eastern Standard Time</td><td>UTC-5</td><td>EDT (UTC-4)</td><td>Нью-Йорк, Торонто, Майами, Атланта</td></tr>
        <tr><td>EDT</td><td>Eastern Daylight Time</td><td>UTC-4</td><td>EST (зима)</td><td>Те же города, мар-ноя</td></tr>
        <tr><td>CST</td><td>Central Standard Time</td><td>UTC-6</td><td>CDT (UTC-5)</td><td>Чикаго, Даллас, Мехико, Хьюстон</td></tr>
        <tr><td>CDT</td><td>Central Daylight Time</td><td>UTC-5</td><td>CST (зима)</td><td>Те же города, мар-ноя</td></tr>
        <tr><td>MST</td><td>Mountain Standard Time</td><td>UTC-7</td><td>MDT (UTC-6)</td><td>Денвер, Финикс*, Эдмонтон, Эль-Пасо</td></tr>
        <tr><td>MDT</td><td>Mountain Daylight Time</td><td>UTC-6</td><td>MST (зима)</td><td>Те же города (кроме Аризоны)</td></tr>
        <tr><td>PST</td><td>Pacific Standard Time</td><td>UTC-8</td><td>PDT (UTC-7)</td><td>Лос-Анджелес, Ванкувер, Сиэтл, Тихуана</td></tr>
        <tr><td>PDT</td><td>Pacific Daylight Time</td><td>UTC-7</td><td>PST (зима)</td><td>Те же города, мар-ноя</td></tr>
        <tr><td>AKST</td><td>Alaska Standard Time</td><td>UTC-9</td><td>AKDT (UTC-8)</td><td>Анкоридж, Фэрбанкс, Джуно</td></tr>
        <tr><td>HST</td><td>Hawaii-Aleutian Standard Time</td><td>UTC-10</td><td>Нет летнего времени</td><td>Гонолулу, Хайло, Адак</td></tr>
    </tbody>
</table>
<p><small>* Аризона (кроме резервации Навахо) не переходит на летнее время и остаётся на MST круглый год.</small></p>
<h2>Атлантические и Южноамериканские часовые пояса</h2>
<table class="tz-table">
    <thead><tr><th>Аббр.</th><th>Полное название</th><th>UTC-смещ.</th><th>Вариант летнего времени</th><th>Основные города</th></tr></thead>
    <tbody>
        <tr><td>AST</td><td>Atlantic Standard Time</td><td>UTC-4</td><td>ADT (UTC-3)</td><td>Галифакс, Сан-Хуан, Бермуды, Каракас</td></tr>
        <tr><td>BRT</td><td>Brasilia Time</td><td>UTC-3</td><td>Нет летнего времени с 2019</td><td>Сан-Паулу, Рио-де-Жанейро, Бразилиа</td></tr>
        <tr><td>ART</td><td>Argentina Time</td><td>UTC-3</td><td>Нет летнего времени с 2009</td><td>Буэнос-Айрес, Кордова, Росарио</td></tr>
        <tr><td>CLT</td><td>Chile Standard Time</td><td>UTC-4</td><td>CLST (UTC-3)</td><td>Сантьяго, Вальпараисо, Консепсьон</td></tr>
    </tbody>
</table>
<h2>Европейские и Африканские часовые пояса</h2>
<table class="tz-table">
    <thead><tr><th>Аббр.</th><th>Полное название</th><th>UTC-смещ.</th><th>Вариант летнего времени</th><th>Основные города</th></tr></thead>
    <tbody>
        <tr><td>GMT</td><td>Greenwich Mean Time</td><td>UTC+0</td><td>BST (UTC+1)</td><td>Лондон, Дублин, Лиссабон (зима)</td></tr>
        <tr><td>BST</td><td>British Summer Time</td><td>UTC+1</td><td>GMT (зима)</td><td>Лондон, Дублин, Эдинбург (лето)</td></tr>
        <tr><td>WET</td><td>Western European Time</td><td>UTC+0</td><td>WEST (UTC+1)</td><td>Лиссабон, Касабланка, Рейкьявик</td></tr>
        <tr><td>CET</td><td>Central European Time</td><td>UTC+1</td><td>CEST (UTC+2)</td><td>Париж, Берлин, Рим, Мадрид, Варшава</td></tr>
        <tr><td>CEST</td><td>Central European Summer Time</td><td>UTC+2</td><td>CET (зима)</td><td>Те же города, мар-окт</td></tr>
        <tr><td>EET</td><td>Eastern European Time</td><td>UTC+2</td><td>EEST (UTC+3)</td><td>Хельсинки, Киев, Бухарест, Каир</td></tr>
        <tr><td>MSK</td><td>Moscow Standard Time</td><td>UTC+3</td><td>Нет летнего времени с 2014</td><td>Москва, Санкт-Петербург, Стамбул, Минск</td></tr>
        <tr><td>SAST</td><td>South Africa Standard Time</td><td>UTC+2</td><td>Нет летнего времени</td><td>Йоханнесбург, Кейптаун, Дурбан</td></tr>
        <tr><td>WAT</td><td>West Africa Time</td><td>UTC+1</td><td>Нет летнего времени</td><td>Лагос, Киншаса, Алжир</td></tr>
    </tbody>
</table>
<h2>Ближневосточные и Центральноазиатские часовые пояса</h2>
<table class="tz-table">
    <thead><tr><th>Аббр.</th><th>Полное название</th><th>UTC-смещ.</th><th>Вариант летнего времени</th><th>Основные города</th></tr></thead>
    <tbody>
        <tr><td>GST</td><td>Gulf Standard Time</td><td>UTC+4</td><td>Нет летнего времени</td><td>Дубай, Абу-Даби, Маскат, Доха</td></tr>
        <tr><td>AST</td><td>Arabia Standard Time</td><td>UTC+3</td><td>Нет летнего времени</td><td>Эр-Рияд, Джидда, Эль-Кувейт, Манама</td></tr>
        <tr><td>IRST</td><td>Iran Standard Time</td><td>UTC+3:30</td><td>IRDT (UTC+4:30)</td><td>Тегеран, Машхад, Исфаган</td></tr>
        <tr><td>AFT</td><td>Afghanistan Time</td><td>UTC+4:30</td><td>Нет летнего времени</td><td>Кабул, Герат, Мазари-Шариф</td></tr>
        <tr><td>PKT</td><td>Pakistan Standard Time</td><td>UTC+5</td><td>Нет летнего времени</td><td>Карачи, Лахор, Исламабад</td></tr>
    </tbody>
</table>
<h2>Южноазиатские и Юго-Восточноазиатские часовые пояса</h2>
<table class="tz-table">
    <thead><tr><th>Аббр.</th><th>Полное название</th><th>UTC-смещ.</th><th>Вариант летнего времени</th><th>Основные города</th></tr></thead>
    <tbody>
        <tr><td>IST</td><td>India Standard Time</td><td>UTC+5:30</td><td>Нет летнего времени</td><td>Мумбаи, Дели, Бангалор, Калькутта, Ченнай</td></tr>
        <tr><td>NPT</td><td>Nepal Time</td><td>UTC+5:45</td><td>Нет летнего времени</td><td>Катманду, Покхара, Биратнагар</td></tr>
        <tr><td>BST</td><td>Bangladesh Standard Time</td><td>UTC+6</td><td>Нет летнего времени</td><td>Дакка, Читтагонг, Силет</td></tr>
        <tr><td>MMT</td><td>Myanmar Time</td><td>UTC+6:30</td><td>Нет летнего времени</td><td>Янгон, Мандалай, Нейпьидо</td></tr>
        <tr><td>ICT</td><td>Indochina Time</td><td>UTC+7</td><td>Нет летнего времени</td><td>Бангкок, Ханои, Джакарта*, Пномпень</td></tr>
        <tr><td>WIB</td><td>Western Indonesian Time</td><td>UTC+7</td><td>Нет летнего времени</td><td>Джакарта, Бандунг, Сурабая</td></tr>
        <tr><td>CST</td><td>China Standard Time</td><td>UTC+8</td><td>Нет летнего времени</td><td>Пекин, Шанхай, Хунконг, Тайбэй</td></tr>
        <tr><td>SGT</td><td>Singapore Time</td><td>UTC+8</td><td>Нет летнего времени</td><td>Сингапур, Куала-Лумпур, Манила, Перт</td></tr>
    </tbody>
</table>
<p><small>* Джакарта использует WIB (UTC+7), а не ICT.</small></p>
<h2>Восточноазиатские и Тихоокеанские часовые пояса</h2>
<table class="tz-table">
    <thead><tr><th>Аббр.</th><th>Полное название</th><th>UTC-смещ.</th><th>Вариант летнего времени</th><th>Основные города</th></tr></thead>
    <tbody>
        <tr><td>JST</td><td>Japan Standard Time</td><td>UTC+9</td><td>Нет летнего времени</td><td>Токио, Осака, Сеул*, Пхеньян*</td></tr>
        <tr><td>KST</td><td>Korea Standard Time</td><td>UTC+9</td><td>Нет летнего времени</td><td>Сеул, Пусан, Инчхон</td></tr>
        <tr><td>AWST</td><td>Australian Western Standard Time</td><td>UTC+8</td><td>Нет летнего времени</td><td>Перт, Брум, Карратха</td></tr>
        <tr><td>ACST</td><td>Australian Central Standard Time</td><td>UTC+9:30</td><td>ACDT (UTC+10:30)</td><td>Аделаида, Дарвин, Алис-Спрингс</td></tr>
        <tr><td>AEST</td><td>Australian Eastern Standard Time</td><td>UTC+10</td><td>AEDT (UTC+11)</td><td>Сидней, Мельбурн, Брисбен*, Канберра</td></tr>
        <tr><td>NZST</td><td>New Zealand Standard Time</td><td>UTC+12</td><td>NZDT (UTC+13)</td><td>Окленд, Веллингтон, Крайстчерч</td></tr>
    </tbody>
</table>
<p><small>* Сеул и Пхеньян используют KST, а не JST. * Брисбен (Квинсленд) не переходит на летнее время.</small></p>
<h2>Двусмысленные аббревиатуры — Внимание</h2>
<p>Некоторые аббревиатуры в зависимости от контекста означают разные зоны:</p>
<ul>
    <li><strong>CST</strong> — Central Standard Time (UTC-6, Северная Америка) <em>или</em> China Standard Time (UTC+8) <em>или</em> Cuba Standard Time (UTC-5)</li>
    <li><strong>IST</strong> — India Standard Time (UTC
