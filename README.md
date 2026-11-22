# Reorapetse Molefe — CV Website

A personal CV website built in Python with [Streamlit](https://streamlit.io).

Pages: **Home · Experience · Accomplishments · Education & Research · Projects**

## Project structure

```
cv-website/
├── streamlit_app.py        # Entry point: page config + navigation
├── cv_data.py              # ALL website content (edit this to update the site)
├── ui.py                   # Shared styling (CSS) and small HTML components
├── views/
│   ├── home.py
│   ├── experience.py
│   ├── accomplishments.py
│   ├── education.py        # Includes the master's research summary
│   └── projects.py
├── assets/
│   └── Reorapetse_Molefe_CV.pdf   # Served by the "Download CV" button
├── .streamlit/config.toml  # Theme colours
└── requirements.txt
```

## Run it locally

```bash
cd ~/Documents/cv-website
python3 -m venv .venv            # first time only
source .venv/bin/activate
pip install -r requirements.txt  # first time only
streamlit run streamlit_app.py
```

The site opens at http://localhost:8501. It reloads automatically when you save a file.

## Common edits

| To change… | Edit |
|---|---|
| Wording of any role, bullet or summary | `cv_data.py` → `EXPERIENCE`, `SUMMARY` |
| Headline numbers on the home page | `cv_data.py` → `HEADLINE_METRICS` |
| Accomplishment tiles | `cv_data.py` → each role's `achievements` list |
| Research summary | `cv_data.py` → `RESEARCH` |
| Add a project | `cv_data.py` → append to `PROJECTS` (set `status` to `"Completed"`, add `link`) |
| Show phone number / add LinkedIn | `cv_data.py` → `SHOW_PHONE`, `PROFILE["linkedin"]` |
| Update the downloadable CV | Replace `assets/Reorapetse_Molefe_CV.pdf` (keep the same file name) |
| Colours / fonts | `ui.py` (CSS) and `.streamlit/config.toml` |

## Publish changes

```bash
git add .
git commit -m "Describe your change"
git push
```

Streamlit Community Cloud redeploys automatically within about a minute of each push.

## Deploy (first time)

1. Create a free GitHub account at https://github.com/signup.
2. Create a new **empty** repository named `cv-website` (no README, no .gitignore).
3. Connect this folder to it and push:
   ```bash
   git remote add origin https://github.com/<your-username>/cv-website.git
   git push -u origin main
   ```
   When asked for a password, use a GitHub **personal access token**, not your account
   password (GitHub → Settings → Developer settings → Personal access tokens). Alternatively,
   install the GitHub CLI (`brew install gh`, then `gh auth login`) and it handles this for you.
4. Go to https://share.streamlit.io, sign in with GitHub, click **Create app**, choose
   the `cv-website` repo, branch `main`, main file `streamlit_app.py`, and pick a custom
   subdomain (e.g. `reorapetse-molefe.streamlit.app`). Click **Deploy**.

Apps on the free tier go to sleep after a period with no visitors; the first visitor
afterwards waits a few seconds for it to wake up.
