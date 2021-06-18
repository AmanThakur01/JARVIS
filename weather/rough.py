# QScrollBar:vertical {"
#                                  "    border: 1px solid #999999;"
#                                  "    background:white;"
#                                  "    width:10px;    "
#                                  "    margin: 0px 0px 0px 0px;"
#                                  "}"
#                                  "QScrollBar::handle:vertical {"
#                                  "    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,"
#                                  "    stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130), stop:1 rgb(32, 47, 130));"
#                                  "    min-height: 0px;"
#                                  "}"
#                                  "QScrollBar::add-line:vertical {"
#                                  "    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,"
#                                  "    stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));"
#                                  "    height: 0px;"
#                                  "    subcontrol-position: bottom;"
#                                  "    subcontrol-origin: margin;"
#                                  "}"
#                                  "QScrollBar::sub-line:vertical {"
#                                  "    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,"
#                                  "    stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));"
#                                  "    height: 0 px;"
#                                  "    subcontrol-position: top;"
#                                  "    subcontrol-origin: margin;"
#                                  "}"


# self.pushButton.clicked.connect(lambda: self.draw())
# self.pushButton_2.clicked.connect(self.close())
#
# def draw(self):
#     x = np.random.normal(size=1000)
#     y = np.random.normal(size=(3, 1000))
#     for i in range(3):
#         self.graphicsView.plot(x, y[i], pen=(i, 3))
#
#
# def close(self):
#     self.graphicsView.clear()


import datetime
import json
import sys
from threading import Thread

import pandas as pd
import numpy as np
import requests
import seaborn as sns
import matplotlib.pyplot as plt
from PyQt5 import QtGui
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5.uic.properties import QtWidgets
from PyQt5 import QtWidgets, uic
from pyqtgraph import PlotWidget
import pyqtgraph as pg
import sys


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

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        #Load the UI Page
        uic.loadUi('main_gui.ui', self)
        self.pushButton.clicked.connect(self.startjarvis)
        self.pushButton_2.clicked.connect(self.close)
    def startjarvis(self):
        # main gif run
        self.movie = QtGui.QMovie(
            "/home/aman/PycharmProjects/weather/thunder.gif")
        self.label.setMovie(self.movie)
        self.movie.start()
        self.draw()
        # # initlization gif run
        # self.ui.movie = QtGui.QMovie(
        #     "/home/aman/PycharmProjects/JARVIS/data/inslization.gif")
        # self.ui.label_3.setMovie(self.ui.movie)
        # self.ui.movie.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start(1000)

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
        self.show()

    def showtime(self):
        global f
        # datetime.datetime.now().strftime("%H hour and %M minutes")
        # textbox=background:transparent;\nfont: 75 11pt "Purisa";\ncolor:white;
        self.textBrowser_2.setText(
            datetime.datetime.now().strftime("%H:%M"))  # :%S
        self.textBrowser_3.setText(datetime.datetime.now().strftime("%A"))
        self.textBrowser.setText(datetime.datetime.now().strftime("%B %Y"))
        self.textBrowser_4.setText(datetime.datetime.now().strftime("%d"))
        self.textBrowser_5.setText(datetime.datetime.now()
                                      .strftime(f"{arts}   |  {str(round(temperature - 273.15))}" +
                                                u"\N{DEGREE SIGN}C   | " + f" Humidity-{humidity}"))
        # self.ui.textBrowser_6.append(f.getvalue())
def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()