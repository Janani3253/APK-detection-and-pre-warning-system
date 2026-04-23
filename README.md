# 📱 APK Detection and Pre-Warning System

## 📌 Overview

The **APK Detection and Pre-Warning System** is a mobile + backend application designed to analyze Android APK files and identify potential security risks before installation.

It provides **early warnings** about malicious behavior by analyzing permissions, running classification logic, and simulating sandbox checks.

---

## 🧱 Project Structure

```
APK-detection-and-pre-warning-system/
│
├── frontend/        # Flutter mobile application
├── backend/         # Python (FastAPI) backend
└── README.md
```

---

## 🚀 Features

* 🔍 APK analysis before installation
* ⚠️ Pre-warning system for suspicious apps
* 🔐 Permission-based risk detection
* 🧠 Classification of APK behavior
* 🧪 Sandbox execution support
* 📱 User-friendly mobile interface

---

## 🛠️ Tech Stack

### Frontend

* Flutter (Dart)

### Backend

* Python
* FastAPI
* Uvicorn

---

## ⚙️ Setup Instructions

---

### 📱 Run Frontend (Flutter)

```bash
flutter clean
flutter pub get
flutter run
```

---

### ⚙️ Run Backend (Python - FastAPI)

#### 1. Activate Virtual Environment

**Windows:**

```bash
.venv\Scripts\activate
```

**Mac/Linux:**

```bash
source .venv/bin/activate
```

---

#### 2. Start Backend Server

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

---

## 🔗 API Endpoint

* Base URL:

```
http://localhost:8000
```

---

## 📂 Important Notes

* Do NOT upload:

  * `venv/` or `.venv/`
  * `__pycache__/`
  * APK files or large uploads
* Ensure `requirements.txt` is included for backend setup

---

## 🧪 How It Works

1. User uploads APK via mobile app
2. Backend processes APK
3. Permission analysis is performed
4. Classification model evaluates risk
5. Sandbox simulation runs (if applicable)
6. Result is returned with warning level

---

