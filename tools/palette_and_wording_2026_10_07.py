"""Author site, 7 Oct 2026 (Michael):
1. Wording. "I tested aircraft for a living" is not something he would say: he worked in testing only at
   Mitsubishi, though all aerospace engineering is checked several times. The headline becomes a question,
   and every "flight test engineer" / "certifying aircraft" phrasing is corrected.
2. Colors. "A lot of the author's page is different shades of white ... borrow the dark blue, medium blue,
   gunmetal, gray, red, black and yellow from the other site ... Even texture or grain would be better."
   Palette from eequalsicsquared.com: navy #1a1d33, blue #005ba5, gunmetal gradients (canonical, copied
   verbatim), grays #8fa0b0/#5a6878/#4a5868 and #e8edf2, red #8B0000, black #111111, yellow #f1e303.
   Light areas get a faint grain instead of flat white. Run once."""
import io, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def edit(name, pairs):
    p = os.path.join(ROOT, name)
    s = io.open(p, encoding="utf-8").read()
    for a, b in pairs:
        assert s.count(a) == 1, (name, a[:70])
        s = s.replace(a, b)
    io.open(p, "w", encoding="utf-8").write(s)


edit("index.html", [
    ('content="Michael K. Baines tested aircraft for a living and now tests ideas: what the universe is made of, and how connected we really are.',
     'content="After 39 years in aerospace engineering, Michael K. Baines asks two questions: what the universe is made of, and how connected we really are.'),
    ('content="What the universe is made of, and how connected we really are. Two books, one method: test it."',
     'content="What the universe is made of, and how connected we really are. Two books, one question: what holds up when you check it?"'),
    ('<h1>I tested aircraft for a living. <em>Now I test ideas.</em></h1>',
     '<h1>What holds up <em>when you check it?</em></h1>'),
    ('<p class="lead">Two questions run through my work: what the universe is made of, and how connected we really are. I write about both the way an engineer would, by asking what holds up when you test it.</p>',
     '<p class="lead">Two questions run through my work: what the universe is made of, and how connected we really are. I spent 39 years in aerospace engineering, where every piece of work is checked several times before anyone flies on it. I bring that habit to both questions.</p>'),
    ('<p>Certification testing teaches one habit for life: a claim is only as good as the test it survives. I took that habit to bigger questions.',
     '<p>Aerospace engineering teaches one habit for life: nothing is trusted until it has been checked, and checked again. I took that habit to bigger questions.'),
])
edit("press.html", [
    ("Michael K. Baines is a flight test engineer turned author and researcher. He writes about what the universe is made of and how connected we really are, testing both questions the way aircraft are certified.",
     "Michael K. Baines is an aerospace engineer turned author and researcher. He writes about what the universe is made of and how connected we really are, and checks both questions the way aerospace work is checked: several times, before anything is trusted."),
    ("Michael K. Baines spent his engineering career making sure things work before people trust them with their lives. Over 39 years",
     "Michael K. Baines spent 39 years in aerospace engineering, where every piece of work is checked several times before anyone flies on it. Over that time"),
    ("He now applies the same habit, that a claim is only as good as the test it survives, to larger questions.",
     "He now brings the same habit, checking a claim before trusting it, to larger questions."),
    ("<li><strong>From flight test to first principles.</strong> What certifying aircraft teaches about testing big ideas.</li>",
     "<li><strong>From aircraft to first principles.</strong> What aerospace engineering teaches about checking big ideas.</li>"),
])

GRAIN = ("url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='180' height='180'>"
         "<filter id='g'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' stitchTiles='stitch'/>"
         "<feColorMatrix values='0 0 0 0 .1  0 0 0 0 .11  0 0 0 0 .2  0 0 0 .09 0'/></filter>"
         "<rect width='100%' height='100%' filter='url(%23g)'/></svg>\")")

css = os.path.join(ROOT, "style.css")
s = io.open(css, encoding="utf-8").read()
old_tokens = s[s.index(":root {"):s.index("}", s.index(":root {")) + 1]
new_tokens = """:root {
  --paper: #f1f3f6;
  --paper-2: #e8edf2;
  --card: #ffffff;
  --ink: #1a1d33;
  --soft: #4a5868;
  --line: #d0d5dd;
  --moss: #005ba5;
  --moss-2: #1a1d33;
  --clay: #8B0000;
  --clay-2: #6b0000;
  --sand: #e8edf2;
  --sun: #f1e303;
  --mint: #e8edf2;
  --navy: #1a1d33;
  --black: #111111;
  --night: #1a1d33;
  --gunmetal: linear-gradient(135deg, #8fa0b0 0%, #5a6878 100%);
  --gunmetal-dark: linear-gradient(135deg, #5a6878 0%, #4a5868 100%);
  --grain: """ + GRAIN + """;
  --shadow: 0 8px 26px rgba(26, 29, 51, .10);
  --max: 1120px;
  /* verdict colors, from the same palette */
  --v-strong: #2e7d32; --v-holds: #1a5c2a; --v-test: #7a5000; --v-none: #5a6878; --v-push: #8B0000;
}"""
s = s.replace(old_tokens, new_tokens)
s = s.replace("/* michaelkbaines.com, October 2026. Friendly and warm: cream, teal, coral and a touch of sun.\n   Deliberately distinct from the Ic² Research Institute's navy and red. */",
              "/* michaelkbaines.com, October 2026. The Ic² palette (navy, blue, gunmetal, grays, red, black, yellow),\n   with a faint grain on light areas instead of flat white. */")
s += """

/* ---------- Ic² palette, 7 Oct 2026 (later rules win) ---------- */
body { background-color: var(--paper); background-image: var(--grain); }
.top { background: rgba(255,255,255,.96); border-bottom: 3px solid var(--navy); }
a { color: var(--moss); }
.nav a:hover, .nav a[aria-current] { color: var(--clay); }
.nav a.btn-sm { background: var(--clay); }
.nav a.btn-sm:hover { background: var(--clay-2); }
.btn.ghost { background: transparent; color: var(--navy); border: 1.5px solid var(--navy); }
.btn.ghost:hover { background: var(--navy); color: #fff; }
.eyebrow { background: #fff; color: var(--moss); border: 1px solid var(--line); }

/* hero: navy, white type, yellow accent */
.hero { background: var(--navy); color: #fff; border-bottom: 6px solid var(--clay); }
.hero h1 { color: #fff; }
.hero h1 em { color: var(--sun); }
.hero .lead { color: rgba(255,255,255,.88); }
.hero .eyebrow { background: var(--sun); color: var(--navy); border: 0; }
.hero .btn { background: var(--moss); }
.hero .btn:hover { background: #fff; color: var(--navy); }
.hero .btn.ghost { background: transparent; color: #fff; border-color: rgba(255,255,255,.7); }
.hero .btn.ghost:hover { background: #fff; color: var(--navy); }
.portrait::before { background: var(--sun); }
.portrait::after { background: var(--moss); }

/* light sections: gray with grain, white cards with a visible edge */
section.alt { background-color: var(--paper-2); background-image: var(--grain); }
.q, .vcard, .claimrow, .bio, .parts li, .tell, .form { border: 1px solid var(--line); }
.q .cov { background: var(--navy); }
.tag { background: var(--paper-2); color: var(--moss); }
.tag.clay { background: #fff; color: var(--clay); border: 1px solid var(--clay); }
.typecover { background: var(--moss); }
.parts li::before { color: var(--clay); }
.tell { border-left: 6px solid var(--sun); }
.chip[aria-pressed="true"] { border-color: var(--navy); background: var(--navy); color: #fff; }

/* newsletter: dark gunmetal, white type, white form card */
.signup { background: var(--gunmetal-dark); color: #fff; }
.signup h2 { color: #fff; }
.signup p, .signup ul { color: rgba(255,255,255,.92); }
.signup .eyebrow { background: var(--sun); color: var(--navy); border: 0; }
.signup .form p.fine { color: var(--soft); }

/* story: quote card in navy */
.story blockquote { background: var(--navy); color: #fff; }
.story blockquote cite { color: rgba(255,255,255,.8); }
.timeline li::before { border-color: var(--moss); }

/* Institute band: black with a yellow rule */
.band { background: var(--black); color: #fff; border-top: 6px solid var(--sun); }
.band h2 { color: #fff; }
.band p { color: rgba(255,255,255,.85); }
.band .btn.ghost { color: #fff; border-color: #fff; }
.band .btn.ghost:hover { background: var(--sun); color: var(--navy); border-color: var(--sun); }

/* book and claims pages */
.holds-hero h1 { color: var(--navy); }
.note { border-left-color: var(--clay); }

footer { background: var(--navy); color: rgba(255,255,255,.85); border-top: 0; }
footer a { color: #fff; }
"""
io.open(css, "w", encoding="utf-8").write(s)
print("ok")
