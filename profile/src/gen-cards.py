import pathlib
HERE = pathlib.Path(__file__).parent
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Geist:wght@500;600&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@500&display=block" rel="stylesheet">'
ICON = {
 "bolt": '<path d="M13 3L5 14h6l-1 7 8-11h-6l1-7z"/>',
 "route": '<circle cx="6" cy="6" r="2.5"/><circle cx="18" cy="18" r="2.5"/><path d="M8.5 6H14a4 4 0 0 1 0 8h-4a4 4 0 0 0 0 8h5.5"/>',
 "gauge": '<path d="M4 15a8 8 0 0 1 16 0"/><path d="M12 15l4-5"/><path d="M4 19h16"/>',
 "hub": '<circle cx="12" cy="12" r="3"/><circle cx="5" cy="6" r="2"/><circle cx="19" cy="6" r="2"/><circle cx="12" cy="20" r="2"/><path d="M6.7 7.3l3.3 3M17.3 7.3l-3.3 3M12 15v3"/>',
 "shield": '<path d="M12 3l7 3v5c0 5-3.5 8.5-7 10-3.5-1.5-7-5-7-10V6l7-3z"/><path d="M9.5 12l2 2 3.5-4"/>',
 "doc": '<rect x="5" y="4" width="14" height="16" rx="2"/><path d="M9 9h6"/><path d="M9 13h6"/><path d="M9 17h4"/>',
 "brain": '<path d="M9 4a3 3 0 0 0-3 3v1a3 3 0 0 0-1 5.5V15a3 3 0 0 0 3 3h1"/><path d="M15 4a3 3 0 0 1 3 3v1a3 3 0 0 1 1 5.5V15a3 3 0 0 1-3 3h-1"/><path d="M12 4v16"/>',
 "db": '<ellipse cx="12" cy="6" rx="7" ry="3"/><path d="M5 6v12c0 1.7 3.1 3 7 3s7-1.3 7-3V6"/><path d="M5 12c0 1.7 3.1 3 7 3s7-1.3 7-3"/>',
 "off": '<circle cx="12" cy="12" r="8.5"/><path d="M8 12h8"/>',
}
def card(name, theme, brand, title, sub, rows, foot):
    dark = theme != "light"
    if dark:
        acc = "#00e599" if theme == "dark" else "#c084fc"
        glow = "rgba(0,229,153,.25)" if theme == "dark" else "rgba(192,132,252,.25)"
        css = f""":root{{--bg:#060b18;--card:#0f1629;--ink:#f8fafc;--text:#e2e8f0;--muted:#94a3b8;--dim:#7e8ca6;--line:rgba(148,163,184,.14);--acc:{acc};--glow:{glow}}}
.card{{background:var(--bg);border:1px solid var(--line)}}
.scene{{background:radial-gradient(ellipse 80% 60% at 50% 18%,{glow.replace('.25','.14')},transparent 70%)}}
.ico{{border:1px solid var(--line);background:rgba(255,255,255,.03);color:var(--acc)}}
.foot{{background:rgba(255,255,255,.03);border-top:1px solid var(--line);color:var(--muted)}}
.mark img{{filter:drop-shadow(0 0 8px var(--glow)) drop-shadow(0 0 20px var(--glow))}}"""
    else:
        css = """:root{--bg:#FFFFFF;--card:#FFFFFF;--ink:#060B18;--text:#3D4C6E;--muted:#64748B;--dim:#8A95AB;--line:#E3E9F4;--acc:#00754E;--glow:rgba(0,229,153,.10)}
.card{background:var(--bg);border:1px solid var(--line)}
.scene{background:radial-gradient(ellipse 80% 60% at 50% 18%,rgba(0,229,153,.12),transparent 70%)}
.ico{border:1px solid #CFD9EB;background:#fff;color:var(--acc)}
.foot{background:#F5F7FC;border-top:1px solid var(--line);color:var(--muted)}
.mark img{filter:invert(1) brightness(0)}"""
    rows_html = "".join(f'<div class="row"><div class="ico"><svg viewBox="0 0 24 24">{ICON[i]}</svg></div><p>{t}</p></div>' for i, t in rows)
    html = f"""<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>
{css}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:420px;height:520px;background:transparent}}
.card{{position:relative;width:420px;height:520px;border-radius:20px;overflow:hidden;font-family:'Inter',sans-serif;color:var(--text);isolation:isolate}}
.scene{{position:absolute;inset:0;z-index:-1}}
.brand{{position:absolute;left:30px;top:30px;display:flex;align-items:center;gap:12px}}
.mark{{width:44px;height:44px;display:flex;align-items:center;justify-content:center}}
.mark img{{width:42px;height:42px}}
.mark.word{{border-radius:12px;border:1px solid var(--line);font-family:'JetBrains Mono',monospace;font-weight:500;font-size:15px;color:var(--acc);letter-spacing:.02em}}
.brand b{{display:block;font-weight:700;font-size:19px;color:var(--ink);line-height:1}}
.brand small{{display:block;margin-top:5px;font-family:'JetBrains Mono',monospace;font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--dim)}}
h1{{position:absolute;left:30px;top:106px;font-family:'Geist',sans-serif;font-weight:600;font-size:46px;letter-spacing:-.025em;line-height:1;color:var(--ink)}}
h1 em{{font-style:normal;color:var(--acc)}}
.sub{{position:absolute;left:30px;right:30px;top:166px;font-size:15.5px;line-height:1.45;color:var(--muted)}}
.rows{{position:absolute;left:30px;right:30px;top:232px;display:flex;flex-direction:column;gap:18px}}
.row{{display:flex;align-items:center;gap:14px}}
.ico{{flex:none;width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center}}
.ico svg{{width:20px;height:20px;fill:none;stroke:currentColor;stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round}}
.row p{{font-size:15px;line-height:1.35;color:var(--text)}}
.foot{{position:absolute;left:0;right:0;bottom:0;height:52px;display:flex;align-items:center;justify-content:center;font-size:13px;text-align:center;padding:0 20px}}
</style></head><body><div class="card"><div class="scene"></div>
<div class="brand">{brand}</div>
<h1>{title}</h1>
<p class="sub">{sub}</p>
<div class="rows">{rows_html}</div>
<div class="foot">{foot}</div>
</div></body></html>"""
    (HERE / f"card-{name}.html").write_text(html)

card("rtk", "dark",
 '<div class="mark"><img src="helmet.webp" alt=""></div><div><b>RTK</b><small>Free and open source</small></div>',
 'Less <em>cost.</em>', 'The cost reduction engine for AI coding agents.',
 [("bolt", "Install &amp; forget: up to 90% less command output"), ("route", "Pipelines: delegate reads, compress more, clean API traffic"), ("gauge", "<code>rtk gain</code> shows what you saved")],
 'Claude Code, Cursor, Codex, Gemini CLI and 14 more')
card("pro", "light",
 '<div class="mark"><img src="helmet.webp" alt=""></div><div><b>RTK Pro</b><small>AI control layer</small></div>',
 'Stay in <em>control.</em>', 'The control layer for every AI agent, for one developer or the whole company.',
 [("hub", "One gateway for every AI call, whichever provider"), ("shield", "Spend and budgets, Shield, policies"), ("doc", "Team catalog and audit log")],
 'On each developer\'s machine. No secret value leaves it.')
card("icm", "violet",
 '<div class="mark word">icm</div><div><b>ICM</b><small>Free and open source</small></div>',
 'A <em>memory.</em>', 'Long-term memory for AI coding agents, shared across your tools.',
 [("brain", "What one agent learns, the next session knows"), ("db", "One binary, one SQLite file, MCP native"), ("off", "No LLM call to store or recall a memory")],
 'Shared across your agents over MCP')
print("3 cards written")
