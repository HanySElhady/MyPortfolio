import streamlit as st
import json

config = json.load(open("app/config.json", "r", encoding="utf-8"))

st.title("📊 Skills")

for skill in config["skills"]:
    st.markdown(f"- ✅ **{skill}**")

