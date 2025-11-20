import streamlit as st
import json

config = json.load(open("app/config.json", "r", encoding="utf-8"))

st.title("👨🏻‍🎓 Education")

for skill in config["education"]:
    st.markdown(f"- ✅ **{skill}**")

