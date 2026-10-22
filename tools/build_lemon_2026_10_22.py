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

NAV = [('index.html', 'หน้าแรก'), ('places.html', 'สถานที่ในเรื่อง'), ('culture.html', 'ภาคใต้และวัฒนธรรม'), ('toolkit.html', 'เครื่องมือของคาร์ลอส')]

def page(fname, title, desc, body, og='../assets/lemon-cover.jpg'):
    nav = ''.join(f'<a href="{h}"{" aria-current=page" if h == fname else ""}>{t}</a>' for h, t in NAV)
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

# ---------------- index ----------------
index = f'''
<div class="hero"><div class="wrap">
<div>
<p class="eyebrow">นิยายสองภาษา · ไทย–อังกฤษ · เล่มหนึ่งกำลังจะออก</p>
<h1>การผจญภัยของมะนาว<span class="en">The Adventures of Lemon</span></h1>
<p class="lead">มะนาวเป็นแม่บ้านโรงแรมที่อ่าวนาง พูดภาษาอังกฤษได้แค่ประโยคบนกระดาษของป้าเพ็ญ แล้ววันหนึ่งแขกห้อง 412 ก็ถามคำถามที่ไม่อยู่ในกระดาษ</p>
<p class="lead en">Lemon is a hotel housekeeper in Ao Nang who can only speak the English on Auntie Pen's card. Then the guest in Room 412 asks a question that isn't on it.</p>
<div class="actions"><a class="btn" href="#watch">▶ ดูก่อน อ่านทีหลัง</a><a class="btn ghost" href="places.html">ไปเที่ยวกระบี่กับมะนาว</a></div>
</div>
<img class="cover" src="../assets/lemon-cover.jpg" alt="ปกหนังสือ การผจญภัยของมะนาว · Cover of The Adventures of Lemon" width="600" height="900">
</div></div>

<section id="watch"><div class="wrap">
<h2>ดูก่อน อ่านทีหลัง</h2><p class="en">Watch first, read later</p>
<p class="intro">ไม่ชอบอ่านยาวๆ ไม่เป็นไร เริ่มจากดูที่ที่มะนาวอยู่ก่อน แล้วค่อยเปิดหนังสือ</p>
<div class="videos">
{video('HTwP6yO21Yc', 'กระบี่ อ่าวนาง ไร่เลย์ ใน 10 นาที', 'Krabi, Ao Nang and Railay · World Wild Hearts · ภาษาอังกฤษ')}
{video('PclWXHDAy28', 'แอโรบิกในสวน ความสุขทะลัก', 'Free park aerobics, like Thara Park in Chapter 2 · Thai PBS · ภาษาไทย')}
{video('2H6P4pRuCLU', 'สงกรานต์ที่ไทยทาวน์ ลอสแอนเจลิส', 'Songkran in Thai Town, Los Angeles · ภาษาอังกฤษ')}
</div>
</div></section>

<section class="paper"><div class="wrap">
<h2>สำรวจโลกของมะนาว</h2><p class="en">Explore Lemon's world</p>
<div class="tiles">
<a class="tile" href="places.html"><img src="{un(PH['aonang'][0], 700)}" alt="เรือหางยาวที่กระบี่" loading="lazy"><div><h3>สถานที่ในเรื่อง</h3><p>เมืองกระบี่ อ่าวนาง ไร่เลย์ และไทยทาวน์ในแอลเอ · Places in the book</p></div></a>
<a class="tile" href="culture.html"><img src="{un(PH['street'][0], 700)}" alt="แผงอาหารริมทาง" loading="lazy"><div><h3>ภาคใต้และวัฒนธรรม</h3><p>อาหาร คำไทยที่แปลไม่ได้ และชีวิตริมทะเลอันดามัน · The South and Thai culture</p></div></a>
<a class="tile" href="toolkit.html"><img src="img/act1.jpg" alt="ภาพจากหนังสือ อ่าวนาง" loading="lazy"><div><h3>เครื่องมือของคาร์ลอส</h3><p>เรียนภาษาอังกฤษจากเพลง ซีรีส์ และโทรศัพท์ · Carlos's toolkit</p></div></a>
</div>
</div></section>

<section><div class="wrap">
<h2>ตัวละคร</h2><p class="en">Who's who</p>
<div class="people">
<div class="person"><b>มะนาว</b><span>Lemon, 26</span><p>แม่บ้านโรงแรมที่อ่าวนาง ลูกสาวช่างซ่อมมอเตอร์ไซค์ เก่งทุกอย่าง ยกเว้นการถูกมองเห็น</p></div>
<div class="person"><b>คาร์ลอส</b><span>Carlos</span><p>แขกห้อง 412 จากแอลเอ แม่เป็นคนอุบล พ่อเป็นคนบราซิล พูดไทยสำเนียงเพี้ยนๆ</p></div>
<div class="person"><b>โรเบิร์ต</b><span>Robert</span><p>แฟนของมะนาว ลูกชายเจ้าของร้านอาหารบนหน้าผา ผู้ชายที่พูดแทนเธอ</p></div>
<div class="person"><b>ดา</b><span>Da</span><p>เพื่อนแม่บ้าน คนกระบี่ มุสลิม พูดได้สามภาษา ซ้อนมอเตอร์ไซค์ไปทำงานกับมะนาวทุกเช้า</p></div>
<div class="person"><b>ป้าเพ็ญ</b><span>Auntie Pen</span><p>หัวหน้าแม่บ้าน ข่าวของป้าเร็วกว่าไวไฟ</p></div>
<div class="person"><b>เบียร์</b><span>Beer</span><p>เพื่อนสนิทตั้งแต่อนุบาล อยู่แคลิฟอร์เนีย คนที่สอนเสียงตัวอักษรให้มะนาวใต้ต้นมะม่วง</p></div>
</div>
<p class="note">ภาพตัวละครกำลังวาด จะมาเร็วๆ นี้ · Character illustrations are on the way.</p>
</div></section>

<section class="paper"><div class="wrap">
<h2>ทำไมหนังสือเล่มนี้ต่าง</h2><p class="en">Why this book is different</p>
<div class="cards">
<div class="card"><h3>เริ่มจากที่คุณรู้</h3><p class="en">Begin from what you know</p><p>บทแรกเป็นภาษาไทยเกือบทั้งหมด ภาษาอังกฤษเพิ่มขึ้นทีละนิดตามที่มะนาวเก่งขึ้น</p></div>
<div class="card"><h3>เป็นละคร ไม่ใช่ตำรา</h3><p class="en">A drama, not a textbook</p><p>มีคู่แข่ง มีแม่ผัวในอนาคต มีสงครามผ้าเช็ดตัว และสงครามส้มตำที่ทำให้โดนห้ามเข้าร้าน</p></div>
<div class="card"><h3>ชีวิตจริงของคนไทย</h3><p class="en">Real Thai life</p><p>หนี้นอกระบบ ซองเงินเดือนห้าซอง แอปที่เลิกใช้ และความกลัวพูดผิดที่คนไทยหลายคนรู้จัก</p></div>
</div>
</div></section>

<section><div class="wrap">
<h2>ซีรีส์มะนาว</h2><p class="en">The Lemon series</p>
<p class="intro">เล่มหลักเล่าเรื่องทั้งหมด เล่มต่อไปเริ่มจากคำที่คุณได้ยินในงานของคุณ</p>
<ul class="series"><li class="now">มะนาวเรียนรู้ · Lemon Learns</li><li>มะนาวเดินทาง · Travels</li><li>มะนาวกินข้าวนอกบ้าน · Dines</li><li>มะนาวช้อปปิ้ง · Shops</li><li>มะนาวไปหาหมอ · Heals</li><li>มะนาวทำงาน · Works</li></ul>
<div class="actions"><a class="btn" href="../#newsletter">รับข่าวเมื่อหนังสือออก</a><a class="btn ghost" style="color:var(--teal);border-color:var(--teal)" href="../">หนังสือเล่มอื่นของผู้เขียน · Other books</a></div>
</div></section>
'''
page('index.html', 'การผจญภัยของมะนาว · The Adventures of Lemon', 'นิยายสองภาษาไทย–อังกฤษ สำหรับคนไทยที่อยากพูดภาษาอังกฤษ พร้อมสถานที่ในเรื่อง วัฒนธรรมภาคใต้ และเครื่องมือเรียนฟรี', index)

# ---------------- places ----------------
def place(media, th, en, chips, body, facts, say_en, say_th, extra=''):
    ch = ''.join(f'<span class="chip">{c}</span>' for c in chips)
    fl = ''.join(f'<li>{f}</li>' for f in facts)
    return f'''<article class="place"><div class="media">{media}{extra}</div><div>
<h3>{th}</h3><p class="en">{en}</p>{ch}<p>{body}</p><ul class="facts">{fl}</ul>
<div class="say"><b>พูดเป็นภาษาอังกฤษ · Say it in English</b><span>{say_en}</span><br>{say_th}</div></div></article>'''

places = f'''
<div class="hero"><div class="wrap">
<div><p class="eyebrow">สถานที่ในเรื่อง · Places in the book</p>
<h1>ไปเที่ยวกับมะนาว<span class="en">Travel with Lemon</span></h1>
<p class="lead">ทุกที่ในหนังสือเป็นที่จริง ยกเว้นโรงแรมกับร้านอาหาร ดูภาพ ดูคลิป แล้วลองพูดประโยคภาษาอังกฤษของแต่ละที่</p>
<p class="lead en">Every place in the book is real except the hotel and the restaurants. Look, watch, then try each place's English sentence.</p></div>
<img class="art" src="img/act0.jpg" alt="บ้านและอู่ของพ่อมะนาว ภาพจากหนังสือ" width="1400" height="747">
</div></div>
<section><div class="wrap">
{place(bookfig('act0.jpg', 'บ้านกับอู่ของพ่อ ใต้ต้นมะม่วง · Father\'s workshop'),
 'เมืองกระบี่', 'Krabi Town · บ้านของมะนาว', ['บทที่ 1–3', 'บทที่ 20'],
 'บ้านไม้สองชั้นกับอู่ซ่อมรถของพ่ออยู่ในซอยเล็กๆ ในเมืองกระบี่ ไม่ใช่ที่อ่าวนาง ที่นี่คือที่ที่คนกระบี่ใช้ชีวิตจริง ตลาดเช้า วัด มัสยิด และแม่น้ำกระบี่',
 ['ชื่อ กระบี่ แปลว่า ดาบ และดาบไขว้คือสัญลักษณ์ของจังหวัด',
  'เขาขนาบน้ำ ภูเขาหินปูนสองลูกสูงราว 100 เมตร ยืนประกบแม่น้ำกระบี่ เป็นภาพจำของเมือง',
  'นั่งเรือหางยาวจากท่าเรือเจ้าฟ้า ใกล้รูปปั้นปูดำตัวใหญ่ ไปเขาขนาบน้ำใช้เวลาราว 15 นาที ข้างใต้มีถ้ำที่พบร่องรอยคนโบราณ'],
 'I live in Krabi Town, not in Ao Nang.', 'ฉันอยู่ในเมืองกระบี่ ไม่ได้อยู่อ่าวนาง')}
{place(fig('market'), 'สวนธารา และถนนคนเดิน', 'Thara Park and Walking Street', ['บทที่ 2', 'บทที่ 3', 'บทที่ 21'],
 'ทุกเย็น มะนาว แม่ ป้าเพ็ญ และดา มาเต้นแอโรบิกที่ลานริมแม่น้ำในสวนธารา ครูนับเป็นภาษาอังกฤษ Left! Right! Turn around! และนี่คือที่ที่ป้าเพ็ญบอกว่าใส่ชุดดำแปลว่าโสด',
 ['สวนธาราเป็นสวนสาธารณะฟรีริมแม่น้ำกระบี่ มีลู่วิ่งราว 1.15 กิโลเมตร และเครื่องออกกำลังกายกลางแจ้งให้ใช้ฟรี',
  'คนมาเดิน วิ่ง เล่นฟุตบอล ตั้งแต่ห้าโมงเย็น',
  'ถนนคนเดินกระบี่เปิดวันศุกร์ เสาร์ อาทิตย์ ห้าโมงเย็นถึงสี่ทุ่ม ที่ซอยมหาราช 8 มีลานอาหารและดนตรีสด'],
 'Left! Right! Turn around! Again!', 'ซ้าย ขวา หมุนตัว อีกครั้ง',
 extra='<p class="note" style="margin-top:12px">ภาพนี้เป็นตลาดกลางคืนในไทย ไม่ใช่ถนนคนเดินกระบี่โดยตรง · Photo shows a Thai night market, not Krabi\'s Walking Street itself.</p>')}
{place(fig('monkey'), 'วัดถ้ำเสือ', 'Tiger Cave Temple · Wat Tham Suea', ['ใกล้บ้านมะนาว'],
 'วัดบนภูเขาที่คนกระบี่ไปทำบุญ และนักท่องเที่ยวไปปีนบันได ถ้าคุณอยากรู้ว่ามะนาวรู้สึกยังไงตอนเรียนภาษาอังกฤษ ลองปีนดู ทีละขั้น',
 ['อยู่ห่างจากเมืองกระบี่ราว 15 นาที', 'บันไดขึ้นยอดราว 1,260 ขั้น ข้างบนมีพระพุทธรูปและวิวรอบทิศ', 'ระวังลิง มันชอบขโมยของ'],
 'One step at a time.', 'ทีละขั้น')}
{place(fig('aonang'), 'อ่าวนาง', 'Ao Nang · ที่ทำงานของมะนาว', ['บทที่ 2–10', 'บทที่ 21'],
 'โรงแรมอันดามันซีบรีซในเรื่องเป็นโรงแรมสมมุติ แต่ชายหาด ร้านตัดสูทของคุณราช และแถวเรือหางยาวเป็นของจริง ทุกเช้ามะนาวกับดาขี่มอเตอร์ไซค์จากเมืองมาที่นี่ ยี่สิบกิโลเมตร',
 ['ร้านค้าหลายร้านที่อ่าวนางเป็นของคนจากอินเดีย เนปาล และอีกหลายประเทศ ภาษาอังกฤษจึงเป็นภาษากลาง',
  'เรือหางยาวผูกผ้าสามสีกับพวงมาลัยที่หัวเรือ ถวายแม่ย่านาง ผู้คุ้มครองเรือ',
  'เรือจากอ่าวนางไปไร่เลย์ไม่กี่นาที'],
 'Housekeeping! Would you like me to clean your room now?', 'แม่บ้านค่ะ ทำห้องตอนนี้ไหมคะ')}
{place(fig('railay'), 'ไร่เลย์', 'Railay', ['บทที่ 9'],
 'ลุงแดงพามะนาวกับคาร์ลอสนั่งเรือหางยาวไปไร่เลย์ แล้วคลื่นก็สาดหน้าคาร์ลอส ลุงแดงหัวเราะ แม่ย่านางทักทาย',
 ['ไร่เลย์ถูกภูเขาหินปูนล้อมจนไปได้ทางเรือเท่านั้น', 'เป็นที่ปีนผาที่มีชื่อเสียงระดับโลก'],
 'Railay! One hundred baht! Go, go!', 'ไร่เลย์ ร้อยบาท ไปๆ', extra=fig('railay2', 900))}
{place(fig('tonsai'), 'ทะเลอันดามันและหมู่เกาะ', 'The Andaman Sea and the islands', ['บทที่ 3', 'บทที่ 21'],
 'โรเบิร์ตพามะนาวนั่งเรือไปเกาะปอดะตอนพระอาทิตย์ตก และในตอนจบ ลุงแดงเสนอพามะนาวกับคาร์ลอสไปเกาะห้อง ราคาพิเศษ',
 ['กระบี่มีเกาะมากกว่าร้อยเกาะ', 'ทัวร์สี่เกาะจากอ่าวนางเป็นทัวร์ยอดนิยม'],
 'Tomorrow, Hong Island. Special price!', 'พรุ่งนี้ ไปเกาะห้อง ราคาพิเศษ')}
{place(bookfig('act2.jpg', 'ลอสแอนเจลิส · Los Angeles'), 'ไทยทาวน์ ลอสแอนเจลิส', 'Thai Town, Los Angeles', ['บทที่ 12', 'บทที่ 16'],
 'วันแรกในอเมริกา คาร์ลอสพามะนาวไปกินส้มตำที่ร้านอีสานเล็กๆ ในไทยทาวน์ ป้าฟันทองพูดอีสานเร็วจนคาร์ลอสฟังไม่ทัน และมะนาวต้องแปลภาษาแม่ของเขาให้เขาฟัง',
 ['สภาเมืองลอสแอนเจลิสประกาศให้ย่านนี้เป็น ไทยทาวน์ เมื่อ 27 ตุลาคม 1999 เป็นที่แรกในอเมริกาที่ได้ชื่อนี้',
  'อยู่บนถนนฮอลลีวูดระหว่างถนนนอร์มังดีกับเวสเทิร์น ทางเข้ามีรูปปั้นอัปสรสีห์',
  'ทุกเดือนเมษายนมีงานสงกรานต์ ขบวนแห่ และอาหารไทยเต็มถนน'],
 'Medium spicy, please.', 'เผ็ดกลางค่ะ', extra=f'<div style="margin-top:14px">{video("2H6P4pRuCLU", "อาหารในงานสงกรานต์ ไทยทาวน์", "Songkran food in Thai Town, 2026")}</div>')}
</div></section>
<section class="paper"><div class="wrap">
<h2>ดูกระบี่</h2><p class="en">Watch Krabi</p>
<div class="videos">{video('HTwP6yO21Yc', '10 ที่เที่ยวในกระบี่', 'Ao Nang, the four-island tour, Tiger Cave Temple, Krabi Town, Railay · World Wild Hearts')}
{video('PclWXHDAy28', 'แอโรบิกในสวน', 'Park aerobics in Bangkok, like Thara Park in the book · Thai PBS')}</div>
<p class="note">แหล่งข้อมูล · Sources: <a href="https://krabinature.com/thara-park-in-krabi-town/" target="_blank" rel="noopener">Thara Park, Krabi Nature</a> · <a href="https://nashaplaneta.net/asia/thai/krabi-town-dostoprimechatelnosti-walking-street_en" target="_blank" rel="noopener">Krabi Walking Street</a> · <a href="https://www.thaizer.com/krabis-twin-mountains-khao-khanap-nam/" target="_blank" rel="noopener">Khao Khanap Nam, Thaizer</a> · <a href="https://www.theplanetedit.com/tiger-cave-temple-krabi/" target="_blank" rel="noopener">Tiger Cave Temple, The Planet Edit</a> · <a href="https://en.wikipedia.org/wiki/Thai_Town,_Los_Angeles" target="_blank" rel="noopener">Thai Town, Wikipedia</a></p>
</div></section>
'''
page('places.html', 'สถานที่ในเรื่อง · Places in The Adventures of Lemon', 'เมืองกระบี่ สวนธารา อ่าวนาง ไร่เลย์ และไทยทาวน์ในลอสแอนเจลิส สถานที่จริงในนิยาย การผจญภัยของมะนาว', places)

# ---------------- culture ----------------
def card(th, en, body, say_en=None, say_th=None):
    s = f'<div class="say"><b>พูดเป็นภาษาอังกฤษ · Say it in English</b><span>{say_en}</span><br>{say_th}</div>' if say_en else ''
    return f'<div class="card"><h3>{th}</h3><p class="en">{en}</p><p>{body}</p>{s}</div>'

culture = f'''
<div class="hero"><div class="wrap">
<div><p class="eyebrow">ภาคใต้และวัฒนธรรมไทย · The South and Thai culture</p>
<h1>บ้านของมะนาว<span class="en">Where Lemon comes from</span></h1>
<p class="lead">หนังสือเล่มนี้ไม่ได้เล่าเมืองไทยแบบนักท่องเที่ยว มันเล่าจากในบ้าน จากอู่ซ่อมรถ จากไลน์กลุ่มครอบครัว และจากสวนตอนหกโมงเย็น</p>
<p class="lead en">This book doesn't show Thailand like a postcard. It tells it from inside the house, the workshop, the family LINE group, and the park at six in the evening.</p></div>
<img class="art" src="img/act4.jpg" alt="อ่าวนางตอนพระอาทิตย์ตก ภาพจากหนังสือ" width="1400" height="747">
</div></div>

<section class="band"><div class="wrap">
<h2>หมายเหตุเรื่องภูมิภาค</h2><p class="en">A note on the region</p>
<p class="intro">กระบี่อยู่บนชายฝั่งทะเลอันดามันของภาคใต้ ภูเขาหินปูน ป่าชายเลน และเกาะนับร้อย คนกระบี่มีทั้งชาวพุทธ ชาวมุสลิม และคนไทยเชื้อสายจีน อยู่ด้วยกันมาหลายร้อยปี วัดกับมัสยิดอยู่ห่างกันไม่กี่ซอย ชุมชนมุสลิมส่วนใหญ่อยู่ในเมืองกระบี่และรอบๆ เมือง ส่วนร้านค้าที่อ่าวนางหลายร้านเป็นของคนจากอินเดียและประเทศอื่น</p>
<div class="stats">
<div class="stat"><b>~65%</b><span>ชาวพุทธในจังหวัดกระบี่ · Buddhist (2000 census)</span></div>
<div class="stat"><b>~35%</b><span>ชาวมุสลิมในจังหวัดกระบี่ · Muslim (2000 census)</span></div>
<div class="stat"><b>100+</b><span>เกาะในจังหวัด · islands</span></div>
<div class="stat"><b>3</b><span>ภาษาของดา: ไทยกลาง ภาษาใต้ มลายู · Da's languages</span></div>
</div>
<p class="note" style="background:rgba(255,255,255,.06);border-color:rgba(255,255,255,.25);color:#CFE5E8">ตัวเลขศาสนามาจากสำมะโนประชากรปี 2000 · Religion figures: Thai census 2000, via <a style="color:#fff" href="https://en.wikipedia.org/wiki/Nationality,_religion,_and_language_data_for_the_provinces_of_Thailand" target="_blank" rel="noopener">Wikipedia</a>.</p>
</div></section>

<section><div class="wrap">
<h2>คำไทยที่แปลไม่ได้</h2><p class="en">Thai words English doesn't have</p>
<p class="intro">ในหนังสือ คาร์ลอสบอกว่าภาษาอังกฤษเป็นภาษาของ ตัวฉัน ส่วนภาษาไทยเป็นภาษาของ ช่องว่างระหว่างคน คำพวกนี้อยู่ในช่องว่างนั้น</p>
<div class="cards">
{card('เกรงใจ', 'Greng jai', 'ไม่อยากเป็นภาระ ไม่อยากทำให้ใครลำบากใจ มะนาวเกรงใจทุกคน จนลืมถามตัวเองว่าอยากได้อะไร', "I don't want to trouble you.", 'ไม่อยากรบกวนค่ะ')}
{card('บุญคุณ', 'Bun khun · a debt of gratitude', 'หนี้ที่ใช้คืนด้วยเงินไม่ได้ โรเบิร์ตจ่ายหนี้ห้าหมื่นให้พ่อ และมะนาวก็พูดคำว่าไม่ไม่ได้อีกเลย', 'I will never forget what you did for my family.', 'จะไม่ลืมสิ่งที่คุณทำให้ครอบครัวเรา')}
{card('ทำบุญ', 'Making merit', 'ตอนกลับบ้าน มะนาวไปวัดกับแม่ตอนหกโมงเช้า ทำบุญให้แม่ของคาร์ลอส แม่ไม่ถาม แต่แม่รู้', 'I made merit for a friend\'s mother.', 'ทำบุญให้แม่ของเพื่อน')}
{card('ลอตเตอรี่วันที่ 1 และ 16', 'The lottery, twice a month', 'พ่อส่งรูปลอตเตอรี่ในไลน์กลุ่มครอบครัวทุกงวด พร้อมคำว่า ลุ้น แปดสิบบาท แลกกับสองอาทิตย์ของความหวัง', 'Fingers crossed!', 'ลุ้น')}
{card('ไลน์กลุ่มครอบครัว', 'The family LINE group', 'แม่ส่งสติกเกอร์ดอกกุหลาบ สวัสดีวันจันทร์ ทุกเช้า หนองส่งแมวหัวเราะกลับไป ใครมีกลุ่มแบบนี้ ยกมือขึ้น', 'Happy Monday! Have a nice day.', 'สวัสดีวันจันทร์')}
{card('ศาลพระภูมิกับน้ำแดง', 'Spirit houses and red soda', 'ที่ไทยทาวน์ในแอลเอ มะนาวเจอศาลที่มีน้ำแดงวางไว้ เหมือนที่กระบี่ มีคนไกลบ้านหมื่นกิโลยังจำได้ว่าผีชอบน้ำแดง', 'Someone remembered the spirits like red soda.', 'มีคนจำได้ว่าผีชอบน้ำแดง')}
</div>
</div></section>

<section class="paper"><div class="wrap">
<h2>กลิ่นและรสของภาคใต้</h2><p class="en">The smells and tastes of the South</p>
<p class="intro">ในหนังสือ มะนาวได้ยินข้าวกะเพราก่อนได้กลิ่น เสียงตะหลิว เสียงพริกลงน้ำมันร้อน แล้วกลิ่นใบกะเพราก็ฉุนขึ้นจมูกจนคนรอคิวไอกันทั้งแถว</p>
<div class="photo-row">{fig('street', 900)}{fig('durian', 900)}</div>
<div class="cards">
{card('ข้าวกะเพรา', 'Pad kaprao', 'จานละสี่สิบบาทจากรถเข็นปากซอย อาหารที่คนไทยกินบ่อยที่สุด และฝรั่งจามบ่อยที่สุด', 'It smells sharp and peppery.', 'กลิ่นฉุนและเผ็ด')}
{card('แกงส้ม', 'Gaeng som · sour curry', 'แม่ทำแกงส้มปลาคืนที่ครอบครัวรวมเงินส่งมะนาวไปอเมริกา เปรี้ยวจนน้ำตาไหลก่อนจะได้ชิม', 'It tastes sour and spicy.', 'รสเปรี้ยวและเผ็ด')}
{card('ทุเรียน', 'Durian', 'วันที่มะนาวกลับบ้าน แม่ซื้อทุเรียนลูกสุดท้ายของฤดูไว้รอ หนามแหลมกดฝ่ามือ บอกเธอว่าถึงบ้านแล้ว', 'The spikes are sharp in my hands.', 'หนามแหลมทิ่มมือ')}
{card('มะม่วงจิ้มพริกเกลือ', 'Green mango with chili salt', 'ของกินใต้ต้นมะม่วง ตอนเบียร์สอนเสียงตัวอักษร เปรี้ยวจนหน้าเบ้', 'It is so sour!', 'เปรี้ยวมาก')}
</div>
</div></section>

<section><div class="wrap">
<h2>ทะเล เรือ และแม่ย่านาง</h2><p class="en">The sea, the boats and Mae Ya Nang</p>
<div class="photo-row">{fig('railay2', 900)}{fig('temple', 900)}</div>
<p class="intro">เรือหางยาวที่กระบี่จมน้ำลึกเพราะบรรทุกหนัก หัวเรือผูกผ้าสามสีกับพวงมาลัยดาวเรือง ถวายแม่ย่านาง ผู้คุ้มครองเรือ บางลำมีธงชาติไทยผืนเล็ก เสียงเครื่องยนต์ของมันคือเสียงวัยเด็กของมะนาว ดังสนั่น แล้วค่อยๆ เงียบ เหลือแค่เสียงน้ำตีลำเรือ</p>
<div class="say" style="max-width:40em"><b>พูดเป็นภาษาอังกฤษ · Say it in English</b><span>The engine roared, then coughed, then stopped.</span><br>เครื่องยนต์ดังสนั่น แล้วไอ แล้วก็ดับ</div>
</div></section>
'''
page('culture.html', 'ภาคใต้และวัฒนธรรมไทย · The South and Thai culture', 'กระบี่และภาคใต้ของไทยจากในบ้าน คำไทยที่แปลไม่ได้ อาหาร และเรือหางยาว จากนิยาย การผจญภัยของมะนาว', culture)

# ---------------- toolkit ----------------
TOOLS = [
 ('ถ้าคุณชอบร้องเพลง', 'If you love singing', [
  ('LyricsTraining', 'ดูมิวสิกวิดีโอแล้วเติมคำที่หายไป เริ่มจากระดับง่าย ฟรี', 'Fill in missing lyrics as the video plays.', 'https://lyricstraining.com', 'lyricstraining.com'),
  ('Musixmatch', 'เนื้อเพลงวิ่งตามเพลง บางเพลงมีคำแปล', 'Lyrics that scroll with the song.', 'https://www.musixmatch.com', 'musixmatch.com'),
  ('วิธีของคาร์ลอส · บทที่ 15', 'พิมพ์ค้นหา: ชื่อเพลง + lyrics + Thai and English ฟังก่อน รู้สึกก่อน แล้วค่อยอ่าน', 'Listen, feel, then read, then sing.', None, None)]),
 ('ถ้าคุณชอบดูซีรีส์และคลิป', 'If you love shows and videos', [
  ('Language Reactor', 'ซับอังกฤษและไทยพร้อมกันบน YouTube และ Netflix', 'Dual subtitles.', 'https://www.languagereactor.com', 'languagereactor.com'),
  ('YouGlish', 'ฟังคนจริงพูดคำเดียวกันในคลิปจริงหลายร้อยคลิป', 'Hear a word in real mouths.', 'https://youglish.com', 'youglish.com'),
  ('ELLLO', 'บทฟังสั้นๆ สำเนียงจากทั่วโลก มีบทถอดความ ฟรี', 'Accents from around the world.', 'https://www.elllo.org', 'elllo.org'),
  ('BBC Learning English', '6 Minute English ฟังบนรถเมล์ได้', 'Six minutes for the bus.', 'https://www.bbc.co.uk/learningenglish', 'bbc.co.uk/learningenglish'),
  ('VOA Learning English', 'ข่าวอ่านช้า ใช้คำง่าย', 'Slow, simple news.', 'https://learningenglish.voanews.com', 'learningenglish.voanews.com')]),
 ('พจนานุกรม', 'Dictionaries · บทที่ 3: เครื่องแปลไม่ใช่พจนานุกรม', [
  ('Cambridge Dictionary', 'มีภาษาอังกฤษ–ไทย สัญลักษณ์เสียง และปุ่มฟังเสียง', 'English–Thai with audio.', 'https://dictionary.cambridge.org', 'dictionary.cambridge.org'),
  ('Oxford Learner\'s Dictionaries', 'เสียงอังกฤษและอเมริกัน พร้อมประโยคตัวอย่าง', 'British and American audio.', 'https://www.oxfordlearnersdictionaries.com', 'oxfordlearnersdictionaries.com'),
  ('Longdo Dict', 'พจนานุกรมไทย–อังกฤษ ค้นจากภาษาไทยได้', 'Thai–English, fast.', 'https://dict.longdo.com', 'dict.longdo.com')]),
 ('คุยกับคนจริง', 'Talk to real people', [
  ('HelloTalk', 'คุณช่วยเขาเรียนไทย เขาช่วยคุณเรียนอังกฤษ พิมพ์ก็ได้', 'Trade languages.', 'https://www.hellotalk.com', 'hellotalk.com'),
  ('Tandem', 'หาคู่ฝึกตามความสนใจ', 'Find a partner.', 'https://www.tandem.net', 'tandem.net'),
  ('italki', 'เรียนกับครูออนไลน์เมื่อพร้อม เลือกครูที่พูดไทยได้', 'Online tutors.', 'https://www.italki.com', 'italki.com')]),
 ('อ่าน', 'Read', [
  ('British Council LearnEnglish', 'บทเรียนแยกตามระดับ วิดีโอ และเกม', 'Levelled lessons.', 'https://learnenglish.britishcouncil.org', 'learnenglish.britishcouncil.org'),
  ('Breaking News English', 'ข่าวเดียวกัน เจ็ดระดับ', 'One story, seven levels.', 'https://breakingnewsenglish.com', 'breakingnewsenglish.com'),
  ('English e-Reader', 'หนังสืออ่านง่ายแบ่งระดับ', 'Graded readers.', 'https://english-e-reader.net', 'english-e-reader.net')]),
]
shelves = ''
for th, en, items in TOOLS:
    cards = ''.join(f'<article class="tool"><h4>{n}</h4><p>{t}</p><p class="en">{e}</p>' + (f'<a class="go" href="{u}" target="_blank" rel="noopener">{l} →</a>' if u else '') + '</article>' for n, t, e, u, l in items)
    shelves += f'<h3 class="shelf">{th} <span>{en}</span></h3><div class="tools">{cards}</div>'

toolkit = f'''
<div class="hero"><div class="wrap">
<div><p class="eyebrow">เครื่องมือของคาร์ลอส · บทที่ 14</p>
<h1>ห้องเรียนหนึ่งชั่วโมง ชีวิตที่เหลือคือบทเรียน<span class="en">Class is one hour. Life is the rest.</span></h1>
<p class="lead">ไม่ต้องเพิ่มการบ้าน เปลี่ยนสิ่งที่คุณทำอยู่แล้วทุกวัน ฟังเพลง ดูซีรีส์ เล่นโทรศัพท์ ให้เป็นการเรียน เลือกทีละอย่าง สัปดาห์ละหนึ่งเครื่องมือ</p>
<p class="lead en">Change what you already do. One tool per week, like Lemon's father fixing an engine one part at a time.</p></div>
<img class="art" src="img/act1.jpg" alt="อ่าวนาง ภาพจากหนังสือ" width="1400" height="747">
</div></div>
<section><div class="wrap">{shelves}</div></section>
<section class="paper"><div class="wrap">
<h2>สามสิบวันแรก</h2><p class="en">Your first 30 days, 15 minutes a day</p>
<p class="intro">พลาดหนึ่งวัน ไม่ต้องเริ่มใหม่ ทำวันถัดไปต่อเลย ไม่มีตัวเลขไหนกลายเป็นศูนย์</p>
<div class="plan">
<div><b>สัปดาห์ 1 · เสียง</b><p>เสียงตัวอักษรและ e วิเศษ พูดตามทุกคำ อัดเสียงตัวเองวันแรก</p></div>
<div><b>สัปดาห์ 2 · เพลง</b><p>LyricsTraining วันละหนึ่งเพลง ระดับง่าย</p></div>
<div><b>สัปดาห์ 3 · ซีรีส์</b><p>ซับสองภาษา หยุดวันละห้าประโยค พูดตาม</p></div>
<div><b>สัปดาห์ 4 · คน</b><p>คุยหรือพิมพ์กับคนจริงวันละสิบนาที</p></div>
<div><b>วันที่ 30 · ฟังย้อน</b><p>อัดเสียงเรื่องเดิม ฟังสองเสียงต่อกัน</p></div>
</div>
</div></section>
<section><div class="wrap">
<h2>อ่านพจนานุกรมให้เป็น</h2><p class="en">Ten sound symbols worth knowing</p>
<div class="tablewrap"><table><thead><tr><th>สัญลักษณ์</th><th>เสียงใกล้เคียง · Sounds like</th><th>ตัวอย่าง</th></tr></thead><tbody>
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
<p class="note">เร็วๆ นี้: เสียงอ่านภาษาอังกฤษทุกบท ปริศนาพิมพ์ได้ และเพลย์ลิสต์ของมะนาว · Coming soon: chapter audio, printable puzzles and Lemon's playlist.</p>
</div></section>
'''
page('toolkit.html', 'เครื่องมือของคาร์ลอส · Carlos\'s Toolkit', 'เครื่องมือเรียนภาษาอังกฤษฟรีจากนิยาย การผจญภัยของมะนาว เพลง ซีรีส์ พจนานุกรม และแผนสามสิบวัน', toolkit)
print('built')
