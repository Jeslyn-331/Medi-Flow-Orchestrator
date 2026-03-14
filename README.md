

## Overview



The system automatically detects "Intents for Action" (ordering tests, medications, referrals) within clinical transcripts and routes digital orders to relevant departments in real-time.

### The Problem
- Manual order entry causes delays between clinical consultation and department execution
- Orders get lost or delayed in communication handoffs
- Pharmacy, Lab, and Radiology don't receive timely, structured orders
- Clinical workflows are interrupted by administrative burden

### The Solution
```
Clinical Transcript → AI Intent Detection → Digital Orders → Auto-Routing → Departments
```

---

## 🎯 MVP Features

### 1. **Automated Intent Detection**
Analyzes clinical transcripts to identify 5 types of medical intents:
- 🧪 **Lab Tests** → Laboratory Department
- 💊 **Medications** → Pharmacy Department  
- 🖼️ **Imaging** → Radiology Department
- 👨‍⚕️ **Referrals** → Referrals Department
- 🏥 **Procedures** → Surgery/Procedures Department

### 2. **Digital Order Generation**
Creates structured, machine-readable orders with:
- Unique Order IDs
- Patient and Physician information
- Specific items to order
- Priority levels
- Clinical context

### 3. **Intelligent Routing**
Automatically routes orders to:
- Correct department
- Department-specific contact
- Priority-based queuing
- Routing history tracking

### 4. **Real-Time Dashboard**
Provides visibility into:
- Detected intents
- Generated orders
- Department workload
- Processing history

---

## 🏗️ Architecture

### Core Modules

```
┌─────────────────────────────────────────────┐
│    Clinical Transcript (Text Input)         │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│   Intent Detector (intent_detector.py)      │
│  - Keyword matching                         │
│  - Confidence scoring                       │
│  - Context extraction                       │
└──────────────────┬──────────────────────────┘
                   │ (List[Intent])
┌──────────────────▼──────────────────────────┐
│  Order Generator (order_generator.py)       │
│  - Create DigitalOrder objects              │
│  - Format prescriptions                     │
│  - Batch processing                         │
└──────────────────┬──────────────────────────┘
                   │ (List[DigitalOrder])
┌──────────────────▼──────────────────────────┐
│  Orchestrator (orchestrator.py)             │
│  - Coordinate workflow                      │
│  - Route to departments                     │
│  - Maintain history                         │
└──────────────────┬──────────────────────────┘
                   │ (Routing Result)
┌──────────────────▼──────────────────────────┐
│  Departments (Lab, Pharmacy, Radiology)     │
│  - Receive structured orders                │
│  - Process immediately                      │
│  - Send confirmations back                  │
└─────────────────────────────────────────────┘
```

### File Structure

```
hackathon/
├── intent_detector.py      # Intent detection engine
├── order_generator.py      # Digital order creation
├── orchestrator.py         # Main orchestration logic
├── app.py                  # Main Streamlit app
├── pages/
│   └── orchestrator.py     # Orchestrator UI page
├── demo.py                 # Demonstration script
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

---

## 🚀 Getting Started

### Installation

```bash
# Navigate to project directory
cd hackathon

# Install dependencies
pip install -r requirements.txt

# Set up API key (if using Gemini)
# Add GEMINI_API_KEY to Streamlit secrets (Settings > Secrets)
```

### Run the Application

#### Option 1: Web Interface (Recommended)
```bash
streamlit run app.py
```
Then navigate to the **🔄 Orchestrator** section in the sidebar

#### Option 2: Command Line Demo
```bash
python demo.py
```

---

## 📋 Usage Examples

### Example 1: Simple Lab Order

**Input Transcript:**
```
Patient presents with persistent fatigue. 
Order CBC and metabolic panel to rule out anemia.
Also check thyroid function.
```

**Output:**
- ✅ 3 Intents detected
- ✅ 1 Lab Order generated
- ✅ Routed to Laboratory

### Example 2: Complete Treatment Plan

**Input Transcript:**
```
Patient James Wilson with suspected pneumonia.
Chest examination reveals crackles.

PLAN:
1. Order CBC and blood cultures
2. Request chest X-ray
3. Prescribe amoxicillin 500mg TID
4. Refer to pulmonology if not improved in 5 days
```

**Output:**
- ✅ 5 Intents detected
- ✅ 4 Orders generated:
  - Lab: CBC + Blood cultures
  - Imaging: Chest X-ray
  - Pharmacy: Amoxicillin prescription
  - Referrals: Pulmonology consultation
- ✅ Routed to 4 departments simultaneously

---

## 🔍 Intent Detection Details

### Supported Keywords

#### Lab Tests
- "blood test", "CBC", "FBC", "metabolic panel", "lipid panel"
- "liver function", "kidney function", "thyroid", "TSH"
- "glucose", "HbA1c", "urinalysis", "culture"

#### Medications
- "prescribe", "prescription", "medication", "drug"
- "metformin", "lisinopril", "atorvastatin", "aspirin"
- "start on", "begin on", "put on"

#### Imaging
- "X-ray", "CT scan", "MRI", "ultrasound", "echocardiogram"
- "radiograph", "radiologic", "scan"

#### Referrals
- "refer", "consultation", "specialist"
- "cardiology", "dermatology", "neurology", "orthopedics"

#### Procedures
- "procedure", "surgery", "operation", "biopsy"
- "endoscopy", "colonoscopy", "catheterization"

### Confidence Scoring

Each detected intent receives a confidence score (0-100%):
- **≥75%**: High confidence (specific medical terms)
- **50-74%**: Medium confidence (clear context)
- **<50%**: Low confidence (ambiguous - filtered)

Default threshold: **50%** (configurable)

---

## 📊 API Reference

### IntentDetector Class

```python
from intent_detector import IntentDetector

# Initialize
detector = IntentDetector(confidence_threshold=0.5)

# Detect intents
intents = detector.detect_intents("transcript text here")

# Get intent details
for intent in intents:
    print(f"Type: {intent.type.value}")
    print(f"Item: {intent.item}")
    print(f"Confidence: {intent.confidence:.0%}")
```

### OrderGenerator Class

```python
from order_generator import OrderGenerator

# Initialize
generator = OrderGenerator(default_physician="Dr. Smith")

# Generate order from intent
order = generator.generate_order_from_intent(
    intent=intent,
    patient_id="P-2026-001",
    priority="routine"
)

# Get formatted output
formatted = generator.create_prescription_format(order)
print(formatted)
```

### MediFlowOrchestrator Class

```python
from orchestrator import MediFlowOrchestrator

# Initialize
orchestrator = MediFlowOrchestrator()

# Process entire workflow
result = orchestrator.process_transcript(
    transcript="Patient presents with...",
    patient_id="P-2026-001",
    ordering_physician="Dr. John Doe",
    auto_route=True
)

# Get results
print(f"Intents: {result['summary']['intents_count']}")
print(f"Orders: {result['summary']['orders_count']}")
print(f"Departments: {result['summary']['departments_involved']}")
```

---

## 🎨 Web Interface Features

### 📝 Process Transcript Tab
- Paste clinical transcripts
- Specify patient info
- Real-time analysis
- Visual order display

### 📊 Dashboard Tab
- Department workload metrics
- Intent type distribution
- Historical trends
- Performance analytics

### 📋 Order History Tab
- View all processed transcripts
- Filter by patient
- Drill down into details
- Export options

### 🎯 Intent Guide Tab
- Reference of supported intents
- Keyword examples
- Best practices
- Confidence scoring explanation

---

## 🧪 Testing

### Run Demo Script
```bash
python demo.py
```

Includes 3 real-world test cases:
1. Pneumonia evaluation
2. Diabetes management
3. Post-operative care

### Manual Testing

Create a test script:
```python
from orchestrator import MediFlowOrchestrator

orchestrator = MediFlowOrchestrator()

transcript = """
Patient Jane Doe with hypertension.
Order lipid panel and kidney function test.
Prescribe lisinopril 10mg daily.
"""

result = orchestrator.process_transcript(
    transcript=transcript,
    patient_id="TEST-001"
)

print(result)
```

---

## 🔧 Configuration

### Adjusting Confidence Threshold

```python
# Higher threshold = fewer but more confident detections
detector = IntentDetector(confidence_threshold=0.7)

# Lower threshold = more detections but potentially false positives
detector = IntentDetector(confidence_threshold=0.3)
```

### Setting Default Physician

```python
orchestrator = MediFlowOrchestrator(
    default_physician="Dr. Your Name"
)
```

---

## 📈 Performance & Scalability

- **Processing Speed**: <1 second per transcript
- **Accuracy**: Keyword-based detection with confidence scoring
- **Scalability**: Can handle multiple concurrent transcripts
- **Memory**: Stores routing history for analytics

### Future Enhancements
- Machine Learning-based intent detection (NER)
- Voice transcript integration
- Real-time department feedback
- Order fulfillment tracking
- Integration with EHR systems

---

## 📝 API Integration Examples

### Integration with External Systems

```python
# After generating orders, send to department systems
orders = orchestrator.process_transcript(transcript)

for order in orders['orders_generated']:
    dept = order['department']
    order_id = order['order_id']
    
    # Send to department API
    send_to_department(dept, order_id, order)
```

---

## 🤝 Contributing

Suggestions for enhancement:
- Add more medical keywords
- Implement NER for better entity extraction
- Add NLP-based confidence scoring
- Integrate with hospital EHR systems
- Add audio transcript support

---

## 📞 Support

For issues or questions:
1. Check the **Intent Guide** for supported keywords
2. Run `demo.py` to see working examples
3. Adjust confidence threshold if getting false positives

---

## 📄 License

This project is created for hackathon purposes.

---

## ✨ Key Highlights

✅ **Eliminates Manual Order Entry** - Automatically detects and creates orders  
✅ **Real-Time Routing** - Orders reach departments instantly  
✅ **Smart Prioritization** - High-priority orders flagged automatically  
✅ **Complete History** - Track all processed transcripts and orders  
✅ **Confidence Scoring** - Know how confident the system is about each detection  
✅ **Department-Specific** - Auto-routes to correct department  
✅ **Easy Integration** - Simple Streamlit interface  

---

**Built for the Hackathon - Bringing Speed & Clarity to Healthcare Operations** 🚀

