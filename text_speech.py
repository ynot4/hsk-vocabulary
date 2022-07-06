from playsound import playsound
import pyttsx3

location = "speech.wav"


def speech(text, language):
    engine = pyttsx3.init()  # object creation
    print(text, language)
    voices = engine.getProperty('voices')
    for voice in voices:
        if language == "Cantonese":
            if "TTS_MS_ZH-HK" in voice.id:
                engine.setProperty("voice", voice.id)
                break
        else:
            if "TTS_MS_ZH-CN" in voice.id:
                engine.setProperty("voice", voice.id)
                break

    engine.save_to_file(text, location)
    engine.runAndWait()
    engine.stop()

    playsound(location)
