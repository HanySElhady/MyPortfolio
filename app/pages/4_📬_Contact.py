import streamlit as st
import json

config = json.load(open("app/config.json", "r", encoding="utf-8"))

st.title("📬 Contact me")

st.write("### 📧 Email")
st.write(config["email"])

st.write("### 📧 Linkedin")
st.write(config["linkedin"])

st.write("### 📞 Phone")
st.write(config["phone"])

st.write("### 📍 Location")
st.write(config["location"])

