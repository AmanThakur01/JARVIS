import datetime
import json
import sys
from threading import Thread

import requests
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from PyQt5 import QtGui
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from weather.main_gui import Ui_MainWindow

url = "https://api.openweathermap.org/data/2.5/forecast?q=bhopal&appid=ef831cc525f939c8eb6824aa48c69c82"
req = requests.get(url)
text_data = req.text
json_dict = json.loads(text_data)

df = pd.DataFrame.from_dict(json_dict["list"])
# df.to_excel("output.xlsx")
main = df.main
weather = df.weather
dt_txt = df.dt_txt
df2 = pd.DataFrame(main)
data_dict = {"feels_like": [], "temp_min": [], "temp_max": [], 'temp': [], "humidity": [], "dt_txt": [], 'cloud': [],
             'type': []}
arts = weather[0][0]['main']
temperature = main[0]['temp']
humidity = main[0]["humidity"]


class MainThread(Thread):
    def run(self):
        for t in dt_txt:
            data_dict["dt_txt"].append(t)
        for i in main:
            data_dict['feels_like'].append(i['feels_like'] - 273.15)
            data_dict['temp_min'].append(i['temp_min'] - 273.15)
            data_dict['temp_max'].append(i['temp_max'] - 273.15)
            data_dict['temp'].append(i['temp'] - 273.15)
            data_dict['humidity'].append(i['humidity'])
        for w in weather:
            data_dict['cloud'].append(w[0]['main'])
            data_dict['type'].append(w[0]['description'])


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startjarvis)
        self.ui.pushButton_2.clicked.connect(self.close)

    def draw(self):
        # x = np.random.normal(size=1000)
        # y = np.random.normal(size=(3, 1000))
        # for i in range(3):
        #     self.ui.graphicsView.plot(x, y[i], pen=(i, 3))
        new_df = pd.DataFrame(data_dict)

        sns.set_theme(style="darkgrid")
        plt.figure(figsize=(25, 10), )
        plot = sns.lineplot(x="type", y="dt_txt", hue='cloud',
                            data=new_df)
        plt.setp(plot.get_xticklabels(), rotation=10)
        self.ui.graphicsView.plot(x="type", y="dt_txt",data=new_df)

    def draw2(self):
        new_df = pd.DataFrame(data_dict)

        sns.set_theme(style="white", context="talk")
        # rs = np.random.RandomState(8)

        # Set up the matplotlib figure
        f, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(24, 15))  # , sharex=True

        # Generate some sequential data
        # y1 = np.arange(1, 11)
        plot1 = sns.barplot(x=new_df['temp'], y=new_df['type'], palette="Greens_d", ax=ax1, data=new_df)
        ax1.axhline(0, color="k", clip_on=False)
        ax1.set_ylabel("few clouds,\nscattered clouds,\nclear sky,\nbroken clouds,\novercast clouds,\nlight rain")
        # Center the data to make it diverging
        # y2 = y1 - 5.5
        plot2 = sns.barplot(x=new_df['temp'], y=new_df['cloud'], palette="vlag", ax=ax2, data=new_df)
        ax2.axhline(0, color="k", clip_on=False)
        # ax2.set_ylabel("cloud")

        # Randomly reorder the data to make it qualitative
        # y3 = rs.choice(y1, len(y1), replace=False)
        plot3 = sns.barplot(x=round(new_df['temp']), y=new_df['humidity'], palette="deep", ax=ax3, data=new_df)
        ax3.axhline(0, color="k", )
        # ax3.set_ylabel("humidity")

        # Finalize the plot
        sns.despine(bottom=True)
        plt.setp(plot1.get_yticklabels(), rotation=180)
        plt.setp(plot1.get_xticklabels(), rotation=75)
        plt.setp(plot2.get_xticklabels(), rotation=75)
        plt.setp(plot3.get_xticklabels(), rotation=75)

        plt.setp(f.axes, yticks=[])
        plt.tight_layout(h_pad=2)
        # plt.show()

    def startjarvis(self):
        # main gif run
        self.ui.movie = QtGui.QMovie(
            "/home/aman/PycharmProjects/weather/thunder.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.draw()
        # # initlization gif run
        # self.ui.movie = QtGui.QMovie(
        #     "/home/aman/PycharmProjects/JARVIS/data/inslization.gif")
        # self.ui.label_3.setMovie(self.ui.movie)
        # self.ui.movie.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start(1000)
        startExecution.start()

    def showtime(self):
        global f
        # datetime.datetime.now().strftime("%H hour and %M minutes")
        # textbox=background:transparent;\nfont: 75 11pt "Purisa";\ncolor:white;
        self.ui.textBrowser_2.setText(
            datetime.datetime.now().strftime("%H:%M"))  # :%S
        self.ui.textBrowser_3.setText(datetime.datetime.now().strftime("%A"))
        self.ui.textBrowser.setText(datetime.datetime.now().strftime("%B %Y"))
        self.ui.textBrowser_4.setText(datetime.datetime.now().strftime("%d"))
        self.ui.textBrowser_5.setText(datetime.datetime.now()
                                      .strftime(f"{arts}   |  {str(round(temperature - 273.15))}" +
                                                u"\N{DEGREE SIGN}C   | " + f" Humidity-{humidity}"))
        # self.ui.textBrowser_6.append(f.getvalue())


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())
