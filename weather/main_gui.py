# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(810, 587)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 190, 791, 351))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 775, 1218))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(0, 1200))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.graphicsView = PlotWidget(self.frame)
        self.graphicsView.setGeometry(QtCore.QRect(40, 10, 681, 331))
        self.graphicsView.setMaximumSize(QtCore.QSize(2000, 2000))
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(710, 10, 80, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("thunder.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 0, 151, 91))
        self.textBrowser_2.setStyleSheet("background:white;\n"
"color: rgb(80, 185, 223);\n"
"font: 75 30pt \"Umpush\";")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(130, 40, 201, 51))
        self.textBrowser_3.setStyleSheet("background:white;\n"
"color: rgb(80, 185, 223);\n"
"font: 75 15pt \"Umpush\";")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(130, 0, 81, 41))
        self.textBrowser_4.setStyleSheet("background:white;\n"
"color: rgb(80, 185, 223);\n"
"font: 75 12pt \"Umpush\";\n"
"")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_5.setGeometry(QtCore.QRect(20, 80, 301, 41))
        self.textBrowser_5.setStyleSheet("background:white;\n"
"color: rgb(252, 140, 8);\n"
"font: 75 10pt \"Umpush\";\n"
"")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(600, 110, 89, 25))
        self.pushButton.setStyleSheet("background-color: rgb(52, 101, 164);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(700, 110, 89, 25))
        self.pushButton_2.setStyleSheet("background-color: rgb(239, 41, 41);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(160, 0, 161, 41))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 810, 22))
        self.menubar.setObjectName("menubar")
        self.menuhelp = QtWidgets.QMenu(self.menubar)
        self.menuhelp.setObjectName("menuhelp")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuhelp.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setStatusTip(_translate("MainWindow", "User Guide"))
        MainWindow.setWhatsThis(_translate("MainWindow", "help for user"))
        self.frame.setStatusTip(_translate("MainWindow", "Graphs"))
        self.frame.setWhatsThis(_translate("MainWindow", "graphs"))
        self.label.setStatusTip(_translate("MainWindow", "Weather Forecast"))
        self.label.setWhatsThis(_translate("MainWindow", "Thunder Rain"))
        self.pushButton.setText(_translate("MainWindow", "Refreash"))
        self.pushButton_2.setText(_translate("MainWindow", "Exit"))
        self.menuhelp.setStatusTip(_translate("MainWindow", "user guide to help"))
        self.menuhelp.setWhatsThis(_translate("MainWindow", "user guide to help"))
        self.menuhelp.setTitle(_translate("MainWindow", "Help"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))

from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

