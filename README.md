🚨 Voice-Activated SOS Alert & Location Sharing System
📌 Problem We Are Solving

During an emergency, a person may not have enough time to unlock their phone, type a message, and manually share their location.

This project provides a quick SOS mechanism where the user can simply say "Help me" to trigger an emergency alert with their location.

📝 Short Description

A Python-based voice-activated SOS system that:

🎤 Detects the voice command "Help me"
📍 Gets the latest latitude and longitude
🗺️ Generates a Google Maps location link
🚨 Creates an emergency message
💻 Prints the message in the terminal

Current Prototype: Simulated GPS coordinates are used because a physical GPS module was not available. These simulated coordinates can be replaced with a real GPS module in the future.

🔄 Project Workflow
👤 User
   │
   │ "Help me"
   ▼
🎤 Speech Recognition
   │
   ▼
🚨 SOS Detection
   │
   ▼
📍 Request Latest Location
   │
   ▼
🖥️ Flask Server
   │
   │ Simulated Latitude + Longitude
   ▼
📍 Latest Location
   │
   ▼
🗺️ Google Maps Link
   │
   ▼
🚨 Emergency Message
   │
   ▼
💻 Terminal
🛠️ Tech Stack
Technology	Purpose
Python	Main programming language
Tkinter	Graphical User Interface
SpeechRecognition	Voice command detection
Flask	Server/API for simulated GPS coordinates
Requests	Communication with Flask server
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
🧠 Pseudocode
START
   ↓
Listen for user's voice
   ↓
Convert speech → text
   ↓
Is "help me" detected?
   │
   ├── NO → Continue listening
   │
   └── YES
         ↓
   Request latest location
         ↓
   Is location available?
         │
         ├── NO → Show "GPS unavailable"
         │
         └── YES
               ↓
        Get latitude + longitude
               ↓
        Create Google Maps link
               ↓
        Create emergency message
               ↓
        Print message in terminal
               ↓
              END
⚠️ Current Limitations
📍 GPS Module

A physical GPS module was not available during development, so the current prototype uses simulated latitude and longitude.

The Flask API is already designed to receive latitude and longitude, so in the future:

Simulated GPS
      ↓
      ❌
      ↓
Real GPS Module
      ↓
Latitude + Longitude
      ↓
Flask Server

The real GPS module can therefore replace the simulated coordinate source without changing the main SOS logic.

📱 Twilio

The original project used Twilio for sending SMS alerts.

Due to current Twilio service/account limitations, SMS was replaced with terminal output for the prototype.

The emergency message generation remains the same.

In the future:

Emergency Message
       ↓
SMS / WhatsApp / Push Notification

can replace the terminal output.

🔮 Future Improvements
📍 Integrate a physical GPS module
📱 Add SMS / WhatsApp / Push notifications
🔄 Implement continuous location tracking
🔐 Add API authentication
🔒 Use HTTPS for secure communication
☁️ Deploy the Flask application on a production server
📲 Develop a mobile application using the phone's GPS
📂 Project Structure
SOS-Voice-Alert-System/
│
├── gps_reciever.py
│   └── Flask server for simulated GPS coordinates
│
└── sos_alert.py
    └── Voice-based SOS application
🎯 Project Goal

The goal is to combine:

Voice Recognition + Location Data + REST API + Google Maps + Emergency Notification

into a simple and fast SOS system.

The current prototype demonstrates the complete software workflow using simulated GPS data.
