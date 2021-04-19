import pyttsx3

engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
rate = engine.getProperty("rate")
# engine.setProperty("voice", voices[67].id)
engine.setProperty('voice', 'english+f2')
engine.setProperty("rate", 130)#140
newVol = 11


# engine.setProperty('volume', newVol)

class JarvisSpeak:
    @staticmethod
    def speak(audio):
        print(audio)
        engine.say(audio)
        engine.runAndWait()


# obj=JarvisSpeak()
# obj.speak("this is me always for you from engine import Engine ModuleNotFoundError: No module named 'engine'")
#######################################################
