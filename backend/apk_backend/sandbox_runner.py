# sandbox_runner.py

import os
import random
import time

def run_sandbox(apk_path: str) -> dict:
    """
    Simulate running an APK in a sandbox environment.
    
    Args:
        apk_path: Path to the APK file.
        
    Returns:
        Dictionary with sandbox results.
    """

    if not os.path.exists(apk_path):
        raise FileNotFoundError(f"APK not found at path: {apk_path}")

    # Simulate some delay as if the APK is being executed in a sandbox
    time.sleep(2)

    # Generate random but structured sandbox results
    # In a real sandbox, you'd check network calls, API usage, file system access, etc.
    possible_behaviors = [
        "Accessed contacts",
        "Sent SMS",
        "Read location",
        "Tried to request install packages",
        "Opened camera",
        "Accessed microphone",
        "Connected to external server",
        "No malicious behavior observed"
    ]

    behavior_detected = random.choices(
        possible_behaviors, 
        weights=[3, 2, 2, 1, 2, 2, 1, 5], 
        k=random.randint(1, 3)
    )

    # Flag as malicious if any high-risk behavior found
    malicious_keywords = [
        "Sent SMS",
        "Tried to request install packages",
        "Accessed contacts",
        "Read location",
        "Connected to external server"
    ]
    is_malicious = any(b in malicious_keywords for b in behavior_detected)

    risk_score = random.randint(5, 50) + (30 if is_malicious else 0)
    risk_score = min(risk_score, 100)

    result = {
        "sandbox_behaviors": behavior_detected,
        "is_malicious": is_malicious,
        "sandbox_risk_score": risk_score
    }

    return result

# Quick test
if __name__ == "__main__":
    test_apk = "uploads/example.apk"
    print(run_sandbox(test_apk))
