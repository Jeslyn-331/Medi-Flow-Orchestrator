import streamlit as st
import base64
import os

st.set_page_config(
    page_title="M-FLO | Workspace", 
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

# --- REFINED BIG & BOLD CSS ---
st.markdown(f"""
    <style>
    .main .block-container {{
        padding-top: 140px !important;
    }}

    /* FIXED TOP BAR */
    div[data-testid="stHeader"] {{
        height: 120px !important;
        background-color: rgba(255, 255, 255, 0.98) !important;
        backdrop-filter: blur(20px);
        border-bottom: 3px solid #93C572;
        z-index: 999999 !important;
    }}

    div[data-testid="column"] {{
        display: flex;
        align-items: center;
        justify-content: center;
    }}

    /* TALL SEARCH INPUT */
    .stTextInput > div > div > input {{
        height: 70px !important;
        font-size: 22px !important;
        border-radius: 25px !important;
        border: 2px solid #93C572 !important;
        padding: 0 30px !important;
        background-color: #F9FFF9 !important;
    }}

    /* BIG LOGO STYLE (Now for Sidebar) */
    .sidebar-logo-container {{
        text-align: center;
        margin-bottom: 40px;
    }}

    .big-logo-text {{
        font-size: 48px !important;
        font-weight: 900 !important;
        color: #124D41;
        letter-spacing: -3px;
    }}

    /* LARGE CARDS */
    div[data-testid="stVerticalBlockBorderWrapper"] {{
        background: white !important;
        border-radius: 50px !important;
        padding: 50px !important;
        box-shadow: 0 30px 60px rgba(0, 0, 0, 0.05) !important;
    }}

    /* SIDEBAR WIDTH */
    section[data-testid="stSidebar"] {{
        width: 380px !important;
    }}
    
    .stButton > button {{
        height: 70px !important;
        font-size: 24px !important;
        font-weight: 800 !important;
        border-radius: 25px !important;
        margin-bottom: 20px !important;
    }}

    h1 {{ font-size: 70px !important; font-weight: 900 !important; }}
    </style>
    """, unsafe_allow_html=True)

if not st.session_state.auth:
    # --- LOGIN PAGE ---
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    logo_html = f'<img src="data:image/png;base64,{logo_b64}" style="width:350px;">' if logo_b64 else '<h1 class="big-logo-text">M-FLO</h1>'
    st.markdown(f'<div style="border: 4px solid #93C572; border-radius: 60px; padding: 80px; background-color: #F9FFF9; text-align: center; max-width: 700px; margin: auto;">{logo_html}<div style="color: #93C572; font-weight: 800; font-size: 35px; margin-top: 20px;">67+2 PODCAST</div><div style="color: #124D41; font-size: 80px; font-weight: 900; margin: 0; letter-spacing: -4px;">M-FLO</div></div>', unsafe_allow_html=True)

    _, col2, _ = st.columns([1, 2, 1])
    with col2:
        u = st.text_input("Physician ID")
        p = st.text_input("Security Key", type="password")
        if st.button("AUTHENTICATE SYSTEM", use_container_width=True):
            if u == "doctor1" and p == "mediflow2026":
                st.session_state.auth = True
                st.rerun()
else:
    # --- TOP BAR (LOGO REMOVED, SEARCH & GREETING ONLY) ---
    with st.container():
        # Adjusting columns to fill the space since logo is gone from here
        t1, t2 = st.columns([4, 1.5])
        
        with t1:
            search_val = st.text_input("search_input", placeholder="🔍 Search clinical functions...", label_visibility="collapsed", key="top_search")
            if search_val:
                pages = ["Homepage", "Messages", "Patients", "Reservation", "Community"]
                suggestions = [p for p in pages if search_val.lower() in p.lower()]
                if suggestions:
                    cols = st.columns(len(suggestions))
                    for idx, s in enumerate(suggestions):
                        if cols[idx].button(f"Go to {s}", key=f"sug_{s}", use_container_width=True):
                            st.session_state.current_page = s
                            st.rerun()

        with t2:
            st.markdown(f"<div style='text-align:right; color:#124D41; font-size:26px; font-weight:700; padding-top:15px;'>Hello, {user_name}</div>", unsafe_allow_html=True)

    # --- SIDEBAR (LOGO ADDED HERE) ---
    with st.sidebar:
        # LOGO AT THE TOP OF THE MENU
        st.markdown('<div class="sidebar-logo-container">', unsafe_allow_html=True)
        if logo_b64:
            st.image(f"data:image/png;base64,{logo_b64}", use_container_width=True)
        else:
            st.markdown('<h1 class="big-logo-text">M-FLO</h1>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # MENU BUTTONS
        if st.button("🏠 Homepage", use_container_width=True): st.session_state.current_page = "Homepage"
        if st.button("💬 Messages", use_container_width=True): st.session_state.current_page = "Messages"
        if st.button("👤 Patients", use_container_width=True): st.session_state.current_page = "Patients"
        if st.button("📅 Reservation", use_container_width=True): st.session_state.current_page = "Reservation"
        if st.button("🤝 Community", use_container_width=True): st.session_state.current_page = "Community"
        st.divider()
        if st.button("Logout"):
            st.session_state.auth = False
            st.rerun()

    # --- CONTENT AREA ---
    if st.session_state.current_page == "Community":
        st.markdown("<h1>Medical Community</h1>", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("### Create Post")
            st.text_area("What's on your mind?", height=150, label_visibility="collapsed", key="post_area")
            st.button("Post to Forum", type="primary", use_container_width=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        with st.container(border=True):
            st.markdown("### **u/Cardio_Expert**")
            st.write("Does anyone have tips for scaling high-fidelity dashboards in Streamlit?")
            c1, c2, _ = st.columns([0.2, 0.2, 0.6])
            c1.button("🔼 254", key="upvote_btn")
            c2.button("💬 86", key="comment_btn")

    elif st.session_state.current_page == "Homepage":
        st.markdown("<h1>Dashboard</h1>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("### Welcome, Doctor.")
            st.info("The M-FLO system is optimized and ready for your next consultation.")
