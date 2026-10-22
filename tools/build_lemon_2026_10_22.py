"""Builds the Lemon microsite pages in /lemon/ from shared header, footer and content.
Run from the repo root: python3 tools/build_lemon_2026_10_22.py"""
import os

OUT = os.path.join(os.path.dirname(__file__), '..', 'lemon')
UTM = '?utm_source=michaelkbaines_lemon&utm_medium=referral'

def un(photo, w=1200):
    return f'https://images.unsplash.com/{photo}?auto=format&fit=crop&w={w}&q=70'

def credit(name, user, note=''):
    n = f'{note} · ' if note else ''
    return f'<figcaption>{n}ภาพ · Photo: <a href="https://unsplash.com/@{user}{UTM}" target="_blank" rel="noopener">{name}</a> / <a href="https://unsplash.com/{UTM}" target="_blank" rel="noopener">Unsplash</a></figcaption>'

def bi(th, en, cls=''):
    c = f' class="{cls}"' if cls else ''
    return f'<p{c}>{th}<span class="t-en">{en}</span></p>'

def li(f):
    th, en = f
    return f'<li>{th}<span class="t-en">{en}</span></li>'

PH = {
  'aonang': ('photo-1730772408559-c9d60fda6560', 'Aleksei Zhivilov', 'bb009x', 'คนขับเรือหางยาวนำเรือเข้าฝั่งที่กระบี่ · A boatman bringing a longtail in, Krabi'),
  'railay': ('photo-1664542777435-be75eb20ecd5', 'Steven Watson', 'ottz0', 'หาดไร่เลย์ · Railay Beach'),
  'railay2': ('photo-1736753399626-578b167b85b7', 'Laura', 'lauraemma_d', 'เรือหางยาวที่ไร่เลย์ · Longtails at Railay'),
  'tonsai': ('photo-1773489347098-423767290139', 'Jan Hildebrand', 'hildi_', 'หน้าผาหินปูนที่หาดต้นไทร · Limestone cliffs at Tonsai'),
  'monkey': ('photo-1603649637473-1aaeff93d311', 'Ioana Mohanu', 'iua713', 'ลิงที่วัดถ้ำเสือ · A monkey at Tiger Cave Temple'),
  'street': ('photo-1655562546244-f54950d0858a', 'ThaimaaOpas', 'thaimaaopas', 'แผงอาหารริมทาง · A street food stall'),
  'durian': ('photo-1653877490794-188135cd450b', 'Alexey Demidov', 'alexeydemidov', 'ทุเรียน · Durian'),
  'market': ('photo-1551717309-88444dbe54f5', 'Joshua Rawson-Harris', 'joshrh19', 'ตลาดกลางคืนในไทย · A night market in Thailand'),
  'temple': ('photo-1780776145695-634f694ec0b3', 'Marcel L.', 'ml_75', 'วัดไทย · A Thai temple'),
  'buddha': ('photo-1584263477058-c0017f00c971', 'Syed Ahmad', 'syedabsarahmad', 'พระพุทธรูปบนยอดวัดถ้ำเสือ · The Buddha at the top of Tiger Cave Temple'),
  'krathong': ('photo-1766430310165-0b19fb2c45e2', 'Fabio & Muri', 'fabio2304', 'กระทงลอยน้ำ · Krathongs on the water'),
  'lax': ('photo-1792500285826-fe68e959fe34', 'David Syphers', 'dsyphers', 'อาคารผู้โดยสารระหว่างประเทศทอม แบรดลีย์ สนามบิน LAX · Tom Bradley International Terminal, LAX'),
  'freeway': ('photo-1609320518571-cbde7ea56184', 'kaleb tapp', 'kalebtapp', 'ฟรีเวย์ในลอสแอนเจลิส · A Los Angeles freeway'),
  'getty': ('photo-1582346992845-c963d5b0ba0d', 'Lydia Koh', 'lydiakphotography', 'ทางเข้าเก็ตตี้ เซ็นเตอร์ · The entrance to the Getty Center'),
  'gettyview': ('photo-1582346992837-4b98df3bf1e0', 'Lydia Koh', 'lydiakphotography', 'วิวลอสแอนเจลิสจากเก็ตตี้ · Looking out over Los Angeles from the Getty'),
  'coast': ('photo-1764565689754-e1b90e6ab7a2', 'Fabio Sasso', 'abduzeedo', 'ถนนเลียบชายฝั่งแคลิฟอร์เนีย · A California coast road'),
  'diner': ('photo-1772164521259-786fa72a8e2d', 'adam roye', 'psco', 'ร้านไดเนอร์แบบอเมริกัน · An American diner'),
}

def fig(key, w=1200, alt=None):
    p, name, user, cap = PH[key]
    return f'<figure><img src="{un(p, w)}" alt="{alt or cap}" loading="lazy" width="1200" height="800">{credit(name, user, cap)}</figure>'

def bookfig(src, cap):
    return f'<figure><img src="img/{src}" alt="{cap}" loading="lazy" width="1400" height="747">' \
           f'<figcaption>{cap} · ภาพจากหนังสือ · From the book</figcaption></figure>'

def video(vid, title, sub):
    return f'''<div class="video"><div class="frame" data-yt="{vid}">
<img src="https://i.ytimg.com/vi/{vid}/hqdefault.jpg" alt="" loading="lazy" width="480" height="360">
<button type="button" aria-label="เล่นวิดีโอ · Play video: {title}">▶ เล่น</button></div>
<div class="cap"><b>{title}</b><span>{sub}</span></div></div>'''

LOGO = '''<svg viewBox="0 0 100 100" aria-hidden="true"><circle cx="50" cy="50" r="48" fill="#F2C230"/><circle cx="50" cy="50" r="41" fill="#FFF4CC"/><g stroke="#F2C230" stroke-width="4"><line x1="50" y1="10" x2="50" y2="90"/><line x1="10" y1="50" x2="90" y2="50"/><line x1="22" y1="22" x2="78" y2="78"/><line x1="78" y1="22" x2="22" y2="78"/></g></svg>'''

NAV = [('index.html', 'หน้าแรก', 'Home'), ('places.html', 'สถานที่', 'Places'), ('culture.html', 'วัฒนธรรม', 'Culture'), ('toolkit.html', 'เครื่องมือ', 'Toolkit')]

def page(fname, title, desc, body, og='../assets/lemon-cover.jpg'):
    nav = ''.join(f'<a href="{h}"{" aria-current=page" if h == fname else ""}>{t}<small>{e}</small></a>' for h, t, e in NAV)
    html = f'''<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://michaelkbaines.com/lemon/{'' if fname == 'index.html' else fname}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://michaelkbaines.com/assets/lemon-cover.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Prompt:wght@500;600;700&family=Sarabun:ital,wght@0,400;0,600;1,400&family=Lora:ital@1&display=swap" rel="stylesheet">
<link rel="stylesheet" href="lemon.css">
</head>
<body>
<header class="bar"><div class="wrap">
<a class="brand" href="index.html">{LOGO}<span>การผจญภัยของมะนาว<small>The Adventures of Lemon</small></span></a>
<nav class="nav" aria-label="เมนู · Menu">{nav}</nav>
</div></header>
<main>
{body}
</main>
<footer><div class="wrap">
<span>© 2026 Michael K. Baines · <a href="../">michaelkbaines.com</a> · <a href="../#newsletter">รับข่าวเมื่อหนังสือออก · Newsletter</a></span>
<span>ไม่มีคุกกี้ วิดีโอโหลดเมื่อคุณกดเล่นเท่านั้น · No cookies; videos load only when you press play.</span>
</div></footer>
<script>
document.querySelectorAll('.frame[data-yt]').forEach(function(f){{
  f.querySelector('button').addEventListener('click',function(){{
    var i=document.createElement('iframe');
    i.src='https://www.youtube-nocookie.com/embed/'+f.dataset.yt+'?autoplay=1&rel=0';
    i.title=this.getAttribute('aria-label');
    i.allow='autoplay; encrypted-media; picture-in-picture'; i.allowFullscreen=true;
    f.innerHTML=''; f.appendChild(i);
  }});
}});
</script>
</body>
</html>
'''
    open(os.path.join(OUT, fname), 'w').write(html)

PH.update({
  'griffith': ('photo-1766548729668-30bd92a37856', 'Venti Views', 'ventiviews', 'หอดูดาวกริฟฟิธกับดวงจันทร์ · Griffith Observatory and the moon'),
  'redondo': ('photo-1619778490679-f874d860c790', 'Hester Qiang', 'hesterqiang', 'พระอาทิตย์ตกที่เรดอนโดบีช · Sunset at Redondo Beach'),
  'catalina': ('photo-1745907429414-56c75c35b30f', 'Erick Morales Oyola', 'ejmoralesoyola', 'อ่าวอวาลอน เกาะคาทาลินา · Avalon Harbor, Catalina Island'),
})

def say(en, th):
    return f'<div class="say"><b>พูดเป็นภาษาอังกฤษ · Say it in English</b><span>{en}</span><br>{th}</div>'

def head(th, en):
    return f'<h2>{th}</h2><p class="en">{en}</p>'

# ---------------- index ----------------
index = f'''
<div class="hero"><div class="wrap">
<div>
<p class="eyebrow">นิยายสองภาษา ไทย–อังกฤษ · เล่มหนึ่งกำลังจะออก<span class="t-en">A bilingual Thai–English novel · Book One coming soon</span></p>
<h1>การผจญภัยของมะนาว<span class="en">The Adventures of Lemon</span></h1>
<p class="lead">มะนาวเป็นแม่บ้านโรงแรมที่อ่าวนาง พูดภาษาอังกฤษได้แค่ประโยคบนกระดาษของป้าเพ็ญ แล้ววันหนึ่งแขกห้อง 412 ก็ถามคำถามที่ไม่อยู่ในกระดาษ</p>
<p class="lead en">Lemon is a hotel housekeeper in Ao Nang who can only speak the English on Auntie Pen's card. Then the guest in Room 412 asks a question that isn't on it.</p>
<div class="actions"><a class="btn" href="#watch">▶ ดูก่อน อ่านทีหลัง · Watch first</a><a class="btn ghost" href="places.html">ไปเที่ยวกับมะนาว · Travel with Lemon</a></div>
</div>
<img class="cover" src="../assets/lemon-cover.jpg" alt="ปกหนังสือ การผจญภัยของมะนาว · Cover of The Adventures of Lemon" width="600" height="900">
</div></div>

<section class="band slim"><div class="wrap">
{bi('ทุกข้อความในเว็บนี้มีภาษาไทยอยู่บน ภาษาอังกฤษอยู่ล่าง อ่านไทยก่อน แล้วดูว่าภาษาอังกฤษพูดเรื่องเดียวกันอย่างไร แค่เลื่อนดูก็ได้เรียนแล้ว', 'Every line on this site is in Thai first, with English underneath. Read the Thai, then see how English says the same thing. Just scrolling is learning.', 'intro')}
</div></section>

<section id="watch"><div class="wrap">
{head('ดูก่อน อ่านทีหลัง', 'Watch first, read later')}
{bi('ไม่ชอบอ่านยาวๆ ไม่เป็นไร เริ่มจากดูที่ที่มะนาวอยู่ก่อน แล้วค่อยเปิดหนังสือ', "Don't like reading long things? That's fine. Start by seeing where Lemon lives, then open the book.", 'intro')}
<div class="videos">
{video('HTwP6yO21Yc', 'กระบี่ อ่าวนาง ไร่เลย์ ใน 10 นาที', 'Krabi, Ao Nang and Railay in 10 minutes · World Wild Hearts · English')}
{video('PclWXHDAy28', 'แอโรบิกในสวน ความสุขทะลัก', 'Free park aerobics, like Thara Park in Chapter 2 · Thai PBS · Thai')}
{video('2H6P4pRuCLU', 'สงกรานต์ที่ไทยทาวน์ ลอสแอนเจลิส', 'Songkran in Thai Town, Los Angeles · English')}
</div>
</div></section>

<section class="paper"><div class="wrap">
{head('สำรวจโลกของมะนาว', "Explore Lemon's world")}
<div class="tiles">
<a class="tile" href="places.html"><img src="{un(PH['aonang'][0], 700)}" alt="เรือหางยาวที่กระบี่ · A longtail boat in Krabi" loading="lazy"><div><h3>สถานที่ในเรื่อง</h3><p>เมืองกระบี่ อ่าวนาง วัด ไร่เลย์<span class="t-en">Krabi Town, Ao Nang, temples, Railay</span></p></div></a>
<a class="tile" href="places.html#la"><img src="{un(PH['getty'][0], 700)}" alt="เก็ตตี้ เซ็นเตอร์ · The Getty Center" loading="lazy"><div><h3>ลอสแอนเจลิส</h3><p>สนามบิน ฟรีเวย์ พิพิธภัณฑ์ ท่าเรือ เกาะ<span class="t-en">The airport, freeway, museum, pier and island</span></p></div></a>
<a class="tile" href="culture.html"><img src="{un(PH['krathong'][0], 700)}" alt="กระทง · Krathongs" loading="lazy"><div><h3>ภาคใต้และวัฒนธรรม</h3><p>อาหาร เทศกาล และคำไทยที่แปลไม่ได้<span class="t-en">Food, festivals and Thai words English doesn't have</span></p></div></a>
<a class="tile" href="toolkit.html"><img src="img/act1.jpg" alt="ภาพจากหนังสือ · Art from the book" loading="lazy"><div><h3>เครื่องมือของคาร์ลอส</h3><p>เรียนจากเพลง ซีรีส์ และโทรศัพท์<span class="t-en">Learn from songs, shows and your phone</span></p></div></a>
</div>
</div></section>

<section><div class="wrap">
{head('ตัวละคร', "Who's who")}
<div class="people">
<div class="person"><b>มะนาว</b><span>Lemon, 26</span>{bi('แม่บ้านโรงแรมที่อ่าวนาง ลูกสาวช่างซ่อมมอเตอร์ไซค์ เก่งทุกอย่าง ยกเว้นการถูกมองเห็น', "A hotel housekeeper in Ao Nang and a motorbike mechanic's daughter. Good at everything except being seen.")}</div>
<div class="person"><b>คาร์ลอส</b><span>Carlos</span>{bi('แขกห้อง 412 จากแอลเอ แม่เป็นคนอุบล พ่อเป็นคนบราซิล พูดไทยสำเนียงอีสาน', 'The guest in Room 412, from L.A. His mother is from Ubon, his father from Brazil. He speaks Thai with an Isaan accent.')}</div>
<div class="person"><b>โรเบิร์ต</b><span>Robert</span>{bi('แฟนของมะนาว ลูกชายเจ้าของร้านอาหารบนหน้าผา ผู้ชายที่พูดแทนเธอ', "Lemon's boyfriend, son of the cliff-top restaurant's owner. The man who speaks for her.")}</div>
<div class="person"><b>ดา</b><span>Da</span>{bi('เพื่อนแม่บ้าน คนเมืองกระบี่ มุสลิม พูดได้สามภาษา ซ้อนมอเตอร์ไซค์ไปทำงานกับมะนาวทุกเช้า', 'A fellow housekeeper from Krabi Town. Muslim, speaks three languages, rides to work with Lemon every morning.')}</div>
<div class="person"><b>ป้าเพ็ญ</b><span>Auntie Pen</span>{bi('หัวหน้าแม่บ้าน ข่าวของป้าเร็วกว่าไวไฟ', "The head housekeeper. Her news travels faster than Wi-Fi.")}</div>
<div class="person"><b>เบียร์</b><span>Beer</span>{bi('เพื่อนสนิทตั้งแต่อนุบาล อยู่แคลิฟอร์เนีย คนที่สอนเสียงตัวอักษรให้มะนาวใต้ต้นมะม่วง', 'Her best friend since kindergarten, now in California. She taught Lemon letter sounds under the mango tree.')}</div>
</div>
<p class="note">ภาพตัวละครกำลังวาด จะมาเร็วๆ นี้<span class="t-en">Character illustrations are on the way.</span></p>
</div></section>

<section class="paper"><div class="wrap">
{head('ทำไมหนังสือเล่มนี้ต่าง', 'Why this book is different')}
<div class="cards">
<div class="card"><h3>เริ่มจากที่คุณรู้</h3><p class="en">Begin from what you know</p>{bi('บทแรกเป็นภาษาไทยเกือบทั้งหมด ภาษาอังกฤษเพิ่มขึ้นทีละนิดตามที่มะนาวเก่งขึ้น', 'The first chapter is almost all Thai. English grows a little at a time as Lemon gets better.')}</div>
<div class="card"><h3>เป็นละคร ไม่ใช่ตำรา</h3><p class="en">A drama, not a textbook</p>{bi('มีคู่แข่ง มีแม่ผัวในอนาคต มีสงครามผ้าเช็ดตัว และสงครามส้มตำที่ทำให้โดนห้ามเข้าร้าน', 'A rival, a future mother-in-law, a towel war, and a som tam fight that gets everyone banned from a restaurant.')}</div>
<div class="card"><h3>ชีวิตจริงของคนไทย</h3><p class="en">Real Thai life</p>{bi('หนี้นอกระบบ ซองเงินเดือนห้าซอง แอปที่เลิกใช้ และความกลัวพูดผิดที่คนไทยหลายคนรู้จัก', 'Informal debt, five payday envelopes, abandoned apps, and the fear of mistakes that many Thai people know.')}</div>
</div>
</div></section>

<section><div class="wrap">
{head('ซีรีส์มะนาว', 'The Lemon series')}
{bi('เล่มหลักเล่าเรื่องทั้งหมด เล่มต่อไปเริ่มจากคำที่คุณได้ยินในงานของคุณ', 'The main book tells the whole story. The next books start from the words you hear at your job.', 'intro')}
<ul class="series"><li class="now">มะนาวเรียนรู้ · Lemon Learns</li><li>มะนาวเดินทาง · Travels</li><li>มะนาวกินข้าวนอกบ้าน · Dines</li><li>มะนาวช้อปปิ้ง · Shops</li><li>มะนาวไปหาหมอ · Heals</li><li>มะนาวทำงาน · Works</li></ul>
<div class="actions"><a class="btn" href="../#newsletter">รับข่าวเมื่อหนังสือออก · Get news</a><a class="btn ghost" style="color:var(--teal);border-color:var(--teal)" href="../">หนังสือเล่มอื่นของผู้เขียน · Other books</a></div>
</div></section>
'''
page('index.html', 'การผจญภัยของมะนาว · The Adventures of Lemon', 'นิยายสองภาษาไทย–อังกฤษ สำหรับคนไทยที่อยากพูดภาษาอังกฤษ · A bilingual Thai–English novel, with real places, Southern Thai culture and free learning tools.', index)

# ---------------- places ----------------
def place(media, th, en, chips, body, facts, say_en, say_th, extra='', pid=''):
    ch = ''.join(f'<span class="chip">{c}</span>' for c in chips)
    fl = ''.join(li(f) for f in facts)
    i = f' id="{pid}"' if pid else ''
    return f'''<article class="place"{i}><div class="media">{media}{extra}</div><div>
<h3>{th}</h3><p class="en">{en}</p>{ch}{bi(*body)}<ul class="facts">{fl}</ul>
{say(say_en, say_th)}</div></article>'''

places = f'''
<div class="hero"><div class="wrap">
<div><p class="eyebrow">สถานที่ในเรื่อง<span class="t-en">Places in the book</span></p>
<h1>ไปเที่ยวกับมะนาว<span class="en">Travel with Lemon</span></h1>
<p class="lead">ทุกที่ในหนังสือเป็นที่จริง ยกเว้นโรงแรมกับร้านอาหาร ดูภาพ ดูคลิป แล้วลองพูดประโยคภาษาอังกฤษของแต่ละที่</p>
<p class="lead en">Every place in the book is real except the hotel and the restaurants. Look, watch, then try each place's English sentence.</p>
<div class="actions"><a class="btn" href="#krabi">กระบี่ · Krabi</a><a class="btn ghost" href="#la">ลอสแอนเจลิส · Los Angeles</a></div></div>
<img class="art" src="img/act0.jpg" alt="บ้านและอู่ของพ่อมะนาว ภาพจากหนังสือ · Father's house and workshop, from the book" width="1400" height="747">
</div></div>

<section id="krabi"><div class="wrap">
{head('กระบี่', 'Krabi')}
{place(bookfig('act0.jpg', "บ้านกับอู่ของพ่อ ใต้ต้นมะม่วง · Father's workshop"),
 'เมืองกระบี่', "Krabi Town · Lemon's home", ['บทที่ 1–3 · Ch 1–3', 'บทที่ 20–21 · Ch 20–21'],
 ('บ้านไม้สองชั้นกับอู่ซ่อมรถของพ่ออยู่ในซอยเล็กๆ ในเมืองกระบี่ ไม่ใช่ที่อ่าวนาง ที่นี่คือที่ที่คนกระบี่ใช้ชีวิตจริง ตลาดเช้า วัด มัสยิด และแม่น้ำกระบี่',
  "Father's two-storey wooden house and workshop are in a small soi in Krabi Town, not in Ao Nang. This is where Krabi people really live: the morning market, the temple, the mosque and the Krabi River."),
 [('ชื่อ กระบี่ แปลว่า ดาบ และดาบไขว้คือสัญลักษณ์ของจังหวัด', 'Krabi means "sword", and crossed swords are the province\'s symbol.'),
  ('เขาขนาบน้ำ ภูเขาหินปูนสองลูกสูงราว 100 เมตร ยืนประกบแม่น้ำกระบี่', 'Khao Khanap Nam: two limestone hills, about 100 metres high, stand on either side of the Krabi River.'),
  ('นั่งเรือหางยาวจากท่าเรือเจ้าฟ้าไปเขาขนาบน้ำราว 15 นาที', 'A longtail from Chao Fah Pier to Khao Khanap Nam takes about 15 minutes.')],
 'I live in Krabi Town, not in Ao Nang.', 'ฉันอยู่ในเมืองกระบี่ ไม่ได้อยู่อ่าวนาง')}
{place(fig('temple'), 'วัดแก้วโกรวาราม', 'Wat Kaew Korawaram · the white temple', ['บทที่ 20 · Ch 20'],
 ('เช้าวันแรกที่กลับบ้าน มะนาวไปทำบุญกับแม่ที่วัดสีขาวบนเนินกลางเมืองกระบี่ ทำบุญให้แม่ของเพื่อนคนหนึ่ง แม่ไม่ถามว่าเพื่อนคนไหน แต่แม่รู้',
  "On her first morning home, Lemon goes with her mother to the white temple on the hill in the middle of Krabi Town. She makes merit for a friend's mother. Her mother doesn't ask which friend. She knows."),
 [('วัดสีขาวทั้งหลัง อยู่บนเนินกลางเมือง ต้องเดินขึ้นบันไดยาว', 'The whole temple is white, on a hill in the centre of town, up a long staircase.'),
  ('ข้างในมีภาพจิตรกรรมฝาผนัง', 'Inside, the walls are covered in murals.'),
  ('ถอดรองเท้าก่อนเข้าโบสถ์ แต่งกายสุภาพ', 'Take off your shoes before going in, and dress politely.')],
 'Please take off your shoes.', 'กรุณาถอดรองเท้า',
 extra='<p class="note" style="margin-top:12px">ภาพนี้เป็นวัดไทยทั่วไป รอภาพจริงของผู้เขียน<span class="t-en">Photo shows a Thai temple; the author\'s own photo of Wat Kaew is coming.</span></p>')}
{place(fig('buddha'), 'วัดถ้ำเสือ', 'Tiger Cave Temple · Wat Tham Suea', ['บทที่ 20 · Ch 20'],
 ('หนองพามะนาวมาปีนบันไดราวหนึ่งพันสองร้อยหกสิบขั้น เพราะอ่านในพันทิปว่าคนอกหักต้องปีน ที่ยอด นักท่องเที่ยวขอให้เธอถ่ายรูป สี่ปีก่อนเธอยืนนิ่ง วันนี้เธอพูดว่า Sure',
  'Nong brings Lemon to climb about 1,260 steps, because he read on Pantip that broken hearts have to climb it. At the top, tourists ask her to take their photo. Four years ago she froze. Today she says, "Sure."'),
 [('อยู่ห่างจากเมืองกระบี่ราว 15 นาที', 'About 15 minutes from Krabi Town.'),
  ('บันไดราว 1,260 ขั้น แต่ละขั้นสูงไม่เท่ากัน ข้างบนมีพระพุทธรูปและวิวรอบทิศ', 'About 1,260 steps, all different heights. At the top: a golden Buddha and views in every direction.'),
  ('ระวังลิง มันชอบขโมยขวดน้ำ', 'Watch out for the monkeys. They love water bottles.')],
 'Could you take a photo of us?', 'ช่วยถ่ายรูปให้หน่อยได้ไหม', extra=fig('monkey', 900))}
{place(fig('market'), 'สวนธารา และถนนคนเดิน', 'Thara Park and Walking Street', ['บทที่ 2–3 · Ch 2–3', 'บทที่ 21 · Ch 21'],
 ('ทุกเย็น มะนาว แม่ ป้าเพ็ญ และดา มาเต้นแอโรบิกที่ลานริมแม่น้ำในสวนธารา ครูนับเป็นภาษาอังกฤษ และนี่คือที่ที่ป้าเพ็ญบอกว่าใส่ชุดดำแปลว่าโสด',
  'Every evening, Lemon, her mother, Auntie Pen and Da dance aerobics by the river in Thara Park. The teacher counts in English. And this is where Auntie Pen says wearing black means you are single.'),
 [('สวนสาธารณะฟรีริมแม่น้ำกระบี่ มีลู่วิ่งราว 1.15 กิโลเมตร', 'A free public park on the Krabi River, with a running track of about 1.15 km.'),
  ('ถนนคนเดินกระบี่เปิดศุกร์ เสาร์ อาทิตย์ ห้าโมงเย็นถึงสี่ทุ่ม', 'Krabi Walking Street is open Friday to Sunday, 5 to 10 p.m.')],
 'Left! Right! Turn around! Again!', 'ซ้าย ขวา หมุนตัว อีกครั้ง',
 extra='<p class="note" style="margin-top:12px">ภาพนี้เป็นตลาดกลางคืนในไทย ไม่ใช่ถนนคนเดินกระบี่โดยตรง<span class="t-en">Photo shows a Thai night market, not Krabi\'s Walking Street itself.</span></p>')}
{place(fig('aonang'), 'อ่าวนาง', "Ao Nang · where Lemon works", ['บทที่ 2–10 · Ch 2–10', 'บทที่ 21 · Ch 21'],
 ('โรงแรมในเรื่องเป็นโรงแรมสมมุติ แต่ชายหาด ร้านตัดสูทของคุณราช และแถวเรือหางยาวเป็นของจริง ทุกเช้ามะนาวกับดาขี่มอเตอร์ไซค์จากเมืองมาที่นี่ ยี่สิบกิโลเมตร',
  "The hotel in the story is made up, but the beach, Mr. Raj's tailor shop and the line of longtail boats are real. Every morning Lemon and Da ride twenty kilometres here from town."),
 [('ร้านค้าหลายร้านที่อ่าวนางเป็นของคนจากอินเดีย เนปาล และอีกหลายประเทศ', 'Many Ao Nang shops are run by people from India, Nepal and other countries.'),
  ('หัวเรือหางยาวผูกผ้าสามสีกับพวงมาลัย ถวายแม่ย่านาง ผู้คุ้มครองเรือ', "Longtail bows are tied with three-coloured cloth and garlands for Mae Ya Nang, the boat's guardian spirit.")],
 'Housekeeping! Would you like me to clean your room now?', 'แม่บ้านค่ะ ทำห้องตอนนี้ไหมคะ')}
{place(fig('railay'), 'ไร่เลย์', 'Railay', ['บทที่ 9 · Ch 9'],
 ('ลุงแดงพามะนาวกับคาร์ลอสนั่งเรือหางยาวไปไร่เลย์ แล้วคลื่นก็สาดหน้าคาร์ลอส ลุงแดงหัวเราะ',
  "Uncle Daeng takes Lemon and Carlos to Railay by longtail, and a wave hits Carlos in the face. Uncle Daeng laughs."),
 [('ไร่เลย์ถูกภูเขาหินปูนล้อมจนไปได้ทางเรือเท่านั้น', 'Railay is surrounded by limestone cliffs. You can only get there by boat.'),
  ('เป็นที่ปีนผาที่มีชื่อเสียงระดับโลก', "It's a world-famous rock-climbing spot.")],
 'Railay! One hundred baht! Go, go!', 'ไร่เลย์ ร้อยบาท ไปๆ', extra=fig('railay2', 900))}
</div></section>

<section class="paper" id="la"><div class="wrap">
{head('ลอสแอนเจลิส', 'Los Angeles')}
{bi('มะนาวไปอเมริกาหนึ่งเดือน พักบ้านเบียร์ที่ทอร์แรนซ์ คาร์ลอสให้การบ้านทุกวัน ไม่ใช่ในห้องเรียน แต่ในเมือง', "Lemon goes to America for one month and stays at Beer's house in Torrance. Carlos gives her homework every day, not in a classroom, but in the city.", 'intro')}
{place(fig('lax'), 'สนามบินลอสแอนเจลิส', 'LAX · Los Angeles International Airport', ['บทที่ 12 · Ch 12'],
 ('มะนาวไม่รู้คำว่า purpose แต่เธอรู้จักห้องนี้และรู้จักคำถามนี้ สถานที่สอนคำศัพท์ได้ เธออ่านป้ายทุกป้ายที่แขวนจากเพดาน',
  'Lemon doesn\'t know the word "purpose", but she knows this room and this question. A place can teach you a word. She reads every sign hanging from the ceiling.'),
 [('ป้ายที่มะนาวอ่าน: ARRIVALS, ALL PASSPORTS, BAGGAGE CLAIM, GROUND TRANSPORTATION', 'Signs Lemon reads: ARRIVALS, ALL PASSPORTS, BAGGAGE CLAIM, GROUND TRANSPORTATION.'),
  ('ไฟลต์ระหว่างประเทศส่วนใหญ่ใช้อาคารทอม แบรดลีย์', 'Most international flights use the Tom Bradley International Terminal.'),
  ('คำถามที่ตม.: What\'s the purpose of your visit? How long are you staying?', 'Questions at immigration: purpose of visit, and length of stay.')],
 'I am visiting my friend. I am staying for one month.', 'มาเยี่ยมเพื่อน อยู่หนึ่งเดือน')}
{place(fig('freeway'), 'ฟรีเวย์', 'The freeway', ['บทที่ 12 · Ch 12'],
 ('ฟรีเวย์คือแม่น้ำเหล็ก หกเลนไปทางหนึ่ง หกเลนกลับอีกทาง ป้ายเขียวใหญ่แขวนเหนือถนน มะนาวอ่านทันแค่ครึ่งเดียว',
  'The freeway is a river of metal. Six lanes one way, six lanes the other. Big green signs hang over the road. Lemon can only read half of them in time.'),
 [('ป้ายบอกทางบนฟรีเวย์เป็นสีเขียว ป้ายทางออกเขียนว่า EXIT', 'Freeway direction signs are green. Exit signs say EXIT.'),
  ('คนแอลเอบอกระยะทางเป็นเวลา ไม่ใช่ไมล์', 'People in L.A. give distance in minutes, not miles.')],
 "It's twenty minutes without traffic.", 'ถ้ารถไม่ติดยี่สิบนาที')}
{place(bookfig('act2.jpg', 'ลอสแอนเจลิส · Los Angeles'), 'ไทยทาวน์', 'Thai Town', ['บทที่ 12 · Ch 12', 'บทที่ 17 · Ch 17'],
 ('วันแรกในอเมริกา คาร์ลอสพามะนาวไปกินส้มตำที่ร้านอีสานเล็กๆ ป้าฟันทองพูดอีสานเร็วจนคาร์ลอสฟังไม่ทัน และมะนาวต้องแปลภาษาแม่ของเขาให้เขาฟัง',
  "On her first day in America, Carlos takes Lemon for som tam at a small Isaan restaurant. The gold-toothed auntie speaks Isaan so fast that Carlos can't keep up, and Lemon has to translate his own mother's language for him."),
 [('ย่านไทยทาวน์แห่งแรกในอเมริกา ตั้งชื่อเมื่อปี 1999', "America's first official Thai Town, named in 1999."),
  ('อยู่บนถนนฮอลลีวูด ทางเข้ามีรูปปั้นอัปสรสีห์', 'On Hollywood Boulevard, with Apsonsi statues at the entrance.'),
  ('ทุกเดือนเมษายนมีงานสงกรานต์', 'Every April there is a Songkran festival.')],
 'Medium spicy, please.', 'เผ็ดกลางค่ะ', extra=f'<div style="margin-top:14px">{video("2H6P4pRuCLU", "อาหารในงานสงกรานต์ ไทยทาวน์", "Songkran food in Thai Town")}</div>')}
{place(fig('redondo'), 'ท่าเรือเรดอนโดบีช', 'Redondo Beach Pier', ['บทที่ 14 · Ch 14'],
 ('การบ้านวันที่สามคือท่าเรือ มะนาวคุยกับคุณลุงชาวฟิลิปปินส์ที่ตกปลาอยู่ยี่สิบนาที เรื่องปลา เรือ และหลาน โดยไม่ได้คิดเรื่องไวยากรณ์เลย',
  "Day three's homework is the pier. Lemon talks to a Filipino grandfather who is fishing for twenty minutes, about fish, boats and grandchildren, and doesn't think about grammar once."),
 [('ท่าเรือรูปเกือกม้า ห่างทอร์แรนซ์ไม่กี่นาที', 'A horseshoe-shaped pier, a few minutes from Torrance.'),
  ('สิงโตทะเลนอนอยู่แถวท่าเรือคิงฮาร์เบอร์ เสียงดังมาก', 'Sea lions sleep near King Harbor. They are very loud.'),
  ('ตลาดปลาขายปูเป็นปอนด์ ตกปลาบนท่าเรือไม่ต้องมีใบอนุญาต', 'The fish market sells crab by the pound. You don\'t need a licence to fish from the pier.')],
 'How much is one crab?', 'ปูตัวละเท่าไหร่')}
{place(fig('diner'), 'ร้านไดเนอร์ริมถนนเลียบชายฝั่ง', 'A diner on Pacific Coast Highway', ['บทที่ 14 · Ch 14'],
 ('พนักงานเสิร์ฟเรียกมะนาวว่า sweetie กับ hon เบียร์อธิบายว่าไม่ได้แปลว่าชอบ แปลว่าเป็นกันเอง เหมือนแม่ค้าที่ตลาดเรียกทุกคนว่าลูก',
  'The waitress calls Lemon "sweetie" and "hon". Beer explains it doesn\'t mean she likes her. It means "I\'m friendly", like a market auntie who calls everyone "child".'),
 [('ไดเนอร์อเมริกันมีเบาะแดง เคาน์เตอร์ยาว และกาแฟเติมฟรี', 'American diners have red seats, a long counter and free coffee refills.'),
  ('ทิปประมาณ 15–20 เปอร์เซ็นต์ของค่าอาหาร', 'The tip is about 15–20% of the bill.')],
 'Can I get a grilled cheese and a Coke, please?', 'ขอแซนด์วิชชีสย่างกับโค้กค่ะ', extra=fig('coast', 900))}
{place(fig('getty'), 'เก็ตตี้ เซ็นเตอร์', 'The Getty Center', ['บทที่ 14 · Ch 14'],
 ('การบ้านคือพิพิธภัณฑ์ อ่านป้ายทุกป้ายโดยไม่ใช้แอปแปล มะนาวอ่านไปสี่สิบเอ็ดป้าย เข้าใจครึ่งหนึ่ง สี่ปีก่อนเธออ่านเมนูยังไม่ได้',
  "The homework is a museum: read every label without a translation app. Lemon reads forty-one labels and understands about half. Four years ago she couldn't read a menu."),
 [('เข้าฟรี จ่ายแค่ค่าจอดรถ', 'Entry is free. You only pay for parking.'),
  ('รถรางไม่มีคนขับพาขึ้นเขา ใช้เวลาไม่กี่นาที', 'A driverless tram takes you up the hill in a few minutes.'),
  ('ภาพ Irises ของแวนโก๊ะอยู่ที่นี่', "Van Gogh's Irises hangs here.")],
 'Please do not touch the artwork.', 'กรุณาอย่าจับงานศิลปะ', extra=fig('gettyview', 900))}
{place(fig('griffith'), 'หอดูดาวกริฟฟิธ', 'Griffith Observatory', ['บทที่ 15 · Ch 15'],
 ('คาร์ลอสพามะนาวขึ้นเขาเหนือฮอลลีวูดตอนกลางคืน เธอส่องกล้องดูดาวเสาร์ แล้วพูดว่า มันเหมือนหมวก อาสาสมัครหัวเราะ มะนาวเล่นมุกภาษาอังกฤษได้โดยไม่ตั้งใจ',
  'Carlos takes Lemon up into the hills above Hollywood at night. She looks at Saturn through a telescope and says, "It is like a hat." The volunteer laughs. Lemon has made an English joke by accident.'),
 [('เข้าฟรี เปิดมาตั้งแต่ปี 1935', 'Free to enter, open since 1935.'),
  ('ส่องกล้องดูดาวฟรีทุกคืนที่ฟ้าใส ปิดวันจันทร์', 'Free telescope viewing on clear nights. Closed Mondays.'),
  ('มองเห็นป้าย HOLLYWOOD และไฟทั้งเมือง', 'You can see the Hollywood sign and the lights of the whole city.')],
 "I see it. I see the rings.", 'เห็นแล้ว เห็นวงแหวนแล้ว')}
{place(fig('catalina'), 'เกาะคาทาลินา', 'Catalina Island', ['บทที่ 15 · Ch 15'],
 ('สตีเว่นเมาเรือ มะนาวบอกให้ไปยืนท้ายเรือแล้วมองเส้นขอบฟ้า ได้ผล บนเกาะคนขับรถกอล์ฟแทนรถยนต์ มะนาวขับเหมือนขี่มอเตอร์ไซค์ในเมืองกระบี่ เบียร์กรี๊ดตลอดทาง',
  'Steven gets seasick. Lemon tells him to stand at the back and look at the horizon. It works. On the island people drive golf carts instead of cars. Lemon drives like she rides her motorbike in Krabi Town. Beer screams the whole way.'),
 [('เรือเร็วจากลองบีชไปเมืองอวาลอนใช้เวลาราวหนึ่งชั่วโมง', 'The fast ferry from Long Beach to Avalon takes about an hour.'),
  ('ในเมืองมีรถยนต์น้อยมาก คนใช้รถกอล์ฟ', 'There are very few cars in town. People use golf carts.'),
  ('บนเกาะมีควายไบซันที่อยู่กันเอง', 'Wild bison live on the island.')],
 'Look at the line where the sea meets the sky.', 'มองเส้นที่ทะเลกับฟ้ามาเจอกัน')}
<p class="note">แหล่งข้อมูล · Sources: <a href="https://krabinature.com/thara-park-in-krabi-town/" target="_blank" rel="noopener">Thara Park</a> · <a href="https://www.thaizer.com/krabis-twin-mountains-khao-khanap-nam/" target="_blank" rel="noopener">Khao Khanap Nam</a> · <a href="https://www.theplanetedit.com/tiger-cave-temple-krabi/" target="_blank" rel="noopener">Tiger Cave Temple</a> · <a href="https://en.wikipedia.org/wiki/Thai_Town,_Los_Angeles" target="_blank" rel="noopener">Thai Town</a> · <a href="https://www.getty.edu/visit/center/" target="_blank" rel="noopener">Getty Center</a> · <a href="https://griffithobservatory.lacity.gov/explore/daily-programs/" target="_blank" rel="noopener">Griffith Observatory</a> · <a href="https://www.visitlongbeach.com/blog/visit-catalina-island-from-long-beach/" target="_blank" rel="noopener">Catalina from Long Beach</a> · <a href="https://jazwanderlust.com/redondo-beach-pier/" target="_blank" rel="noopener">Redondo Beach Pier</a></p>
</div></section>

<section><div class="wrap">
{head('ดูกระบี่', 'Watch Krabi')}
<div class="videos">{video('HTwP6yO21Yc', '10 ที่เที่ยวในกระบี่', 'Ao Nang, four islands, Tiger Cave Temple, Krabi Town, Railay · World Wild Hearts')}
{video('PclWXHDAy28', 'แอโรบิกในสวน', 'Park aerobics, like Thara Park in the book · Thai PBS')}</div>
</div></section>
'''
page('places.html', 'สถานที่ในเรื่อง · Places in The Adventures of Lemon', 'กระบี่และลอสแอนเจลิส สถานที่จริงในนิยาย การผจญภัยของมะนาว · Krabi and Los Angeles: the real places in The Adventures of Lemon.', places)

# ---------------- culture ----------------
def card(th, en, body, say_en=None, say_th=None):
    s = say(say_en, say_th) if say_en else ''
    return f'<div class="card"><h3>{th}</h3><p class="en">{en}</p>{bi(*body)}{s}</div>'

culture = f'''
<div class="hero"><div class="wrap">
<div><p class="eyebrow">ภาคใต้และวัฒนธรรมไทย<span class="t-en">The South and Thai culture</span></p>
<h1>บ้านของมะนาว<span class="en">Where Lemon comes from</span></h1>
<p class="lead">หนังสือเล่มนี้ไม่ได้เล่าเมืองไทยแบบนักท่องเที่ยว มันเล่าจากในบ้าน จากอู่ซ่อมรถ จากไลน์กลุ่มครอบครัว และจากสวนตอนหกโมงเย็น</p>
<p class="lead en">This book doesn't show Thailand like a postcard. It tells it from inside the house, the workshop, the family LINE group, and the park at six in the evening.</p></div>
<img class="art" src="img/act4.jpg" alt="อ่าวนางตอนพระอาทิตย์ตก ภาพจากหนังสือ · Ao Nang at sunset, from the book" width="1400" height="747">
</div></div>

<section class="band"><div class="wrap">
{head('หมายเหตุเรื่องภูมิภาค', 'A note on the region')}
{bi('กระบี่อยู่บนชายฝั่งทะเลอันดามันของภาคใต้ ภูเขาหินปูน ป่าชายเลน และเกาะนับร้อย คนกระบี่มีทั้งชาวพุทธ ชาวมุสลิม และคนไทยเชื้อสายจีน อยู่ด้วยกันมาหลายร้อยปี ชุมชนมุสลิมส่วนใหญ่อยู่ในเมืองกระบี่และรอบๆ เมือง ส่วนร้านค้าที่อ่าวนางหลายร้านเป็นของคนจากอินเดียและประเทศอื่น',
 "Krabi is on the Andaman coast of the South: limestone mountains, mangroves and over a hundred islands. Buddhists, Muslims and Thai-Chinese have lived here together for centuries. Most of the Muslim community lives in and around Krabi Town, while many shops in Ao Nang are run by people from India and other countries.", 'intro')}
<div class="stats">
<div class="stat"><b>~65%</b><span>ชาวพุทธในจังหวัดกระบี่<span class="t-en">Buddhist (2000 census)</span></span></div>
<div class="stat"><b>~35%</b><span>ชาวมุสลิมในจังหวัดกระบี่<span class="t-en">Muslim (2000 census)</span></span></div>
<div class="stat"><b>100+</b><span>เกาะในจังหวัด<span class="t-en">islands in the province</span></span></div>
<div class="stat"><b>3</b><span>ภาษาของดา: ไทยกลาง ภาษาใต้ มลายู<span class="t-en">Da's languages: Central Thai, Southern Thai, Malay</span></span></div>
</div>
<p class="note" style="background:rgba(255,255,255,.06);border-color:rgba(255,255,255,.25);color:#CFE5E8">ตัวเลขศาสนามาจากสำมะโนประชากรปี 2000<span class="t-en" style="color:#CFE5E8">Religion figures: Thai census 2000, via <a style="color:#fff" href="https://en.wikipedia.org/wiki/Nationality,_religion,_and_language_data_for_the_provinces_of_Thailand" target="_blank" rel="noopener">Wikipedia</a>.</span></p>
</div></section>

<section id="festivals"><div class="wrap">
{head('เทศกาล', 'Festivals')}
<div class="place" style="border-top:0"><div class="media">{fig('krathong')}</div><div>
<h3>ลอยกระทง</h3><p class="en">Loy Krathong · บทที่ 21 · Ch 21</p>
{bi('คืนวันเพ็ญเดือนสิบสอง คนทั้งเมืองกระบี่ลงไปที่แม่น้ำ มะนาว แม่ ป้าเพ็ญ ฟ้า และดา ไปด้วยกัน ดาไม่ลอยกระทง แต่ไม่เคยพลาดโรตี มะนาวกับคาร์ลอสลอยกระทงหนึ่งใบให้แม่ของเขา',
 'On the night of the full moon of the twelfth month, the whole of Krabi Town goes down to the river. Lemon, her mother, Auntie Pen, Fah and Da go together. Da doesn\'t float a krathong, but she never misses the roti. Lemon and Carlos float one krathong together for his mother.')}
<ul class="facts">
{li(('กระทงทำจากหยวกกล้วย ใบตอง ดอกไม้ เทียนหนึ่งเล่ม และธูปสามดอก', 'A krathong is made from a slice of banana trunk, banana leaves, flowers, one candle and three incense sticks.'))}
{li(('เป็นการขอบคุณและขอขมาแม่น้ำ และปล่อยสิ่งไม่ดีของปีนี้ไป', 'It thanks the river, says sorry to it, and lets go of the bad things from this year.'))}
{li(('บางคนใส่เหรียญ เส้นผม หรือเล็บลงไปด้วย', 'Some people add a coin, a hair or a fingernail clipping.'))}
{li(('มักตรงกับเดือนพฤศจิกายน', 'It usually falls in November.'))}
</ul>
{say('Make a wish. In English or in Thai? Both.', 'อธิษฐานสิ ภาษาอังกฤษหรือภาษาไทย ทั้งสองภาษา')}
</div></div>
<div class="cards">
{card('สงกรานต์', 'Songkran · Thai New Year', ('ทุกเดือนเมษายน ที่ไทยทาวน์ในแอลเอก็มีงานสงกรานต์ ขบวนแห่ อาหารไทย และน้ำ คนไทยไกลบ้านหมื่นกิโลยังรดน้ำดำหัวกันอยู่', "Every April, Thai Town in L.A. has Songkran too: a parade, Thai food and water. Thai people ten thousand kilometres from home still pour water for their elders."), 'Happy Thai New Year!', 'สุขสันต์วันสงกรานต์')}
{card('ทำบุญที่วัด', 'Making merit at the temple', ('ตอนกลับบ้าน มะนาวไปวัดแก้วกับแม่ตอนหกโมงเช้า ทำบุญให้แม่ของคาร์ลอส แม่ไม่ถาม แต่แม่รู้', "Back home, Lemon goes to Wat Kaew with her mother at six in the morning and makes merit for Carlos's mother. Her mother doesn't ask, but she knows."), "I made merit for a friend's mother.", 'ทำบุญให้แม่ของเพื่อน')}
</div>
</div></section>

<section class="paper"><div class="wrap">
{head('คำไทยที่แปลไม่ได้', "Thai words English doesn't have")}
{bi('ในหนังสือ คาร์ลอสบอกว่าภาษาอังกฤษเป็นภาษาของ ตัวฉัน ส่วนภาษาไทยเป็นภาษาของ ช่องว่างระหว่างคน คำพวกนี้อยู่ในช่องว่างนั้น', 'In the book, Carlos says English is a language about "me", and Thai is a language about the space between people. These words live in that space.', 'intro')}
<div class="cards">
{card('เกรงใจ', 'Greng jai', ('ไม่อยากเป็นภาระ ไม่อยากทำให้ใครลำบากใจ มะนาวเกรงใจทุกคน จนลืมถามตัวเองว่าอยากได้อะไร', "Not wanting to be a burden or make anyone uncomfortable. Lemon is greng jai with everyone, until she forgets to ask herself what she wants."), "I don't want to trouble you.", 'ไม่อยากรบกวนค่ะ')}
{card('บุญคุณ', 'Bun khun · a debt of gratitude', ('หนี้ที่ใช้คืนด้วยเงินไม่ได้ โรเบิร์ตจ่ายหนี้ห้าหมื่นให้พ่อ และมะนาวก็พูดคำว่าไม่ไม่ได้อีกเลย', "A debt money can't repay. Robert paid Father's 50,000-baht debt, and Lemon could never say no again."), 'I will never forget what you did for my family.', 'จะไม่ลืมสิ่งที่คุณทำให้ครอบครัวเรา')}
{card('ลอตเตอรี่วันที่ 1 และ 16', 'The lottery, twice a month', ('พ่อส่งรูปลอตเตอรี่ในไลน์กลุ่มครอบครัวทุกงวด พร้อมคำว่า ลุ้น แปดสิบบาท แลกกับสองอาทิตย์ของความหวัง', 'Father posts his lottery ticket in the family LINE group every draw, with the word "ลุ้น". Eighty baht for two weeks of hope.'), 'Fingers crossed!', 'ลุ้น')}
{card('ไลน์กลุ่มครอบครัว', 'The family LINE group', ('แม่ส่งสติกเกอร์ดอกกุหลาบ สวัสดีวันจันทร์ ทุกเช้า หนองส่งแมวหัวเราะกลับไป', 'Mother sends a rose sticker saying "Happy Monday" every morning. Nong sends back a laughing cat.'), 'Happy Monday! Have a nice day.', 'สวัสดีวันจันทร์')}
{card('ศาลพระภูมิกับน้ำแดง', 'Spirit houses and red soda', ('ที่ไทยทาวน์ในแอลเอ มะนาวเจอศาลที่มีน้ำแดงวางไว้ เหมือนที่กระบี่ มีคนไกลบ้านหมื่นกิโลยังจำได้ว่าผีชอบน้ำแดง', 'In Thai Town, L.A., Lemon finds a spirit house with red soda, just like in Krabi. Someone ten thousand kilometres from home still remembers the spirits like red soda.'), 'Someone remembered the spirits like red soda.', 'มีคนจำได้ว่าผีชอบน้ำแดง')}
</div>
</div></section>

<section><div class="wrap">
{head('กลิ่นและรสของภาคใต้', 'The smells and tastes of the South')}
{bi('ในหนังสือ มะนาวได้ยินข้าวกะเพราก่อนได้กลิ่น เสียงตะหลิว เสียงพริกลงน้ำมันร้อน แล้วกลิ่นใบกะเพราก็ฉุนขึ้นจมูกจนคนรอคิวไอกันทั้งแถว', 'In the book, Lemon hears pad kaprao before she smells it: the spatula, the chilies hitting hot oil. Then the holy basil hits so hard the whole queue starts coughing.', 'intro')}
<div class="photo-row">{fig('street', 900)}{fig('durian', 900)}</div>
<div class="cards">
{card('ข้าวกะเพรา', 'Pad kaprao', ('จานละสี่สิบบาทจากรถเข็นปากซอย อาหารที่คนไทยกินบ่อยที่สุด และฝรั่งจามบ่อยที่สุด', 'Forty baht a plate from the cart at the end of the soi. The food Thai people eat most, and foreigners sneeze at most.'), 'It smells sharp and peppery.', 'กลิ่นฉุนและเผ็ด')}
{card('แกงส้ม', 'Gaeng som · sour curry', ('แม่ทำแกงส้มปลาคืนที่ครอบครัวรวมเงินส่งมะนาวไปอเมริกา', 'Mother made fish sour curry the night the family pooled their money to send Lemon to America.'), 'It tastes sour and spicy.', 'รสเปรี้ยวและเผ็ด')}
{card('ทุเรียน', 'Durian', ('วันที่มะนาวกลับบ้าน แม่ซื้อทุเรียนลูกสุดท้ายของฤดูไว้รอ หนามแหลมกดฝ่ามือ บอกเธอว่าถึงบ้านแล้ว', "The day Lemon comes home, Mother has bought the last durian of the season. The spikes press into her palms and tell her she's home."), 'The spikes are sharp in my hands.', 'หนามแหลมทิ่มมือ')}
{card('โรตี', 'Roti', ('แป้งทอดกรอบ ราดนมข้นกับน้ำตาล ร้านโรตีมุสลิมมีทุกตลาดในกระบี่ และเป็นของโปรดของดา', 'Crispy fried dough with condensed milk and sugar. Muslim roti stalls are in every Krabi market, and they are Da\'s favourite.'), 'One banana roti, please.', 'โรตีกล้วยหนึ่งที่ค่ะ')}
</div>
</div></section>

<section class="paper"><div class="wrap">
{head('ทะเล เรือ และแม่ย่านาง', 'The sea, the boats and Mae Ya Nang')}
<div class="photo-row">{fig('railay2', 900)}{fig('tonsai', 900)}</div>
{bi('เรือหางยาวที่กระบี่จมน้ำลึกเพราะบรรทุกหนัก หัวเรือผูกผ้าสามสีกับพวงมาลัยดาวเรือง ถวายแม่ย่านาง ผู้คุ้มครองเรือ เสียงเครื่องยนต์ของมันคือเสียงวัยเด็กของมะนาว ดังสนั่น แล้วค่อยๆ เงียบ เหลือแค่เสียงน้ำตีลำเรือ',
 "Krabi's longtails sit low in the water because they carry so much. Their bows are tied with three-coloured cloth and marigold garlands for Mae Ya Nang, the guardian of boats. Their engines are the sound of Lemon's childhood: a roar, then quiet, then only water slapping the hull.", 'intro')}
{say('The engine roared, then coughed, then stopped.', 'เครื่องยนต์ดังสนั่น แล้วไอ แล้วก็ดับ')}
</div></section>
'''
page('culture.html', 'ภาคใต้และวัฒนธรรมไทย · The South and Thai culture', 'กระบี่และภาคใต้ของไทยจากในบ้าน เทศกาล อาหาร และคำไทยที่แปลไม่ได้ · Southern Thailand from the inside: festivals, food and Thai words English doesn\'t have.', culture)

# ---------------- toolkit ----------------
TOOLS = [
 ('ถ้าคุณชอบร้องเพลง', 'If you love singing', [
  ('LyricsTraining', 'ดูมิวสิกวิดีโอแล้วเติมคำที่หายไป เริ่มจากระดับง่าย ฟรี', 'Watch a music video and fill in the missing words. Start at the easy level. Free.', 'https://lyricstraining.com', 'lyricstraining.com'),
  ('Musixmatch', 'เนื้อเพลงวิ่งตามเพลง บางเพลงมีคำแปล', 'Lyrics that move with the song. Some songs have translations.', 'https://www.musixmatch.com', 'musixmatch.com'),
  ('วิธีของคาร์ลอส · บทที่ 15', 'พิมพ์ค้นหา: ชื่อเพลง + lyrics + Thai and English ฟังก่อน รู้สึกก่อน แล้วค่อยอ่าน', 'Search: song name + lyrics + Thai and English. Listen first, feel first, then read.', None, None)]),
 ('ถ้าคุณชอบดูซีรีส์และคลิป', 'If you love shows and videos', [
  ('Language Reactor', 'ซับอังกฤษและไทยพร้อมกันบน YouTube และ Netflix', 'English and Thai subtitles together on YouTube and Netflix.', 'https://www.languagereactor.com', 'languagereactor.com'),
  ('YouGlish', 'ฟังคนจริงพูดคำเดียวกันในคลิปจริงหลายร้อยคลิป', 'Hear real people say the same word in hundreds of real videos.', 'https://youglish.com', 'youglish.com'),
  ('ELLLO', 'บทฟังสั้นๆ สำเนียงจากทั่วโลก มีบทถอดความ ฟรี', 'Short listening lessons with accents from around the world, with transcripts. Free.', 'https://www.elllo.org', 'elllo.org'),
  ('BBC Learning English', '6 Minute English ฟังบนรถเมล์ได้', '6 Minute English: you can listen on the bus.', 'https://www.bbc.co.uk/learningenglish', 'bbc.co.uk/learningenglish'),
  ('VOA Learning English', 'ข่าวอ่านช้า ใช้คำง่าย', 'News read slowly, with easy words.', 'https://learningenglish.voanews.com', 'learningenglish.voanews.com')]),
 ('พจนานุกรม', 'Dictionaries · บทที่ 3: เครื่องแปลไม่ใช่พจนานุกรม', [
  ('Cambridge Dictionary', 'มีภาษาอังกฤษ–ไทย สัญลักษณ์เสียง และปุ่มฟังเสียง', 'English–Thai, with sound symbols and a button to hear the word.', 'https://dictionary.cambridge.org', 'dictionary.cambridge.org'),
  ('Oxford Learner\'s Dictionaries', 'เสียงอังกฤษและอเมริกัน พร้อมประโยคตัวอย่าง', 'British and American pronunciation, with example sentences.', 'https://www.oxfordlearnersdictionaries.com', 'oxfordlearnersdictionaries.com'),
  ('Longdo Dict', 'พจนานุกรมไทย–อังกฤษ ค้นจากภาษาไทยได้', 'A Thai–English dictionary. You can search in Thai.', 'https://dict.longdo.com', 'dict.longdo.com')]),
 ('คุยกับคนจริง', 'Talk to real people', [
  ('HelloTalk', 'คุณช่วยเขาเรียนไทย เขาช่วยคุณเรียนอังกฤษ พิมพ์ก็ได้', 'You help them learn Thai, they help you learn English. Typing is fine.', 'https://www.hellotalk.com', 'hellotalk.com'),
  ('Tandem', 'หาคู่ฝึกตามความสนใจ', 'Find a practice partner with the same interests.', 'https://www.tandem.net', 'tandem.net'),
  ('italki', 'เรียนกับครูออนไลน์เมื่อพร้อม เลือกครูที่พูดไทยได้', 'Learn with an online teacher when you are ready. Choose one who speaks Thai.', 'https://www.italki.com', 'italki.com')]),
 ('อ่าน', 'Read', [
  ('British Council LearnEnglish', 'บทเรียนแยกตามระดับ วิดีโอ และเกม', 'Lessons by level, with videos and games.', 'https://learnenglish.britishcouncil.org', 'learnenglish.britishcouncil.org'),
  ('Breaking News English', 'ข่าวเดียวกัน เจ็ดระดับ', 'The same news story at seven levels.', 'https://breakingnewsenglish.com', 'breakingnewsenglish.com'),
  ('English e-Reader', 'หนังสืออ่านง่ายแบ่งระดับ', 'Easy books, sorted by level.', 'https://english-e-reader.net', 'english-e-reader.net')]),
]
shelves = ''
for th, en, items in TOOLS:
    cards = ''.join(f'<article class="tool"><h4>{n}</h4><p>{t}</p><p class="en">{e}</p>' + (f'<a class="go" href="{u}" target="_blank" rel="noopener">{l} →</a>' if u else '') + '</article>' for n, t, e, u, l in items)
    shelves += f'<h3 class="shelf">{th}<span class="t-en">{en}</span></h3><div class="tools">{cards}</div>'

toolkit = f'''
<div class="hero"><div class="wrap">
<div><p class="eyebrow">เครื่องมือของคาร์ลอส · บทที่ 14<span class="t-en">Carlos's toolkit · Chapter 14</span></p>
<h1>ห้องเรียนหนึ่งชั่วโมง ชีวิตที่เหลือคือบทเรียน<span class="en">Class is one hour. Life is the rest.</span></h1>
<p class="lead">ไม่ต้องเพิ่มการบ้าน เปลี่ยนสิ่งที่คุณทำอยู่แล้วทุกวัน ฟังเพลง ดูซีรีส์ เล่นโทรศัพท์ ให้เป็นการเรียน เลือกทีละอย่าง สัปดาห์ละหนึ่งเครื่องมือ</p>
<p class="lead en">You don't need more homework. Turn what you already do every day, music, shows, your phone, into learning. Pick one thing at a time: one tool per week.</p></div>
<img class="art" src="img/act1.jpg" alt="อ่าวนาง ภาพจากหนังสือ" width="1400" height="747">
</div></div>
<section><div class="wrap">{shelves}</div></section>
<section class="paper"><div class="wrap">
<h2>สามสิบวันแรก วันละสิบห้านาที</h2><p class="en">Your first 30 days, 15 minutes a day</p>
<p class="intro">พลาดหนึ่งวัน ไม่ต้องเริ่มใหม่ ทำวันถัดไปต่อเลย ไม่มีตัวเลขไหนกลายเป็นศูนย์<span class="t-en">Miss a day? Don't start again. Just carry on the next day. No number goes back to zero.</span></p>
<div class="plan">
<div><b>สัปดาห์ 1 · เสียง · Sounds</b><p>เสียงตัวอักษรและ e วิเศษ พูดตามทุกคำ อัดเสียงตัวเองวันแรก<span class="t-en">Letter sounds and magic e. Repeat every word. Record yourself on day one.</span></p></div>
<div><b>สัปดาห์ 2 · เพลง · Songs</b><p>LyricsTraining วันละหนึ่งเพลง ระดับง่าย<span class="t-en">One song a day on LyricsTraining, easy level.</span></p></div>
<div><b>สัปดาห์ 3 · ซีรีส์ · Shows</b><p>ซับสองภาษา หยุดวันละห้าประโยค พูดตาม<span class="t-en">Two-language subtitles. Pause on five sentences a day and say them.</span></p></div>
<div><b>สัปดาห์ 4 · คน · People</b><p>คุยหรือพิมพ์กับคนจริงวันละสิบนาที<span class="t-en">Talk or type with a real person for ten minutes a day.</span></p></div>
<div><b>วันที่ 30 · ฟังย้อน · Listen back</b><p>อัดเสียงเรื่องเดิม ฟังสองเสียงต่อกัน<span class="t-en">Record the same story again. Listen to both, one after the other.</span></p></div>
</div>
</div></section>
<section><div class="wrap">
<h2>อ่านพจนานุกรมให้เป็น สิบสัญลักษณ์เสียงที่ควรรู้</h2><p class="en">Read a dictionary: ten sound symbols worth knowing</p>
<div class="tablewrap"><table><thead><tr><th>สัญลักษณ์ · Symbol</th><th>เสียงใกล้เคียง · Sounds like</th><th>ตัวอย่าง · Example</th></tr></thead><tbody>
<tr><td>ˈ</td><td>เน้นพยางค์ถัดไป · stress the next syllable</td><td>/ˈlemən/ lemon</td></tr>
<tr><td>ə</td><td>เออะ เบาๆ · soft uh</td><td>about, banana</td></tr>
<tr><td>æ</td><td>แอ</td><td>cat, bad</td></tr>
<tr><td>ʌ</td><td>อะ</td><td>cup, love</td></tr>
<tr><td>ɪ</td><td>อิ</td><td>sit, kitchen</td></tr>
<tr><td>iː</td><td>อี ยาว</td><td>see, feel</td></tr>
<tr><td>θ</td><td>th เบา</td><td>think</td></tr>
<tr><td>ð</td><td>th ก้อง</td><td>this</td></tr>
<tr><td>ʃ</td><td>ช กระซิบ · sh</td><td>she</td></tr>
<tr><td>ŋ</td><td>ง</td><td>sing</td></tr>
</tbody></table></div>
<p class="note">เร็วๆ นี้: เสียงอ่านภาษาอังกฤษทุกบท ปริศนาพิมพ์ได้ และเพลย์ลิสต์ของมะนาว<span class="t-en">Coming soon: chapter audio, printable puzzles and Lemon's playlist.</span></p>
</div></section>
'''
page('toolkit.html', 'เครื่องมือของคาร์ลอส · Carlos\'s Toolkit', 'เครื่องมือเรียนภาษาอังกฤษฟรีจากนิยาย การผจญภัยของมะนาว เพลง ซีรีส์ พจนานุกรม และแผนสามสิบวัน', toolkit)
print('built')
