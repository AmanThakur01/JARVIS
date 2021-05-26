from classesAndModule import playlist
from jarvisVoice import JarvisSpeak as j


class stop:

    @classmethod
    def calculator(cls, cal, i):
        if i == 1:
            cls.calcu = cal
        else:
            cls.calcu.terminate()
            j.speak("calculator closed")

    @classmethod
    def calendar(cls, cal, i):
        if i == 1:
            cls.calen = cal
        else:
            cls.calen.terminate()
            j.speak("calendar closed")

    @classmethod
    def terminal(cls, cal, i):
        if i == 1:
            cls.termi = cal
        else:
            cls.termi.terminate()
            j.speak("terminal closed")

    @classmethod
    def chrome(cls, cal, i):
        if i == 1:
            cls.stp = cal
        else:
            cls.stp.terminate()
            j.speak("google chrome closed")

    @classmethod
    def stopPlaylist(cls, cal, i):
        if i == 1:
            cls.plalst = cal
        else:
            playlist.o11.kill()
            j.speak("killed")

    @classmethod
    def monitor(cls, cal, i):
        if i == 1:
            cls.moni = cal
        else:
            cls.moni.terminate()
            j.speak("system monitor closed")

    @classmethod
    def office(cls, cal, i):
        if i == 1:
            cls.writer = cal
        else:
            cls.writer.terminate()
            j.speak("libreoffice writer closed")

    @classmethod
    def vscode(cls, cal, i):
        if i == 1:
            cls.vs = cal

        else:
            cls.vs.terminate()
            j.speak("VisualStudio code closed")

    @classmethod
    def steam(cls, cal, i):
        if i == 1:
            cls.stm = cal
        else:
            cls.stm.terminate()
            j.speak("steam closed")

    @classmethod
    def pycharm(cls, cal, i):
        if i == 1:
            cls.pchm = cal
        else:
            cls.pchm.terminate()
            j.speak("pycharm closed")

    @classmethod
    def netbeans(cls, cal, i):
        if i == 1:
            cls.net = cal
        else:
            cls.net.terminate()
            j.speak("netbeans closed")

    @classmethod
    def skype(cls, cal, i):
        if i == 1:
            cls.sky = cal
        else:
            cls.sky.terminate()
            j.speak("skype closed")

    @classmethod
    def telegram(cls, cal, i):
        if i == 1:
            cls.tele = cal
        else:
            cls.tele.terminate()
            j.speak("telegram closed")

    @classmethod
    def firfox(cls, cal, i):
        if i == 1:
            cls.fir = cal
        else:
            cls.fir.terminate()
            j.speak("mozilla firfox closed")

    @classmethod
    def gedit(cls, cal, i):
        if i == 1:
            cls.edit = cal
        else:
            cls.edit.terminate()
            j.speak("gedit text editor closed")
