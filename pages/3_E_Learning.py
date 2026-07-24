import streamlit as st

st.set_page_config(page_title="E-Learning")
st.title("🎓 E-Learning Zone")

st.subheader("Training Videos")
st.video("https://www.youtube.com/watch?v=2ZIpFytCSVc")
st.video("https://www.youtube.com/watch?v=iHhcHTlGtRs")

st.subheader("Book an Instructor")
name = st.text_input("Your Name")
date = st.date_input("Preferred Date")
time = st.time_input("Preferred Time")
purpose = st.text_area("Training Requirement")

if st.button("Book Instructor"):
    st.success("✅ Instructor booked successfully!")

st.subheader("Ask Our Chatbot")
query = st.text_input("Ask a question")
if st.button("Ask"):
    st.info("Chatbot response placeholder (LLaMA API integration)")
