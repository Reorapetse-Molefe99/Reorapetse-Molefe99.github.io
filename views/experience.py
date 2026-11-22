import streamlit as st

from cv_data import EXPERIENCE
from ui import chips, e, html, page_header

page_header(
    "Professional experience",
    "Nearly five years across banking, credit risk, collections analytics and data science.",
)

companies = list(dict.fromkeys(job["company"] for job in EXPERIENCE))
selected = st.pills(
    "Filter by organisation",
    options=companies,
    selection_mode="multi",
    default=companies,
)

jobs = [job for job in EXPERIENCE if job["company"] in (selected or companies)]

for job in jobs:
    badge = ' <span class="badge badge-current">Current</span>' if job["current"] else ""
    with st.container(border=True):
        html(f"""
        <div class="card-head">
          <div class="card-title">{e(job["role"])}{badge}</div>
          <div class="date">{e(job["start"])} – {e(job["end"])}</div>
        </div>
        <div class="card-sub">{e(job["company"])} | {e(job["team"])}</div>
        <p style="margin:.45rem 0 .2rem">{e(job["summary"])}</p>
        """)
        with st.expander("Responsibilities and impact", expanded=job["current"]):
            for point in job["highlights"]:
                st.markdown(f"- {point}")
            html(f'<div style="margin-top:.6rem">{chips(job["skills"])}</div>')
