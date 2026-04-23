# main.py
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from androguard.core.apk import APK
from androguard.core.axml import AXMLPrinter
import os
from app_classifier import detect_app_category
from permission_analyser import ANALYSER
from sandbox import run_sandbox  # <- SANDBOX IMPORT

app = FastAPI()

UPLOAD_DIR = "uploads"
REPORTS_DIR = "reports"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)

# ---------------- SAFE TEXT ----------------
def safe_text(text):
    if not text:
        return ""
    return "".join(c if 32 <= ord(c) <= 126 else "?" for c in str(text))

def safe_list(items):
    return [safe_text(i) for i in items if i]

def get_verdict(risk_score: float) -> str:
    if risk_score <= 10:
        return "SAFE"
    elif risk_score <= 30:
        return "SOMEWHAT_SAFE"
    elif risk_score <= 55:
        return "SUSPICIOUS"
    elif risk_score <= 75:
        return "HIGH_RISK"
    else:
        return "MALICIOUS"

# ---------------- STATIC ANALYSIS ----------------
def detect_malicious_indicators(apk_obj):
    indicators = {
        "suspicious_permissions": [],
        "hidden_components": [],
        "risk_factors": []
    }

    dangerous_perms = {
        "android.permission.REQUEST_INSTALL_PACKAGES": "Can install other apps",
        "android.permission.SYSTEM_ALERT_WINDOW": "Overlay apps risk",
        "android.permission.WRITE_SECURE_SETTINGS": "Modify system settings",
        "android.permission.BIND_DEVICE_ADMIN": "Device admin privileges",
        "android.permission.PACKAGE_USAGE_STATS": "Access app usage data"
    }

    permissions = apk_obj.get_permissions()
    for perm in permissions:
        if perm in dangerous_perms:
            indicators["suspicious_permissions"].append({
                "permission": perm,
                "risk": dangerous_perms[perm]
            })

    activities = apk_obj.get_activities()
    for activity in activities:
        if "hidden" in activity.lower() or "overlay" in activity.lower():
            indicators["hidden_components"].append(activity)

    try:
        axml = apk_obj.get_android_manifest_axml()
        if axml:
            ap = AXMLPrinter(axml.get_buff())
            manifest_xml = ap.get_xml()
            if "android:debuggable" in manifest_xml and "true" in manifest_xml:
                indicators["risk_factors"].append("App is debuggable")
    except:
        pass

    if os.path.getsize(apk_obj.filename) < 100000:
        indicators["risk_factors"].append("Unusually small APK size")

    return indicators

# ---------------- PDF GENERATION ----------------
def generate_pdf(report_path, apk, category, analysis, signature, malicious_indicators):
    try:
        from fpdf import FPDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(True, 15)
        pdf.set_font("Arial", size=12)

        pdf.cell(0, 10, "APK SECURITY ANALYSIS REPORT", ln=True)
        pdf.ln(5)
        pdf.cell(0, 8, f"App Name: {safe_text(apk['app_name'])}", ln=True)
        pdf.cell(0, 8, f"Package: {safe_text(apk['package_name'])}", ln=True)
        pdf.cell(0, 8, f"Version: {safe_text(apk['version_name'])}", ln=True)
        pdf.cell(0, 8, f"Category: {safe_text(category)}", ln=True)
        pdf.cell(0, 8, f"Signature: {safe_text(signature)}", ln=True)
        pdf.cell(0, 8, f"Risk Score: {analysis['risk_score']}%", ln=True)

        pdf.ln(5)
        pdf.cell(0, 8, "Expected Permissions:", ln=True)
        pdf.multi_cell(0, 8, ", ".join(safe_list(analysis["expected"])))
        pdf.ln(3)
        pdf.cell(0, 8, "Acceptable Permissions:", ln=True)
        pdf.multi_cell(0, 8, ", ".join(safe_list(analysis["acceptable"])))
        pdf.ln(3)
        pdf.cell(0, 8, "Dangerous Permissions:", ln=True)
        pdf.multi_cell(0, 8, ", ".join(safe_list(analysis["dangerous"])))

        if malicious_indicators["suspicious_permissions"] or malicious_indicators["hidden_components"] or malicious_indicators["risk_factors"]:
            pdf.ln(5)
            pdf.cell(0, 8, "Malicious Indicators Detected:", ln=True)
            if malicious_indicators["suspicious_permissions"]:
                pdf.ln(3)
                pdf.cell(0, 8, "Suspicious Permissions:", ln=True)
                for perm in malicious_indicators["suspicious_permissions"]:
                    pdf.multi_cell(0, 8, f"- {perm['permission']}: {perm['risk']}")
            if malicious_indicators["hidden_components"]:
                pdf.ln(3)
                pdf.cell(0, 8, "Hidden Components:", ln=True)
                pdf.multi_cell(0, 8, ", ".join(safe_list(malicious_indicators["hidden_components"])))
            if malicious_indicators["risk_factors"]:
                pdf.ln(3)
                pdf.cell(0, 8, "Risk Factors:", ln=True)
                for factor in malicious_indicators["risk_factors"]:
                    pdf.cell(0, 8, f"- {factor}", ln=True)

        pdf.output(report_path)
        return True
    except Exception as e:
        print("PDF generation failed:", e)
        return False

# ---------------- ROOT ----------------
@app.get("/")
def root():
    return {"status": "APK Analyzer backend running 🚀"}

# ---------------- UPLOAD & ANALYZE APK ----------------
@app.post("/upload-apk")
async def upload_apk(file: UploadFile = File(...)):
    if not file.filename.endswith(".apk"):
        raise HTTPException(status_code=400, detail="Only APK files allowed")

    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())

    try:
        apk_obj = APK(file_path)
        apk_details = {
            "app_name": apk_obj.get_app_name(),
            "package_name": apk_obj.get_package(),
            "version_name": apk_obj.get_androidversion_name(),
            "version_code": apk_obj.get_androidversion_code(),
            "permissions": apk_obj.get_permissions(),
            "file_size_mb": round(os.path.getsize(file_path) / (1024 * 1024), 2),
            "file": file.filename
        }

        category = detect_app_category(apk_details["app_name"], apk_details["package_name"])
        analysis = ANALYSER(category, set(apk_details["permissions"]))

        # ---------------- SANDBOX ANALYSIS ----------------
        sandbox_result = run_sandbox(file_path)
        analysis["sandbox"] = sandbox_result  # store sandbox output in analysis

        malicious_indicators = detect_malicious_indicators(apk_obj)

        additional_risk = len(malicious_indicators["suspicious_permissions"]) * 5 + \
                          len(malicious_indicators["hidden_components"]) * 10 + \
                          len(malicious_indicators["risk_factors"]) * 15
        analysis["risk_score"] = min(100, analysis["risk_score"] + additional_risk)

        if apk_obj.is_signed():
            signature = "Valid Signature"
            analysis["risk_score"] = max(0, round(analysis["risk_score"] * 0.65, 2))
        else:
            signature = "Invalid / Unknown Signature"

        verdict = get_verdict(analysis["risk_score"])

        report_name = f"{apk_details['package_name']}_report.pdf"
        report_path = os.path.join(REPORTS_DIR, report_name)
        pdf_created = generate_pdf(report_path, apk_details, category, analysis, signature, malicious_indicators)

        host_ip = os.environ.get('HOST_IP', '127.0.0.1')

        return {
            "message": "APK uploaded and analyzed ✅",
            "apk_details": apk_details,
            "app_category": category,
            "permission_analysis": analysis,
            "malicious_indicators": malicious_indicators,
            "signature": signature,
            "verdict": verdict,
            "warning": f"This APK has been classified as {verdict}. " +
                       ("Proceed with caution!" if verdict in ["HIGH_RISK", "MALICIOUS"] else "Appears safe to install."),
            "report_path": f"http://{host_ip}:8000/reports/{report_name}" if pdf_created else None
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"APK processing failed: {str(e)}")

# ---------------- SERVE PDF REPORTS ----------------
@app.get("/reports/{filename}")
def get_report(filename: str):
    path = os.path.join(REPORTS_DIR, filename)
    if os.path.exists(path):
        return FileResponse(path, media_type='application/pdf', filename=filename)
    raise HTTPException(status_code=404, detail="Report not found")
