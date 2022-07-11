from playsound import playsound
import pyttsx3
import requests
import os
from gtts import gTTS
import tkinter as tk
import tkinter.messagebox


def check_internet_connection():
    try:
        requests.head("http://www.google.com/", timeout=1)
        return True
    except requests.ConnectionError:
        return False


location = "speech.wav"
engine = pyttsx3.init()  # object creation
voices = engine.getProperty('voices')


def speech(text, language, mand_var):
    offline_voice_available = False
    if language == "Cantonese":
        for voice in voices:
            if "ZH-HK" in voice.id.upper():
                offline_voice_available = True
                engine.setProperty("voice", voice.id)
                break
        if not offline_voice_available:
            tk.messagebox.showerror(title="Error",
                                    message="Cantonese text to speech is not available. Please install the Chinese "
                                            "(Traditional, Hong Kong SAR) language pack in Settings.")

    else:
        if mand_var == "Taiwanese":
            var = "ZH-TW"
        else:
            var = "ZH-CN"
        for voice in voices:
            if var in voice.id.upper():
                offline_voice_available = True
                engine.setProperty("voice", voice.id)
                break
        if not offline_voice_available:
            if check_internet_connection():
                tts = gTTS(text, lang=var)
                filename = "speech.mp3"
                tts.save(filename)
                playsound(filename)
                os.remove(filename)
            else:
                if mand_var == "Taiwanese":
                    tk.messagebox.showerror(title="Error",
                                            message="Mandarin text to speech is not available. Please install the "
                                                    "Chinese (Traditional, Taiwan) language pack in Settings or connect"
                                                    " to the internet.")
                else:
                    tk.messagebox.showerror(title="Error",
                                            message="Mandarin text to speech is not available. Please install the "
                                                    "Chinese (Simplified, China) language pack in Settings or connect "
                                                    "to the internet.")

    if offline_voice_available:
        engine.say(text)
        engine.runAndWait()
        engine.stop()
