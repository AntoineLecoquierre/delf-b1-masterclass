#!/usr/bin/env python3
"""Generates the /method/ area: one page per module, plus an index.

Fill VIMEO and DOCS below with real ids/links and re-run. Anything left as
None renders as a visible "not connected yet" placeholder rather than a
broken embed, so the pages are safe to ship half-finished.
"""
import os, html

# ── fill these in ────────────────────────────────────────────────────────
VIMEO = {1: None, 2: None, 3: None, 4: None, 5: None}   # e.g. 1: "912345678"
DOCS = {                                                 # e.g. "Workbook": "https://drive.google.com/..."
  1: {"Six-week study plan": None},
  2: {"Listening exam 1": None, "Listening exam 2": None, "Audio pack": None, "Annotated keys": None},
  3: {"Reading test 1": None, "Reading test 2": None, "Annotated keys": None},
  4: {"Writing prompts": None, "Graded models + grid": None},
  5: {"Speaking pack": None, "Role-play cards": None, "Grammar reference": None},
}
INDEXABLE = False          # flip to True to let search engines in
# ─────────────────────────────────────────────────────────────────────────

MODULES = [
 (1,"1-blueprint","Foundation","The exam blueprint",
  "The four sections, how each is marked, and the elimination rule that quietly fails candidates who do not know it. Then a six-week plan telling you what to do each day."),
 (2,"2-listening","Compréhension de l'oral","Listening",
  "How the audio is built, and the Two-Listen Strategy: what to catch on the first play, what to hunt on the second. Then two complete exams under real conditions."),
 (3,"3-reading","Compréhension des écrits","Reading",
  "Reading is a race against the clock. The skim-then-scan method, and how to spot the distractor answers built to trap you."),
 (4,"4-writing","Production écrite","Writing",
  "More than half the marks are for structure, not vocabulary. The four-paragraph frame that works for any prompt, the official grid decoded, and graded model answers."),
 (5,"5-speaking","Production orale","Speaking",
  "The oral frightens most candidates, yet it is the most predictable section once you know its three parts. Each one walked through, with role-play cards and model answers."),
]

ROBOTS = "index, follow" if INDEXABLE else "noindex, nofollow"

def head(title, desc, depth):
    up = "../" * depth
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(title)} · DELF B1 Masterclass</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="robots" content="{ROBOTS}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{up}blog/style.css">
<style>
.mth-vid{{position:relative;aspect-ratio:16/9;background:#123838;border:1px solid var(--border-soft);border-radius:10px;overflow:hidden;margin:26px 0;}}
.mth-vid iframe{{position:absolute;inset:0;width:100%;height:100%;border:0;}}
.mth-soon{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;color:#9db3aa;font-size:14.5px;text-align:center;padding:20px;}}
.mth-soon b{{color:#e9e2cf;font-size:16px;}}
.mth-docs{{list-style:none;margin:22px 0 0;padding:0;display:grid;gap:10px;}}
.mth-docs li{{margin:0;}}
.mth-docs a,.mth-docs span{{display:flex;align-items:center;justify-content:space-between;gap:14px;padding:14px 18px;border:1px solid var(--border-soft);border-radius:8px;text-decoration:none;font-size:15px;}}
.mth-docs a{{color:var(--ink);}}
.mth-docs a:hover{{border-color:var(--gold);}}
.mth-docs a::after{{content:"Download";font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--gold-deep);white-space:nowrap;}}
.mth-docs span{{color:#8d8578;}}
.mth-docs span::after{{content:"Coming shortly";font-size:12px;letter-spacing:.08em;text-transform:uppercase;white-space:nowrap;}}
.mth-nav{{display:flex;justify-content:space-between;gap:14px;margin-top:44px;padding-top:22px;border-top:1px solid var(--border-soft);font-size:14.5px;}}
.mth-nav a{{color:var(--gold-deep);}}
.mth-list{{list-style:none;margin:30px 0 0;padding:0;display:grid;gap:12px;}}
.mth-list a{{display:block;padding:20px 22px;border:1px solid var(--border-soft);border-radius:10px;text-decoration:none;}}
.mth-list a:hover{{border-color:var(--gold);}}
.mth-k{{font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--gold-deep);display:block;margin-bottom:5px;}}
.mth-t{{font-family:'Playfair Display',serif;font-size:21px;font-weight:700;color:var(--ink);display:block;}}
</style>
</head>
<body>

<div class="bl-top">
  <div class="bl-top-in">
    <a class="bl-brand" href="{up}">DELF&nbsp;B1&nbsp;<b>MASTERCLASS</b></a>
    <a class="bl-cta" href="{up}book/">Book a session →</a>
  </div>
</div>

<div class="bl-wrap">'''

FOOT = '''</div>

<footer class="bl-foot">
  <p>Taught entirely in English by Antoine L. — Native French Teacher, Paris</p>
</footer>

</body>
</html>
'''

os.makedirs("method", exist_ok=True)
for n, slug, fr, title, blurb in MODULES:
    os.makedirs(f"method/{slug}", exist_ok=True)
    vid = VIMEO.get(n)
    player = (f'<iframe src="https://player.vimeo.com/video/{vid}?dnt=1&title=0&byline=0&portrait=0" '
              f'allow="fullscreen; picture-in-picture" title="{html.escape(title)} — video lesson"></iframe>'
              if vid else
              '<!-- Paste the Vimeo id into VIMEO in build_method.py and re-run. -->'
              '<div class="mth-soon"><b>This lesson is being uploaded</b>It will appear here shortly — your workbook below is ready now.</div>')
    docs = "".join(
        f'<li><a href="{html.escape(url)}" target="_blank" rel="noopener noreferrer">{html.escape(name)}</a></li>'
        if url else f'<li><span>{html.escape(name)}</span></li>'
        for name, url in DOCS.get(n, {}).items())
    prev = f'<a href="../{MODULES[n-2][1]}/">← Module {n-1}</a>' if n > 1 else '<a href="../">← All modules</a>'
    nxt  = f'<a href="../{MODULES[n][1]}/">Module {n+1} →</a>' if n < len(MODULES) else '<a href="../../book/">Book a session →</a>'
    body = f'''
  <header class="bl-head">
    <p class="bl-crumb"><a href="../">The method</a> › Module {n}</p>
    <p class="bl-kick">Module {n} · {html.escape(fr)}</p>
    <h1 class="bl-title">{html.escape(title)}</h1>
  </header>

  <div class="bl-body">
    <p class="lead">{html.escape(blurb)}</p>
    <div class="mth-vid">{player}</div>
    <h2>Your workbook</h2>
    <p>Download these before you watch, and work through them afterwards. Everything is yours to keep.</p>
    <ul class="mth-docs">{docs}</ul>
    <div class="mth-nav">{prev}{nxt}</div>
  </div>
'''
    open(f"method/{slug}/index.html","w",encoding="utf-8").write(
        head(f"Module {n} — {title}", blurb[:150], 2) + body + FOOT)

items = "".join(
    f'<li><a href="{slug}/"><span class="mth-k">Module {n} · {html.escape(fr)}</span>'
    f'<span class="mth-t">{html.escape(title)}</span></a></li>'
    for n, slug, fr, title, _ in MODULES)
index_body = f'''
  <header class="bl-head">
    <h1 class="bl-title">The <em>method</em></h1>
    <p class="bl-kick">Five modules · every part of the exam</p>
  </header>

  <div class="bl-body">
    <p class="lead">Each module pairs a video lesson with the workbook you practise on. Work through them in order — the first one changes how you read the other four.</p>
    <ul class="mth-list">{items}</ul>
    <div class="mth-nav"><a href="../">← Home</a><a href="../book/">Book a session →</a></div>
  </div>
'''
open("method/index.html","w",encoding="utf-8").write(
    head("The method", "The five modules of the DELF B1 Masterclass.", 1) + index_body + FOOT)
print(f"généré : method/index.html + {len(MODULES)} modules · robots = {ROBOTS}")
