import streamlit as st
import json
from PIL import Image
from pathlib import Path

education_data = [
    {
        "institution": "Modern Academy Maadi",
        "degree": "Bachelor's Degree, Computational Science",
        "period": "May 1999 - Jul 2004",
        "grade": "Very Good",
        "notes": (
            "Modern Academy for computer science sponsored by UDC District Columbia University. "
            "General point grade: Good. Final graduation project grade: Excellent. "
            "Fifth year (final year) grade: Very Good. From 1999 to 2004."
        )
    },
    {
        "institution": "Egyptian Data Scientists",
        "degree": "Data Science",
        "notes": "Machine Learning Algorithms Linear and Multilinear regression and Data classifications"
    },
    {
        "institution": "Udacity",
        "degree": "Nanodegree, Advanced Data Analysis",
        "notes": "Descriptive statistics, Data visualization, Inferential statistics, Predictive analytics"
    },
    {
        "institution": "Udacity",
        "degree": "Nanodegree, Data Engineering with Amazon Web Services",
        "notes": "Creating Data Lakes and Data Warehouses on AWS and Airflow for Data Pipelines."
    },
    {
        "institution": "Udemy Alumni",
        "degree": "Certificate of Undergraduate Studies, Project Management",
        "notes": "Data Analysis challenges using Excel, SQL,Python"
    }
]

# ---------- Page Setup ----------
st.set_page_config(page_title="HanyElhady-Portfolio", layout="wide")

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
theme_file = Path(f"app/assets/themes/{theme}.css")
if theme_file.exists():
    with open(theme_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# General CSS
custom_css = Path("app/assets/custom.css")
if custom_css.exists():
    with open(custom_css) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

import base64

# ---------- Profile Section ----------
profile_pic_path = Path("app/assets/Profile1.jpeg")

# CSS Frame for Image
st.markdown("""
<style>
.profile-frame {
    width: 220px;
    height: 220px;
    border-radius: 50%;
    overflow: hidden;
    border: 5px solid #4A90E2;
    box-shadow: 0 4px 15px rgba(0,0,0,0.25);
    margin: auto;
}
.profile-frame img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
</style>
""", unsafe_allow_html=True)

# Convert image to Base64
if profile_pic_path.exists():
    with open(profile_pic_path, "rb") as f:
        img_base64 = base64.b64encode(f.read()).decode()
else:
    st.error("Profile image not found!")
    img_base64 = None

col1, col2 = st.columns([1, 3])

with col1:
    if img_base64:
        st.markdown(
            f"""
            <div class="profile-frame">
                <img src="data:image/jpeg;base64,{img_base64}">
            </div>
            """,
            unsafe_allow_html=True
        )

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
    certs_path = Path("app/assets/certificates")
    if certs_path.exists():
        cert_files = list(certs_path.glob("*.*"))
        for cert in cert_files:
            st.image(cert, width=600)

elif page == "Education":
    st.header("🎓 Education")

    for edu in education_data:
        st.markdown(f"""
        **🏫 {edu['institution']}**

        - 🎓 *{edu.get('degree', '')}*
        {f"- 🕓 {edu.get('period', '')}" if edu.get('period') else ""}
        {f"- 📊 Grade: {edu.get('grade', '')}" if edu.get('grade') else ""}
        """)

        if edu.get("notes"):
            with st.expander("🔍 Details"):
                st.write(edu["notes"])

        st.markdown("---")


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

