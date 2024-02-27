import speech_recognition as sr
import os

def say(text):
    os.system(f"say {text}")
def recognize_speech():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)

    try:
        # Use the Google Web Speech API to recognize the audio
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text

    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Web Speech API; {0}".format(e))

if __name__ == "__main__":

    say(recognize_speech())