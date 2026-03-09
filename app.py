import streamlit as st
import os
import time

# --- 1. GLOBAL PAGE SETUP ---
st.set_page_config(page_title="M-FLO | Medi-Flow", page_icon="⚕️", layout="wide")

# --- 2. THE "MOCKUP-ACCURATE" CSS ---
st.markdown("""
    <style>
    /* 1. Force Pure White Background globally */
    .stApp { background-color: #FFFFFF !important; }
    
    /* 2. Target the Container Border (Pistachio Frame) */
    /* This styles the st.container(border=True) specifically */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        border: 2.5px solid #93C572 !important;
        border-radius: 20px !important;
        background-color: #F9FFF9 !important;
        padding: 30px !important;
        max-width: 480px !important;
        margin: auto !important;
    }

    /* 3. Force Input Boxes to be White with Dark Green Text */
    div[data-baseweb="input"], div[data-baseweb="textarea"] {
        background-color: #FFFFFF !important;
        border: 1.5px solid #93C572 !important;
        border-radius: 10px !important;
    }
    input {
        color: #124D41 !important;
        -webkit-text-fill-color: #124D41 !important;
        font-weight: 500 !important;
    }

    /* 4. Labels & M-FLO Title Styling */
    label p { 
        color: #124D41 !important; 
        font-weight: bold !important; 
        text-align: left !important; 
    }
    .mflo-header {
        color: #124D41;
        font-size: 38px;
        font-weight: 850;
        margin-bottom: -10px;
        text-align: center;
    }
    .mflo-sub {
        color: #124D41;
        font-size: 14px;
        text-align: center;
        margin-bottom: 20px;
    }

    /* 5. The Mint "Authenticate" Button */
    div.stButton > button {
        background-color: #98FFD9 !important;
        color: #124D41 !important;
        border: none !important;
        font-weight: 800 !important;
        font-size: 16px !important;
        text-transform: uppercase;
        width: 100%;
        padding: 15px;
        border-radius: 10px;
        margin-top: 10px;
    }

    /* 6. Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #F0F4F2 !important;
        border-right: 1px solid #93C572;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SESSION STATE ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# --- 4. NAVIGATION LOGIC ---

if not st.session_state.authenticated:
    # --- PAGE 1: LOGIN (CENTERED & FRAMED) ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # We use columns to force the container to stay in the center
    _, center_col, _ = st.columns([1, 1.5, 1])
    
    with center_col:
        # Everything inside this 'with' block is now framed in Pistachio
        with st.container(border=True):
            
            # 1. Logo
            if os.path.exists("logo_medical.png"):
                st.image("logo_medical.png", use_container_width=True)
            
            # 2. Text Content (Ensuring high visibility)
            st.markdown('<div class="mflo-header">M-FLO</div>', unsafe_allow_html=True)
            st.markdown('<div class="mflo-sub">Medi-Flow Orchestrator v2.1 | Secure Portal</div>', unsafe_allow_html=True)
            st.markdown("<hr style='border-top: 1.5px solid #93C572;'>", unsafe_allow_html=True)

            # 3. Interactive Inputs
            phys_id = st.text_input("Physician ID", placeholder="doctor1")
            sec_key = st.text_input("Security Key", type="password", placeholder="••••••••")
            
            # 4. Action Button
            if st.button("AUTHENTICATE SYSTEM"):
                if phys_id == "doctor1" and sec_key == "mediflow2026":
                    st.session_state.authenticated = True
                    st.rerun()
                else:
                    st.error("Invalid Security Credentials.")

            st.markdown("<p style='text-align:center; font-size:11px; color:gray; margin-top:10px;'>Auth: MD-Level Encrypted Access Only</p>", unsafe_allow_html=True)
        
        # Demo Credentials Box (outside the main frame)
        st.info("ℹ️ Demo: doctor1 / mediflow2026")

else:
    # --- PAGE 2: MAIN DASHBOARD ---
    with st.sidebar:
        if os.path.exists("logo_medical.png"):
            st.image("logo_medical.png", width=120)
        st.title("M-FLO v2.1")
        st.write("Current: **Dr. John Doe**")
        st.divider()
        if st.button("LOGOUT"):
            st.session_state.authenticated = False
            st.rerun()

    # Clinical Layout
    st.subheader("⚕️ Patient Consultation Workspace")
    c1, c2, c3 = st.columns([1, 2, 2])

    with c1:
        st.markdown("#### Patient Context")
        with st.container(border=True):
            st.write("**J. Doe** | ID: #8821")
            st.error("⚠️ Allergy: Penicillin")
            st.warning("⚠️ High Blood Pressure")

    with c2:
        st.markdown("#### Clinical Transcription")
        st.text_area("Live Audio or Physician Notes:", height=300, placeholder="Paste clinical context here...")
        if st.button("RUN INTENT ANALYSIS"):
            st.toast("Processing notes...")

    with c3:
        st.markdown("#### Generated Orders")
        with st.container(border=True):
            st.write("💊 **Pharmacy:** Amoxicillin 500mg")
            st.button("VERIFY & ROUTE", key="ord1")
