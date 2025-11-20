import streamlit as st
import json
from PIL import Image

config = json.load(open("app/config.json", "r", encoding="utf-8"))

#st.title("🏠 الصفحة الرئيسية")
st.write(config["about_me"])

st.header("📜 Certificates")

st.image("app/assets/certificates/cert1.png", width=400)
st.image("app/assets/certificates/cert2.png", width=400)
st.image("app/assets/certificates/cert3.png", width=400)
st.image("app/assets/certificates/cert4.png", width=400)

st.image("app/assets/certificates/cert5.png", width=400)
