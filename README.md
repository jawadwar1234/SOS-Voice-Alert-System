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
- 💻 Prints the message in the terminal

**Current Prototype:**  
Simulated GPS coordinates are used because a physical GPS module was not available.

In the future, the simulated coordinates can be replaced with a real GPS module.

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
              ┌─────────────────┐
              │  FLASK SERVER   │
              │                 │
              │ Simulated GPS   │
              │    Coordinates  │
              └────────┬────────┘
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
🛠️ Tech Stack
Technology	Purpose
Python	Main programming language
Tkinter	Graphical User Interface
SpeechRecognition	Voice command detection
Flask	Server/API for simulated GPS coordinates
Requests	Communication with Flask
Google Maps	Location visualization
Threading	Keeps GUI responsive
🔌 Flask API
POST /location

Receives the simulated GPS coordinates.

{
    "latitude": 18.5230,
    "longitude": 73.8590
}

The Flask server stores the latest latitude and longitude.

GET /latest-location

The SOS application uses this endpoint to retrieve the latest coordinates.

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
🧠 Pseudocode
START
  │
  ▼
Listen for user's voice
  │
  ▼
Convert Speech → Text
  │
  ▼
Is "help me" detected?
  │
  ├── NO ──→ Continue Listening
  │
  ▼ YES
Request Latest Location
  │
  ▼
Is Location Available?
  │
  ├── NO ──→ Show "GPS Unavailable"
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
⚠️ Current Limitations
📍 GPS Module

A physical GPS module was not available during development.

Therefore, the current prototype uses simulated latitude and longitude.

The Flask API is already designed to receive latitude and longitude.

In the future:

Simulated Coordinates
        ↓
   Replace With
        ↓
   Real GPS Module
        ↓
Latitude + Longitude
        ↓
   Flask Server

The real GPS module can replace the simulated coordinate source without
changing the main SOS logic.

📱 Twilio

The original project used Twilio for SMS alerts.

Due to current Twilio service/account limitations, SMS was replaced with
terminal output for the prototype.

In the future:

Emergency Message
        ↓
SMS / WhatsApp / Push Notification
🔮 Future Improvements
📍 Integrate a physical GPS module
📱 Add SMS / WhatsApp / Push notifications
🔄 Implement continuous location tracking
🔐 Add API authentication
🔒 Use HTTPS for secure communication
☁️ Deploy Flask using a production server
📂 Project Structure
SOS-Voice-Alert-System/
│
├── gps_reciever.py
│   └── Flask server for simulated GPS coordinates
│
└── sos_alert.py
    └── Voice-based SOS application
🎯 Project Goal

The project combines:

🎤 Voice Recognition
        +
📍 Location Data
        +
🌐 REST API
        +
🗺️ Google Maps
        +
🚨 Emergency Notification

to create a simple and fast SOS system.

The current prototype demonstrates the complete software workflow using
simulated GPS data.
