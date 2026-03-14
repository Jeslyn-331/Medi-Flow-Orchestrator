"""

Detects clinical intents (tests, medications, referrals) from transcripts
"""

import re
from typing import List, Dict, Tuple
from enum import Enum

class IntentType(Enum):
    """Types of medical intents"""
    LAB_TEST = "lab_test"
    MEDICATION = "medication"
    REFERRAL = "referral"
    IMAGING = "imaging"
    PROCEDURE = "procedure"

class Intent:
    """Represents a detected intent from clinical transcript"""
    def __init__(self, intent_type: IntentType, item: str, details: str, confidence: float):
        self.type = intent_type
        self.item = item
        self.details = details
        self.confidence = confidence
    
    def to_dict(self):
        return {
            "type": self.type.value,
            "item": self.item,
            "details": self.details,
            "confidence": self.confidence
        }

class IntentDetector:
    """Detects medical intents from clinical transcripts"""
    
    # Keywords mapping for intent detection
    INTENT_KEYWORDS = {
        IntentType.LAB_TEST: {
            "keywords": [
                "blood test", "CBC", "FBC", "metabolic panel", "lipid panel",
                "liver function", "kidney function", "thyroid", "TSH", "glucose",
                "HbA1c", "urinalysis", "culture", "serology", "antibody",
                "order.*test", "lab.*test", "request.*test", "send.*lab",
                "take.*blood", "draw.*blood", "PT", "INR", "platelet", "creatinine",
                "BUN", "albumin", "bilirubin", "electrolytes"
            ],
            "department": "Laboratory"
        },
        IntentType.MEDICATION: {
            "keywords": [
                "prescribe", "prescription", "medication", "drug", "give",
                "administer", "metformin", "lisinopril", "atorvastatin", "aspirin",
                "ibuprofen", "amoxicillin", "start.*on", "begin.*on", "put.*on",
                "antibiotic", "paracetamol", "acetaminophen", "diclofenac"
            ],
            "department": "Pharmacy"
        },
        IntentType.IMAGING: {
            "keywords": [
                "X-ray", "CT scan", "MRI", "ultrasound", "echocardiogram",
                "chest.*X-ray", "CT.*abdomen", "brain.*MRI", "order.*imaging",
                "imaging study", "radiograph", "radiologic", "scan"
            ],
            "department": "Radiology"
        },
        IntentType.REFERRAL: {
            "keywords": [
                "refer", "consultation", "specialist", "cardiology", "dermatology",
                "neurology", "orthopedics", "ophthalmology", "ENT", "refer.*to",
                "send.*to", "consult.*with", "see.*specialist"
            ],
            "department": "Referrals"
        },
        IntentType.PROCEDURE: {
            "keywords": [
                "procedure", "surgery", "operation", "biopsy", "endoscopy",
                "colonoscopy", "ultrasound", "catheterization", "angiogram",
                "perform", "conduct", "schedule"
            ],
            "department": "Surgery/Procedures"
        }
    }

    def __init__(self, confidence_threshold: float = 0.5):
        """
        Initialize intent detector
        
        Args:
            confidence_threshold: Minimum confidence score (0-1) to report an intent
        """
        self.confidence_threshold = confidence_threshold
        self._compile_patterns()
    
    def _compile_patterns(self):
        """Compile regex patterns for all keywords"""
        self.patterns = {}
        for intent_type, config in self.INTENT_KEYWORDS.items():
            patterns = []
            for keyword in config["keywords"]:
                # Create case-insensitive regex pattern
                patterns.append(re.compile(re.escape(keyword), re.IGNORECASE))
            self.patterns[intent_type] = patterns
    
    def detect_intents(self, transcript: str) -> List[Intent]:
        """
        Detect all intents from a clinical transcript
        
        Args:
            transcript: Clinical transcript text
            
        Returns:
            List of detected Intent objects
        """
        intents = []
        detections = {}  # Track detections by type
        
        # Search for each intent type
        for intent_type, patterns in self.patterns.items():
            for pattern in patterns:
                matches = pattern.finditer(transcript)
                for match in matches:
                    # Calculate context window for details
                    start = max(0, match.start() - 100)
                    end = min(len(transcript), match.end() + 100)
                    context = transcript[start:end].strip()
                    
                    # Store detection info
                    if intent_type not in detections:
                        detections[intent_type] = []
                    
                    detections[intent_type].append({
                        "match": match.group(),
                        "context": context
                    })
        
        # Create Intent objects from detections
        for intent_type, detections_list in detections.items():
            for detection in detections_list:
                # Calculate confidence based on specificity
                confidence = self._calculate_confidence(detection["match"], intent_type)
                
                if confidence >= self.confidence_threshold:
                    intent = Intent(
                        intent_type=intent_type,
                        item=detection["match"],
                        details=detection["context"],
                        confidence=confidence
                    )
                    intents.append(intent)
        
        return intents
    
    def _calculate_confidence(self, matched_text: str, intent_type: IntentType) -> float:
        """
        Calculate confidence score for a detected intent
        
        Args:
            matched_text: The text that matched
            intent_type: Type of intent detected
            
        Returns:
            Confidence score between 0 and 1
        """
        # Base confidence: 0.7 for direct keyword match
        confidence = 0.7
        
        # Boost confidence for specific medial terms
        if len(matched_text) > 4:
            confidence += 0.15
        
        # More specific patterns get higher confidence
        if intent_type == IntentType.LAB_TEST and any(x in matched_text.upper() for x in ["CBC", "FBC", "TSH"]):
            confidence += 0.15
        elif intent_type == IntentType.MEDICATION and any(x in matched_text.lower() for x in ["prescribe", "prescription"]):
            confidence += 0.15
        
        return min(1.0, confidence)
    
    def get_department(self, intent_type: IntentType) -> str:
        """Get the department responsible for an intent type"""
        return self.INTENT_KEYWORDS[intent_type]["department"]

    def extract_with_context(self, transcript: str, intent_type: IntentType) -> Dict:
        """
        Extract intents of a specific type with full context
        
        Args:
            transcript: Clinical transcript
            intent_type: Type of intent to extract
            
        Returns:
            Dictionary with extracted information
        """
        intents = self.detect_intents(transcript)
        filtered = [i for i in intents if i.type == intent_type]
        
        return {
            "intent_type": intent_type.value,
            "department": self.get_department(intent_type),
            "count": len(filtered),
            "intents": [i.to_dict() for i in filtered]
        }
