import speech_recognition as sr
import pyttsx3
r = sr.Recognizer()
def recordtext():
    while(1):
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2,duration=0.2)
                audio2 = r.listen(source2)
                myText = r.recognize_google(audio2)
                return myText

        except sr.RequestError as e:
            print(f"could not request result; {e}")
        except sr.UnknownValueError:
            print("unknwn error occur")

        return



def output_text():
    f= open("output.txt","a")
    f.write(text)
    f.write("\n")
    f.close()
    return



while(1):
    text = recordtext()
    output_text(text)