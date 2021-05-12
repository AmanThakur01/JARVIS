# import pyttsx3
#
# engine = pyttsx3.init('espeak')
# voices = engine.getProperty('voices')
# rate = engine.getProperty("rate")
# # engine.setProperty("voice", voices[67].id)
# engine.setProperty('voice', 'english+f2')
# engine.setProperty("rate", 135)#140
# newVol = 11
#
#
# # engine.setProperty('volume', newVol)
#
# class JarvisSpeak:
#     @staticmethod
#     def speak(audio):
#         print(audio)
#         engine.say(audio)
#         engine.runAndWait()
#
#
# obj=JarvisSpeak()
# obj.speak("this is me always for you from engine import Engine ModuleNotFoundError: No module named 'engine'")
#######################################################
import os
import playsound
from gtts import gTTS


class JarvisSpeak():
    @staticmethod
    def speak(output):
        print(output)
        # jarvis.ui.textBrowser_5.setText()
        response = gTTS(text=output, lang='en-in')
        file = "response.mp3"
        response.save(file)
        playsound.playsound(file, True)
        os.remove(file)
        return 0
