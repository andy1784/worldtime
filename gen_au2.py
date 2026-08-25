# -*- coding: utf-8 -*-
"""AU DST translations part 2: IT, ZH, JA, UK."""
import json as _json

def _faq(qa):
    items = [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qa]
    return _json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": items}, ensure_ascii=False)

POSTS_AU2 = []

# ---------------- IT ----------------
POSTS_AU2.append(('it',
 'Come funziona l\u2019ora legale in Australia — guida stato per stato',
 'L\u2019ora legale in Australia varia a seconda dello stato. Alcuni la osservano, altri no, e le differenze di orario cambiano quattro volte l\u2019anno.',
 'ora legale Australia, fusi orari Australia, ora Sydney, ora Perth',
 ('Home', 'Blog', 'Ora legale in Australia', 'Vai al contenuto principale', 'Caricamento di World Time...', 'Briciole di pane', 'Privacy', 'Chi siamo', 'Contatti', 'Termini'),
 '📅 27 giugno 2026 &nbsp;·&nbsp; ⏱ 8 min di lettura &nbsp;·&nbsp; 🏷 Australia',
 f'''<h2>Come funziona l\u2019ora legale in Australia</h2>
<p>L\u2019Australia è uno dei paesi più fuorvianti al mondo per quanto riguarda l\u2019ora legale. Non esiste una regola nazionale unica: ogni stato e territorio decide da solo. Il risultato è un mosaico in cui la differenza tra Sydney e Brisbane cambia due volte l\u2019anno, mentre quella tra Sydney e Perth si sposta due volte l\u2019anno seguendo uno schema completamente diverso.</p>
<h2>Gli stati che spostano le lancette</h2>
<p>Nuovo Galles del Sud, Victoria, Australia Meridionale, Tasmania e Territorio della Capitale Australiana passano all\u2019ora legale la prima domenica di ottobre e tornano alla normale la prima domenica di aprile. Durante questo periodo anticipano gli orologi di un\u2019ora.</p>
<h2>Gli stati che non la osservano</h2>
<p>Queensland, Australia Occidentale e Territorio del Nord vivono tutto l\u2019anno sull\u2019ora standard. Il Queensland ha sottoposto la questione a referendum nel 1992, respingendola. L\u2019Australia Occidentale ha fatto una prova dal 2006 al 2009; il referendum del 2009 ha detto no anche lui.</p>
<h2>Il carosello delle differenze orarie</h2>
<p>Di norma Sydney (Nuovo Galles del Sud) e Brisbane (Queensland) stanno entrambe su UTC+10: nessuna differenza. Ma quando inizia l\u2019ora legale a ottobre, Sydney passa a UTC+11 mentre Brisbane resta a UTC+10. Per sei mesi le due maiores città della costa est sono separate da un\u2019ora.</p>
<p>Perth (Australia Occidentale) normalmente sta due ore indietro rispetto a Sydney (UTC+8 contro UTC+10). Con l\u2019ora legale il divario sale a tre ore (UTC+8 contro UTC+11). Per le aziende nazionali è un rompicapo che cambia continuamente.</p>
<h2>L\u2019eccezione: isola Lord Howe</h2>
<p>L\u2019isola Lord Howe, appartenente al Nuovo Galles del Sud, porta l\u2019idea all\u2019estremo: sposta l\u2019orologio solo di 30 minuti invece dei soliti 60. È il cambio di ora legale più piccolo del mondo: in estate l\u2019isola passa da UTC+10:30 a UTC+11:00.</p>
<h2>Perché l\u2019Australia funziona così?</h2>
<p>Risposta breve: federalismo e geografia. Gli stati settentrionali vicini all\u2019equatore vedono poca variazione nella durata del giorno durante l\u2019anno, quindi l\u2019ora legale rende poco. Gli stati meridionali come la Tasmania hanno inverni con giornate brevissime, e lì l\u2019idea è più popolare. Il governo federale ha rinunciato a imporre una regola nazionale, lasciando la decisione ai singoli stati.</p>
<p>Se pianificate riunioni tra stati australiani, controllate sempre l\u2019offset attuale. Aprite <a href="/">World Time Sync</a> per vedere gli orologi in diretta di Sydney, Melbourne, Brisbane, Perth e Adelaide.</p>
<h2>Domande frequenti</h2>
<div class="faq-section">
<div class="faq-item"><h3>Tutti gli stati australiani cambiano ora?</h3><p>No. Il sud-est (Nuovo Galles del Sud, Victoria, Australia Meridionale, Tasmania, ACT) osserva l\u2019ora legale; Queensland, Australia Occidentale e Territorio del Nord no.</p></div>
<div class="faq-item"><h3>Quando inizia e finisce l\u2019ora legale in Australia?</h3><p>Inizia la prima domenica di ottobre e finisce la prima domenica di aprile — al contrario dell\u2019emisfero boreale.</p></div>
<div class="faq-item"><h3>Quanto dista Perth da Sydney in estate?</h3><p>Tre ore: Sydney su UTC+11, Perth su UTC+8.</p></div>
</div>''',
 _faq([('Tutti gli stati australiani cambiano ora?', 'No. Il sud-est sì; Queensland, Australia Occidentale e Territorio del Nord no.'),
       ('Quando inizia e finisce l\'ora legale in Australia?', 'Prima domenica di ottobre fino alla prima domenica di aprile.'),
       ('Quanto dista Perth da Sydney in estate?', 'Tre ore: UTC+11 contro UTC+8.')]),
 '2026-06-27', 8))

# ---------------- ZH ----------------
POSTS_AU2.append(('zh',
 '澳大利亚的夏令时是怎么运作的 —— 分州指南',
 '澳大利亚的夏令时因州而异。有的州实行,有的不实行,两地时差一年要变四次。',
 '澳大利亚夏令时, 澳大利亚时区, 悉尼时间, 珀斯时间',
 ('首页', '博客', '澳大利亚的夏令时', '跳到主要内容', 'World Time 加载中...', '面包屑导航', '隐私政策', '关于我们', '联系我们', '服务条款'),
 '📅 2026年6月27日 &nbsp;·&nbsp; ⏱ 8 分钟阅读 &nbsp;·&nbsp; 🏷 澳大利亚',
 f'''<h2>澳大利亚的夏令时是怎么运作的</h2>
<p>在夏令时这件事上,澳大利亚是世界上最让人摸不着头脑的国家之一。它没有全国统一规则——每个州和领地各自决定。结果就是一幅拼布图景:悉尼与布里斯班的时差每年变化两次,而悉尼与珀斯的时差则按另一套完全不同的节奏每年移动两次。</p>
<h2>实行夏令时的州</h2>
<p>新南威尔士、维多利亚、南澳大利亚、塔斯马尼亚和首都领地在十月的第一个星期日进入夏令时,在四月的第一个星期日调回。期间这些州把时钟拨快一小时。</p>
<h2>不实行夏令时的州</h2>
<p>昆士兰、西澳大利亚和北领地全年使用标准时间。昆士兰曾在1992年就此举行公投并否决;西澳在2006至2009年试行过,2009年的公投同样说了“不”。</p>
<h2>时差的“轮换舞”</h2>
<p>正常情况下,悉尼(新南威尔士)和布里斯班(昆士兰)都在UTC+10——没有时差。但十月夏令时开始后,悉尼跳到UTC+11,布里斯班仍停留在UTC+10。整整半年,澳洲东海岸两座最大城市之间隔着一个小时。</p>
<p>珀斯(西澳)平时比悉尼慢两小时(UTC+8 对 UTC+10)。到了夏令时,差距扩大为三小时(UTC+8 对 UTC+11)。对全国性企业来说,这是常年头疼的问题。</p>
<h2>例外:豪勋爵岛</h2>
<p>隶属新南威尔士的豪勋爵岛把这套玩法推到极致:它的时钟只拨30分钟而不是常规的60分钟。这是世界上最小的夏令时调整——夏季该岛从UTC+10:30变为UTC+11:00。</p>
<h2>澳大利亚为什么这样安排?</h2>
<p>简短回答:联邦制加地理。靠近赤道的北部各州全年日照长度几乎不变,夏令时收益很小。塔斯马尼亚等南部州冬季白昼极短,那里对夏令时更欢迎。联邦政府不愿强推全国规则,把决定权留给各州。</p>
<p>如果你要在澳大利亚各州之间安排会议,务必核对当前的偏移量。打开<a href="/">World Time Sync</a>,查看悉尼、墨尔本、布里斯班、珀斯和阿德莱德的实时时钟。</p>
<h2>常见问题</h2>
<div class="faq-section">
<div class="faq-item"><h3>澳大利亚所有州都调钟吗?</h3><p>不是。东南部(新南威尔士、维多利亚、南澳、塔斯马尼亚、首都领地)实行夏令时;昆士兰、西澳和北领地不实行。</p></div>
<div class="faq-item"><h3>澳大利亚的夏令时什么时候开始和结束?</h3><p>十月第一个星期日开始,四月第一个星期日结束——正好与北半球相反。</p></div>
<div class="faq-item"><h3>夏季悉尼和珀斯相差几小时?</h3><p>三小时:悉尼UTC+11,珀斯UTC+8。</p></div>
</div>''',
 _faq([('澳大利亚所有州都调钟吗?', '不是。东南部实行;昆士兰、西澳和北领地不实行。'),
       ('澳大利亚夏令时何时开始和结束?', '十月第一个星期日至四月第一个星期日。'),
       ('夏季悉尼和珀斯相差几小时?', '三小时:UTC+11 对 UTC+8。')]),
 '2026-06-27', 8))

# ---------------- JA ----------------
POSTS_AU2.append(('ja',
 'オーストラリアのサマータイムの仕組み — 州ごとのガイド',
 'オーストラリアのサマータイムは州によって異なります。実施する州としない州があり、時差は年に4回変動します。',
 'オーストラリア サマータイム, オーストラリア タイムゾーン, シドニー時間, パース時間',
 ('ホーム', 'ブログ', 'オーストラリアのサマータイム', '本文へスキップ', 'World Time を読み込み中...', 'パンくずリスト', 'プライバシー', '私たちについて', 'お問い合わせ', '利用規約'),
 '📅 2026年6月27日 &nbsp;·&nbsp; ⏱ 8分で読める &nbsp;·&nbsp; 🏷 オーストラリア',
 f'''<h2>オーストラリアのサマータイムの仕組み</h2>
<p>サマータイムに関して、オーストラリアは世界でも最も紛らわしい国の一つです。全国的な統一ルールはなく、各州・準領土が独自に判断します。その結果、シドニーとブリスベンの時差は年に2回変わる一方、シドニーとパースの時差はまったく別のサイクルで年に2回ずれる、モザイク状の状況になっています。</p>
<h2>サマータイムを実施する州</h2>
<p>ニューサウスウェールズ、ビクトリア、南オーストラリア、タスマニア、首都特別地域(ACT)は10月第1日曜日にサマータイムへ移行し、4月第1日曜日に戻ります。この期間、時計を1時間進めます。</p>
<h2>実施しない州</h2>
<p>クイーンズランド、西オーストラリア、ノーザンテリトリーは一年中標準時です。クイーンズランドは1992年に住民投票を行い否決されました。西オーストラリアは2006〜2009年に試験導入しましたが、2009年の住民投票でも否決されています。</p>
<h2>時差の「入れ替わりダンス」</h2>
<p>通常、シドニー(NSW)とブリスベン(クイーンズランド)はどちらもUTC+10で、時差はありません。しかし10月にサマータイムが始まると、シドニーはUTC+11へ移行し、ブリスベンはUTC+10のまま。半年間、東海岸の2大都市には1時間のずれが生じます。</p>
<p>パース(西豪州)は通常シドニーの2時間後ろ(UTC+8 対 UTC+10)ですが、サマータイム中は3時間差(UTC+8 対 UTC+11)になります。全国展開する企業にとっては悩みの種です。</p>
<h2>例外:ロード・ハウ島</h2>
<p>NSWに属するロード・ハウ島はこの発想を極限まで進めています。時計を通常の60分ではなくわずか30分しか動かさないのです。これは世界最小のサマータイム調整で、夏季は島がUTC+10:30からUTC+11:00へ移行します。</p>
<h2>なぜこんな仕組みなのか?</h2>
<p>短く言えば、連邦制と地理です。赤道に近い北部の州では昼の長さが年間を通してほぼ変わらず、サマータイムのメリットが小さくなります。タスマニアのような南部の州は冬の日照が非常に短く、賛成派が多いのです。連邦政府は全国的なルールを課すことを避け、判断を各州に委ねています。</p>
<p>オーストラリア国内の州をまたぐ会議を計画する際は、必ず現在のオフセットを確認してください。<a href="/">World Time Sync</a>を開けば、シドニー、メルボルン、ブリスベン、パース、アデレードのライブ時計が見られます。</p>
<h2>よくある質問</h2>
<div class="faq-section">
<div class="faq-item"><h3>オーストラリアのすべての州が時計を変えますか?</h3><p>いいえ。南東部(NSW、ビクトリア、南豪、タスマニア、ACT)は実施しますが、クイーンズランド、西豪州、ノーザンテリトリーは実施しません。</p></div>
<div class="faq-item"><h3>オーストラリアのサマータイムはいつ始まりいつ終わりますか?</h3><p>10月第1日曜日に始まり、4月第1日曜日に終わります。北半球とは逆です。</p></div>
<div class="faq-item"><h3>夏のシドニーとパースの時差は?</h3><p>3時間です。シドニーUTC+11、パースUTC+8。</p></div>
</div>''',
 _faq([('オーストラリアのすべての州が時計を変えますか?', 'いいえ。南東部のみ実施し、QLD・WA・NTは実施しません。'),
       ('サマータイムはいつ始まりいつ終わりますか?', '10月第1日曜日開始、4月第1日曜日終了。'),
       ('夏のシドニーとパースの時差は?', '3時間:UTC+11 対 UTC+8。')]),
 '2026-06-27', 8))
