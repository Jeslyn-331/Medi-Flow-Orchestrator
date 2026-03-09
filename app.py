import streamlit as st
import base64
import os

# 1. PAGE CONFIG
st.set_page_config(
    page_title="M-FLO | Healthcare", 
    page_icon="⚕️", 
    layout="wide"
)

# 2. DEFINE GLOBAL VARIABLES (Fixes the NameError)
user_name = "Dr. John Doe" 

def get_base64(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

logo_b64 = get_base64("logo_medical.png")

# 3. INITIALIZE SESSION STATE
if "auth" not in st.session_state:
    st.session_state.auth = False
if "current_page" not in st.session_state:
    st.session_state.current_page = "Homepage"

# 4. REFINED PROFESSIONAL CSS
st.markdown("""
    <style>
    /* Standard Website Scaling */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        font-size: 16px !important;
        color: #124D41;
    }

    .stApp { background: #FDFDFD !important; }

    /* SEARCH BAR FIX: NO CLIPPING & PERFECT CENTERING */
    .stTextInput > div > div {
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        height: 50px !important; 
        background-color: #F4F4F4 !important;
        border-radius: 12px !important;
        border: 1.5px solid #E0E0E0 !important;
        padding: 0 !important;
    }

    .stTextInput > div > div > input {
        text-align: center !important;
        font-size: 16px !important;
        background: transparent !important;
        border: none !important;
        padding: 0 !important;
        width: 100% !important;
        height: 100% !important;
        line-height: normal !important; /* Prevents vertical cutting */
    }

    /* SIDEBAR STYLING */
    section[data-testid="stSidebar"] { width: 300px !important; }
    
    .stButton > button {
        height: 45px !important;
        font-size: 16px !important;
        border-radius: 8px !important;
        text-align: left !important;
        padding-left: 15px !important;
    }

    /* CARDS */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 15px !important;
        padding: 25px !important;
        background: white !important;
        border: 1px solid #EEE !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 5. APP LOGIC
if not st.session_state.auth:
    # --- LOGIN PAGE ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    logo_html = f'<img src="data:image/png;base64,{logo_b64}" style="width:200px;">' if logo_b64 else "<h2>M-FLO</h2>"
    
    with st.container(border=True):
        st.markdown(f"<div style='text-align:center;'>{logo_html}</div>", unsafe_allow_html=True)
        u = st.text_input("Physician ID")
        p = st.text_input("Security Key", type="password")
        if st.button("Sign In", use_container_width=True):
            if u == "doctor1" and p == "mediflow2026":
                st.session_state.auth = True
                st.rerun()
else:
    # --- TOP NAV ---
    t1, t2, t3 = st.columns([1, 2, 1])
    with t2:
        # Centered Search Bar
        st.text_input("search", placeholder="Search patients or records...", label_visibility="collapsed", key="top_search")
    with t3:
        # Variable is now defined globally, so no NameError here
        st.markdown(f"<p style='text-align:right; font-weight:600; padding-top:10px;'>{user_name}</p>", unsafe_allow_html=True)

    # --- SIDEBAR ---
    with st.sidebar:
        if logo_b64:
            st.image(f"data:image/png;base64,{logo_b64}", width=150)
        st.markdown("### Navigation")
        if st.button("📊 Dashboard", use_container_width=True): st.session_state.current_page = "Homepage"
        if st.button("👥 Patients", use_container_width=True): st.session_state.current_page = "Patients"
        st.divider()
        if st.button("Logout", use_container_width=True):
            st.session_state.auth = False
            st.rerun()

    # --- MAIN CONTENT ---
    st.title(f"{st.session_state.current_page}")
    with st.container(border=True):
        st.write("The search bar and text scaling have been balanced for a standard website feel.")
        st.line_chart({"data": [1, 5, 2, 6, 3, 7]})
