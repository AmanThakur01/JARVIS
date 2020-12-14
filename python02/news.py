import pyttsx3    # pyttsx3 is a text-to-speech conversion library in Python
import requests
import json

engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
rate = engine.getProperty("rate")
# print(voices[10].id)
engine.setProperty("voice", voices[10].id)# 9,10(default),11,12,13,14,15,16,67
engine.setProperty("rate", 140)


def speak(art):
    engine.say(art)
    engine.runAndWait()


if __name__ == "__main__":
    speak("News Of Today")
    url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=35bdda38281e49258867bfbac2124d32"
    news = requests.get(url).text
    news_dect = json.loads(news)
    print(news_dect["articles"])
    arts = news_dect["articles"]
    for article in arts:
        speak(article["title"])
        speak("Our next news is")