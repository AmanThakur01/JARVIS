from userInterface import UserInterface
from bookService import BookService
from PyQt5 import QtGui, QtWidgets, QtCore
# from PyQt5.QtCore import QTime, QTimer, QDate, Qt
# from PyQt5.QtGui import QMovie
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from lib_gui import Ui_library
from threading import Thread
import sys


class MainThread(Thread):
    def run(self):
        service = BookService()
        service.old()

        ui = UserInterface(service)
        ui.main_menu()


startExecution = MainThread()


class Main(QMainWindow):
    # global f

    def __init__(self):
        super().__init__()
        self.ui = Ui_library()
        print("Initiating.. System modules")
        self.ui.setupUi(self)
        self.startlib()
        self.ui.pushButton_3.clicked.connect(self.close)

    def startlib(self):
        pass
        # main gif run
        # self.ui.movie = QtGui.QMovie(
        #     "/home/aman/PycharmProjects/JARVIS/data/mainf.gif")
        # self.ui.label_2.setMovie(self.ui.movie)
        # self.ui.movie.start()
        # # initlization gif run
        # self.ui.movie = QtGui.QMovie(
        #     "/home/aman/PycharmProjects/JARVIS/data/inslization.gif")
        # self.ui.label_3.setMovie(self.ui.movie)
        # self.ui.movie.start()


app = QApplication(sys.argv)
library = Main()
library.show()
exit(app.exec_())
