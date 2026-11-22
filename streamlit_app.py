"""
Entry point for the CV website.

Run locally:   streamlit run streamlit_app.py
Edit content:  cv_data.py
"""

import streamlit as st

from cv_data import PROFILE
from ui import footer, inject_css, sidebar

st.set_page_config(
    page_title=f"{PROFILE['name']} | CV",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

pages = [
    st.Page("views/home.py", title="Home", icon=":material/home:", default=True),
    st.Page("views/experience.py", title="Experience", icon=":material/work:"),
    st.Page("views/accomplishments.py", title="Accomplishments", icon=":material/trophy:"),
    st.Page("views/education.py", title="Education & Research", icon=":material/school:"),
    st.Page("views/projects.py", title="Projects", icon=":material/construction:"),
]

nav = st.navigation(pages)
inject_css()
sidebar()
nav.run()
footer()
