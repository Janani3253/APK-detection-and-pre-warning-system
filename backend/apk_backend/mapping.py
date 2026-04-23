# mapping.py

APP_PERMISSION_PROFILES = {
    "TORCH": {
        "keywords": ["torch", "flash", "light", "flashlight"],
        "expected": {"android.permission.CAMERA"},
        "acceptable": {"android.permission.WAKE_LOCK"},
        "dangerous": {
            "android.permission.READ_CONTACTS",
            "android.permission.SEND_SMS",
            "android.permission.ACCESS_FINE_LOCATION",
            "android.permission.RECORD_AUDIO",
            "android.permission.READ_SMS",
            "android.permission.CALL_PHONE"
        }
    },

    "CONTACTS": {
        "keywords": ["contact", "dialer", "phone", "address book"],
        "expected": {"android.permission.READ_CONTACTS", "android.permission.WRITE_CONTACTS"},
        "acceptable": {"android.permission.INTERNET"},
        "dangerous": {
            "android.permission.READ_SMS",
            "android.permission.SEND_SMS",
            "android.permission.RECORD_AUDIO",
            "android.permission.ACCESS_FINE_LOCATION",
            "android.permission.CAMERA"
        }
    },

    "CHAT": {
        "keywords": ["chat", "message", "messenger", "whatsapp", "telegram", "signal", "discord", "skype"],
        "expected": {
            "android.permission.INTERNET",
            "android.permission.CAMERA",
            "android.permission.RECORD_AUDIO",
            "android.permission.READ_CONTACTS"
        },
        "acceptable": {"android.permission.ACCESS_NETWORK_STATE", "android.permission.VIBRATE"},
        "dangerous": {
            "android.permission.READ_SMS",
            "android.permission.SEND_SMS",
            "android.permission.ACCESS_FINE_LOCATION",
            "android.permission.WRITE_EXTERNAL_STORAGE"
        }
    },

    "GAME": {
        "keywords": ["game", "puzzle", "arcade", "fun", "gaming", "rpg", "action", "strategy", "casual"],
        "expected": {"android.permission.INTERNET", "android.permission.VIBRATE"},
        "acceptable": {"android.permission.WAKE_LOCK", "android.permission.BLUETOOTH", "android.permission.ACCESS_NETWORK_STATE"},
        "dangerous": {
            "android.permission.READ_CONTACTS",
            "android.permission.READ_SMS",
            "android.permission.ACCESS_FINE_LOCATION",
            "android.permission.RECORD_AUDIO",
            "android.permission.SEND_SMS",
            "android.permission.CAMERA"
        }
    },

    "FINANCE": {
        "keywords": ["bank", "wallet", "pay", "finance", "crypto", "bitcoin", "money", "transaction", "payment"],
        "expected": {"android.permission.INTERNET", "android.permission.READ_SMS", "android.permission.USE_BIOMETRIC"},
        "acceptable": {"android.permission.ACCESS_NETWORK_STATE"},
        "dangerous": {
            "android.permission.RECORD_AUDIO",
            "android.permission.READ_CONTACTS",
            "android.permission.ACCESS_FINE_LOCATION",
            "android.permission.SEND_SMS",
            "android.permission.WRITE_EXTERNAL_STORAGE",
            "android.permission.CAMERA"
        }
    },

   "UTILITY": {
    "keywords": ["utility", "tools", "manager", "app store", "fdroid", "file manager", "cleaner", "booster"],
    "expected": {
        "android.permission.INTERNET",
        "android.permission.READ_EXTERNAL_STORAGE",
        "android.permission.WRITE_EXTERNAL_STORAGE",
        "android.permission.REQUEST_INSTALL_PACKAGES",
        "android.permission.ACCESS_NETWORK_STATE"
    },
    "acceptable": {"android.permission.WAKE_LOCK", "android.permission.VIBRATE"},
    "dangerous": {
        "android.permission.READ_CONTACTS",
        "android.permission.RECORD_AUDIO",
        "android.permission.CAMERA",
        "android.permission.SEND_SMS",
        "android.permission.ACCESS_FINE_LOCATION",
        "android.permission.WRITE_SECURE_SETTINGS"
    }
    },

    "MEDIA": {
        "keywords": ["music", "video", "camera", "gallery", "photo", "media", "recorder", "player", "stream"],
        "expected": {
            "android.permission.CAMERA",
            "android.permission.RECORD_AUDIO",
            "android.permission.READ_EXTERNAL_STORAGE",
            "android.permission.WRITE_EXTERNAL_STORAGE"
        },
        "acceptable": {"android.permission.INTERNET", "android.permission.ACCESS_NETWORK_STATE", "android.permission.VIBRATE"},
        "dangerous": {
            "android.permission.READ_CONTACTS",
            "android.permission.SEND_SMS",
            "android.permission.ACCESS_FINE_LOCATION",
            "android.permission.READ_SMS"
        }
    },

    "SOCIAL": {
        "keywords": ["social", "network", "friends", "share", "community"],
        "expected": {"android.permission.INTERNET", "android.permission.READ_CONTACTS"},
        "acceptable": {"android.permission.CAMERA", "android.permission.RECORD_AUDIO"},
        "dangerous": {
            "android.permission.READ_SMS",
            "android.permission.SEND_SMS",
            "android.permission.ACCESS_FINE_LOCATION",
            "android.permission.WRITE_EXTERNAL_STORAGE"
        }
    },

    "HEALTH": {
        "keywords": ["health", "fitness", "tracker", "step", "heart", "wellness"],
        "expected": {"android.permission.BODY_SENSORS"},
        "acceptable": {"android.permission.INTERNET", "android.permission.ACCESS_FINE_LOCATION"},
        "dangerous": {
            "android.permission.READ_CONTACTS",
            "android.permission.READ_SMS",
            "android.permission.RECORD_AUDIO",
            "android.permission.SEND_SMS"
        }
    },

    "EDUCATION": {
        "keywords": ["education", "learn", "study", "school", "quiz", "tutorial"],
        "expected": {"android.permission.INTERNET"},
        "acceptable": {"android.permission.READ_EXTERNAL_STORAGE"},
        "dangerous": {
            "android.permission.READ_CONTACTS",
            "android.permission.SEND_SMS",
            "android.permission.ACCESS_FINE_LOCATION",
            "android.permission.CAMERA"
        }
    },

    "TRAVEL": {
        "keywords": ["maps", "travel", "navigation", "taxi", "ride"],
        "expected": {"android.permission.ACCESS_FINE_LOCATION", "android.permission.INTERNET"},
        "acceptable": {"android.permission.ACCESS_NETWORK_STATE"},
        "dangerous": {
            "android.permission.READ_CONTACTS",
            "android.permission.SEND_SMS",
            "android.permission.RECORD_AUDIO"
        }
    },

    "SHOPPING": {
        "keywords": ["shop", "ecommerce", "buy", "sell", "cart"],
        "expected": {"android.permission.INTERNET"},
        "acceptable": {"android.permission.ACCESS_NETWORK_STATE"},
        "dangerous": {
            "android.permission.READ_CONTACTS",
            "android.permission.SEND_SMS",
            "android.permission.ACCESS_FINE_LOCATION",
            "android.permission.CAMERA"
        }
    },

    "TRADING": {
        "keywords": ["stock", "crypto", "trade", "finance"],
        "expected": {"android.permission.INTERNET", "android.permission.READ_SMS"},
        "acceptable": {"android.permission.USE_BIOMETRIC"},
        "dangerous": {
            "android.permission.RECORD_AUDIO",
            "android.permission.READ_CONTACTS",
            "android.permission.SEND_SMS",
            "android.permission.ACCESS_FINE_LOCATION"
        }
    },

    "TOOLS": {
        "keywords": ["calculator", "converter", "tools", "utility"],
        "expected": set(),
        "acceptable": {"android.permission.INTERNET"},
        "dangerous": {
            "android.permission.CAMERA",
            "android.permission.READ_CONTACTS",
            "android.permission.SEND_SMS",
            "android.permission.ACCESS_FINE_LOCATION"
        }
    },

    "BROWSER": {
        "keywords": ["browser", "web", "chrome", "firefox", "safari", "internet"],
        "expected": {"android.permission.INTERNET"},
        "acceptable": {"android.permission.ACCESS_NETWORK_STATE", "android.permission.WRITE_EXTERNAL_STORAGE"},
        "dangerous": {
            "android.permission.CAMERA",
            "android.permission.RECORD_AUDIO",
            "android.permission.ACCESS_FINE_LOCATION",
            "android.permission.READ_CONTACTS"
        }
    },

    "NEWS": {
        "keywords": ["news", "feed", "article", "headline", "journal"],
        "expected": {"android.permission.INTERNET"},
        "acceptable": {"android.permission.ACCESS_NETWORK_STATE"},
        "dangerous": {
            "android.permission.CAMERA",
            "android.permission.RECORD_AUDIO",
            "android.permission.ACCESS_FINE_LOCATION",
            "android.permission.READ_CONTACTS",
            "android.permission.SEND_SMS"
        }
    },

    "WEATHER": {
        "keywords": ["weather", "forecast", "climate", "temperature"],
        "expected": {"android.permission.INTERNET", "android.permission.ACCESS_FINE_LOCATION"},
        "acceptable": {"android.permission.ACCESS_NETWORK_STATE"},
        "dangerous": {
            "android.permission.CAMERA",
            "android.permission.RECORD_AUDIO",
            "android.permission.READ_CONTACTS",
            "android.permission.SEND_SMS"
        }
    },

    "PRODUCTIVITY": {
        "keywords": ["productivity", "office", "document", "note", "task", "calendar"],
        "expected": {"android.permission.INTERNET", "android.permission.WRITE_EXTERNAL_STORAGE"},
        "acceptable": {"android.permission.READ_EXTERNAL_STORAGE", "android.permission.ACCESS_NETWORK_STATE"},
        "dangerous": {
            "android.permission.CAMERA",
            "android.permission.RECORD_AUDIO",
            "android.permission.ACCESS_FINE_LOCATION",
            "android.permission.READ_CONTACTS",
            "android.permission.SEND_SMS"
        }
    },

    "ENTERTAINMENT": {
        "keywords": ["entertainment", "movie", "tv", "stream", "video player"],
        "expected": {"android.permission.INTERNET", "android.permission.READ_EXTERNAL_STORAGE"},
        "acceptable": {"android.permission.ACCESS_NETWORK_STATE"},
        "dangerous": {
            "android.permission.CAMERA",
            "android.permission.RECORD_AUDIO",
            "android.permission.ACCESS_FINE_LOCATION",
            "android.permission.READ_CONTACTS"
        }
    },

    "SECURITY": {
        "keywords": ["security", "antivirus", "vpn", "password", "safe"],
        "expected": {"android.permission.INTERNET", "android.permission.REQUEST_INSTALL_PACKAGES"},
        "acceptable": {"android.permission.ACCESS_NETWORK_STATE"},
        "dangerous": {
            "android.permission.CAMERA",
            "android.permission.RECORD_AUDIO",
            "android.permission.ACCESS_FINE_LOCATION",
            "android.permission.READ_CONTACTS",
            "android.permission.SEND_SMS",
            "android.permission.WRITE_SECURE_SETTINGS"
        }
    }
}