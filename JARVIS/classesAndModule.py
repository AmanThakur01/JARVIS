from threading import Thread
import datefinder
import time
import datetime
import re
from playsound import playsound
import smtplib
from JARVIS.idList import pwd,gmail
from JARVIS.speechRecog import speechRecog
from JARVIS.jarvisVoice import jspeak as j
global cmd , index , alarmsec
import json
import requests
import glob
import random
import vlc
# from JARVIS.closeModule import stop

class Alarm():
    def setAlarm(i):
        global cmd, index, alarmsec
        cmd = i
        class t6(Thread):
            def run(self):
                global cmd, index, alarmsec
                dateList = datefinder.find_dates(cmd)
                for dateStr in dateList:
                    pass
                dateStr = str(dateStr)
                dateStr = dateStr[11:]
                dateStr = dateStr.split(":")
                timeList = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,
                            0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
                hourNow = int(datetime.datetime.now().hour)
                if int(dateStr[0]) == hourNow:
                    alarmsec = (int(dateStr[1]) - int(datetime.datetime.now().minute))*60
                else:
                    alarmsec = (int(dateStr[1])*60)
                newTimeList = timeList[hourNow:]
                index=0
                for i in newTimeList:
                    if i == int(dateStr[0]):
                        break
                    index = index +1
                alarmSecHour = index*60*60
                time.sleep(alarmsec+alarmSecHour-3)
                playsound("brownrang.mp3")
                time.sleep(30)
                playsound.stop()
        o6 = t6()
        o6.start()
        return 0

class sendMail:
    def sendProcess(to):
        try:
            j.speak("what is content")
            content = speechRecog.take_command(self=None)
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(gmail, pwd)
            server.sendmail(gmail, to, content)
            server.close()
            j.speak("Gmail is sended")
        except:
            j.speak("sorry,Email is not sent")
            j.speak("Try again")
        return 0

    def sendGmail(usr_command):
        mail = []
        splitedList = re.split("\s", usr_command)
        for i in splitedList:
            path = re.compile(r".*@.*")
            mailList = path.finditer(i)
            for k in mailList:
                a = k.group()
                mail.append(a)
        try:
            if "shubha" in splitedList:
                to = "shubhathakur@gmail.com"
                sendMail.sendProcess(to)
            elif "vyabha" in splitedList:
                to = "vyabhathakur@gmail.com"
                sendMail.sendProcess(to)
            elif "aman" in splitedList:
                to = "amanmrthakur@gmail.com"
                sendMail.sendProcess(to)
            else:
                a = 1 / 0
        except:
            j.speak("please enter destination email address :")
            to = input("")
            sendMail.sendProcess(to)
        return 0

class news:
    def newsOf(num):
        try:
            j.speak("News Of Today")
            url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=35bdda38281e49258867bfbac2124d32"
            news = requests.get(url).text
            news_dect = json.loads(news)
            # print(news_dect["articles"])
            arts = news_dect["articles"]
            index = 0
            for article in arts:
                if index < int(num):
                    j.speak(article["title"] + "     \n")
                else:
                    break
                index += 1
        except:
            print("Please check your internet connection!")
        return 0

class playlist():
    def playlist(ipath,ival):
        global t11,path,val
        path = ipath
        val = ival
        class t11(Thread):
            def run(self):
                global val,path
                # print(glob.glob(path))
                lst=glob.glob(path)
                if val != None:
                    # index = int(speechRecog.take_command(self=None))
                    while 0 < val:
                        song = random.choice(lst)
                        playsound(song)
                        val = val - 1
                else:
                    while 0 < len(lst):
                        song = random.choice(lst)
                        playsound(song)
                return 0

        o11 = t11()
        o11.start()
