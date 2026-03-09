import streamlit as st
import base64
import os
import time

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="M-FLO | Medi-Flow Orchestrator", 
    page_icon="⚕️", 
    layout="wide"
)

# --- 2. LOGO ENCODER (Ensures PNG stays inside the frame) ---
def get_base64_image(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return None

# Ensure your file is named 'logo_medical.png' in the same folder
logo_b64 = get_base64_image("logo_medical.png")

# --- 3. THE "NUCLEAR" CSS (Animations, Hover Effects & Dark Mode Fixes) ---
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
    
    /* 2. THE BLACK BOX FIX: Forcing inputs to stay white */
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

    /* 4. Text Styling */
    .mflo-header {{ color: #124D41; font-size: 45px; font-weight: 900; margin: 0; line-height: 1; }}
    label p {{ color: #124D41 !important; font-weight: bold !important; text-align: left !important; }}

    /* 5. Live Activity Indicator (Podcast/Audio Theme) */
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

    /* 6. High-Gloss Mint Button with Hover */
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

    /* Sidebar Styling */
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
    
    # Generate Logo HTML
    if logo_b64:
        logo_html = f'<img src="data:image/png;base64,{logo_b64}" style="width:280px; margin-bottom:15px;">'
    else:
        logo_html = '<h2 style="color:#93C572;">67+2 PODCAST</h2>'

    st.markdown(f"""
        <div class="login-card">
            {logo_html}
            <div class="mflo-header">M-FLO</div>
            <p style="color: #124D41; font-size: 15px; margin-bottom: 25px; font-weight: 500; opacity: 0.8;">
                Medi-Flow Orchestrator v2.1 | Secure Physician Access
            </p>
            <hr style="border-top: 2px solid #93C572; margin-bottom: 30px; opacity: 0.3;">
        </div>
    """, unsafe_allow_html=True)

    # Inputs aligned to the frame
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
        if logo_b64:
            st.markdown(f'<img src="data:image/png;base64,{logo_b64}" width="150">', unsafe_allow_html=True)
        st.title("M-FLO v2.1")
        st.write("Logged in: **Dr. John Doe**")
        st.divider()
        if st.button("LOGOUT / LOCK"):
            st.session_state.auth = False
            st.session_state.orders = []
            st.rerun()

    # Dashboard Animation Container
    st.markdown('<div class="animate-in">', unsafe_allow_html=True)
    st.subheader("⚕️ Clinical Intelligence Workspace")
    
    col_pat, col_trans, col_res = st.columns([1, 2, 2])

    with col_pat:
        st.markdown("#### Patient Context")
        with st.container(border=True):
            # Animated ECG Heart Monitor Line
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

    with col_trans:
        st.markdown("#### Audio Intelligence")
        st.markdown('<div class="live-indicator">● LIVE CLINICAL TRANSCRIPT</div>', unsafe_allow_html=True)
        notes = st.text_area("Listening...", height=400, placeholder="Paste or type patient consultation notes here...")
        
        if st.button("RUN INTENT ANALYSIS"):
            if notes:
                with st.spinner("Decoding Clinical Path..."):
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
