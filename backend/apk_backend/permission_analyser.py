# permission_analyser.py
from mapping import APP_PERMISSION_PROFILES

# Define weights for dangerous permissions (example)
DANGEROUS_PERMISSION_WEIGHTS = {
    "READ_CONTACTS": 5,
    "WRITE_CONTACTS": 5,
    "SEND_SMS": 8,
    "READ_SMS": 7,
    "ACCESS_FINE_LOCATION": 6,
    "RECORD_AUDIO": 8,
    "REQUEST_INSTALL_PACKAGES": 10,
    "WRITE_EXTERNAL_STORAGE": 5,
    "READ_EXTERNAL_STORAGE": 5,
    "CAMERA": 5,
    "INTERNET": 3,
    "BLUETOOTH": 2,
    "WAKE_LOCK": 1,
    "FOREGROUND_SERVICE": 2,
    # Add more as needed
}

def ANALYSER(category: str, app_permissions: set, signature_trust: float = 0.0):
    """
    Analyze APK permissions, calculate granular risk score.

    Args:
        category: app category (from app_classifier)
        app_permissions: set of permissions from APK
        signature_trust: 0.0–0.3 for reduction based on signature

    Returns:
        Dictionary with:
            - expected
            - acceptable
            - dangerous
            - risk_score (0–100, realistic)
    """
    if category not in APP_PERMISSION_PROFILES:
        category = "UTILITY"

    profile = APP_PERMISSION_PROFILES[category]

    expected = profile.get("expected", set())
    acceptable = profile.get("acceptable", set())
    dangerous_profile = profile.get("dangerous", set())

    actual_expected = []
    actual_acceptable = []
    actual_dangerous = []
    total_weight = 0
    dangerous_weight = 0

    for perm in app_permissions:
        if perm in expected:
            actual_expected.append(perm)
            total_weight += 0
        elif perm in acceptable:
            actual_acceptable.append(perm)
            weight = DANGEROUS_PERMISSION_WEIGHTS.get(perm, 2)
            total_weight += weight
        else:
            actual_dangerous.append(perm)
            weight = DANGEROUS_PERMISSION_WEIGHTS.get(perm, 5)
            total_weight += weight
            dangerous_weight += weight

    # Avoid division by zero
    if total_weight == 0:
        risk_score = 0
    else:
        risk_score = (dangerous_weight / total_weight) * 100

    # Apply signature trust reduction
    if signature_trust > 0:
        risk_score = risk_score * (1 - signature_trust)

    return {
        "expected": actual_expected,
        "acceptable": actual_acceptable,
        "dangerous": actual_dangerous,
        "risk_score": round(risk_score, 2)
    }