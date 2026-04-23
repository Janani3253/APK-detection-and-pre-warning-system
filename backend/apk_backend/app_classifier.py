# app_classifier.py
from mapping import APP_PERMISSION_PROFILES

def detect_app_category(app_name: str, package_name: str) -> str:
    """Detect the app category based on app name or package name keywords."""
    name = app_name.lower()
    package = package_name.lower()

    for category, profile in APP_PERMISSION_PROFILES.items():
        for keyword in profile["keywords"]:
            if keyword.lower() in name or keyword.lower() in package:
                return category
    return "UTILITY"  # fallback if nothing matches