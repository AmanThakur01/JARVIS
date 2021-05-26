# sound = pyglet.resource.media('brownrang.mp3', streaming=True)
# sound.play()
# pyglet.app.run()
# time.sleep(10)

# usr_command = "hello"
# path = "/home/aman/Downloads"+usr_command
# print(path)
# import json
# import requests
# url = "http://api.openweathermap.org/data/2.5/weather?q=bhopal&appid=ef831cc525f939c8eb6824aa48c69c82"
# News = requests.get(url).json()
# # news_dect = json.loads(News)
# arts = News["weather"][0]["main"]
# print(arts)
# index = 0
# for article in arts:
#     print(article["main"])
#     print(article["description"])
#     print(article["icon"])

# from pocketsphinx import LiveSpeech
# for phrase in LiveSpeech():
#     print(phrase)
# #
# from gtts import gTTS
# # from pygame import *
# import pyttsx3
# import vlc
# txt = " Astrophysical Journal, with generally longer articles to supplement the material in the journal. It publishes six"
# obj = gTTS(txt,lang='en')
# obj.save("gtts_file.mp3")
# print("obj is pass")
# # mixer.init()
# # mixer.music.load("gtts_file.mp3")
# # mixer.music.play()
# # mixer.music.set_endevent()
# # print("play is pass")
# voice = vlc.MediaPlayer("gtts_file.mp3")
# voice.play()
# import time
# time.sleep(19)
# str = ""
# str = " day"
# if str.find("\sday") >=0:
#     print("day")
# else:
#     print("day is not")
# import pyaudio
# import vlc
# import time
# from pynput import keyboard
#
# paused = False    # global to track if the audio is paused
# def on_press(key):
#     global paused
#     print (key)
#     if key == keyboard.Key.space:
#         if stream.is_stopped():     # time to play audio
#             print ('play pressed')
#             stream.start_stream()
#             paused = False
#             return False
#         elif stream.is_active():   # time to pause audio
#             print ('pause pressed')
#             stream.stop_stream()
#             paused = True
#             return False
#     return False
#
#
# # you audio here
# wf = vlc.MediaPlayer("gtts_file.mp3")
#
# # instantiate PyAudio
# p = pyaudio.PyAudio()
#
# # define callback
# def callback(in_data, frame_count, time_info, status):
#     data = wf.readframes(frame_count)
#     return (data, pyaudio.paContinue)
#
# # open stream using callback
# stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
#                 channels=wf.getnchannels(),
#                 rate=wf.getframerate(),
#                 output=True,
#                 stream_callback=callback)
#
# # start the stream
# stream.start_stream()
#
# while stream.is_active() or paused==True:
#     with keyboard.Listener(on_press=on_press) as listener:
#         listener.join()
#     time.sleep(0.1)
#
# # stop stream
# stream.stop_stream()
# stream.close()
# wf.close()
#
# # close PyAudio
# p.terminate()
# import multiprocessing
# from playsound import playsound
# x=0
# p= multiprocessing.Process(target=playsound, args=("gtts_file.mp3",))
# if x == 0 :
# import pyttsx3
# engine = pyttsx3.init('espeak')
# voices = engine.getProperty('voices')
# rate = engine.getProperty("rate")
# engine.setProperty("voice", voices[66].id)
# engine.setProperty("rate", 140)
# engine.say("this is jarvis")
# engine.runAndWait()
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# driver = webdriver.Chrome(executable_path=r"/usr/bin/chromium-browser")
# driver.get("https://www.google.com")
# driver.implicitly_wait(3)
# driver.execute_script("window.open('http://www.facebook.com', 'new window')")
# print("done")
# ele = driver.find_element_by_tag_name("body")
# time.sleep(3)
# ele.send_keys(Keys.CONTROL+"t")
# time.sleep(3)
# ele.send_keys(Keys.CONTROL+"w")


# import subprocess
# import os
# os.system("/usr/bin/gedit")
# os.system("libreoffice --calc")
# sky = subprocess.Popen("/usr/bin/gnome-calendar")
# sky = subprocess.Popen("/usr/bin/gnome-screenshot")
# global a
# import os
# os.system("/usr/bin/oclock")
# from threading  import Thread
# class t(Thread):
#     def run(self):
#         global  a
#         a = os.system("libreoffice --writer")
#         a.kill()
# o=t()
# o.start()
# print("qwertyuisdhj")
# import vlc
# import random
# import time
# from glob import glob
# print("how many song you want to listen")
# path = ""
# lst=glob.glob(path)
# index = int(input("Enter value : "))
# while 0 < index:
#     song = random.choice(lst)
#     # playsound(song)
#     media = vlc.MediaPlayer(song)
#     media.audio_set_volume(70)
#     duration = media.get_length()
#     media.play()
#     time.sleep(duration)
#     index=-1
# from JARVIS import jarvisVoice as j
# j.JarvisSpeak.speak("hello thi is mic testing")
# j.newVol = int(j.newVol + int(9))
# j.engine.setProperty('volume', j.newVol)
#
# j.JarvisSpeak.speak("hello thi is mic testing")
# # newVol = input("enter")
# j.newVol = int(j.newVol + int(9))
# # engine.setProperty('volume', newVol)
#
# j.JarvisSpeak.speak("hello thi is mic testing")
# import subprocess

# import vlc
# import time
# media = vlc.MediaPlayer("brownrang.mp3")
# media.play()
# # time.sleep(3*60)
# print("now")
# media.stop()
# a = media.get_state()
# print(a)
#


# import pyautogui
# m1 = pyautogui.screenshot()
# m1.save("/home/aman/Pictures/triomer{}.png".format("1"))
# p = subprocess.Popen("/usr/bin/gnome-screenshot")
# import time
# time.sleep(10)
# distance = 100
# while distance > 0:
#     pyautogui.drag(distance, 0, duration=0.5)   # move right
#     distance -= 5
#     pyautogui.drag(0, distance, duration=0.5)   # move down
#     pyautogui.drag(-distance, 0, duration=0.5)  # move left
#     distance -= 5
#     pyautogui.drag(0, -distance, duration=0.5)  # move up

# import speech_recognition as sr  # convert speech to text
# import datetime  # for fetching date and time
# import wikipedia
# import webbrowser
# import requests
# import playsound  # to play saved mp3 file
# from gtts import gTTS  # google text to speech
# import os  # to save/open files
# # import wolframalpha  # to calculate strings into formula
# # from selenium import webdriver  # to control browser operations
#
#
# def respond(output):
#     print(output)
#     response = gTTS(text=output, lang='en-in')
#     file = "response.mp3"
#     response.save(file)
#     playsound.playsound(file, True)
#     os.remove(file)
#
# respond("hello this is me your personal assistant")
#
# import time
#
# import requests
# from ipregistry import IpregistryClient
#
# client = IpregistryClient("tryout")
# ipInfo = client.lookup()
# print(ipInfo)

import requests

import json
#
# send_url = "http://api.ipstack.com/check?access_key=2e5cc084aed1721597ed30a2b5219112"
# geo_req = requests.get(send_url)
# geo_json = json.loads(geo_req.text)
# latitude = geo_json['latitude']
# longitude = geo_json['longitude']
# city = geo_json['city']
# state=geo_json['region_name']
# country = geo_json['country_name']
# print(f"If i am not wrong, then you are in  .{city} {country} {geo_json}")
# # {city}

# import playsound
# # # time.sleep(1)
# playsound.playsound("/home/aman/PycharmProjects/JARVIS/data/female_laugh.wav")
# # # time.sleep(3)
# # playsound.playsound("/home/aman/PycharmProjects/JARVIS/data/short_haa.mp3")
# # # time.sleep(3)
# playsound.playsound("/home/aman/PycharmProjects/JARVIS/data/shy_femail.mp3")
#
# # print("Getting URL\n")
# # url = "https://official-joke-api.appspot.com/random_ten"
# joke = requests.get(url).text
# news_dect = json.loads(joke)
# # print(news_dect)
# arts = news_dect
# for article in arts:
#    print(article['setup'])
#    print(article['punchline'])sudo apt-get install -y python-pip; sudo pip install glances[gpu]
