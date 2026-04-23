import os
import random
import time

def run_sandbox(apk_path: str) -> dict:
    """
    Simulate running the APK in a sandbox environment.
    Returns a dictionary of sandbox analysis results.
    """
    apk_name = os.path.basename(apk_path)

    # Simulate install / launch / crash
    installed = True
    launched = True
    crashed = random.choice([False, False, True])  # small chance it crashes

    # Simulate some dynamic behavior flags
    dynamic_behaviors = [
        "sends_sms",
        "access_contacts",
        "access_location",
        "network_traffic",
        "executes_native_code",
        "creates_files",
        "modifies_system_settings",
        "access_camera"
    ]

    # Randomly choose behaviors to simulate
    observed_behaviors = random.sample(dynamic_behaviors, k=random.randint(0, 3))

    # Calculate a sandbox risk score based on behaviors
    sandbox_score = 0
    risk_weights = {
        "sends_sms": 20,
        "access_contacts": 15,
        "access_location": 10,
        "network_traffic": 15,
        "executes_native_code": 25,
        "creates_files": 10,
        "modifies_system_settings": 25,
        "access_camera": 15
    }
    for behavior in observed_behaviors:
        sandbox_score += risk_weights.get(behavior, 5)

    sandbox_score = min(sandbox_score, 100)

    # Simulate logs
    logs = [
        f"[INFO] Installing APK: {apk_name}",
        f"[INFO] Launching APK: {apk_name}",
    ]
    if crashed:
        logs.append(f"[ERROR] APK crashed during sandbox execution")
    logs.append(f"[INFO] Observed behaviors: {', '.join(observed_behaviors) if observed_behaviors else 'none'}")
    logs.append(f"[INFO] Sandbox risk score: {sandbox_score}%")

    result = {
        "installed": installed,
        "launched": launched,
        "crashed": crashed,
        "sandbox_score": sandbox_score,
        "observed_behaviors": observed_behaviors,
        "logs": logs
    }

    # Simulate runtime delay
    time.sleep(1)

    return result

# Quick test
if __name__ == "__main__":
    test_apk = "example.apk"
    sandbox_result = run_sandbox(test_apk)
    for key, value in sandbox_result.items():
        print(f"{key}: {value}")
