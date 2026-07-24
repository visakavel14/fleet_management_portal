import streamlit as st
import datetime

st.set_page_config(page_title="Dashboard")
st.title("📊 Operator Dashboard")

st.subheader("Fuel Consumption")
st.metric(label="Fuel Used Today", value="38 Litres")

st.subheader("Tasks Assigned")
st.table({
    "Task": ["Transport Load A", "Deliver to Zone B"],
    "Time": ["10:00 AM", "12:30 PM"],
    "Status": ["Pending", "In Progress"]
})

st.subheader("Hazards Nearby")
st.warning("⚠ Obstacle detected at rear-left")

st.subheader("Emergency Message")
st.error("🌩 Heavy storm alert - Halt operations after 5 PM")

st.subheader("Estimate Task Completion Time")
capacity = st.number_input("Enter Load Capacity (kg)", value=1000)
fuel = st.number_input("Enter Available Fuel (litres)", value=30)
weather = st.selectbox("Weather Condition", ["Sunny", "Rainy", "Windy"])

if st.button("Predict Completion Time"):
    base_time = 30
    if weather == "Rainy":
        base_time += 15
    elif weather == "Windy":
        base_time += 5
    result = base_time + (1000 - capacity) / 100 + (40 - fuel) / 2
    st.success(f"Estimated Time: {round(result, 2)} minutes")

if st.button("Log Incident"):
    st.switch_page("pages/2_Incident_Logging.py")

st.subheader("Task Summary")
st.table({
    "Total Loads": [10],
    "Completed": [4],
    "Current Location": ["Zone B"]
})
