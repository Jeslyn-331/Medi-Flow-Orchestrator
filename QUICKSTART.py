"""

"""

# ============================================================================
# 1. INSTALLATION
# ============================================================================

# Install dependencies:
# pip install -r requirements.txt

# ============================================================================
# 2. RUNNING THE APPLICATION
# ============================================================================

# Option A: Web Interface (Recommended)
# streamlit run app.py


# Option B: Command Line Demo
# python demo.py

# ============================================================================
# 3. AUTHENTICATION
# ============================================================================

# Login credentials (for demo):
# ID: doctor1
# Key: mediflow2026

# ============================================================================
# 4. USAGE EXAMPLE - COMMAND LINE
# ============================================================================






# Example transcript
transcript = """
Patient presents with elevated glucose levels.
Order CBC and metabolic panel to assess condition.
Request HbA1c test for diabetes screening.
Prescribe metformin 500mg twice daily.
Refer to endocrinology for specialized care.
"""

# Process the transcript

    transcript=transcript,
    patient_id="PATIENT-001",
    ordering_physician="Dr. Sarah Johnson"
)

# Access results
print(f"Intents detected: {result['summary']['intents_count']}")
print(f"Orders generated: {result['summary']['orders_count']}")
print(f"Departments: {result['summary']['departments_involved']}")

# Print intents
print("\n=== DETECTED INTENTS ===")
for intent in result['intents_detected']:
    print(f"  • {intent['type']}: {intent['item']} ({intent['confidence']:.0%})")

# Print orders
print("\n=== GENERATED ORDERS ===")
for order in result['orders_generated']:
    print(f"  • {order['order_id']}: {order['type'].upper()}")
    print(f"    Department: {order['department']}")
    print(f"    Items: {', '.join(order['items'])}")

# ============================================================================
# 5. WEB INTERFACE WALKTHROUGH
# ============================================================================

# STEP 1: Login
# - Enter ID: doctor1
# - Enter Key: mediflow2026
# - Click "AUTHENTICATE SYSTEM"




# STEP 3: Process Transcript
# - Paste a clinical transcript in the text area
# - Enter patient ID (or use default)
# - Enter ordering physician (or use default)
# - Ensure "Auto-Route Orders" is checked
# - Click "🚀 Process Transcript"

# STEP 4: Review Results
# - See visual metrics for intents and orders
# - Expand each order to see details
# - Check routing status

# STEP 5: Dashboard
# - Switch to "📊 Analysis Dashboard" tab
# - View department workload
# - See intent distribution charts

# ============================================================================
# 6. SUPPORTED KEYWORDS - QUICK REFERENCE
# ============================================================================

# LAB TESTS
lab_keywords = [
    "blood test", "CBC", "FBC", "metabolic panel", "lipid panel",
    "liver function", "kidney function", "thyroid", "TSH", "glucose",
    "HbA1c", "urinalysis", "culture"
]

# MEDICATIONS
med_keywords = [
    "prescribe", "prescription", "medication", "drug",
    "metformin", "lisinopril", "atorvastatin", "aspirin", "amoxicillin"
]

# IMAGING
imaging_keywords = [
    "X-ray", "CT scan", "MRI", "ultrasound", "echocardiogram"
]

# REFERRALS
referral_keywords = [
    "refer", "consultation", "specialist", "cardiology", "neurology", "dermatology"
]

# PROCEDURES
procedure_keywords = [
    "procedure", "surgery", "biopsy", "endoscopy", "colonoscopy"
]

# ============================================================================
# 7. ADVANCED: CUSTOMIZATION
# ============================================================================

# Change confidence threshold (lower = more detections but less accurate)
from intent_detector import IntentDetector

detector = IntentDetector(confidence_threshold=0.6)
intents = detector.detect_intents(transcript)

# Get department info for an intent type
from intent_detector import IntentType
dept = detector.get_department(IntentType.LAB_TEST)  # Returns "Laboratory"

# Extract specific intent type only
lab_intents = detector.extract_with_context(transcript, IntentType.LAB_TEST)

# ============================================================================
# 8. OUTPUT FORMATS
# ============================================================================

# Order Object Structure:
{
    "order_id": "A1B2C3D4",
    "timestamp": "2026-03-11T14:30:00",
    "type": "lab_test",
    "patient_id": "PATIENT-001",
    "ordering_physician": "Dr. John Doe",
    "department": "Laboratory",
    "items": ["Complete Blood Count", "Metabolic Panel"],
    "details": "Patient presents with fatigue...",
    "priority": "routine",
    "status": "routed",
    "routing_log": [
        {"timestamp": "2026-03-11T14:30:00", "status": "generated"},
        {"timestamp": "2026-03-11T14:30:05", "status": "routed"}
    ]
}

# Intent Object Structure:
{
    "type": "lab_test",
    "item": "blood test CBC",
    "details": "Patient presents with fatigue. Take blood for CBC.",
    "confidence": 0.85
}

# ============================================================================
# 9. TROUBLESHOOTING
# ============================================================================

# Issue: "No intents detected"
# Solution: Check that your transcript includes specific keywords
# Example: "Order blood test" instead of "Check blood"

# Issue: "Wrong department assigned"
# Solution: Use clearer terminology
# Example: "Refer to cardiology" instead of "See heart specialist"

# Issue: Order confidence too low
# Solution: Adjust confidence_threshold or use more specific terms

# Issue: "Module not found"
# Solution: Run `pip install -r requirements.txt`

# ============================================================================
# 10. NEXT STEPS
# ============================================================================

# 1. Integrate with your hospital's EHR system
# 2. Add voice transcript support
# 3. Implement machine learning-based intent detection
# 4. Add order fulfillment tracking
# 5. Set up real-time department notifications
# 6. Create admin dashboard for analytics

# ============================================================================

print("Quick Start Guide loaded successfully!")
print("Run this file with 'python quickstart.py' for examples")
