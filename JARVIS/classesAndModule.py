import vlc
import random
import glob
import requests
import json
import os.path
from threading import Thread
import datefinder
import time
import datetime
import re

from future.backports.email import encoders
from future.backports.email.mime.base import MIMEBase
from future.backports.email.mime.text import MIMEText
from playsound import playsound
import smtplib
from JARVIS.idList import pwd, gmail
from JARVIS.speechRecog import speechRecog
from JARVIS.jarvisVoice import JarvisSpeak as j
from future.backports.email.mime.multipart import MIMEMultipart

global cmd, index, alarmsec


class Wtsp():
    @staticmethod
    def wtsp_num(contact_name):
        j.speak(f"sending whatsapp to {contact_name}")
        file = open('/home/aman/PycharmProjects/JARVIS/data/contact.vcf', 'r')
        contacts = []
        # phone = []
        for line in file:
            name = re.findall('FN:(.*)', line)
            nm = ''.join(name)
            if len(nm) == 0:
                continue
            name_ = nm.strip()
            # print(name)
            data = {'name': name_.lower()}
            for lin in file:
                tel = re.findall('TEL;CELL:(.*)', lin)
                tel = ''.join(tel)

                if len(tel) == 0:
                    continue

                tel = tel.strip()
                # print(tel)
                tel = ''.join(e for e in tel if e.isalnum())
                data['phone'] = tel
                break
            contacts.append(data)

        contact_name = contact_name.split(" ")
        for name_dict in contacts:
            for c_name in contact_name:
                if name_dict['name'] == c_name:
                    contact_num = name_dict['phone']
                    return contact_num
                else:
                    pass


# from JARVIS.closeModule import stop
usr_obj = speechRecog()


class Alarm():
    @staticmethod
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
                timeList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
                            0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
                hourNow = int(datetime.datetime.now().hour)
                if int(dateStr[0]) == hourNow:
                    alarmsec = (
                        int(dateStr[1]) - int(datetime.datetime.now().minute)) * 60
                else:
                    alarmsec = (int(dateStr[1]) * 60)
                newTimeList = timeList[hourNow:]
                index = 0
                for i in newTimeList:
                    if i == int(dateStr[0]):
                        break
                    index = index + 1
                alarmSecHour = index * 60 * 60
                time.sleep(alarmsec + alarmSecHour - 3)
                playsound("brownrang.mp3")
                time.sleep(30)
                playsound.stop()

        o6 = t6()
        o6.start()
        return 0


class sendMail:
    @staticmethod
    # /home/aman/Pictures/chart.jpeg
    def sendProcess(to, file):
        def server_connection(content):
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(gmail, pwd)
            server.sendmail(gmail, to, content)
            server.close()
            j.speak("Gmail is sent")

        try:
            if file == 1:
                j.speak("what is the Message for this File")
                message = usr_obj.take_command()

                msg = MIMEMultipart()
                msg['From'] = gmail
                msg['To'] = to
                msg['Subject'] = "A File From JARVIS"
                msg.attach(MIMEText(message, 'plain'))
                j.speak("Please Enter File Location :")
                file_location = input()
                filename = os.path.basename(file_location)
                attachment = open(file_location, 'rb')
                part = MIMEBase("application", 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition',
                                'attachment; filename="%s"' % filename)
                msg.attach(part)
                text = msg.as_string()
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.ehlo()
                server.starttls()
                server.login(gmail, pwd)
                server.sendmail(gmail, to, text)
                server.close()
                j.speak("Gmail is sent")

            else:
                j.speak("what is content")
                content = usr_obj.take_command()
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.ehlo()
                server.starttls()
                server.login(gmail, pwd)
                server.sendmail(gmail, to, content)
                server.close()
                j.speak("Gmail is sent")
        except Exception as ex:
            print(ex)
            j.speak("sorry,Email is not sent")
            j.speak("Try again")
        return 0

    @staticmethod
    def sendGmail(usr_command):
        mail = []
        file = 0
        splitedList = re.split("\s", usr_command)
        for i in splitedList:
            path = re.compile(r".*@.*")
            mailList = path.finditer(i)
            for k in mailList:
                a = k.group()
                mail.append(a)
        if "file" in splitedList:
            file = 1
        else:
            file = 0
        try:

            if "shubha" in splitedList:
                to = "shubhathakur@gmail.com"
                sendMail.sendProcess(to, file)
            elif "vyabha" in splitedList:
                to = "vyabhathakur@gmail.com"
                sendMail.sendProcess(to, file)
            elif "aman" in splitedList:
                to = "amanmrthakur@gmail.com"
                sendMail.sendProcess(to, file)
            else:
                a = 1 / 0
        except:
            j.speak("please enter destination email address :")
            to = input("")
            sendMail.sendProcess(to, file)
        return 0


class News:
    @staticmethod
    def news_of(num):
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
    global o11

    @staticmethod
    def playlist(ipath, ival):
        global o11, path, val
        path = ipath
        val = ival

        class Thread11(Thread):
            def run(self):
                global val, path
                # print(glob.glob(path))
                lst = glob.glob(path)
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

        o11 = Thread11()
        o11.start()
