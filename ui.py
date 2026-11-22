"""Shared styling and small HTML components used by every page."""

from html import escape
from pathlib import Path

import streamlit as st

from cv_data import PROFILE, SHOW_PHONE

ROOT = Path(__file__).parent

NAVY = "#14324F"
TEAL = "#1C8A9A"

CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700&family=Lato:wght@400;700&display=swap');

:root {{
  --navy: {NAVY};
  --teal: {TEAL};
  --teal-soft: #E3F2F4;
  --ink: #1F2933;
  --muted: #5F6B7A;
  --line: #E2E8F0;
  --card: #FFFFFF;
}}

html, body, [class*="css"], .stMarkdown, p, li {{ font-family: 'Lato', sans-serif; }}
h1, h2, h3, h4, .hero-name {{ font-family: 'Poppins', sans-serif !important; color: var(--navy); }}
.block-container {{ padding-top: 2rem; max-width: 1100px; }}

/* Hero banner */
.hero {{
  background: var(--navy); color: #fff; border-radius: 14px;
  padding: 2.2rem 2.4rem; border-left: 12px solid var(--teal); margin-bottom: 1.5rem;
}}
.hero-name {{ color: #fff !important; font-size: 2.6rem; font-weight: 700; letter-spacing: .02em;
  margin: 0; line-height: 1.1; text-transform: uppercase; }}
.hero-title {{ color: #7FD3DD; font-family: 'Poppins', sans-serif; font-size: 1.15rem; margin: .5rem 0 .9rem; }}
.hero-contact {{ color: #D8E2EC; font-size: .95rem; }}
.hero-contact a {{ color: #D8E2EC; text-decoration: none; border-bottom: 1px dotted #7FD3DD; }}
.hero-contact .sep {{ color: #7FD3DD; margin: 0 .6rem; }}

/* Page header */
.page-title {{ font-family: 'Poppins', sans-serif; color: var(--teal); text-transform: uppercase;
  font-size: 1.6rem; font-weight: 600; border-bottom: 2px solid var(--line);
  padding-bottom: .4rem; margin: .2rem 0 .4rem; }}
.page-sub {{ color: var(--muted); margin-bottom: 1.4rem; }}

/* Metric tiles */
.metric {{ background: var(--card); border: 1px solid var(--line); border-top: 4px solid var(--teal);
  border-radius: 10px; padding: 1rem 1.1rem; height: 100%; }}
.metric .value {{ font-family: 'Poppins', sans-serif; font-size: 1.7rem; font-weight: 700;
  color: var(--navy); line-height: 1.15; }}
.metric .label {{ color: var(--ink); font-weight: 700; font-size: .92rem; margin-top: .3rem; }}
.metric .detail {{ color: var(--muted); font-size: .85rem; margin-top: .35rem; }}
.metric .org {{ color: var(--teal); font-size: .78rem; font-weight: 700; text-transform: uppercase;
  letter-spacing: .04em; margin-top: .55rem; }}

/* Generic card */
.card {{ background: var(--card); border: 1px solid var(--line); border-radius: 12px;
  padding: 1.2rem 1.4rem; margin-bottom: 1rem; }}
.card-head {{ display: flex; justify-content: space-between; align-items: baseline; gap: 1rem; flex-wrap: wrap; }}
.card-title {{ font-family: 'Poppins', sans-serif; color: var(--navy); font-weight: 600; font-size: 1.1rem; }}
.card-sub {{ color: var(--muted); font-size: .92rem; }}
.date {{ color: var(--teal); font-weight: 700; font-size: .9rem; white-space: nowrap; }}

/* Chips and badges */
.chip {{ display: inline-block; background: var(--teal-soft); color: var(--navy); border-radius: 999px;
  padding: .18rem .7rem; margin: .18rem .25rem .18rem 0; font-size: .82rem; }}
.badge {{ display: inline-block; border-radius: 6px; padding: .12rem .55rem; font-size: .75rem;
  font-weight: 700; letter-spacing: .03em; text-transform: uppercase; vertical-align: middle; }}
.badge-current {{ background: #DCFCE7; color: #166534; }}
.badge-progress {{ background: #FEF3C7; color: #92400E; }}
.badge-done {{ background: #DBEAFE; color: #1E40AF; }}

/* Timeline */
.tl {{ border-left: 3px solid var(--line); margin-left: .5rem; padding-left: 1.4rem; }}
.tl-item {{ position: relative; margin-bottom: 1.3rem; }}
.tl-item::before {{ content: ""; position: absolute; left: -1.95rem; top: .35rem; width: 14px; height: 14px;
  border-radius: 50%; background: #fff; border: 3px solid var(--teal); }}
.tl-item.current::before {{ background: var(--teal); }}

/* Finding cards on the education page */
.finding {{ background: var(--card); border: 1px solid var(--line); border-left: 4px solid var(--teal);
  border-radius: 10px; padding: .9rem 1.1rem; margin-bottom: .8rem; height: 100%; }}
.finding h4 {{ margin: 0 0 .35rem; font-size: 1rem; }}
.finding p {{ margin: 0; color: var(--ink); font-size: .92rem; }}
.callout {{ background: var(--teal-soft); border-radius: 10px; padding: 1rem 1.2rem; color: var(--navy); }}

/* Sidebar */
[data-testid="stSidebar"] {{ background: #F4F7FA; }}
.side-name {{ font-family: 'Poppins', sans-serif; font-weight: 700; color: var(--navy); font-size: 1.05rem; }}
.side-role {{ color: var(--muted); font-size: .85rem; }}

.footer {{ color: var(--muted); font-size: .8rem; text-align: center; margin-top: 3rem;
  border-top: 1px solid var(--line); padding-top: 1rem; }}

@media (max-width: 640px) {{
  .hero {{ padding: 1.5rem 1.3rem; border-left-width: 8px; }}
  .hero-name {{ font-size: 1.8rem; }}
  .hero-contact .sep {{ display: block; height: 0; overflow: hidden; }}
}}
</style>
"""


def inject_css() -> None:
    st.markdown(CSS, unsafe_allow_html=True)


def html(markup: str) -> None:
    """Render raw HTML. Lines are stripped so Markdown does not treat indents as code."""
    st.markdown("".join(line.strip() for line in markup.splitlines()), unsafe_allow_html=True)


def e(text: str) -> str:
    return escape(text, quote=True)


def contact_items() -> list[str]:
    items = [e(PROFILE["location"]),
             f'<a href="mailto:{e(PROFILE["email"])}">{e(PROFILE["email"])}</a>']
    if SHOW_PHONE and PROFILE.get("phone"):
        items.append(e(PROFILE["phone"]))
    if PROFILE.get("linkedin"):
        items.append(f'<a href="{e(PROFILE["linkedin"])}" target="_blank">LinkedIn</a>')
    if PROFILE.get("github"):
        items.append(f'<a href="{e(PROFILE["github"])}" target="_blank">GitHub</a>')
    return items


def hero() -> None:
    sep = '<span class="sep">|</span>'
    html(f"""
    <div class="hero">
      <div class="hero-name">{e(PROFILE["name"])}</div>
      <div class="hero-title">{e(PROFILE["title"])}</div>
      <div class="hero-contact">{sep.join(contact_items())}</div>
    </div>
    """)


def page_header(title: str, subtitle: str = "") -> None:
    sub = f'<div class="page-sub">{e(subtitle)}</div>' if subtitle else ""
    html(f'<div class="page-title">{e(title)}</div>{sub}')


def chips(items: list[str]) -> str:
    return "".join(f'<span class="chip">{e(i)}</span>' for i in items)


def metric_tile(value: str, label: str, detail: str = "", org: str = "") -> str:
    detail_html = f'<div class="detail">{e(detail)}</div>' if detail else ""
    org_html = f'<div class="org">{e(org)}</div>' if org else ""
    return (f'<div class="metric"><div class="value">{e(value)}</div>'
            f'<div class="label">{e(label)}</div>{detail_html}{org_html}</div>')


def metric_grid(tiles: list[str], cols: int = 4) -> None:
    for start in range(0, len(tiles), cols):
        row = st.columns(cols)
        for col, tile in zip(row, tiles[start:start + cols]):
            with col:
                html(tile)
        st.write("")


def sidebar() -> None:
    with st.sidebar:
        html(f'<div class="side-name">{e(PROFILE["name"])}</div>'
             f'<div class="side-role">{e(PROFILE["title"])}</div>')
        st.write("")
        pdf = ROOT / PROFILE["cv_pdf"]
        if pdf.exists():
            st.download_button(
                "Download CV (PDF)",
                data=pdf.read_bytes(),
                file_name=pdf.name,
                mime="application/pdf",
                use_container_width=True,
            )
        st.link_button("Email me", f"mailto:{PROFILE['email']}", use_container_width=True)


def footer() -> None:
    html(f'<div class="footer">© {e(PROFILE["name"])} · CV last updated '
         f'{e(PROFILE["cv_updated"])}</div>')
