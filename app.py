import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av

st.set_page_config(page_title="Operator Entry System", layout="centered")
st.title("🚧 Operator Entry System")
st.markdown("#### Smart Safety Check Before Login")

# Apply custom theme
st.markdown("""
    <style>
        .main { background-color: #1e1e1e; color: white; }
        .stButton>button { background-color: #FFCC00; color: black; font-weight: bold; }
        .stTextInput>div>div>input, .stSelectbox>div>div>div>div { font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

if 'seatbelt_pass' not in st.session_state:
    st.session_state.seatbelt_pass = False

# Webcam Seatbelt Placeholder
st.subheader("Step 1: Webcam Check (Seatbelt Detection)")

class VideoProcessor:
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        return av.VideoFrame.from_ndarray(img, format="bgr24")

webrtc_streamer(key="webcam", video_processor_factory=VideoProcessor)

if st.button("Simulate Seatbelt Detection"):
    st.success("Seatbelt detected. Proceed to operator login.")
    st.session_state.seatbelt_pass = True

# Login Methods
if st.session_state.seatbelt_pass:
    st.subheader("Step 2: Operator Login")
    method = st.selectbox("Select Login Method", ["Enter Operator ID", "Scan Fingerprint (Simulated)", "Scan Barcode (Simulated)", "Face Recognition (Coming Soon)"])

    if method == "Enter Operator ID":
        op_id = st.text_input("Enter Operator ID")
        if st.button("Login with ID"):
            if op_id.strip() != "":
                st.success(f"✅ Welcome, Operator {op_id}")
                st.session_state.operator_logged_in = True
    elif method == "Scan Fingerprint (Simulated)":
        if st.button("Simulate Fingerprint Scan"):
            st.success("✅ Fingerprint matched. Access granted.")
            st.session_state.operator_logged_in = True
    elif method == "Scan Barcode (Simulated)":
        if st.button("Simulate Barcode Scan"):
            st.success("✅ Barcode verified. Access granted.")
            st.session_state.operator_logged_in = True
    elif method == "Face Recognition (Coming Soon)":
        st.info("Face recognition integration is under development.")
else:
    st.warning("Please perform seatbelt check before accessing login.")
