# 🚨 Voice-Activated SOS Alert & Location Sharing System

## 📌 Problem We Are Solving

During an emergency, a person may not have enough time to unlock their phone,
type a message, and manually share their location.

This project provides a **quick SOS mechanism** where the user can simply say
**"Help me"** to trigger an emergency alert with their location.

---

## 📝 Short Description

A **Python-based voice-activated SOS system** that:

- 🎤 Detects the voice command **"Help me"**
- 📍 Gets the latest latitude and longitude
- 🗺️ Generates a Google Maps location link
- 🚨 Creates an emergency message
- 💻 Prints the emergency message in the terminal

> **Current Prototype:** Simulated GPS coordinates are used because a physical
> GPS module was not available.

> In the future, the simulated coordinates can be replaced with a real GPS
> module.

---

## 🔄 Project Workflow

```text
                         👤 USER
                            │
                            │ Says "Help me"
                            ▼
                   🎤 SPEECH RECOGNITION
                            │
                            ▼
                       🚨 SOS DETECTION
                            │
                            ▼
                     📍 REQUEST LOCATION
                            │
                            ▼
                  ┌─────────────────────┐
                  │    FLASK SERVER     │
                  │                     │
                  │  Simulated GPS      │
                  │    Coordinates      │
                  └──────────┬──────────┘
                             │
                             ▼
                    📍 LATITUDE + LONGITUDE
                             │
                             ▼
                       🗺️ GOOGLE MAPS
                             │
                             ▼
                    🚨 EMERGENCY MESSAGE
                             │
                             ▼
                        💻 TERMINAL
```

---

## 🛠️ Tech Stack

```text
🐍 Python
    │
    ├── 🖥️ Tkinter
    │      └── Graphical User Interface
    │
    ├── 🎤 SpeechRecognition
    │      └── Voice Command Detection
    │
    ├── 🌐 Flask
    │      └── Simulated GPS Location Server
    │
    ├── 🔗 Requests
    │      └── Communication with Flask Server
    │
    ├── 🗺️ Google Maps
    │      └── Location Visualization
    │
    └── 🧵 Threading
           └── Keeps GUI Responsive
```

---

## 🔌 Flask API

### `POST /location`

Receives the **simulated GPS coordinates**.

```json
{
    "latitude": 18.5230,
    "longitude": 73.8590
}
```

The Flask server stores the latest latitude and longitude.

```text
GPS / Simulator
       │
       │ POST /location
       ▼
Flask Server
       │
       ▼
Stores Latest
Latitude + Longitude
```

### `GET /latest-location`

The SOS application uses this endpoint to retrieve the latest coordinates.

```text
SOS Application
       │
       │ GET /latest-location
       ▼
Flask Server
       │
       ▼
Latest Latitude + Longitude
       │
       ▼
SOS Application
```

---

## 🧠 Pseudocode

```text
START
  │
  ▼
🎤 Listen for User's Voice
  │
  ▼
Convert Speech → Text
  │
  ▼
Is "Help me" Detected?
  │
  ├──────── NO ────────► Continue Listening
  │
  ▼ YES
Request Latest Location
  │
  ▼
Is Location Available?
  │
  ├──────── NO ────────► GPS Unavailable
  │
  ▼ YES
Get Latitude + Longitude
  │
  ▼
Create Google Maps Link
  │
  ▼
Create Emergency Message
  │
  ▼
Print Message in Terminal
  │
  ▼
END
```

---

## ⚠️ Current Limitations

### 📍 GPS Module

A **physical GPS module was not available** during development.

Therefore, the current prototype uses **simulated latitude and longitude**.

The Flask API is designed to receive latitude and longitude, so the simulated
coordinate source can be replaced with a real GPS module in the future.

### Current Prototype

```text
Simulated Coordinates
        │
        ▼
   Flask Server
        │
        ▼
Latitude + Longitude
        │
        ▼
 SOS Application
```

### Future GPS Integration

```text
Physical GPS Module
        │
        ▼
Real Latitude + Longitude
        │
        ▼
   Flask Server
        │
        ▼
 SOS Application
        │
        ▼
   Google Maps
```

The real GPS module can therefore replace the simulated coordinate source
without changing the main SOS logic.

---

## 📱 Twilio

The original project used **Twilio for sending SMS emergency alerts**.

Due to current Twilio service/account limitations, SMS was replaced with
**terminal output** for the prototype.

The emergency message generation remains the same.

### Current Prototype

```text
SOS Trigger
     │
     ▼
Emergency Message
     │
     ▼
💻 Terminal Output
```

### Future Notification System

```text
SOS Trigger
     │
     ▼
Emergency Message
     │
     ▼
📱 SMS / WhatsApp / Push Notification
```

---

## 🔮 Future Improvements

```text
Current Prototype
       │
       ├── 📍 Simulated GPS
       │          │
       │          ▼
       │     Real GPS Module
       │
       ├── 💻 Terminal Output
       │          │
       │          ▼
       │     SMS / WhatsApp /
       │     Push Notification
       │
       ├── 📍 Latest Location
       │          │
       │          ▼
       │     Continuous Tracking
       │
       └── 🔐 Basic API
                  │
                  ▼
             Authentication
                  +
                HTTPS
```

---

## 📂 Project Structure

```text
SOS-Voice-Alert-System/
│
├── gps_reciever.py
│   └── Flask server
│       └── Handles simulated GPS coordinates
│
└── sos_alert.py
    └── SOS application
        ├── Voice detection
        ├── Location retrieval
        ├── Google Maps link
        └── Emergency message
```

---

## 🎯 Project Goal

The project combines:

```text
🎤 Voice Recognition
        │
        +
        ▼
📍 Location Data
        │
        +
        ▼
🌐 REST API
        │
        +
        ▼
🗺️ Google Maps
        │
        +
        ▼
🚨 Emergency Notification
        │
        ▼
     SOS System
```

The goal is to create a **simple and fast SOS mechanism** that combines
voice recognition with location sharing.

The current prototype demonstrates the complete software workflow using
**simulated GPS data**.

---

# ⭐ Last-Minute Interview Revision

### 1️⃣ Problem

**Emergency situations require a quick way to request help and share location.**

### 2️⃣ Trigger

```text
User says → "Help me"
```

### 3️⃣ Speech Recognition

```text
Voice
  ↓
SpeechRecognition
  ↓
Text
```

### 4️⃣ Flask

**Acts as the communication layer for the simulated GPS coordinates.**

### 5️⃣ POST `/location`

```text
Send / Update Location
```

### 6️⃣ GET `/latest-location`

```text
Retrieve Latest Location
```

### 7️⃣ Google Maps

```text
Latitude + Longitude
        ↓
Google Maps Link
```

### 8️⃣ Current Prototype

```text
Simulated GPS
      +
Terminal Notification
```

### 9️⃣ Future Version

```text
Real GPS Module
      +
SMS / Notification Service
```

---

## 🎤 One-Line Interview Explanation

> **"I built a Python voice-activated SOS prototype where saying 'Help me'
> triggers a request to a Flask server for the latest simulated GPS
> coordinates, which are converted into a Google Maps link and included
> in an emergency message. The simulated GPS and terminal notification
> can later be replaced with real GPS hardware and an emergency
> notification service."**
