# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lib_gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_library(object):
    def setupUi(self, library):
        library.setObjectName("library")
        library.resize(828, 523)
        library.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        library.setMouseTracking(True)
        library.setFocusPolicy(QtCore.Qt.ClickFocus)
        library.setAcceptDrops(True)
        library.setAutoFillBackground(False)
        library.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(library)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-3, -10, 831, 541))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 140, 81, 71))
        self.pushButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("\n"
"border-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("bookedt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(100, 100))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 831, 91))
        self.label_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_2.setText("")
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(6, 6, 121, 81))
        self.label_3.setStyleSheet("background:transparent;")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("lib2.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(130, 30, 411, 51))
        font = QtGui.QFont()
        font.setFamily("Purisa")
        font.setPointSize(14)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:transparent;\n"
"")
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 44, 89, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("help3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(90, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(720, 45, 91, 41))
        self.pushButton_3.setStyleSheet("background:transparent;")
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("poweroff2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(90, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(340, 140, 91, 71))
        self.pushButton_4.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setStyleSheet("\n"
"border-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.pushButton_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("menu.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(570, 150, 81, 61))
        self.pushButton_5.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_5.setAutoFillBackground(False)
        self.pushButton_5.setStyleSheet("\n"
"border-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.pushButton_5.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("buy2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QtCore.QSize(140, 70))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(120, 330, 81, 71))
        self.pushButton_6.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_6.setAutoFillBackground(False)
        self.pushButton_6.setStyleSheet("\n"
"border-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.pushButton_6.setText("")
        self.pushButton_6.setIcon(icon)
        self.pushButton_6.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(350, 330, 81, 71))
        self.pushButton_7.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_7.setAutoFillBackground(False)
        self.pushButton_7.setStyleSheet("\n"
"border-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.pushButton_7.setText("")
        self.pushButton_7.setIcon(icon)
        self.pushButton_7.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(570, 330, 81, 71))
        self.pushButton_8.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_8.setAutoFillBackground(False)
        self.pushButton_8.setStyleSheet("\n"
"border-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.pushButton_8.setText("")
        self.pushButton_8.setIcon(icon)
        self.pushButton_8.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_8.setObjectName("pushButton_8")
        library.setCentralWidget(self.centralwidget)

        self.retranslateUi(library)
        QtCore.QMetaObject.connectSlotsByName(library)

    def retranslateUi(self, library):
        _translate = QtCore.QCoreApplication.translate
        library.setWindowTitle(_translate("library", "MainWindow"))
        self.label.setWhatsThis(_translate("library", "Book Category"))
        self.pushButton.setWhatsThis(_translate("library", "Book List"))
        self.textBrowser.setWhatsThis(_translate("library", "<html><head/><body><p>LIBRARY</p></body></html>"))
        self.textBrowser.setHtml(_translate("library", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Purisa\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Whelcome To The Temple of Books.</p></body></html>"))
        self.pushButton_4.setWhatsThis(_translate("library", "Book List"))
        self.pushButton_5.setWhatsThis(_translate("library", "Buy Book"))
        self.pushButton_6.setWhatsThis(_translate("library", "Book List"))
        self.pushButton_7.setWhatsThis(_translate("library", "Book List"))
        self.pushButton_8.setWhatsThis(_translate("library", "Book List"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    library = QtWidgets.QMainWindow()
    ui = Ui_library()
    ui.setupUi(library)
    library.show()
    sys.exit(app.exec_())

