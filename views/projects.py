import streamlit as st

from cv_data import PROJECTS
from ui import chips, e, html, page_header

page_header(
    "Projects",
    "Selected projects. Several are still in progress; write-ups, code and results will be "
    "added as each one is completed.",
)

st.info(
    "This section is a work in progress. Completed projects will be added soon.",
    icon=":material/construction:",
)

BADGES = {"In progress": "badge-progress", "Completed": "badge-done"}

for project in PROJECTS:
    badge_cls = BADGES.get(project["status"], "badge-progress")
    link = (f'<p style="margin:.6rem 0 0"><a href="{e(project["link"])}" target="_blank">'
            f'View project →</a></p>') if project.get("link") else ""
    html(f"""
    <div class="card">
      <div class="card-head">
        <div class="card-title">{e(project["name"])}
          <span class="badge {badge_cls}">{e(project["status"])}</span></div>
        <div class="date">{e(project["period"])}</div>
      </div>
      <div class="card-sub">{e(project["client"])}</div>
      <p style="margin:.6rem 0">{e(project["description"])}</p>
      <div>{chips(project["stack"])}</div>
      {link}
    </div>
    """)
    if project.get("image"):
        st.image(project["image"], use_container_width=True)

html("""
<div class="card" style="border-style:dashed;text-align:center;color:var(--muted)">
  <div class="card-title" style="color:var(--muted)">More projects coming soon</div>
  <p style="margin:.4rem 0 0">Further data science and quantitative finance projects are underway.</p>
</div>
""")
