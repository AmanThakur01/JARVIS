import pyttsx3
engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
rate = engine.getProperty("rate")
engine.setProperty("voice", voices[67].id)
engine.setProperty("rate", 140)
newVol = 11
# engine.setProperty('volume', newVol)
class jspeak:
    def speak(audio):
        print(audio)
        engine.say(audio)
        engine.runAndWait()

#######################################################


