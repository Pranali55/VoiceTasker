import speech_recognition as sr

def listen_task():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say your task...")
        audio = r.listen(source)
    try:
        return r.recognize_google(audio)
    except Exception as e:
        return f"Error: {e}"
