from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 527)
        MainWindow.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 10, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Handwriting")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 10pt \"Lucida Handwriting\";")
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 50, 111, 81))
        self.label_2.setStyleSheet("font: 75 18pt \"Candara\";")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(85, 360, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
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
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 360, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color: rgb(67, 66, 66);\n"
"    color: rgb(255, 255, 255);\n"
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
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 390, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"background-color: rgb(67, 66, 66);\n"
"    color: rgb(255, 255, 255);\n"
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
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 340, 151, 20))
        self.label_4.setStyleSheet("font: 63 8pt \"Yu Gothic UI Semibold\";")
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 180, 161, 111))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("background-image:url(:/nurl(:/newPrefix/clipart2228037.png)ewPrefix/clipart2228037.png)")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/newPrefix/clipart2228037.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 360, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "    WELCOME"))
        self.label_2.setText(_translate("MainWindow", "AeroBus"))
        self.pushButton.setText(_translate("MainWindow", "T815"))
        self.pushButton_2.setText(_translate("MainWindow", "T789"))
        self.pushButton_3.setText(_translate("MainWindow", "T870"))
        self.label_4.setText(_translate("MainWindow", "Please Choose Your Bus"))

import logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
