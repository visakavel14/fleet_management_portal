import streamlit as st

st.set_page_config(page_title="Incident Logging")
st.title("📝 Report an Incident")

incident_type = st.selectbox("Incident Type", ["Mechanical Issue", "Near Miss", "Personal Injury", "Other"])
place = st.text_input("Location")
date = st.date_input("Date")
time = st.time_input("Time")
description = st.text_area("Description")
image = st.file_uploader("Upload Photo", type=["png", "jpg", "jpeg"])

if st.button("Submit Report"):
    st.success("✅ Incident submitted successfully!")
