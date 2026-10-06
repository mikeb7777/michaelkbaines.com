"""One-time restyle (6 Oct 2026): friendlier colors, softer type, smaller round portrait.
Michael: the photo did not fit its frame and was still too big; the site looked stiff."""
import io, glob, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
css = os.path.join(ROOT, "style.css")
s = io.open(css, encoding="utf-8").read()

def rep(a, b):
    global s
    assert s.count(a) == 1, a[:70]
    s = s.replace(a, b)

rep("""/* michaelkbaines.com, redesign October 2026. Warm editorial: paper, ink, moss, terracotta.
   Deliberately distinct from the Ic² Research Institute's navy and red. */""",
    """/* michaelkbaines.com, October 2026. Friendly and warm: cream, teal, coral and a touch of sun.
   Deliberately distinct from the Ic² Research Institute's navy and red. */""")
rep("""  --paper: #f6f1e7;
  --paper-2: #efe7d8;
  --card: #fffdf8;
  --ink: #22201b;
  --soft: #5c564b;
  --line: #e2d8c5;
  --moss: #3d5a40;
  --moss-2: #2c4430;
  --clay: #a8502a;
  --clay-2: #8a3f1f;
  --sand: #e8dcc6;
  --night: #1d2422;""",
    """  --paper: #fffaf3;
  --paper-2: #fff1e2;
  --card: #ffffff;
  --ink: #2b2a33;
  --soft: #5b5866;
  --line: #f0e3d2;
  --moss: #1f7a6c;
  --moss-2: #16645a;
  --clay: #c4502d;
  --clay-2: #a63f22;
  --sand: #fde6d2;
  --sun: #f6c453;
  --mint: #e2f3ee;
  --night: #1d2422;
  --shadow: 0 8px 26px rgba(90, 60, 30, .08);""")
rep("h1, h2, h3, .serif { font-family: 'Fraunces', Georgia, serif; font-weight: 600; line-height: 1.12; letter-spacing: -0.01em; }",
    "h1, h2, h3, .serif { font-family: 'Fraunces', Georgia, serif; font-weight: 560; font-variation-settings: 'SOFT' 100; line-height: 1.14; letter-spacing: -0.005em; }\n"
    ".q .ask, .vcard .claim, .claimrow .ct, .story blockquote, .tell strong, .parts li::before, .typecover, .name { font-variation-settings: 'SOFT' 100; }")
rep(".eyebrow { text-transform: uppercase; letter-spacing: .16em; font-size: 12.5px; font-weight: 700; color: var(--moss); margin-bottom: 14px; }",
    ".eyebrow { font-size: 15px; font-weight: 600; color: var(--moss); margin-bottom: 12px; display: inline-block; background: var(--mint); padding: 4px 12px; border-radius: 999px; }")
rep(".top { position: sticky; top: 0; z-index: 20; background: rgba(246,241,231,.94); backdrop-filter: blur(8px); border-bottom: 1px solid var(--line); }",
    ".top { position: sticky; top: 0; z-index: 20; background: rgba(255,250,243,.92); backdrop-filter: blur(8px); border-bottom: 1px solid var(--line); }")
rep(".btn.ghost { background: transparent; color: var(--ink); border: 1.5px solid var(--ink); }\n.btn.ghost:hover { background: var(--ink); color: var(--paper); }",
    ".btn.ghost { background: var(--card); color: var(--moss-2); border: 1.5px solid #bfe0d8; }\n.btn.ghost:hover { background: var(--mint); color: var(--moss-2); }")

# hero and portrait
rep(".hero { padding: 76px 0 64px; }",
    ".hero { padding: 70px 0 60px; background: radial-gradient(circle at 85% 30%, #ffe9cf 0, rgba(255,233,207,0) 42%), radial-gradient(circle at 10% 90%, #e2f3ee 0, rgba(226,243,238,0) 38%); }")
rep(".hero .wrap { display: grid; grid-template-columns: 1.25fr .75fr; gap: 56px; align-items: center; }",
    ".hero .wrap { display: grid; grid-template-columns: 1.4fr .6fr; gap: 48px; align-items: center; }")
rep(""".portrait { position: relative; max-width: 330px; justify-self: end; width: 100%; }
.portrait img { width: 100%; height: auto; aspect-ratio: 4/5; object-fit: cover; border-radius: 4px; display: block; }
.portrait::after { content: ''; position: absolute; inset: 14px -14px -14px 14px; border: 1.5px solid var(--clay); border-radius: 4px; z-index: -1; }""",
    """.portrait { position: relative; max-width: 250px; justify-self: center; width: 100%; }
.portrait img { width: 100%; height: auto; aspect-ratio: 1/1; object-fit: cover; object-position: 50% 28%; border-radius: 50%; display: block; border: 6px solid #fff; box-shadow: var(--shadow); position: relative; }
.portrait::before { content: ''; position: absolute; width: 46%; aspect-ratio: 1; border-radius: 50%; background: var(--sun); right: -6%; top: -4%; z-index: 0; }
.portrait::after { content: ''; position: absolute; width: 30%; aspect-ratio: 1; border-radius: 50%; background: #bfe0d8; left: -8%; bottom: 2%; z-index: 0; }
.portrait img { z-index: 1; }""")

# sections and cards: no hard rules, rounder, soft shadow
rep("section.alt { background: var(--card); border-top: 1px solid var(--line); border-bottom: 1px solid var(--line); }",
    "section.alt { background: var(--paper-2); }")
rep(".q { background: var(--paper); border: 1px solid var(--line); border-radius: 10px;",
    ".q { background: var(--card); border: 0; border-radius: 20px; box-shadow: var(--shadow);")
rep("section.alt .q { background: var(--paper); }", "section.alt .q { background: var(--card); }")
rep(".tag { align-self: flex-start; font-size: 11.5px; font-weight: 700; letter-spacing: .08em; text-transform: uppercase; padding: 3px 9px; border-radius: 999px; background: #e6eee3; color: var(--moss-2); }",
    ".tag { align-self: flex-start; font-size: 13px; font-weight: 600; padding: 3px 11px; border-radius: 999px; background: var(--mint); color: var(--moss-2); }")
rep(".tag.clay { background: #f3e1d6; color: var(--clay-2); }", ".tag.clay { background: var(--sand); color: var(--clay-2); }")
rep(".typecover { width: 100%; aspect-ratio: 2/3; background: var(--moss);", ".typecover { width: 100%; aspect-ratio: 2/3; border-radius: 4px 10px 10px 4px; background: var(--moss);")

# newsletter band: light mint instead of near-black
rep(""".signup { background: var(--night); color: #efe9dc; }""", """.signup { background: var(--mint); color: var(--ink); }""")
rep(".signup h2 { color: #fff; }", ".signup h2 { color: var(--ink); }")
rep(".signup p { color: rgba(239,233,220,.86); }", ".signup p { color: var(--soft); }")
rep(".signup ul { margin: 16px 0 0 20px; color: rgba(239,233,220,.86); }", ".signup ul { margin: 16px 0 0 20px; color: var(--soft); }")
rep(".form { background: rgba(255,255,255,.06); border: 1px solid rgba(255,255,255,.14); border-radius: 12px; padding: 26px; }",
    ".form { background: var(--card); border: 0; border-radius: 20px; padding: 28px; box-shadow: var(--shadow); }")
rep(".form label { display: block; font-weight: 600; margin-bottom: 8px; color: #fff; }", ".form label { display: block; font-weight: 600; margin-bottom: 8px; color: var(--ink); }")
rep(".form input[type=email] { flex: 1 1 220px; padding: 13px 14px; border-radius: 999px; border: 1px solid rgba(255,255,255,.35); background: #fffdf8;",
    ".form input[type=email] { flex: 1 1 220px; padding: 13px 16px; border-radius: 999px; border: 1.5px solid #cfe6df; background: #fff;")
rep(".form .fine { font-size: 13.5px; color: rgba(239,233,220,.72); margin-top: 12px; }", ".form .fine { font-size: 13.5px; color: var(--soft); margin-top: 12px; }")
rep(".form .fine a { color: #f0c9b2; }", ".form .fine a { color: var(--clay-2); }")

rep(".vcard { background: var(--card); border: 1px solid var(--line); border-radius: 10px; padding: 20px; border-top: 5px solid var(--vc, var(--v-none)); }",
    ".vcard { background: var(--card); border: 0; border-radius: 18px; padding: 22px; box-shadow: var(--shadow); border-top: 6px solid var(--vc, var(--v-none)); }")
rep(".verdict { display: inline-block; font-size: 12px; font-weight: 700; letter-spacing: .06em; text-transform: uppercase;",
    ".verdict { display: inline-block; font-size: 13px; font-weight: 600;")
rep(".story blockquote { font-family: 'Fraunces', Georgia, serif; font-size: clamp(26px, 3.4vw, 36px); font-style: italic; line-height: 1.25; color: var(--clay-2); border-left: 3px solid var(--clay); padding-left: 22px; }",
    ".story blockquote { font-family: 'Fraunces', Georgia, serif; font-size: clamp(26px, 3.4vw, 36px); font-style: italic; line-height: 1.25; color: var(--clay-2); background: var(--card); border-radius: 20px; padding: 26px 28px; box-shadow: var(--shadow); }")
rep(".band { background: var(--paper-2); border-top: 1px solid var(--line); }", ".band { background: var(--sand); }")
rep(".tell { background: var(--card); border: 1px solid var(--line); border-left: 5px solid var(--clay); border-radius: 0 10px 10px 0;",
    ".tell { background: var(--card); border: 0; border-left: 6px solid var(--sun); border-radius: 18px; box-shadow: var(--shadow);")
rep(".chip[aria-pressed=\"true\"] { border-color: var(--ink); background: var(--ink); color: var(--paper); }",
    ".chip[aria-pressed=\"true\"] { border-color: var(--moss); background: var(--moss); color: #fff; }")
rep(".claimrow { background: var(--card); border: 1px solid var(--line); border-radius: 10px; border-left: 6px solid var(--vc); }",
    ".claimrow { background: var(--card); border: 0; border-radius: 18px; box-shadow: var(--shadow); border-left: 6px solid var(--vc); }")
rep(".detail h4 { font-size: 12.5px; text-transform: uppercase; letter-spacing: .1em; color: var(--moss); margin-bottom: 6px; }",
    ".detail h4 { font-size: 14px; color: var(--moss); margin-bottom: 6px; }")
rep(".bio { background: var(--card); border: 1px solid var(--line); border-radius: 10px;", ".bio { background: var(--card); border: 0; border-radius: 18px; box-shadow: var(--shadow);")
rep(".parts li { counter-increment: part; background: var(--card); border: 1px solid var(--line); border-radius: 10px;",
    ".parts li { counter-increment: part; background: var(--card); border: 0; border-radius: 18px; box-shadow: var(--shadow);")
rep(".press-grid aside img { width: 100%; height: auto; border-radius: 6px; display: block; }",
    ".press-grid aside img { width: 100%; height: auto; border-radius: 18px; display: block; box-shadow: var(--shadow); }")
rep("  .portrait { justify-self: start; max-width: 240px; }", "  .portrait { justify-self: start; max-width: 190px; margin-left: 8px; }")
io.open(css, "w", encoding="utf-8").write(s)

# softer Fraunces on every page
OLD = "family=Fraunces:ital,opsz,wght@0,9..144,600;1,9..144,500"
NEW = "family=Fraunces:ital,opsz,wght,SOFT@0,9..144,500..600,100;1,9..144,500..600,100"
for f in glob.glob(os.path.join(ROOT, "*.html")):
    h = io.open(f, encoding="utf-8").read()
    if OLD in h:
        io.open(f, "w", encoding="utf-8").write(h.replace(OLD, NEW)); print("font", os.path.basename(f))
# the newsletter eyebrow was colored for the dark band
for f in ("index.html", "rediscovering-oneness.html"):
    p = os.path.join(ROOT, f); h = io.open(p, encoding="utf-8").read()
    h = h.replace('<p class="eyebrow" style="color:#c9d8c3">The newsletter</p>', '<p class="eyebrow">The newsletter</p>')
    io.open(p, "w", encoding="utf-8").write(h)
print("ok")
