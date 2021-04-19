import speech_recognition as sr
from JARVIS.jarvisVoice import JarvisSpeak as j


class speechRecog:
    def take_command(self):
        j.speak("listening")
        while True:
            try:
                # print(1/0)
                r = sr.Recognizer()
                with sr.Microphone() as source2:
                    r.adjust_for_ambient_noise(source2)  # , duration=0.2
                    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tNow.....")
                    audio2 = r.listen(source2)
                    usr_command = r.recognize_google(audio2)
                    usr_command = usr_command.lower()
                    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tyou said ->" + usr_command)
                    return usr_command
            except sr.UnknownValueError:
                print("try Again")
    # def take_command(self):
    #     try:
    #         usr_command = input("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tcommand :")
    #         print("You said : "+usr_command)
    #         return usr_command
    #     except Exception as ex:
    #         print(ex)
    #         return 0
