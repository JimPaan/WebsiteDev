# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'display.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_display(object):
    def setupUi(self, display):
        display.setObjectName("display")
        display.resize(360, 527)
        display.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.centralwidget = QtWidgets.QWidget(display)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 240, 131, 16))
        self.label_2.setStyleSheet("font: 87 8pt \"Arial Black\";\n"
"color: rgb(0, 0, 127);\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 370, 131, 16))
        self.label_3.setStyleSheet("font: 87 8pt \"Arial Black\";\n"
"color: rgb(0, 0, 127);\n"
"")
        self.label_3.setObjectName("label_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 10, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"background-color: rgb(67, 66, 66);\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"}\n"
"QPushbutton:enabled{\n"
"background-color: rgb(85, 0, 255);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(13, 47, 114);\n"
"    color: rgb(255, 255, 254);\n"
"}\n"
"QPushButton:hover:!pressed{\n"
"background-color: rgb(189, 110, 12);\n"
"    color: rgb(12, 47, 112);\n"
"}\n"
"QPushButton:disabled{\n"
"background-color: rgb(170, 170, 170);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(60, 260, 211, 81))
        self.textBrowser.setStyleSheet("border-radius : 25px;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:0.761194 rgba(255, 192, 26, 255), stop:1 rgba(255, 255, 255, 255));")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(60, 400, 211, 81))
        self.textBrowser_2.setStyleSheet("border-radius : 25px;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:0.761194 rgba(255, 192, 26, 255), stop:1 rgba(255, 255, 255, 255));")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(15, 90, 321, 91))
        self.textBrowser_3.setStyleSheet("border-radius : 25px;\n"
"font: 22pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:0.761194 rgba(255, 192, 26, 255), stop:1 rgba(255, 255, 255, 255));")
        self.textBrowser_3.setObjectName("textBrowser_3")
        display.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(display)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 360, 18))
        self.menubar.setObjectName("menubar")
        display.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(display)
        self.statusbar.setObjectName("statusbar")
        display.setStatusBar(self.statusbar)

        self.retranslateUi(display)
        QtCore.QMetaObject.connectSlotsByName(display)

    def retranslateUi(self, display):
        _translate = QtCore.QCoreApplication.translate
        display.setWindowTitle(_translate("display", "MainWindow"))
        self.label_2.setText(_translate("display", "Estimated Arrival"))
        self.label_3.setText(_translate("display", "No. Passenger"))
        self.pushButton_4.setText(_translate("display", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    display = QtWidgets.QMainWindow()
    ui = Ui_display()
    ui.setupUi(display)
    display.show()
    sys.exit(app.exec_())
