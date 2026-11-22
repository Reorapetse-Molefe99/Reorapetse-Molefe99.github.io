import streamlit as st

from cv_data import EXPERIENCE
from ui import e, html, metric_grid, metric_tile, page_header

page_header(
    "Accomplishments",
    "Quantified results from each role. Strategies are tested against holdout groups "
    "wherever possible, so the impact can be measured.",
)

roles_with_results = [job for job in EXPERIENCE if job["achievements"]]

view = st.segmented_control(
    "View",
    options=["All results", "By role"],
    default="All results",
    label_visibility="collapsed",
)

if view == "By role":
    for job in roles_with_results:
        html(f"""
        <div class="card-head" style="margin-top:1rem">
          <div class="card-title">{e(job["role"])}</div>
          <div class="date">{e(job["start"])} – {e(job["end"])}</div>
        </div>
        <div class="card-sub" style="margin-bottom:.7rem">{e(job["company"])} | {e(job["team"])}</div>
        """)
        metric_grid([metric_tile(v, l, d) for v, l, d in job["achievements"]], cols=3)
else:
    tiles = [
        metric_tile(v, l, d, org=f"{job['company']} · {job['start'][-4:]}")
        for job in roles_with_results
        for v, l, d in job["achievements"]
    ]
    metric_grid(tiles, cols=3)

