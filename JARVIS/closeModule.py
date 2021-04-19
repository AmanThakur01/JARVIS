from JARVIS.classesAndModule import playlist
from JARVIS.jarvisVoice import JarvisSpeak as j


class stop:

    @staticmethod
    def calculator(cal, i):
        if i == 1:
            global calcu
            calcu = cal
        else:
            calcu.terminate()
            j.speak("calculator closed")

    @staticmethod
    def calendar(cal, i):
        if i == 1:
            global calen
            calen = cal
        else:
            calen.terminate()
            j.speak("calendar closed")

    @staticmethod
    def terminal(cal, i):
        if i == 1:
            global termi
            termi = cal
        else:
            termi.terminate()
            j.speak("terminal closed")

    @staticmethod
    def chrome(cal, i):
        if i == 1:
            global stp
            stp = cal
        else:
            stp.terminate()
            j.speak("google chrome closed")

    @staticmethod
    def stopPlaylist(cal, i):
        if i == 1:
            global plalst
            plalst = cal
        else:
            playlist.t11.kill()
            j.speak("killed")

    @staticmethod
    def monitor(cal, i):
        if i == 1:
            global moni
            moni = cal
        else:
            moni.terminate()
            j.speak("system monitor closed")

    @staticmethod
    def office(cal, i):
        if i == 1:
            global writer
            writer = cal
        else:
            writer.terminate()
            j.speak("libreoffice writer closed")

    @staticmethod
    def vscode(cal, i):
        if i == 1:
            global vs
            vs = cal

        else:
            vs.terminate()
            j.speak("VisualStudio code closed")

    @staticmethod
    def steam(cal, i):
        if i == 1:
            global stm
            stm = cal
        else:
            stm.terminate()
            j.speak("steam closed")

    @staticmethod
    def pycharm(cal, i):
        if i == 1:
            global pchm
            pchm = cal
        else:
            pchm.terminate()
            j.speak("pycharm closed")

    @staticmethod
    def netbeans(cal, i):
        if i == 1:
            global net
            net = cal
        else:
            net.terminate()
            j.speak("netbeans closed")

    @staticmethod
    def skype(cal, i):
        if i == 1:
            global sky
            sky = cal
        else:
            sky.terminate()
            j.speak("skype closed")

    @staticmethod
    def telegram(cal, i):
        if i == 1:
            global tele
            tele = cal
        else:
            tele.terminate()
            j.speak("telegram closed")

    @staticmethod
    def firfox(cal, i):
        if i == 1:
            global fir
            fir = cal
        else:
            fir.terminate()
            j.speak("mozilla firfox closed")

    @staticmethod
    def gedit(cal, i):
        if i == 1:
            global edit
            edit = cal
        else:
            edit.terminate()
            j.speak("gedit text editor closed")
