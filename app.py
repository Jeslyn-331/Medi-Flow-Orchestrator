To allow you to manage the urgent list, we need to add a "Resolve" or "Dismiss" button to each alert card. I have updated the code to move the `URGENT_PATIENTS` list into the **Session State**.

This allows you to remove a patient from the list in real-time. Once the list is empty, the "Urgent Alerts" count will automatically update to **0**.

### `streamlit_app.py`

```python
import streamlit as st
import base64
import os
import requests
from datetime import date

# 1. PAGE SETUP
st.set_page_config(
    page_title="M-FLO | Cardiology Workspace", 
    page_icon="⚕️", 
    layout="wide"
)

# 2. GLOBAL DATA & VARIABLES (PRESERVED)
user_name = "Dr. John Doe"
GITHUB_RAW_URL = "https://raw.githubusercontent.com/your-username/your-repo/main/doctor_profile.png" 

DOCTOR_BIO = {
    "title": "Senior Consultant Cardiologist",
    "desc": "Specializing in interventional cardiology and structural heart disease with over 15 years of clinical excellence.",
    "certs": ["MD, Harvard Medical School", "Board Certified in Cardiovascular Disease", "FACC Fellowship"],
    "achievements": ["Best Clinician Award 2025", "50+ Published Research Papers", "Lead Researcher - Project HeartBeat"]
}

# 3. FILE ENCODING (PRESERVED)
def get_base64_from_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return base64.b64encode(response.content).decode()
    except: return ""
    return ""

def get_base64(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

logo_b64 = get_base64("logo_medical.png")
doctor_b64 = get_base64_from_url(GITHUB_RAW_URL)
if not doctor_b64:
    doctor_b64 = get_base64("doctor_profile.png")

# 4. SESSION STATE (PRESERVED + DYNAMIC ALERTS)
if "auth" not in st.session_state:
    st.session_state.auth = False
if "current_page" not in st.session_state:
    st.session_state.current_page = "Homepage"
if "show_alerts" not in st.session_state:
    st.session_state.show_alerts = False

# Moving Urgent Patients to Session State so they can be deleted
if "urgent_patients" not in st.session_state:
    st.session_state.urgent_patients = [
        {"Room": "402", "Name": "Alice Tan", "Issue": "Tachycardia Spike"},
        {"Room": "ICU-1", "Name": "Bob Smith", "Issue": "Post-Op Arrhythmia"},
        {"Room": "ER-3", "Name": "Charlie Day", "Issue": "Unstable Angina"}
    ]

if "daily_tasks" not in st.session_state:
    st.session_state.daily_tasks = {
        str(date.today()): ["Review Lab Results", "Surgery Consultation", "Department Meeting"]
    }
if "completed_counts" not in st.session_state:
    st.session_state.completed_counts = {}

# 5. CSS (PRESERVED + DISMISS BUTTON STYLE)
st.markdown(f"""
    <style>
    @keyframes slideUp {{ from {{ opacity: 0; transform: translateY(20px); }} to {{ opacity: 1; transform: translateY(0); }} }}
    [data-testid="stHeader"] {{ display: none; }}
    [data-testid="stAppViewContainer"] {{
        background: radial-gradient(circle at top right, #F9FFF9, #FDFDFD) !important;
        overflow: {"hidden" if not st.session_state.auth else "auto"};
    }}
    .main .block-container {{
        padding: {"0" if not st.session_state.auth else "2rem"} !important;
        display: {"flex" if not st.session_state.auth else "block"};
        align-items: center; justify-content: center; height: 100vh;
    }}
    .stat-box {{ 
        background: #F1F8E9; 
        border-radius: 20px; 
        padding: 20px; 
        text-align: center; 
        border: 1px solid #E1EDD8;
        height: 120px; 
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }}
    .stat-val {{ font-size: 24px; font-weight: 800; color: #124D41; margin: 0; }}
    .stat-lbl {{ font-size: 12px; color: #666; text-transform: uppercase; margin: 0; }}
    .alert-card {{ background: #FFF5F5; border-left: 5px solid #E57373; padding: 15px; border-radius: 12px; margin-bottom: 10px; }}
    .todo-item {{ background:#F1F8E9; padding:12px; border-radius:12px; border-left:5px solid #93C572; margin-bottom:10px; }}
    .profile-card {{ background: white; padding: 35px; border-radius: 30px; border: 1px solid #E0E0E0; box-shadow: 0 10px 40px rgba(0,0,0,0.04); }}
    .profile-img {{ width: 110px; height: 110px; border-radius: 25px; object-fit: cover; border: 3px solid #93C572; }}
    </style>
    """, unsafe_allow_html=True)

# 6. APP FLOW
if not st.session_state.auth:
    with st.form("login_form", clear_on_submit=False):
        if logo_b64:
            st.markdown(f'<div style="text-align:center;"><img src="data:image/png;base64,{logo_b64}" style="width:110px; margin-bottom:15px;"></div>', unsafe_allow_html=True)
        st.markdown('<p style="color:#93C572; font-weight:800; font-size:20px; text-align:center;">67+2 PODCAST</p>', unsafe_allow_html=True)
        st.markdown('<h1 style="color:#124D41; font-size:55px; font-weight:900; text-align:center; margin:0; letter-spacing:-3px;">M-FLO</h1>', unsafe_allow_html=True)
        u = st.text_input("ID", placeholder="Enter ID", label_visibility="collapsed")
        p = st.text_input("Key", type="password", placeholder="Security Key", label_visibility="collapsed")
        if st.form_submit_button("AUTHENTICATE SYSTEM"):
            if u == "doctor1" and p == "mediflow2026":
                st.session_state.auth = True; st.rerun()
else:
    # SIDEBAR
    with st.sidebar:
        if logo_b64: st.image(f"data:image/png;base64,{logo_b64}", use_container_width=True)
        st.divider()
        if st.button("🏠 Homepage", key="nav_h", use_container_width=True): st.session_state.current_page = "Homepage"
        if st.button("📅 Reservation", key="nav_r", use_container_width=True): st.session_state.current_page = "Reservation"
        st.divider()
        if st.button("🚪 Logout", key="nav_l", use_container_width=True): st.session_state.auth = False; st.rerun()

    if st.session_state.current_page == "Homepage":
        t1, t2, t3 = st.columns([1, 2, 1])
        with t1: st.markdown(f'<p style="color:#124D41; font-weight:700; font-size:18px;">Hello, {user_name} 👋</p>', unsafe_allow_html=True)

        # --- UPDATED STATS ROW ---
        s1, s2, s3, s4 = st.columns(4)
        with s1: st.markdown('<div class="stat-box"><p class="stat-lbl">Patients Today</p><p class="stat-val">12</p></div>', unsafe_allow_html=True)
        with s2: st.markdown('<div class="stat-box"><p class="stat-lbl">Surgeries</p><p class="stat-val">02</p></div>', unsafe_allow_html=True)
        with s3:
            # Count now updates dynamically based on the session state list
            alert_count = len(st.session_state.urgent_patients)
            color = "#E57373" if alert_count > 0 else "#93C572"
            st.markdown(f'<div class="stat-box" style="border-color:{color};"><p class="stat-lbl">Urgent Alerts</p><p class="stat-val" style="color:{color};">{alert_count:02d}</p></div>', unsafe_allow_html=True)
            if st.button("Manage Alerts", key="manage_alerts", use_container_width=True):
                st.session_state.show_alerts = not st.session_state.show_alerts
                st.rerun()
        with s4: st.markdown('<div class="stat-box"><p class="stat-lbl">System Health</p><p class="stat-val">98%</p></div>', unsafe_allow_html=True)
        
        # --- DYNAMIC URGENT PATIENT UPDATE LOGIC ---
        if st.session_state.show_alerts:
            st.markdown("#### 🚨 Active Urgent Cases")
            if not st.session_state.urgent_patients:
                st.info("No active urgent alerts.")
            else:
                # Using columns to list patients with a "Resolve" button
                for idx, p_alert in enumerate(st.session_state.urgent_patients):
                    ac1, ac2 = st.columns([4, 1])
                    with ac1:
                        st.markdown(f'<div class="alert-card"><strong>Room {p_alert["Room"]}</strong>: {p_alert["Name"]} | <small>{p_alert["Issue"]}</small></div>', unsafe_allow_html=True)
                    with ac2:
                        # Adding the update/remove button
                        if st.button("Resolve ✅", key=f"res_{idx}", use_container_width=True):
                            st.session_state.urgent_patients.pop(idx)
                            st.rerun()
            st.divider()

        # PROFILE & PLANNING (PRESERVED)
        col_main, col_plan = st.columns([2.2, 1], gap="large")
        with col_main:
            img_html = f'<img src="data:image/png;base64,{doctor_b64}" class="profile-img">' if doctor_b64 else '👨‍⚕️'
            st.markdown(f"""<div class="profile-card"><div style="display:flex; align-items:center; gap:25px;">{img_html}<div><h1 style="margin:0; color:#124D41;">{user_name}</h1><p style="color:#93C572; font-weight:700;">{DOCTOR_BIO['title']}</p></div></div><hr style="border:0; border-top:1px solid #eee; margin:25px 0;"><p style="color:#444;">{DOCTOR_BIO['desc']}</p></div>""", unsafe_allow_html=True)
            
        with col_plan:
            st.markdown("### 📅 Calendar")
            selected_date = str(st.date_input("Schedule", label_visibility="collapsed"))
            if selected_date not in st.session_state.daily_tasks: st.session_state.daily_tasks[selected_date] = []
            if selected_date not in st.session_state.completed_counts: st.session_state.completed_counts[selected_date] = 0
            
            st.divider()
            st.markdown(f"### 📝 Planning: {selected_date}")
            new_task = st.text_input("Add task", key=f"in_{selected_date}")
            if st.button("Add", key=f"btn_{selected_date}"):
                if new_task: st.session_state.daily_tasks[selected_date].append(new_task); st.rerun()

            curr_tasks = st.session_state.daily_tasks[selected_date]
            for i, task in enumerate(curr_tasks):
                c1, c2 = st.columns([5, 1])
                with c1: st.markdown(f'<div class="todo-item">{task}</div>', unsafe_allow_html=True)
                with c2:
                    if st.button("✔️", key=f"d_{selected_date}_{i}"):
                        st.session_state.daily_tasks[selected_date].pop(i)
                        st.session_state.completed_counts[selected_date] = st.session_state.completed_counts.get(selected_date, 0) + 1
                        st.rerun()

```

### What’s New:

1. **Dynamic List:** I moved the patients from a static variable to `st.session_state.urgent_patients`. This means if you delete one, it stays deleted while you navigate the app.
2. **Resolve Button:** Next to each urgent patient card, there is now a **"Resolve ✅"** button. Clicking this removes them from the list.
3. **Auto-Updating Metric:** The "Urgent Alerts" number in the green box now calculates `len(st.session_state.urgent_patients)`. If you resolve all patients, the counter will drop to **00** and the border color will change from Red to Mint Green automatically.

Would you like me to add a **"History"** tab so you can see a list of patients you have already resolved today?
