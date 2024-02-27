import speech_recognition as sr
import os



def say(text):
    os.system(f"say {text}")


def recognize_speech():#take command
    # # Initialize the recognizer
    # recognizer = sr.Recognizer()
    #
    # # Use the default microphone as the audio source
    # with sr.Microphone() as source:
    #     print("Say something:")
    #     audio = recognizer.listen(source)
    #
    #      # Use the Google Web Speech API to recognize the audio
    #     text = recognizer.recognize_google(audio)
    #     print("You said:", text)
    #     return text
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



ON = True
say("hi I am Eric A.I")
say("how are you ,")
while ON == True:

    print("listning...")
    text = recognize_speech()
    say(text)

