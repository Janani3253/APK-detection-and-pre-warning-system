import 'package:flutter/material.dart';

class AppLang extends ChangeNotifier {
  static final AppLang instance = AppLang();

  String current = 'en';

  void switchLang(String lang) {
    current = lang;
    notifyListeners(); // 🔥 tells Flutter to rebuild
  }

  String t(String key) {
    return _localizedValues[current]?[key] ??
        _localizedValues['en']?[key] ??
        key;
  }

  static const Map<String, Map<String, String>> _localizedValues = {
    'en': {
      'app_title': 'APK Secure Analyzer',
      'select_apk': 'Select APK File',
      'analyze': 'Analyze APK',
      'analyzing': 'Analyzing APK...',
      'analysis_complete': 'Analysis Complete',

      // Permissions
      'permissions': 'Expected Permissions',
      'acceptable_permissions': 'Acceptable Permissions',
      'dangerous_permissions': 'Dangerous Permissions',

      // Risk & Verdict
      'risk_score': 'Risk Score',
      'verdict': 'Final Verdict',
      'high_risk': 'HIGH RISK',
      'medium_risk': 'MEDIUM RISK',
      'low_risk': 'LOW RISK',

      // Sandbox
      'sandbox': 'Sandbox Analysis',
      'sandbox_logs': 'Sandbox Logs',
      'installed': 'Installed',
      'launched': 'Launched',
      'crashed': 'Crashed',

      // Buttons
      'download_report': 'Download PDF Report',
      'yes': 'Yes',
      'no': 'No',

      // Messages
      'warning_high':
      '⚠️ This app is highly risky. Installing it may harm your device.',
      'no_permissions': 'No suspicious permissions found',
      'home_hint': 'Upload an APK to start security analysis',
      'error': 'Something went wrong',
    },

    'ta': {
      'app_title': 'APK Secure Analyzer',
      'select_apk': 'APK கோப்பை தேர்ந்தெடுக்கவும்',
      'analyze': 'APK பகுப்பாய்வு செய்யவும்',
      'analyzing': 'APK பகுப்பாய்வு செய்யப்படுகிறது...',
      'analysis_complete': 'பகுப்பாய்வு முடிந்தது',

      // Permissions
      'permissions': 'எதிர்பார்க்கப்படும் அனுமதிகள்',
      'acceptable_permissions': 'ஏற்றுக்கொள்ளத்தக்க அனுமதிகள்',
      'dangerous_permissions': 'ஆபத்தான அனுமதிகள்',

      // Risk & Verdict
      'risk_score': 'ஆபத்து மதிப்பெண்',
      'verdict': 'இறுதி முடிவு',
      'high_risk': 'உயர் ஆபத்து',
      'medium_risk': 'மிதமான ஆபத்து',
      'low_risk': 'குறைந்த ஆபத்து',

      // Sandbox
      'sandbox': 'Sandbox பகுப்பாய்வு',
      'sandbox_logs': 'Sandbox பதிவு குறிப்புகள்',
      'installed': 'நிறுவப்பட்டது',
      'launched': 'தொடங்கப்பட்டது',
      'crashed': 'முறிந்தது',

      // Buttons
      'download_report': 'PDF அறிக்கையை பதிவிறக்கவும்',
      'yes': 'ஆம்',
      'no': 'இல்லை',

      // Messages
      'warning_high':
      '⚠️ இந்த செயலி மிக அதிக ஆபத்தானது. உங்கள் சாதனத்திற்கு சேதம் விளைவிக்கலாம்.',
      'no_permissions': 'ஆபத்தான அனுமதிகள் எதுவும் இல்லை',
      'home_hint': 'பாதுகாப்பு பகுப்பாய்வை தொடங்க APK ஐ பதிவேற்றவும்',
      'error': 'பிழை ஏற்பட்டுள்ளது',
    },
  };
}
