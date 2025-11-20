import streamlit as st
import json

config = json.load(open("config.json", "r", encoding="utf-8"))

st.title("👨🏻‍🎓 Education")


education_data = [
    {
        "institution": "Modern Academy Maadi",
        "degree": "Bachelor's Degree, Computational Science",
        "period": "May 1999 - Jul 2004",
        "grade": "Very Good",
        "notes": (
            "Modern Academies for computer science sponsored by UDC District Columbia University. "
            "General point grade: Good. Final graduation project grade: Excellent. "
            "Fifth year (final year) grade: Very Good. All study in English with the original MOC."
        )
    },
    {
        "institution": "EDS",
        "degree": "Data Science",
        "notes": ""
    },
    {
        "institution": "Udacity",
        "degree": "Nanodegree, Analysis and Functional Analysis",
        "notes": ""
    },
    {
        "institution": "Udacity",
        "degree": "Nanodegree, Data Processing Technology/Technician",
        "notes": ""
    },
    {
        "institution": "Udemy Alumni",
        "degree": "Certificate of Undergraduate Studies, Project Management",
        "notes": ""
    }
]

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