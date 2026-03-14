"""

Generates structured digital orders from detected intents
"""

import uuid
from datetime import datetime
from typing import Dict, Any, List
from intent_detector import Intent, IntentType

class DigitalOrder:
    """Represents a structured digital order/referral"""
    
    def __init__(
        self,
        order_type: str,
        patient_id: str,
        ordering_physician: str,
        department: str,
        items: List[str],
        details: str,
        priority: str = "routine"
    ):
        self.order_id = str(uuid.uuid4())[:8].upper()
        self.timestamp = datetime.now().isoformat()
        self.order_type = order_type  # "lab_test", "medication", "referral", etc.
        self.patient_id = patient_id
        self.ordering_physician = ordering_physician
        self.department = department
        self.items = items
        self.details = details
        self.priority = priority  # "routine", "urgent", "stat"
        self.status = "generated"  # "generated", "routed", "acknowledged", "completed"
        self.routing_log = []
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert order to dictionary"""
        return {
            "order_id": self.order_id,
            "timestamp": self.timestamp,
            "type": self.order_type,
            "patient_id": self.patient_id,
            "ordering_physician": self.ordering_physician,
            "department": self.department,
            "items": self.items,
            "details": self.details,
            "priority": self.priority,
            "status": self.status,
            "routing_log": self.routing_log
        }
    
    def update_status(self, new_status: str, message: str = ""):
        """Update order status with timestamp"""
        self.status = new_status
        self.routing_log.append({
            "timestamp": datetime.now().isoformat(),
            "status": new_status,
            "message": message
        })

class OrderGenerator:
    """Generates digital orders from detected intents"""
    
    # Department routing information
    DEPARTMENT_ROUTES = {
        "Laboratory": {
            "abbreviation": "LAB",
            "contact": "lab@hospital.local",
            "average_turnaround": "24 hours"
        },
        "Pharmacy": {
            "abbreviation": "PHARM",
            "contact": "pharmacy@hospital.local",
            "average_turnaround": "immediate"
        },
        "Radiology": {
            "abbreviation": "RAD",
            "contact": "radiology@hospital.local",
            "average_turnaround": "2-4 hours"
        },
        "Referrals": {
            "abbreviation": "REF",
            "contact": "referrals@hospital.local",
            "average_turnaround": "1-3 business days"
        },
        "Surgery/Procedures": {
            "abbreviation": "SURG",
            "contact": "surgery@hospital.local",
            "average_turnaround": "varies"
        }
    }
    
    def __init__(self, default_physician: str = "Dr. System"):
        self.default_physician = default_physician
        self.generated_orders = []
    
    def generate_order_from_intent(
        self,
        intent: Intent,
        patient_id: str,
        ordering_physician: str = None,
        department: str = None,
        priority: str = "routine"
    ) -> DigitalOrder:
        """
        Generate a structured order from a detected intent
        
        Args:
            intent: Detected Intent object
            patient_id: Patient identifier
            ordering_physician: Name of ordering physician
            department: Target department
            priority: Order priority level
            
        Returns:
            DigitalOrder object
        """
        if not ordering_physician:
            ordering_physician = self.default_physician
        
        # Determine department if not provided
        if not department:
            department = self._get_department_for_intent(intent)
        
        # Extract specific items from intent
        items = self._extract_items(intent)
        
        # Create order
        order = DigitalOrder(
            order_type=intent.type.value,
            patient_id=patient_id,
            ordering_physician=ordering_physician,
            department=department,
            items=items,
            details=intent.details,
            priority=priority
        )
        
        self.generated_orders.append(order)
        order.update_status("generated", f"Order created from transcript analysis")
        
        return order
    
    def generate_orders_batch(
        self,
        intents: List[Intent],
        patient_id: str,
        ordering_physician: str = None
    ) -> List[DigitalOrder]:
        """
        Generate multiple orders from a list of intents
        
        Args:
            intents: List of Intent objects
            patient_id: Patient identifier
            ordering_physician: Name of ordering physician
            
        Returns:
            List of DigitalOrder objects
        """
        orders = []
        for intent in intents:
            order = self.generate_order_from_intent(
                intent=intent,
                patient_id=patient_id,
                ordering_physician=ordering_physician
            )
            orders.append(order)
        
        return orders
    
    def _get_department_for_intent(self, intent: Intent) -> str:
        """Map intent type to department"""
        intent_to_dept = {
            IntentType.LAB_TEST: "Laboratory",
            IntentType.MEDICATION: "Pharmacy",
            IntentType.IMAGING: "Radiology",
            IntentType.REFERRAL: "Referrals",
            IntentType.PROCEDURE: "Surgery/Procedures"
        }
        return intent_to_dept.get(intent.type, "General")
    
    def _extract_items(self, intent: Intent) -> List[str]:
        """Extract specific items from detected intent text"""
        # Simple extraction - can be enhanced with NER
        text_lower = intent.item.lower()
        
        items = []
        
        # For lab tests
        if intent.type == IntentType.LAB_TEST:
            common_tests = {
                "blood test": "Blood Test",
                "CBC": "Complete Blood Count",
                "FBC": "Full Blood Count",
                "metabolic panel": "Metabolic Panel",
                "lipid panel": "Lipid Panel",
                "liver function": "Liver Function Test",
                "kidney function": "Kidney Function Test",
                "thyroid": "Thyroid Function Test",
                "TSH": "Thyroid Stimulating Hormone",
                "glucose": "Glucose Test",
                "HbA1c": "Hemoglobin A1c",
                "urinalysis": "Urinalysis"
            }
            for test_key, test_name in common_tests.items():
                if test_key.lower() in text_lower:
                    items.append(test_name)
        
        # For medications
        elif intent.type == IntentType.MEDICATION:
            common_meds = {
                "metformin": "Metformin",
                "lisinopril": "Lisinopril",
                "atorvastatin": "Atorvastatin",
                "aspirin": "Aspirin",
                "ibuprofen": "Ibuprofen",
                "amoxicillin": "Amoxicillin",
                "paracetamol": "Paracetamol",
                "acetaminophen": "Acetaminophen"
            }
            for med_key, med_name in common_meds.items():
                if med_key.lower() in text_lower:
                    items.append(med_name)
            
            # If no specific medication found, use generic
            if not items:
                items.append("Medication (TBD)")
        
        # For imaging
        elif intent.type == IntentType.IMAGING:
            if "X-ray" in intent.item or "x-ray" in text_lower:
                items.append("X-ray")
            elif "CT" in intent.item or "ct scan" in text_lower:
                items.append("CT Scan")
            elif "MRI" in intent.item or "mri" in text_lower:
                items.append("MRI")
            elif "ultrasound" in text_lower:
                items.append("Ultrasound")
            else:
                items.append("Imaging Study")
        
        # Default
        if not items:
            items.append(intent.item)
        
        return items
    
    def create_prescription_format(self, order: DigitalOrder) -> str:
        """
        Create formatted prescription/order text
        
        Args:
            order: DigitalOrder object
            
        Returns:
            Formatted prescription string
        """
        dept_info = self.DEPARTMENT_ROUTES.get(order.department, {})
        
        format_text = f"""
========================================================
                    DIGITAL ORDER FORM
========================================================
Order ID:           {order.order_id}
Order Type:         {order.order_type.upper()}
Department:         {order.department}
Timestamp:          {order.timestamp}
Priority:           {order.priority.upper()}
────────────────────────────────────────────────────────
Patient ID:         {order.patient_id}
Ordering Physician: {order.ordering_physician}
────────────────────────────────────────────────────────
ITEMS TO ORDER:
"""
        for idx, item in enumerate(order.items, 1):
            format_text += f"  {idx}. {item}\n"
        
        format_text += f"""
────────────────────────────────────────────────────────
CLINICAL DETAILS:
{order.details}
────────────────────────────────────────────────────────
ROUTING INFORMATION:
  Department Contact: {dept_info.get('contact', 'N/A')}
  Abbreviation:      {dept_info.get('abbreviation', 'N/A')}
  Est. Turnaround:    {dept_info.get('average_turnaround', 'N/A')}
────────────────────────────────────────────────────────
Status: {order.status.upper()}
========================================================
"""
        return format_text
    
    def get_orders_summary(self) -> Dict[str, Any]:
        """Get summary of all generated orders grouped by department"""
        summary = {
            "total_orders": len(self.generated_orders),
            "by_department": {},
            "by_type": {},
            "orders": [o.to_dict() for o in self.generated_orders]
        }
        
        for order in self.generated_orders:
            # By department
            if order.department not in summary["by_department"]:
                summary["by_department"][order.department] = 0
            summary["by_department"][order.department] += 1
            
            # By type
            if order.order_type not in summary["by_type"]:
                summary["by_type"][order.order_type] = 0
            summary["by_type"][order.order_type] += 1
        
        return summary
