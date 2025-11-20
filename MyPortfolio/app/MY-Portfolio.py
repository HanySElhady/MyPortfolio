import streamlit as st
import json
from PIL import Image
from pathlib import Path

# ---------- Page Setup ----------
st.set_page_config(page_title="Portfolio", layout="wide")

# ---------- Load Config ----------
config_path = Path("app/config.json")
if not config_path.exists():
    st.error("config.json not found!")
    st.stop()

config = json.load(open(config_path, "r", encoding="utf-8"))

# ---------- SessionState for Theme ----------
if "theme" not in st.session_state:
    st.session_state.theme = "dark"

theme = st.session_state.theme

# ---------- Load CSS ----------
# Theme CSS
theme_file = Path(f"assets/themes/{theme}.css")
if theme_file.exists():
    with open(theme_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# General CSS
custom_css = Path("assets/custom.css")
if custom_css.exists():
    with open(custom_css) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------- Profile Section ----------
profile_pic_path = Path("assets/profile.jpg")
if profile_pic_path.exists():
    profile_pic = Image.open(profile_pic_path)
else:
    profile_pic = None

col1, col2 = st.columns([1, 3])
with col1:
    if profile_pic:
        st.image(profile_pic, width=200)
with col2:
    st.markdown(f"<div class='big-title' style='color:black;'>{config['name']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='sub-title'>{config['title']}</div>", unsafe_allow_html=True)
    st.write(config.get("description", ""))




# ---------- Sidebar Navigation ----------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Home", "Skills","Education", "Projects", "Contact"])

# ---------- Pages ----------
if page == "Home":
    st.header("🎯 About ME")
    st.write(config.get("about_me", ""))

    st.subheader("📜 Certificates")
    certs_path = Path("assets/certificates")
    if certs_path.exists():
        cert_files = list(certs_path.glob("*.*"))
        for cert in cert_files:
            st.image(cert, width=600)

elif page == "Education":
    st.header("👨🏻‍🎓 Education")
    for skill in config.get("education", []):
        st.markdown(f"- ✅ **{skill}**")

elif page == "Skills":
    st.header("📊 Skills")
    for skill in config.get("skills", []):
        st.markdown(f"- ✅ **{skill}**")



elif page == "Projects":
    st.header("💼 Projects")
    for proj in config.get("projects", []):
        st.subheader(proj.get("name", ""))
        st.write(proj.get("description", ""))
        if proj.get("link"):
            st.markdown(f"[🔗 رابط المشروع]({proj['link']})")
        st.write("---")

elif page == "Contact":
    st.header("📬 Contact me")
    st.write(f"### 📧 Email: {config.get('email', '')}")
    st.write(f"### 📞 Phone: {config.get('phone', '')}")
    st.write(f"###  Linked-In: {config.get('linkedin', '')}")
    st.write(f"### 📍 Location: {config.get('location', '')}")

