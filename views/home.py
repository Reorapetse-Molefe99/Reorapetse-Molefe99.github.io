import streamlit as st

from cv_data import EXPERIENCE, HEADLINE_METRICS, SKILLS, SUMMARY
from ui import chips, e, hero, html, metric_grid, metric_tile, page_header

hero()

st.markdown(SUMMARY)
st.write("")

metric_grid([metric_tile(value, label) for value, label in HEADLINE_METRICS])

left, right = st.columns([3, 2], gap="large")

with left:
    page_header("Current roles")
    for job in (j for j in EXPERIENCE if j["current"]):
        html(f"""
        <div class="card">
          <div class="card-head">
            <div class="card-title">{e(job["role"])}</div>
            <div class="date">{e(job["start"])} – {e(job["end"])}</div>
          </div>
          <div class="card-sub">{e(job["company"])} | {e(job["team"])}</div>
          <p style="margin:.6rem 0 0">{e(job["summary"])}</p>
        </div>
        """)
    st.page_link("views/experience.py", label="See full experience", icon=":material/arrow_forward:")

with right:
    page_header("Technical skills")
    for group, items in SKILLS.items():
        html(f'<div style="font-weight:700;color:var(--navy);margin-top:.5rem">{e(group)}</div>'
             f'<div>{chips(items)}</div>')
