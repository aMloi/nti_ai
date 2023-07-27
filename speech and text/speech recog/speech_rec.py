import speech_recognition as sr

def listen_to_microphone():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening... Say something:")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print("Error in the API request. {0}".format(e))

if __name__ == "__main__":
    listen_to_microphone()
