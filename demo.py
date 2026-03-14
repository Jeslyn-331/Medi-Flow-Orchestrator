"""


"""

import sys
import io

# Fix Unicode encoding for Windows
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


from intent_detector import IntentType
import json

def main():

    
    print("\n" + "="*70)

    print("="*70)
    


    
    # Test cases
    test_transcripts = [
        {
            "name": "Case 1: Pneumonia Evaluation",
            "patient_id": "P-2026-001",
            "transcript": """
            Patient James Wilson, 45-year-old male, presents with persistent cough 
            and shortness of breath for 3 days. On examination: fever (38.5°C), 
            crackles in bilateral lower lobes. Oxygen saturation 92% on room air.
            
            Impression: Suspected community-acquired pneumonia pending confirmation.
            
            MANAGEMENT PLAN:
            1. Order CBC, metabolic panel, and blood cultures to assess infection
            2. Request chest X-ray PA and lateral views for diagnosis confirmation
            3. Start on amoxicillin-clavulanate 500mg-125mg three times daily for 7 days
            4. Consider referral to pulmonology if symptoms worsen or don't improve in 5 days
            5. Follow-up chest X-ray in 2 weeks to ensure resolution
            6. Schedule follow-up consultation in one week
            """
        },
        {
            "name": "Case 2: Diabetes Management",
            "patient_id": "P-2026-002",
            "transcript": """
            Patient Maria Garcia, 58-year-old female with Type 2 diabetes.
            HbA1c 8.2%, which is above target.
            
            Physical examination: BMI 32, BP 142/88 mmHg
            
            Plan:
            1. Order comprehensive metabolic panel and lipid profile
            2. Prescribe metformin 1000mg twice daily with meals
            3. Also prescribe atorvastatin 40mg daily for cholesterol management
            4. Referral to endocrinology for specialized diabetes care
            5. Schedule ophthalmology for diabetic retinopathy screening
            6. Request glucose monitoring log from patient before next visit
            """
        },
        {
            "name": "Case 3: Post-Operative Care",
            "patient_id": "P-2026-003",
            "transcript": """
            Follow-up visit for Robert Chen post hernia repair surgery (3 days post-op).
            Wound appears clean, no signs of infection.
            Pain well-controlled with current analgesics.
            
            Assessment: Normal post-operative course
            
            Plan:
            1. Take blood for CBC to check for anemia
            2. Perform abdominal ultrasound to rule out seroma formation
            3. Prescribe ibuprofen 400mg three times daily with food
            4. Prescribe acetaminophen 500mg for breakthrough pain
            5. Refer to general surgery clinic for wound check in 1 week
            6. Continue current activity restrictions until cleared
            """
        }
    ]
    
    # Process each test case
    all_results = []
    workload = {}
    
    for i, test_case in enumerate(test_transcripts, 1):
        print(f"\n\n{'='*70}")
        print(f"Processing: {test_case['name']}")
        print(f"{'='*70}\n")
        
        # Simulate intent/order detection (replace with actual function call)
        # result = process_transcript_intent(test_case["transcript"], test_case["patient_id"], ordering_physician="Dr. Sarah Johnson", auto_route=True)
        result = {
            'intents_detected': [
                {'type': 'Lab Test', 'department': 'Laboratory'},
                {'type': 'Prescription', 'department': 'Pharmacy'}
            ],
            'orders_generated': [
                {'order_id': f"ORD-{i}-LAB", 'type': 'Lab Test', 'department': 'Laboratory', 'items': ['CBC', 'Metabolic Panel'], 'patient_id': test_case['patient_id'], 'ordering_physician': 'Dr. Sarah Johnson', 'details': '', 'priority': 'Normal'},
                {'order_id': f"ORD-{i}-RX", 'type': 'Prescription', 'department': 'Pharmacy', 'items': ['Amoxicillin', 'Metformin'], 'patient_id': test_case['patient_id'], 'ordering_physician': 'Dr. Sarah Johnson', 'details': '', 'priority': 'Normal'}
            ],
            'summary': {
                'intents_count': 2,
                'orders_count': 2,
                'departments_involved': ['Laboratory', 'Pharmacy']
            }
        }
        all_results.append(result)
        
        # Display report
        report = f"Transcript: {test_case['transcript']}\nPatient ID: {test_case['patient_id']}"
        print(report)
        
        # Summary
        print(f"SUMMARY:")
        print(f"  Intents Detected: {result['summary']['intents_count']}")
        print(f"  Orders Generated: {result['summary']['orders_count']}")
        print(f"  Departments Involved: {', '.join(result['summary']['departments_involved'])}")
        
        # Orders details
        if result['orders_generated']:
            print(f"\n  Generated Orders:")
            for order in result['orders_generated']:
                print(f"    • {order['order_id']}: {order['type'].upper()} → {order['department']}")
                print(f"      Items: {', '.join(order['items'])}")
                # Track workload
                workload[order['department']] = workload.get(order['department'], 0) + 1
    
    # Overall statistics
    print(f"\n\n{'='*70}")
    print(f"{'='*70}\n")
    
    total_intents = sum(len(r['intents_detected']) for r in all_results)
    total_orders = sum(len(r['orders_generated']) for r in all_results)
    
    print(f"Total Transcripts Processed: {len(test_transcripts)}")
    print(f"Total Intents Detected: {total_intents}")
    print(f"Total Orders Generated: {total_orders}")
    print(f"\nDepartment Workload Distribution:")
    for dept, count in sorted(workload.items(), key=lambda x: x[1], reverse=True):
        print(f"  • {dept}: {count} orders")
    
    # Intent type distribution
    print(f"\nIntent Type Distribution:")
    intent_counts = {}
    for result in all_results:
        for intent in result['intents_detected']:
            intent_type = intent['type']
            intent_counts[intent_type] = intent_counts.get(intent_type, 0) + 1
    for intent_type, count in sorted(intent_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  • {intent_type}: {count} detections")
    
    # Sample order output
    print(f"\n\n{'='*70}")
    print("SAMPLE FORMATTED ORDER")
    print(f"{'='*70}\n")
    if all_results and all_results[0]['orders_generated']:
        sample_order = all_results[0]['orders_generated'][0]
        # Re-create order object to show formatted output
        from order_generator import DigitalOrder, OrderGenerator
        order = DigitalOrder(
            order_type=sample_order['type'],
            patient_id=sample_order['patient_id'],
            ordering_physician=sample_order['ordering_physician'],
            department=sample_order['department'],
            items=sample_order['items'],
            details=sample_order['details'],
            priority=sample_order['priority']
        )
        generator = OrderGenerator()
        formatted = generator.create_prescription_format(order)
        print(formatted)
    print(f"\n{'='*70}")
    print("DEMO COMPLETE")
    print(f"{'='*70}\n")

if __name__ == "__main__":
    main()
