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
user_name = "Dr. John Doe" # This can be dynamic based on login

# --- ADVANCED UI STYLING ---
st.markdown(f"""
    <style>
    .stApp {{ background: radial-gradient(circle at top right, #F0FFF4, #FFFFFF) !important; }}

    /* 1. TOP BAR STYLING */
    .top-bar {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 40px;
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(15px);
        border-bottom: 1px solid rgba(147, 197, 114, 0.2);
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 999;
        height: 70px;
    }}

    .top-logo {{ height: 45px; }}
    
    .search-container {{
        flex-grow: 1;
        display: flex;
        justify-content: center;
        margin: 0 50px;
    }}

    .search-bar {{
        width: 100%;
        max-width: 500px;
        padding: 10px 20px;
        border-radius: 15px;
        border: 1.5px solid #E0E0E0;
        background: #F9F9F9;
        transition: all 0.3s ease;
        outline: none;
    }}

    .search-bar:focus {{
        border-color: #93C572;
        box-shadow: 0 0 10px rgba(147, 197, 114, 0.2);
        background: #FFFFFF;
    }}

    .user-greeting {{
        color: #124D41;
        font-weight: 700;
        font-size: 16px;
    }}

    /* 2. DRIBBBLE BOUNCE ANIMATIONS */
    @keyframes dribbblePop {{
        0% {{ opacity: 0; transform: scale(0.8) translateY(40px); }}
        60% {{ opacity: 1; transform: scale(1.03) translateY(-10px); }}
        80% {{ transform: scale(0.98) translateY(2px); }}
        100% {{ opacity: 1; transform: scale(1) translateY(0); }}
    }}

    .pop-1 {{ animation: dribbblePop 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) forwards; opacity: 0; }}
    .pop-2 {{ animation: dribbblePop 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) 0.1s forwards; opacity: 0; }}
    .pop-3 {{ animation: dribbblePop 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) 0.2s forwards; opacity: 0; }}

    /* 3. CARD STYLING */
    div[data-testid="stVerticalBlockBorderWrapper"] {{
        background: rgba(255, 255, 255, 0.75) !important;
        backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(147, 197, 114, 0.1) !important;
        border-radius: 30px !important;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.03) !important;
        margin-top: 20px;
    }}

    /* Padding adjustment for fixed top bar */
    .main-content {{ padding-top: 80px; }}
    </style>
    """, unsafe_allow_html=True)

if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    # --- PISTACHIO LOGIN (Existing Logic) ---
    st.markdown('<div style="text-align:center; margin-top:100px;">', unsafe_allow_html=True)
    if st.button("Simulate Login"):
        st.session_state.auth = True
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

else:
    # --- TOP BAR RENDER ---
    logo_img = f'data:image/png;base64,{logo_b64}' if logo_b64 else ""
    st.markdown(f"""
        <div class="top-bar">
            <img src="{logo_img}" class="top-logo">
            <div class="search-container">
                <input type="text" class="search-bar" placeholder="Search patients, messages, or community...">
            </div>
            <div class="user-greeting">Hello, <b>{user_name}</b></div>
        </div>
        <div class="main-content"></div>
    """, unsafe_allow_html=True)

    # --- SIDEBAR MENU ---
    with st.sidebar:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.button("🏠 Homepage", use_container_width=True)
        st.button("💬 Messages", use_container_width=True)
        st.button("👤 Patients", use_container_width=True)
        st.button("📅 Reservation", use_container_width=True)
        st.button("🤝 Community", use_container_width=True)
        st.divider()
        if st.button("Logout"):
            st.session_state.auth = False
            st.rerun()

    # --- MAIN CONTENT ---
    st.markdown('<div class="pop-1"><h1 style="color: #124D41; font-weight:900;">Workspace Overview</h1></div>', unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown('<div class="pop-2">', unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("### **🤝 Community Feed**")
            st.caption("Latest clinical discussions from your peers")
            st.info("**Dr. Aris:** New findings on hypertension management. [Read More]")
            st.success("**Dr. Lee:** Successfully completed the first M-FLO surgery of the week!")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="pop-3">', unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("### **📅 Next Reservation**")
            st.write("**Patient:** Jane Doe")
            st.write("**Time:** 09:30 AM")
            st.button("Check-in Patient", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
