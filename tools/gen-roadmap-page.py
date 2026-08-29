import re, json, pathlib, html
R = pathlib.Path(__file__).resolve().parent.parent
md = (R / "ROADMAP.md").read_text().splitlines()

phases, cur = [], None
for ln in md:
    m = re.match(r"^## (Phase \d+|Unsorted) - (.+)$", ln)
    if m:
        cur = {"n": m.group(1), "title": m.group(2), "why": "", "items": []}
        phases.append(cur); continue
    if ln.startswith("## "): cur = None; continue
    if cur is None: continue
    if re.match(r"^\*\d+ problems\*$", ln): continue
    pm = re.match(r"^- \[ \] \[`([^`]+)`\]\([^)]+\)(.*)$", ln)
    if pm:
        path, rest = pm.group(1), pm.group(2)
        flag, note = None, ""
        if "(never solved)" in rest: flag = "never"; note = "never solved"
        elif "`*`" in rest:
            flag = "redo"; note = rest.split("`*`", 1)[1].strip()
        if "already solved" in rest: flag = "done"; note = "already solved, ported from your C++"
        card = (R / path / "README.md").read_text().splitlines()
        title = card[0].lstrip("# ").strip()
        meta = [x.strip() for x in card[2].split("|")]
        plat = meta[0]; diff = meta[1] if len(meta) > 1 else ""
        tags = meta[2] if len(meta) > 2 else ""
        cur["items"].append({"path": path, "title": title, "plat": plat,
                             "diff": diff, "tags": tags, "flag": flag, "note": note})
        continue
    if ln.strip() and not cur["why"]: cur["why"] = ln.strip()

total = sum(len(p['items']) for p in phases)
assert total > 0

E = html.escape
def rows(items):
    out = []
    for it in items:
        pid = it["path"].split("/")[-1].split("-")[0]
        chip = ""
        if it["flag"] == "redo":
            chip = f'<span class="chip chip-redo" title="{E(it["note"])}">redo</span>'
        elif it["flag"] == "never":
            chip = '<span class="chip chip-never">never solved</span>'
        elif it["flag"] == "done":
            chip = '<span class="chip chip-done">done</span>'
        note = f'<p class="note">{E(it["note"])}</p>' if it["flag"] == "redo" else ""
        out.append(f'''<li class="row" data-diff="{E(it['diff'])}">
<label class="rowmain">
<input type="checkbox" data-key="{E(it['path'])}">
<span class="box" aria-hidden="true"></span>
<span class="pid">{E(pid)}</span>
<span class="rtitle">{E(it['title'])}</span>
<span class="rmeta"><span class="plat">{E(it['plat'])}</span><span class="diff d-{E(it['diff'])}">{E(it['diff'])}</span>{chip}</span>
</label>{note}</li>''')
    return "\n".join(out)

def label(n):
    parts = n.split()
    return parts[1] if len(parts) > 1 else "+"

nav = "\n".join(
    f'<a class="navcard" href="#p{i}"><span class="navnum">{label(p["n"])}</span>'
    f'<span class="navtitle">{E(p["title"])}</span>'
    f'<span class="navcount" data-phase="{i}">0/{len(p["items"])}</span></a>'
    for i, p in enumerate(phases))

secs = "\n".join(f'''<section class="phase" id="p{i}">
<header class="phead">
<span class="pnum">{E(label(p["n"]))}</span>
<div class="pheadtext"><h2>{E(p["title"])}</h2>
<p class="why">{E(p["why"])}</p></div>
<span class="pcount" data-phase="{i}">0/{len(p["items"])}</span>
</header>
<ul class="rows">
{rows(p["items"])}
</ul>
</section>''' for i, p in enumerate(phases))

prio = [it for p in phases for it in p["items"] if it["flag"] in ("redo", "never")]

prio_rows = "\n".join(f'''<li class="prow">
<span class="pid">{E(it["path"].split("/")[-1].split("-")[0])}</span>
<div><span class="rtitle">{E(it["title"])}</span>
<p class="note">{E(it["note"])}</p></div>
<span class="chip chip-{it['flag']}">{"never solved" if it["flag"]=="never" else "redo"}</span>
</li>''' for it in prio)

HTML = f'''<title>117 Problems</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans+Condensed:wght@600;700&family=IBM+Plex+Sans:wght@400;500;600&display=swap">
<style>
:root {{
  --ground:#F3F4F8; --surface:#FFFFFF; --surface-2:#F8F9FC;
  --text:#15161F; --muted:#5D6076; --faint:#8B8EA3;
  --line:#DEE0EA; --line-strong:#C8CBD9;
  --accent:#3B3F94; --accent-soft:#EAEBF7;
  --done:#2E7D5B; --done-soft:#E3F1EA;
  --redo:#9C6717; --redo-soft:#F7EEDE;
  --never:#A63D5A; --never-soft:#F8E6EB;
  --shadow:0 1px 2px rgba(21,22,31,.05), 0 4px 16px rgba(21,22,31,.04);
}}
@media (prefers-color-scheme: dark) {{
  :root:not([data-theme="light"]) {{
    --ground:#131420; --surface:#1B1D2B; --surface-2:#20222F;
    --text:#E7E8F0; --muted:#9A9DB2; --faint:#6E7189;
    --line:#2C2F40; --line-strong:#3C4055;
    --accent:#9296F0; --accent-soft:#24263C;
    --done:#5CBE93; --done-soft:#1B2E27;
    --redo:#D9A155; --redo-soft:#302719;
    --never:#DE7A94; --never-soft:#311E25;
    --shadow:0 1px 2px rgba(0,0,0,.4), 0 4px 20px rgba(0,0,0,.28);
  }}
}}
:root[data-theme="dark"] {{
  --ground:#131420; --surface:#1B1D2B; --surface-2:#20222F;
  --text:#E7E8F0; --muted:#9A9DB2; --faint:#6E7189;
  --line:#2C2F40; --line-strong:#3C4055;
  --accent:#9296F0; --accent-soft:#24263C;
  --done:#5CBE93; --done-soft:#1B2E27;
  --redo:#D9A155; --redo-soft:#302719;
  --never:#DE7A94; --never-soft:#311E25;
  --shadow:0 1px 2px rgba(0,0,0,.4), 0 4px 20px rgba(0,0,0,.28);
}}
* {{ box-sizing:border-box; }}
body {{
  margin:0; background:var(--ground); color:var(--text);
  font-family:"IBM Plex Sans",-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  font-size:15px; line-height:1.6; -webkit-font-smoothing:antialiased;
}}
.wrap {{ max-width:1000px; margin:0 auto; padding:0 24px 96px; }}

/* ---- sticky bar ---- */
.bar {{
  position:sticky; top:0; z-index:20; background:var(--ground);
  border-bottom:1px solid var(--line); margin-bottom:40px;
}}
.barin {{
  max-width:1000px; margin:0 auto; padding:12px 24px;
  display:flex; align-items:center; gap:20px; flex-wrap:wrap;
}}
.barname {{
  font-family:"IBM Plex Sans Condensed",sans-serif; font-weight:700;
  font-size:15px; letter-spacing:.01em; margin-right:auto;
}}
.track {{ flex:1 1 220px; min-width:160px; height:6px; background:var(--line); border-radius:3px; overflow:hidden; }}
.fill {{ height:100%; width:0%; background:var(--accent); border-radius:3px; transition:width .3s ease; }}
.tally {{ font-family:"IBM Plex Mono",monospace; font-size:13px; font-variant-numeric:tabular-nums; color:var(--muted); }}
.tally b {{ color:var(--text); font-weight:600; }}
.reset {{
  font:500 12px/1 "IBM Plex Sans",sans-serif; color:var(--muted);
  background:none; border:1px solid var(--line-strong); border-radius:5px;
  padding:6px 10px; cursor:pointer;
}}
.reset:hover {{ color:var(--text); border-color:var(--muted); }}
.reset:focus-visible, a:focus-visible, label:focus-within {{ outline:2px solid var(--accent); outline-offset:2px; }}

/* ---- masthead ---- */
.mast {{ padding:44px 0 8px; }}
.eyebrow {{
  font-family:"IBM Plex Mono",monospace; font-size:11px; font-weight:500;
  letter-spacing:.14em; text-transform:uppercase; color:var(--accent); margin:0 0 14px;
}}
h1 {{
  font-family:"IBM Plex Sans Condensed",sans-serif; font-weight:700;
  font-size:clamp(34px,6vw,54px); line-height:1.04; letter-spacing:-.015em;
  margin:0 0 18px; text-wrap:balance;
}}
.lede {{ font-size:17px; color:var(--muted); max-width:60ch; margin:0 0 8px; }}
.lede strong {{ color:var(--text); font-weight:500; }}

/* ---- phase index ---- */
.index {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(190px,1fr)); gap:8px; margin:36px 0 56px; }}
.navcard {{
  display:flex; align-items:baseline; gap:9px; text-decoration:none; color:inherit;
  background:var(--surface); border:1px solid var(--line); border-radius:7px;
  padding:11px 13px; transition:border-color .15s, transform .15s;
}}
.navcard:hover {{ border-color:var(--accent); transform:translateY(-1px); }}
.navnum {{ font-family:"IBM Plex Mono",monospace; font-size:11px; font-weight:600; color:var(--accent); }}
.navtitle {{ flex:1; font-size:13px; font-weight:500; line-height:1.3; }}
.navcount {{ font-family:"IBM Plex Mono",monospace; font-size:11px; color:var(--faint); font-variant-numeric:tabular-nums; }}

/* ---- priority ---- */
.prio {{ background:var(--surface); border:1px solid var(--line); border-radius:10px; padding:26px 28px; margin-bottom:64px; box-shadow:var(--shadow); }}
.prio h2 {{ font-family:"IBM Plex Sans Condensed",sans-serif; font-size:23px; margin:0 0 8px; letter-spacing:-.01em; }}
.prio > p {{ color:var(--muted); max-width:62ch; margin:0 0 22px; font-size:14.5px; }}
.plist {{ list-style:none; margin:0; padding:0; display:flex; flex-direction:column; }}
.prow {{ display:grid; grid-template-columns:auto 1fr auto; gap:14px; align-items:start; padding:11px 0; border-top:1px solid var(--line); }}
.prow:first-child {{ border-top:none; }}

/* ---- phases ---- */
.phase {{ margin-bottom:56px; scroll-margin-top:72px; }}
.phead {{ display:grid; grid-template-columns:auto 1fr auto; gap:16px; align-items:start; padding-bottom:14px; border-bottom:2px solid var(--line-strong); margin-bottom:4px; }}
.pnum {{
  font-family:"IBM Plex Mono",monospace; font-size:12px; font-weight:600;
  color:var(--accent); background:var(--accent-soft); border-radius:5px;
  padding:5px 9px; line-height:1; margin-top:5px;
}}
.pheadtext h2 {{ font-family:"IBM Plex Sans Condensed",sans-serif; font-size:26px; margin:0 0 6px; letter-spacing:-.012em; }}
.why {{ color:var(--muted); font-size:14.5px; margin:0; max-width:66ch; }}
.pcount {{ font-family:"IBM Plex Mono",monospace; font-size:12px; color:var(--faint); font-variant-numeric:tabular-nums; margin-top:8px; white-space:nowrap; }}

.rows {{ list-style:none; margin:0; padding:0; }}
.row {{ border-bottom:1px solid var(--line); }}
.rowmain {{ display:flex; align-items:center; gap:12px; padding:10px 6px; cursor:pointer; }}
.rowmain:hover {{ background:var(--surface-2); }}
.rowmain input {{ position:absolute; opacity:0; width:0; height:0; }}
.box {{
  flex:none; width:17px; height:17px; border:1.5px solid var(--line-strong);
  border-radius:4px; background:var(--surface); position:relative; transition:.15s;
}}
input:checked + .box {{ background:var(--done); border-color:var(--done); }}
input:checked + .box::after {{
  content:""; position:absolute; left:5px; top:1.5px; width:4px; height:9px;
  border:solid #fff; border-width:0 2px 2px 0; transform:rotate(42deg);
}}
.pid {{ font-family:"IBM Plex Mono",monospace; font-size:12.5px; color:var(--faint); font-variant-numeric:tabular-nums; flex:none; min-width:44px; }}
.rtitle {{ flex:1; font-size:14.5px; font-weight:500; }}
input:checked ~ .rtitle {{ color:var(--faint); text-decoration:line-through; text-decoration-color:var(--line-strong); }}
.rmeta {{ display:flex; align-items:center; gap:7px; flex:none; }}
.plat {{ font-family:"IBM Plex Mono",monospace; font-size:11px; color:var(--faint); }}
.diff {{ font-family:"IBM Plex Mono",monospace; font-size:11px; padding:2px 6px; border-radius:4px; background:var(--surface-2); color:var(--muted); border:1px solid var(--line); }}
.d-hard {{ color:var(--never); border-color:var(--never); background:var(--never-soft); }}
.d-medium {{ color:var(--redo); border-color:var(--redo); background:var(--redo-soft); }}
.chip {{ font-family:"IBM Plex Mono",monospace; font-size:10.5px; font-weight:500; padding:3px 7px; border-radius:4px; white-space:nowrap; }}
.chip-redo {{ color:var(--redo); background:var(--redo-soft); }}
.chip-never {{ color:var(--never); background:var(--never-soft); }}
.chip-done {{ color:var(--done); background:var(--done-soft); }}
.note {{ margin:-4px 0 10px; padding-left:73px; font-size:13px; color:var(--muted); max-width:70ch; }}
.prow .note {{ padding-left:0; margin:2px 0 0; }}

footer {{ border-top:1px solid var(--line); padding-top:26px; color:var(--muted); font-size:14px; max-width:66ch; }}
footer h3 {{ font-family:"IBM Plex Sans Condensed",sans-serif; font-size:17px; color:var(--text); margin:0 0 8px; }}
footer p {{ margin:0 0 14px; }}
code {{ font-family:"IBM Plex Mono",monospace; font-size:.9em; background:var(--surface-2); border:1px solid var(--line); border-radius:4px; padding:1px 5px; }}
@media (max-width:640px) {{
  .rmeta .plat {{ display:none; }}
  .note {{ padding-left:0; }}
  .phead, .prow {{ grid-template-columns:auto 1fr; }}
  .pcount {{ grid-column:2; }}
}}
@media (prefers-reduced-motion:reduce) {{ * {{ transition:none !important; }} }}
</style>

<div class="bar"><div class="barin">
  <span class="barname">117 Problems</span>
  <span class="track"><span class="fill" id="fill"></span></span>
  <span class="tally"><b id="ndone">0</b> / {total}</span>
  <button class="reset" id="reset">Reset</button>
</div></div>

<div class="wrap">
<header class="mast">
  <p class="eyebrow">competitive-programming-notebook</p>
  <h1>Rebuild the fundamentals, one pattern at a time.</h1>
  <p class="lede">Every problem you have solved since 2023, re-ordered so each phase installs one idea the next depends on. <strong>Pattern-first, not number-first.</strong> Tick a box when you have solved it without reading past the card's Task section.</p>
</header>

<nav class="index">{nav}</nav>

<section class="prio">
  <h2>If you only do eighteen</h2>
  <p>Fourteen of these you solved before, but in a way that sidestepped what the problem was teaching. Four you never solved at all. This is the highest-value work in the repository.</p>
  <ul class="plist">{prio_rows}</ul>
</section>

{secs}

<footer>
  <h3>Using the Review line</h3>
  <p>Every card ends with <code>last: never &nbsp; confidence: 0/5</code>. Set the date and a confidence when you solve it. Revisit anything at 3 or below after a week, anything at 1 or 2 after two days. That is the whole system — the cards exist so a revisit costs two minutes instead of twenty.</p>
  <p>A problem you re-solve cold is worth more than three you read the solution to.</p>
  <h3>One caveat</h3>
  <p>This archive is interview-style DSA, not competitive programming. The two share fundamentals and diverge after that — contests want speed under pressure, and topics barely represented here. There is not a single graph traversal in these 117 problems.</p>
  <p>So run a second track in parallel: Codeforces Div. 2 A and B, on the clock, starting now rather than after Phase 14. This repository builds the foundation. Contests build the thing you actually said you wanted.</p>
</footer>
</div>

<script>
(function () {{
  var KEY = "cpn-roadmap-v1";
  var boxes = Array.prototype.slice.call(document.querySelectorAll('input[type=checkbox]'));
  var state = {{}};
  try {{ state = JSON.parse(localStorage.getItem(KEY) || "{{}}") || {{}}; }} catch (e) {{ state = {{}}; }}

  function save() {{
    try {{ localStorage.setItem(KEY, JSON.stringify(state)); }} catch (e) {{}}
  }}
  function paint() {{
    var done = 0;
    boxes.forEach(function (b) {{ if (b.checked) done++; }});
    document.getElementById("ndone").textContent = done;
    document.getElementById("fill").style.width = (done / boxes.length * 100) + "%";
    document.querySelectorAll(".phase").forEach(function (sec, i) {{
      var bs = sec.querySelectorAll('input[type=checkbox]');
      var d = 0;
      bs.forEach(function (b) {{ if (b.checked) d++; }});
      var txt = d + "/" + bs.length;
      sec.querySelector('.pcount').textContent = txt;
      var nc = document.querySelector('.navcount[data-phase="' + i + '"]');
      if (nc) {{ nc.textContent = txt; nc.style.color = (d === bs.length) ? "var(--done)" : ""; }}
    }});
  }}
  boxes.forEach(function (b) {{
    if (state[b.dataset.key]) b.checked = true;
    b.addEventListener("change", function () {{
      if (b.checked) state[b.dataset.key] = 1; else delete state[b.dataset.key];
      save(); paint();
    }});
  }});
  document.getElementById("reset").addEventListener("click", function () {{
    boxes.forEach(function (b) {{ b.checked = false; }});
    state = {{}}; save(); paint();
  }});
  paint();
}})();
</script>
'''
out = R / "roadmap.html"
out.write_text(HTML)
print("wrote", out, len(HTML), "bytes")
print("phases:", len(phases), "problems:", total, "priority:", len(prio))
