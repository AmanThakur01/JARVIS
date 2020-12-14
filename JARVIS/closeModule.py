from JARVIS.jarvisVoice import jspeak as j
from JARVIS.classesAndModule import playlist
class stop:
    def calculator(cal,i):
        if i==1:
            global calcu
            calcu = cal
        else:
            calcu.terminate()
            j.speak("calculator closed")
       
    def calendar(cal,i):
        if i==1:
            global calen
            calen = cal
        else:
            calen.terminate()
            j.speak("calendar closed")
        

    def terminal(cal,i):
        if i==1:
            global termi
            termi = cal
        else:
            termi.terminate()
            j.speak("terminal closed")
        

    def chrome(cal,i):
        if i==1:
            global stp
            stp = cal
        else:
            stp.terminate()
            j.speak("google chrome closed")
        

    def stopPlaylist(cal,i):
        if i==1:
            global plalst
            plalst = cal
        else:
            playlist.t11.kill()
            j.speak("killed")
        

    def monitor(cal,i):
        if i==1:
            global moni
            moni = cal
        else:
            moni.terminate()
            j.speak("system monitor closed")
        
    def office(cal,i):
        if i==1:
            global writer
            writer = cal
        else:
            writer.terminate()
            j.speak("libreoffice writer closed")
        
    def vscode(cal,i):
        if i==1:
            global vs
            vs = cal
            
        else:
            vs.terminate()
            j.speak("VisualStudio code closed")
            

    def steam(cal,i):
        if i==1:
            global stm
            stm = cal
        else:
            stm.terminate()
            j.speak("steam closed")
        

    def pycharm(cal,i):
        if i==1:
            global pchm
            pchm = cal
        else:
            pchm.terminate()
            j.speak("pycharm closed")
        

    def netbeans(cal,i):
        if i==1:
            global net
            net = cal
        else:
            net.terminate()
            j.speak("netbeans closed")
        

    def skype(cal,i):
        if i==1:
            global sky
            sky = cal
        else:
            sky.terminate()
            j.speak("skype closed")
        
    def telegram(cal,i):
        if i==1:
            global tele
            tele = cal
        else:
            tele.terminate()
            j.speak("telegram closed")
        
    def firfox(cal,i):
        if i==1:
            global fir
            fir = cal
        else:
            fir.terminate()
            j.speak("mozilla firfox closed")
        

    def gedit(cal, i):
        if i == 1:
            global edit
            edit = cal
        else:
            edit.terminate()
            j.speak("gedit text editor closed")
        
