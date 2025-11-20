import streamlit as st
import json
from pathlib import Path

config = json.load(open("app/config.json", "r", encoding="utf-8"))

st.title("💼 Projects")

projects = config.get("projects", [])

# =============================
# 🌟 Custom CSS
# =============================
st.markdown("""
<style>
.project-card {
    background: #ffffff;
    border-radius: 16px;
    padding: 12px;
    margin-bottom: 20px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    transition: 0.3s ease;
}
.project-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 18px rgba(0,0,0,0.12);
}
.project-title {
    font-size: 18px;
    font-weight: 700;
    margin-top: 8px;
    margin-bottom: 4px;
    color: #2a5caa;
}
.project-desc {
    font-size: 14px;
    opacity: 0.85;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)


# =============================
# 📌 3 Column Layout
# =============================
cols = st.columns(3)

for i, proj in enumerate(projects):
    col = cols[i % 3]

    with col:
        st.markdown("<div class='project-card'>", unsafe_allow_html=True)

        

        # 🔹 Title
        st.markdown(
            f"<div class='project-title'>{proj['name']}</div>",
            unsafe_allow_html=True
        )

        # 🔹 Description
        st.markdown(
            f"<div class='project-desc'>{proj.get('description', '')}</div>",
            unsafe_allow_html=True
        )

        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # 🔹 Multiple Images
        if proj.get("images"):
            for img in proj["images"]:
                img_path = Path(img)
                if img_path.exists():

                    st.image(img_path, use_container_width=True)
