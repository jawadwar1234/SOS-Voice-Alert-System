import tkinter as tk
from tkinter import messagebox
import threading
import requests
import speech_recognition as sr


# ---------------------------------
# GPS Server
# ---------------------------------

GPS_SERVER_URL = "http://127.0.0.1:5000/latest-location"


# ---------------------------------
# Get latest GPS location
# ---------------------------------

def get_location():

    try:

        response = requests.get(
            GPS_SERVER_URL,
            timeout=5
        )

        response.raise_for_status()

        data = response.json()

        latitude = data["latitude"]
        longitude = data["longitude"]

        return latitude, longitude

    except requests.RequestException as e:

        print("GPS server error:", e)

        return None, None

    except (KeyError, ValueError):

        print("Invalid GPS data")

        return None, None


# ---------------------------------
# Send SOS Alert
# ---------------------------------

def send_sos_alert():

    latitude, longitude = get_location()

    if latitude is None:

        return None

    maps_link = (
        f"https://www.google.com/maps?"
        f"q={latitude},{longitude}"
    )

    message_body = (
        "\n"
        "========================================\n"
        "        🚨 EMERGENCY SOS ALERT 🚨\n"
        "========================================\n"
        "I need help!\n\n"
        f"Latitude  : {latitude}\n"
        f"Longitude : {longitude}\n\n"
        f"Live Location:\n{maps_link}\n"
        "========================================\n"
    )

    # ---------------------------------
    # Instead of Twilio, print message
    # ---------------------------------

    print(message_body)

    return "TEST_MESSAGE"


# ---------------------------------
# Voice recognition
# ---------------------------------

def listen_for_sos(status_label):

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        status_label.config(
            text="🎤 Listening for 'help me'..."
        )

        recognizer.adjust_for_ambient_noise(source)

        try:

            audio = recognizer.listen(
                source,
                timeout=10
            )

            text = recognizer.recognize_google(
                audio
            ).lower()

            status_label.config(
                text=f"🗣 You said: {text}"
            )

            if "help me" in text:

                status_label.config(
                    text="🚨 Distress word detected!"
                )

                sid = send_sos_alert()

                if sid is None:

                    status_label.config(
                        text="❌ GPS location unavailable"
                    )

                    messagebox.showerror(
                        "SOS Error",
                        "GPS location unavailable"
                    )

                else:

                    status_label.config(
                        text="✅ SOS message printed!"
                    )

                    messagebox.showinfo(
                        "SOS Alert",
                        "Emergency message printed in terminal!"
                    )

            else:

                status_label.config(
                    text="❌ 'Help me' not detected."
                )

        except sr.UnknownValueError:

            status_label.config(
                text="🤷 Could not understand the audio."
            )

        except sr.RequestError:

            status_label.config(
                text="⚠ Speech recognition service error."
            )

        except Exception as e:

            status_label.config(
                text=f"⚠ Error: {e}"
            )


# ---------------------------------
# Run voice recognition in thread
# ---------------------------------

def start_listening_thread(status_label):

    thread = threading.Thread(
        target=listen_for_sos,
        args=(status_label,),
        daemon=True
    )

    thread.start()


# ---------------------------------
# GUI
# ---------------------------------

def main():

    root = tk.Tk()

    root.title("SOS Voice Alert System")
    root.geometry("400x250")

    title_label = tk.Label(
        root,
        text="🔊 SOS Voice Listener",
        font=("Helvetica", 16, "bold")
    )

    title_label.pack(pady=20)

    status_label = tk.Label(
        root,
        text="Press Start to begin",
        font=("Helvetica", 12)
    )

    status_label.pack(pady=10)

    start_button = tk.Button(
        root,
        text="▶ Start Listening",
        font=("Helvetica", 12),
        bg="#4CAF50",
        fg="white",
        command=lambda:
        start_listening_thread(status_label)
    )

    start_button.pack(pady=10)

    exit_button = tk.Button(
        root,
        text="❌ Exit",
        font=("Helvetica", 12),
        bg="#f44336",
        fg="white",
        command=root.quit
    )

    exit_button.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()