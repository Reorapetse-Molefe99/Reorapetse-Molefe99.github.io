import streamlit as st

from cv_data import AFFILIATIONS, EDUCATION, RESEARCH
from ui import chips, e, html, page_header

page_header("Education", "Actuarial science foundation, with a master's in financial engineering.")

for edu in EDUCATION:
    note = f'<p style="margin:.4rem 0 0">{e(edu["note"])}</p>' if edu["note"] else ""
    html(f"""
    <div class="card">
      <div class="card-head">
        <div class="card-title">{e(edu["degree"])}</div>
        <div class="date">{e(edu["period"])}</div>
      </div>
      <div class="card-sub">{e(edu["institution"])}</div>
      {note}
    </div>
    """)

st.write("")
page_header(
    "Master's research",
    "Minor dissertation, BCom Master Financial Engineering, University of Johannesburg",
)

html(f"""
<div class="card" style="border-left:6px solid var(--teal)">
  <div class="card-title" style="font-size:1.25rem">{e(RESEARCH["title"])}</div>
  <div class="card-sub" style="margin:.3rem 0 .6rem">Supervisors: {e(RESEARCH["supervisors"])}</div>
  <div>{chips(RESEARCH["keywords"])}</div>
</div>
""")

tab_overview, tab_method, tab_findings, tab_next = st.tabs(
    ["The problem", "Approach", "Key findings", "Future research"]
)

with tab_overview:
    st.markdown(RESEARCH["problem"])
    st.markdown(
        "**Research question in one line:** if ESG information is treated as *ambiguity* "
        "rather than *risk*, do the resulting portfolios become more sustainable, and does "
        "that cost or improve financial performance, especially when climate policy is "
        "uncertain?"
    )

with tab_method:
    for step in RESEARCH["approach"]:
        st.markdown(f"- {step}")

with tab_findings:
    findings = RESEARCH["findings"]
    for start in range(0, len(findings), 2):
        cols = st.columns(2)
        for col, (head, body) in zip(cols, findings[start:start + 2]):
            with col:
                html(f'<div class="finding"><h4>{e(head)}</h4><p>{e(body)}</p></div>')
    html(f'<div class="callout"><strong>Bottom line:</strong> {e(RESEARCH["conclusion"])}</div>')

with tab_next:
    for item in RESEARCH["future_work"]:
        st.markdown(f"- {item}")

st.write("")
page_header("Professional affiliation")
for a in AFFILIATIONS:
    html(f'<div class="card">{e(a)}</div>')
