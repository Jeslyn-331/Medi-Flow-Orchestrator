import streamlit as st
import time

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="M-FLO | Medi-Flow Orchestrator", 
    page_icon="⚕️", 
    layout="wide"
)

# --- 2. THE CODED LOGO (SVG) ---
# Recreates the 67+2 Podcast / M-FLO branding using pure code.
logo_svg = """
<div style="display: flex; flex-direction: column; align-items: center; justify-content: center; margin-bottom: 10px;">
    <svg width="80" height="80" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect x="9" y="2" width="6" height="12" rx="3" fill="#93C572"/>
        <path d="M5 10V11C5 14.866 8.13401 18 12 18V18C15.866 18 19 14.866 19 11V10" stroke="#93C572" stroke-width="2" stroke-linecap="round"/>
        <line x1="12" y1="18" x2="12" y2="22" stroke="#93C572" stroke-width="2" stroke-linecap="round"/>
        <line x1="9" y1="22" x2="15" y2="22" stroke="#93C572" stroke-width="2" stroke-linecap="round"/>
        <path d="M12 7V11M10 9H14" stroke="white" stroke-width="1.5" stroke-linecap="round"/>
    </svg>
    <div style="color: #93C572; font-family: 'Segoe UI', Tahoma, sans-serif; font-weight: 800; font-size: 24px; letter-spacing: -1px; margin-top: 5px;">
        67+2 <span style="color: #124D41;">PODCAST</span>
    </div>
</div>
"""

# --- 3. THE "NUCLEAR" CSS (Animations & Dark Mode Fixes) ---
st.markdown(f"""
    <style>
    /* 1. Global Light Theme & Entrance Animations */
    .stApp {{ background-color: #FFFFFF !important; color: #2F4F4F !important; }}

    @keyframes fadeInUp {{
        from {{ opacity: 0; transform: translateY(20px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}

    @keyframes pulseIndicator {{
        0% {{ opacity: 0.4; }}
        50% {{ opacity: 1; }}
        100% {{ opacity: 0.4; }}
    }}

    .animate-in {{ animation: fadeInUp 0.6s ease-out forwards; }}
    
    /* 2. THE BLACK BOX FIX: Forcing inputs to stay white with dark text */
    div[data-baseweb="input"], div[data-baseweb="textarea"], .stTextArea textarea {{
        background-color: #FFFFFF !important;
        border: 2px solid #93C572 !important;
        border-radius: 12px !important;
        transition: all 0.3s ease;
    }}
    
    div[data-baseweb="input"]:focus-within {{
        box-shadow: 0 0 12px rgba(147, 197, 114, 0.4);
    }}
    
    input, textarea {{
        color: #124D41 !important;
        -webkit-text-fill-color: #124D41 !important;
    }}

    /* 3. The Pistachio Login Card Frame */
    .login-card {{
        border: 2.5px solid #93C572;
        border-radius: 20px;
        padding: 45px;
        background-color: #F9FFF9;
        text-align: center;
        max-width: 500px;
        margin: auto;
        box-shadow: 0 15px 35px rgba(0,0,0,0.05);
        animation: fadeInUp 0.8s ease-out;
    }}

    /* 4. Text & Label Styling */
    .mflo-header {{ color: #124D41; font-size: 45px; font-weight: 900; margin: 0; line-height: 1; }}
    label p {{ color: #124D41 !important; font-weight: bold !important; text-align: left !important; }}

    /* 5. Live Activity Indicator */
    .live-indicator {{
        color: #FF4B4B;
        font-weight: 800;
        font-size: 12px;
        letter-spacing: 1px;
        animation: pulseIndicator 1.5s infinite;
        display: flex;
        align-items: center;
        gap: 6px;
        margin-bottom: 8px;
    }}

    /* 6. High-Gloss Mint Button */
    div.stButton > button {{
        background-color: #98FFD9 !important;
        color: #124D41 !important;
        border: 1.5px solid #93C572 !important;
        font-weight: 800 !important;
        text-transform: uppercase;
        width: 100%;
        padding: 14px;
        border-radius: 12px;
        margin-top: 10px;
        transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
    }}
    div.stButton > button:hover {{
        transform: scale(1.02);
        box-shadow: 0 8px 20px rgba(152, 255, 217, 0.5) !important;
        background-color: #7CFFCC !important;
    }}

    /* Sidebar Clean-up */
    section[data-testid="stSidebar"] {{
        background-color: #F0F4F2 !important;
        border-right: 1px solid #93C572;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 4. SESSION MANAGEMENT ---
if "auth" not in st.session_state:
    st.session_state.auth = False
if "orders" not in st.session_state:
    st.session_state.orders = []

# --- 5. APPLICATION FLOW ---

if not st.session_state.auth:
    # --- PAGE: SECURE LOGIN ---
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    
    # Everything inside this <div> is contained by the Pistachio border
    st.markdown(f"""
        <div class="login-card">
            {logo_svg}
            <div class="mflo-header">M-FLO</div>
            <p style="color: #124D41; font-size: 15px; margin-bottom: 25px; font-weight: 500; opacity: 0.8;">
                Medi-Flow Orchestrator v2.1 | Secure Physician Access
            </p>
            <hr style="border-top: 2px solid #93C572; margin-bottom: 30px; opacity: 0.3;">
        </div>
    """, unsafe_allow_html=True)

    # Input column alignment to match the card width
    _, col2, _ = st.columns([1, 1.6, 1])
    with col2:
        u = st.text_input("Physician ID", placeholder="doctor1")
        p = st.text_input("Security Key", type="password", placeholder="••••••••")
        
        if st.button("AUTHENTICATE SYSTEM"):
            if u == "doctor1" and p == "mediflow2026":
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("Invalid Credentials. Access Denied.")
        
        st.markdown("<p style='text-align:center; font-size:11px; color:gray; margin-top:15px;'>Encrypted MD-Level Session</p>", unsafe_allow_html=True)
        st.info("ℹ️ Demo: doctor1 / mediflow2026")

else:
    # --- PAGE: CLINICAL DASHBOARD ---
    with st.sidebar:
        st.markdown(logo_svg, unsafe_allow_html=True)
        st.markdown("### **Dr. John Doe**")
        st.caption("Status: Authorized")
        st.divider()
        if st.button("LOGOUT / LOCK"):
            st.session_state.auth = False
            st.session_state.orders = []
            st.rerun()

    # Dashboard Container
    st.markdown('<div class="animate-in">', unsafe_allow_html=True)
    st.subheader("⚕️ Clinical Intelligence Workspace")
    
    # 3-Column Layout
    col_pat, col_trans, col_res = st.columns([1, 2, 2])

    with col_pat:
        st.markdown("#### Patient Context")
        with st.container(border=True):
            # Animated ECG Line
            st.markdown("""
                <div style="height: 40px; overflow: hidden; margin-bottom: 10px; background: #fdfdfd; border-radius: 5px;">
                    <svg viewBox="0 0 100 20" style="width: 100%; height: 100%;">
                        <path d="M0 10 L25 10 L30 2 L40 18 L45 10 L100 10" stroke="#93C572" stroke-width="1.5" fill="none">
                            <animate attributeName="stroke-dasharray" from="0,100" to="100,0" dur="2.5s" repeatCount="indefinite" />
                        </path>
                    </svg>
                </div>
            """, unsafe_allow_html=True)
            st.markdown("### **J. Doe**")
            st.caption("ID: #8821 | Male | 45yo")
            st.divider()
            st.error("⚠️ ALLERGY: Penicillin")
            st.warning("⚠️ BP: 145/95 (Elevated)")
            st.info("📅 Last Visit: 10/01/26")

    with col_trans:
        st.markdown("#### Audio Intelligence")
        st.markdown('<div class="live-indicator">● LIVE CLINICAL TRANSCRIPT</div>', unsafe_allow_html=True)
        notes = st.text_area("Listening...", height=400, placeholder="Paste or type patient consultation notes here...")
        
        if st.button("RUN INTENT ANALYSIS"):
            if notes:
                with st.spinner("Analyzing Clinical Path..."):
                    time.sleep(1.5)
                    st.session_state.orders = [
                        {"type": "PHARMACY", "item": "Lisinopril 10mg", "data": "1x Daily | Qty 30"},
                        {"type": "LAB", "item": "Comprehensive Metabolic Panel", "data": "Urgency: Routine"}
                    ]
                    st.toast("Intents Detected!")

    with col_res:
        st.markdown("#### AI-Suggested Actions")
        if st.session_state.orders:
            for idx, order in enumerate(st.session_state.orders):
                with st.container(border=True):
                    icon = "💊" if order['type'] == "PHARMACY" else "🔬"
                    st.markdown(f"**{icon} {order['type']} ORDER**")
                    st.code(f"{order['item']}\n{order['data']}")
                    
                    c1, c2 = st.columns(2)
                    if c1.button(f"VERIFY & ROUTE", key=f"v_{idx}"):
                        st.success("Order Dispatched")
                    c2.button(f"EDIT", key=f"e_{idx}")
        else:
            st.info("Awaiting transcription analysis to generate orders...")
    
    st.markdown('</div>', unsafe_allow_html=True)
