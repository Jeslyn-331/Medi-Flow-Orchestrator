import streamlit as st
import base64
import os
import time

st.set_page_config(
    page_title="M-FLO | Secure Access Portal", 
    page_icon="⚕️", 
    layout="wide"
)

def get_base64_image(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return None

logo_b64 = get_base64_image("logo_medical.png")

st.markdown(f"""
    <style>
    .stApp {{ background-color: #FFFFFF !important; color: #2F4F4F !important; }}

    @keyframes samsungFadeInUp {{
        from {{
            opacity: 0;
            transform: translateY(40px); 
        }}
        to {{
            opacity: 1;
            transform: translateY(0); 
        }}
    }}

    .animate-in {{
        animation: samsungFadeInUp 0.8s cubic-bezier(0.165, 0.84, 0.44, 1) forwards;
    }}
    
    div[data-baseweb="input"], div[data-baseweb="textarea"], .stTextArea textarea {{
        background-color: #FFFFFF !important;
        border: 2px solid #93C572 !important;
        border-radius: 10px !important;
    }}
    
    input, textarea {{
        color: #124D41 !important;
        -webkit-text-fill-color: #124D41 !important;
    }}

    .login-card {{
        border: 2.5px solid #93C572;
        border-radius: 20px;
        padding: 40px;
        background-color: #F9FFF9;
        text-align: center;
        max-width: 480px;
        margin: auto;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    }}

    .mflo-header {{ color: #124D41; font-size: 42px; font-weight: 900; margin: 0; }}
    label p {{ color: #124D41 !important; font-weight: bold !important; text-align: left !important; }}

    div.stButton > button {{
        background-color: #98FFD9 !important;
        color: #124D41 !important;
        border: 1.5px solid #93C572 !important;
        font-weight: 800 !important;
        text-transform: uppercase;
        width: 100%;
        padding: 12px;
        border-radius: 10px;
        margin-top: 10px;
        transition: all 0.3s ease;
    }}
    
    div.stButton > button:hover {{
        transform: scale(1.02);
        box-shadow: 0 5px 15px rgba(152, 255, 217, 0.4);
    }}

    section[data-testid="stSidebar"] {{
        background-color: #F0F4F2 !important;
        border-right: 1px solid #93C572;
    }}
    </style>
    """, unsafe_allow_html=True)

if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    if logo_b64:
        logo_html = f'<div style="display: flex; justify-content: center;"><img src="data:image/png;base64,{logo_b64}" style="width:250px; margin-bottom:10px;"></div>'
    else:
        logo_html = '<div style="color:#93C572; font-weight:800; font-size:24px; margin-bottom:10px;">67+2 PODCAST</div>'

    st.markdown(f"""
        <div class="login-card">
            {logo_html}
            <div class="mflo-header">M-FLO</div>
            <p style="color: #124D41; font-size: 14px; margin-bottom: 20px; font-weight: 500;">
                Medi-Flow Orchestrator v2.1 | Secure Portal
            </p>
            <hr style="border-top: 1.5px solid #93C572; margin-bottom: 25px;">
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        u = st.text_input("Physician ID", placeholder="doctor1")
        p = st.text_input("Security Key", type="password", placeholder="••••••••")
        
        if st.button("AUTHENTICATE SYSTEM"):
            if u == "doctor1" and p == "mediflow2026":
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("Invalid Credentials. Access Denied.")
        
        st.markdown("<p style='text-align:center; font-size:11px; color:gray; margin-top:15px;'>Auth: MD-Level Encrypted Access Only</p>", unsafe_allow_html=True)

else:
    with st.sidebar:
        if logo_b64:
            st.markdown(f'<img src="data:image/png;base64,{logo_b64}" width="150">', unsafe_allow_html=True)
        st.title("M-FLO v2.1")
        st.write("Logged in: **Dr. John Doe**")
        st.divider()
        if st.button("LOGOUT / LOCK"):
            st.session_state.auth = False
            st.rerun()

    st.markdown('<div class="animate-in">', unsafe_allow_html=True)

    st.subheader("⚕️ Patient Consultation Environment")
    
    col_pat, col_trans, col_res = st.columns([1, 2, 2])

    with col_pat:
        st.markdown("#### Patient Context")
        with st.container(border=True):
            st.markdown("### **J. Doe**")
            st.caption("ID: #8821 | Male | 45yo")
            st.divider()
            st.error("⚠️ ALLERGY: Penicillin")
            st.warning("⚠️ CONDITION: Hypertension")

    with col_trans:
        st.markdown("#### Clinical Interface")
        notes = st.text_area("Live Transcript / Notes", height=350, placeholder="Start typing consultation context...")
        
        if st.button("EXECUTE INTENT ANALYSIS"):
            if notes:
                with st.spinner("Decoding clinical path..."):
                    time.sleep(1.5)
                    st.toast("Intents detected!")

    with col_res:
        st.markdown("#### AI-Generated Orders")
        st.info("Awaiting transcription analysis...")
    
    st.markdown('</div>', unsafe_allow_html=True)
