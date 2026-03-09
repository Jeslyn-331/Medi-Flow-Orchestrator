import streamlit as st
import base64
import os
import time

st.set_page_config(
    page_title="M-FLO | Dashboard", 
    page_icon="⚕️", 
    layout="wide"
)

def get_base64(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

logo_b64 = get_base64("logo_medical.png")
user_name = "Dr. John Doe" 

# --- INITIALIZE SESSION STATES ---
if "auth" not in st.session_state:
    st.session_state.auth = False
if "current_page" not in st.session_state:
    st.session_state.current_page = "Homepage"

# --- UI STYLING ---
st.markdown(f"""
    <style>
    .stApp {{ background: radial-gradient(circle at top right, #F0FFF4, #FFFFFF) !important; }}

    /* 1. FIXED TOP BAR */
    .top-bar {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 40px;
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(12px);
        border-bottom: 1px solid rgba(147, 197, 114, 0.2);
        position: fixed;
        top: 0; left: 0; right: 0;
        z-index: 1000;
        height: 70px;
    }}
    .top-logo-img {{ height: 40px; }}
    .search-wrapper {{ flex-grow: 1; display: flex; justify-content: center; margin: 0 60px; }}
    .search-input {{
        width: 100%; max-width: 600px; padding: 12px 25px;
        border-radius: 20px; border: 1.5px solid #E0E0E0; background: #F9F9F9;
        transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }}
    .search-input:focus {{ border-color: #93C572; box-shadow: 0 0 15px rgba(147, 197, 114, 0.2); outline: none; }}
    .user-tag {{ color: #124D41; font-weight: 700; }}

    /* 2. BOUNCY ANIMATIONS */
    @keyframes springPop {{
        0% {{ opacity: 0; transform: scale(0.8) translateY(50px); }}
        70% {{ transform: scale(1.04) translateY(-10px); }}
        100% {{ opacity: 1; transform: scale(1) translateY(0); }}
    }}
    .pop-in {{ animation: springPop 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) forwards; }}

    /* 3. CARDS & SIDEBAR */
    div[data-testid="stVerticalBlockBorderWrapper"] {{
        background: rgba(255, 255, 255, 0.8) !important;
        backdrop-filter: blur(10px) !important;
        border-radius: 30px !important;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.03) !important;
    }}
    section[data-testid="stSidebar"] {{ padding-top: 80px; }}
    .dashboard-anchor {{ margin-top: 80px; }}

    /* 4. LOGIN CARD */
    .login-card {{
        border: 3px solid #93C572; border-radius: 40px; padding: 50px;
        background-color: #F9FFF9; text-align: center; max-width: 500px; margin: auto;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- ROUTING LOGIC ---
if not st.session_state.auth:
    # --- LOGIN PAGE ---
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    logo_html = f'<div style="display: flex; justify-content: center;"><img src="data:image/png;base64,{logo_b64}" style="width:280px;"></div>' if logo_b64 else ""
    st.markdown(f'<div class="login-card">{logo_html}<div style="color: #93C572; font-weight: 800; font-size: 28px; margin-top: 10px;">67+2 PODCAST</div><div style="color: #124D41; font-size: 55px; font-weight: 900; margin: 0;">M-FLO</div><hr style="border-top: 2px solid #93C572; opacity: 0.2; margin: 30px 0;"></div>', unsafe_allow_html=True)

    _, col2, _ = st.columns([1, 1.8, 1])
    with col2:
        u = st.text_input("Physician ID", placeholder="Enter ID")
        p = st.text_input("Security Key", type="password")
        if st.button("AUTHENTICATE SYSTEM"):
            if u == "doctor1" and p == "mediflow2026":
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("Invalid Credentials")

else:
    # --- TOP BAR ---
    logo_img = f'data:image/png;base64,{logo_b64}' if logo_b64 else ""
    st.markdown(f'<div class="top-bar"><img src="{logo_img}" class="top-logo-img"><div class="search-wrapper"><input type="text" class="search-input" placeholder="Search..."></div><div class="user-tag">Hello, <b>{user_name}</b></div></div><div class="dashboard-anchor"></div>', unsafe_allow_html=True)

    # --- SIDEBAR NAVIGATION ---
    with st.sidebar:
        if st.button("🏠 Homepage", use_container_width=True):
            st.session_state.current_page = "Homepage"
            st.rerun()
        if st.button("💬 Messages", use_container_width=True):
            st.session_state.current_page = "Messages"
            st.rerun()
        if st.button("👤 Patients", use_container_width=True):
            st.session_state.current_page = "Patients"
            st.rerun()
        if st.button("📅 Reservation", use_container_width=True):
            st.session_state.current_page = "Reservation"
            st.rerun()
        if st.button("🤝 Community", use_container_width=True):
            st.session_state.current_page = "Community"
            st.rerun()
        st.divider()
        if st.button("Logout"):
            st.session_state.auth = False
            st.rerun()

    # --- PAGE CONTENT ROUTER ---
    
    # 1. HOMEPAGE
    if st.session_state.current_page == "Homepage":
        st.markdown('<div class="pop-in"><h1 style="color: #124D41;">Welcome Back, Doctor</h1></div>', unsafe_allow_html=True)
        with st.container(border=True):
            st.write("### Today's Focus")
            st.info("You have 4 reservations pending and 2 unread messages.")

    # 2. COMMUNITY (REDDIT STYLE)
    elif st.session_state.current_page == "Community":
        st.markdown('<div class="pop-in"><h1 style="color: #124D41;">Medical Community</h1></div>', unsafe_allow_html=True)
        
        # Post 1
        with st.container(border=True):
            st.markdown("### **u/Cardio_Expert**")
            st.write("Best practices for post-op hypertension in diabetic patients?")
            col1, col2, col3 = st.columns([1,1,6])
            with col1: st.button("🔼 142")
            with col2: st.button("💬 24")
            st.divider()
        
        # Post 2
        with st.container(border=True):
            st.markdown("### **u/Neuro_MD**")
            st.write("Reviewing the new clinical trial data for M-FLO v2.1 integration.")
            col1, col2, col3 = st.columns([1,1,6])
            with col1: st.button("🔼 89")
            with col2: st.button("💬 12")

    # 3. OTHER PAGES (Placeholders)
    else:
        st.markdown(f'<div class="pop-in"><h1 style="color: #124D41;">{st.session_state.current_page}</h1></div>', unsafe_allow_html=True)
        st.write("This section is under development.")
