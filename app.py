import streamlit as st
import base64
import os

# 1. Page Configuration for a Wide, Professional View
st.set_page_config(
    page_title="M-FLO | Clinical Workspace", 
    page_icon="⚕️", 
    layout="wide"
)

def get_base64(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

logo_b64 = get_base64("logo_medical.png")
user_name = "Dr. John Doe" 

if "auth" not in st.session_state:
    st.session_state.auth = False
if "current_page" not in st.session_state:
    st.session_state.current_page = "Homepage"

# --- THE "ULTRA-SCALE" BALANCED CSS ---
st.markdown(f"""
    <style>
    /* 1. GLOBAL TEXT SCALING */
    html, body, [class*="css"] {{
        font-family: 'Inter', sans-serif;
        font-size: 22px !important;
        color: #124D41;
    }}

    .stApp {{ background: #F8F9FA !important; }}

    /* 2. TOP BAR & FIXED SEARCH BAR FIX */
    header[data-testid="stHeader"] {{
        height: 140px !important;
        background-color: rgba(255, 255, 255, 0.98) !important;
        backdrop-filter: blur(20px);
        border-bottom: 2px solid #EAEAEA;
        z-index: 999999 !important;
    }}

    /* SEARCH BAR: Balanced Word Size + No Clipping */
    .stTextInput > div > div > input {{
        height: 100px !important; 
        font-size: 34px !important; /* Scaled to match bar height */
        font-weight: 600 !important;
        border-radius: 35px !important;
        border: 2px solid #F0F0F0 !important;
        background-color: #F9F9F9 !important;
        text-align: center !important; 
        line-height: 100px !important; /* Critical: Centers text vertically */
        padding: 0 !important; 
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }}

    .stTextInput > div > div > input:focus {{
        border-color: #93C572 !important;
        box-shadow: 0 0 35px rgba(147, 197, 114, 0.2) !important;
        background-color: #FFFFFF !important;
    }}

    /* 3. SIDEBAR: Oversized Menu Labels & Buttons */
    section[data-testid="stSidebar"] {{
        width: 480px !important;
        background-color: #FFFFFF !important;
    }}

    .sidebar-label {{
        color: #ADADAD;
        font-size: 20px;
        font-weight: 800;
        margin: 40px 0 15px 30px;
        text-transform: uppercase;
        letter-spacing: 2px;
    }}

    .stButton > button {{
        height: 100px !important;
        font-size: 32px !important; /* Scaled for balance */
        font-weight: 800 !important;
        border-radius: 30px !important;
        margin-bottom: 25px !important;
        border: 1.5px solid transparent !important;
        transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        text-align: left !important;
        padding-left: 40px !important;
    }}

    .stButton > button:hover {{
        background-color: #F9FFF9 !important;
        border-color: #93C572 !important;
        color: #93C572 !important;
        transform: translateX(15px);
        box-shadow: 10px 10px 30px rgba(147, 197, 114, 0.1);
    }}

    /* 4. DASHBOARD CARDS: Massive & Airy */
    div[data-testid="stVerticalBlockBorderWrapper"] {{
        background: white !important;
        border-radius: 65px !important;
        padding: 80px !important;
        box-shadow: 0 45px 110px rgba(0, 0, 0, 0.05) !important;
        border: 1px solid rgba(0,0,0,0.03) !important;
    }}

    /* 5. TYPOGRAPHY SCALING */
    h1 {{ font-size: 110px !important; font-weight: 900 !important; letter-spacing: -6px !important; margin-bottom: 40px !important; }}
    h2 {{ font-size: 70px !important; font-weight: 800 !important; letter-spacing: -3px !important; }}
    h3 {{ font-size: 48px !important; font-weight: 700 !important; }}

    .main .block-container {{ padding-top: 180px !important; }}

    /* Animation */
    @keyframes springPop {{
        0% {{ opacity: 0; transform: scale(0.9) translateY(40px); }}
        100% {{ opacity: 1; transform: scale(1) translateY(0); }}
    }}
    .pop-in {{ animation: springPop 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) forwards; }}
    </style>
    """, unsafe_allow_html=True)

# --- APP ROUTING ---
if not st.session_state.auth:
    # --- LARGE SCALE LOGIN ---
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    logo_html = f'<img src="data:image/png;base64,{logo_b64}" style="width:450px;">' if logo_b64 else '<h1 style="font-size:120px;">M-FLO</h1>'
    
    st.markdown(f"""
        <div style="border: 6px solid #93C572; border-radius: 80px; padding: 120px; background-color: #F9FFF9; text-align: center; max-width: 900px; margin: auto;" class="pop-in">
            {logo_html}
            <div style="color: #93C572; font-weight: 800; font-size: 45px; margin-top: 40px;">67+2 PODCAST</div>
            <div style="color: #124D41; font-size: 120px; font-weight: 900; margin: 0; letter-spacing: -7px;">M-FLO</div>
        </div>
    """, unsafe_allow_html=True)

    _, col2, _ = st.columns([1, 2, 1])
    with col2:
        u = st.text_input("Physician ID", key="user_id")
        p = st.text_input("Security Key", type="password", key="pass_id")
        if st.button("AUTHENTICATE SYSTEM", use_container_width=True):
            if u == "doctor1" and p == "mediflow2026":
                st.session_state.auth = True
                st.rerun()
else:
    # --- TOP BAR ---
    t1, t2, t3 = st.columns([1, 4, 1.5])
    with t2:
        # Perfectly Balanced & Centered Search
        search_val = st.text_input("search", placeholder="Search functions...", label_visibility="collapsed", key="top_search")
        if search_val:
            pages = ["Dashboard", "Patients", "Appointments", "Messages", "Community"]
            for p in pages:
                if search_val.lower() in p.lower():
                    st.session_state.current_page = p if p != "Dashboard" else "Homepage"

    with t3:
        st.markdown(f"<div style='text-align:right; font-weight:900; font-size:36px; color:#124D41; padding-top:15px;'>{user_name}</div>", unsafe_allow_html=True)

    # --- SIDEBAR (LOGO AT TOP) ---
    with st.sidebar:
        st.markdown("<br>", unsafe_allow_html=True)
        if logo_b64:
            st.image(f"data:image/png;base64,{logo_b64}", use_container_width=True)
        else:
            st.markdown("<h1 style='padding-left:35px;'>M-FLO</h1>", unsafe_allow_html=True)
        
        st.markdown('<p class="sidebar-label">Menu</p>', unsafe_allow_html=True)
        if st.button("📊 Dashboard", use_container_width=True): st.session_state.current_page = "Homepage"
        if st.button("👥 Patients", use_container_width=True): st.session_state.current_page = "Patients"
        if st.button("📅 Appointments", use_container_width=True): st.session_state.current_page = "Reservation"
        
        st.markdown('<p class="sidebar-label">Community</p>', unsafe_allow_html=True)
        if st.button("🤝 Forum", use_container_width=True): st.session_state.current_page = "Community"
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.auth = False
            st.rerun()

    # --- MAIN CONTENT ---
    st.markdown('<div class="pop-in">', unsafe_allow_html=True)
    st.markdown(f"<h1>{st.session_state.current_page} Overview</h1>", unsafe_allow_html=True)
    
    col_l, col_r = st.columns([2.5, 1], gap="large")
    
    with col_l:
        with st.container(border=True):
            st.markdown("### **Clinical Performance Metrics**")
            st.line_chart({"Health Score": [80, 85, 82, 90, 88, 92, 95]})
            st.write("Visualizations are now scaled to match the bold typography and massive frames.")

    with col_r:
        with st.container(border=True):
            st.markdown("### **Quick Actions**")
            st.button("New Patient +", use_container_width=True)
            st.button("Export Data ↓", use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)
