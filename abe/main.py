import sys

from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from first import Ui_MainWindow
from display import Ui_display
import Trial


class MyGui(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MyGui, self).__init__()
        #uic.loadUi("first.ui", self)
        self.setupUi(self)
        self.second_window = Display()

        if self.pushButton_3.clicked is True:
            self.no = 3
            self.bus_name = Trial.show_one_display(self.no, 2)
            self.passs = Trial.show_one_display(self.no, 3)
            self.etaa = Trial.show_one_display(self.no, 4)
        elif self.pushButton_2.clicked is True:
            self.no = 2
            self.bus_name = Trial.show_one_display(self.no, 2)
            self.passs = Trial.show_one_display(self.no, 3)
            self.etaa = Trial.show_one_display(self.no, 4)
        else:
            self.no = 1
            self.bus_name = Trial.show_one_display(self.no, 2)
            self.passs = Trial.show_one_display(self.no, 3)
            self.etaa = Trial.show_one_display(self.no, 4)

        self.pushButton.clicked.connect(self.passinginfos)
        self.pushButton_2.clicked.connect(self.passinginfos)
        self.pushButton_3.clicked.connect(self.passinginfos)

    @staticmethod
    def gotoscreen2():
        display = Display()
        widget.addWidget(display)
        widget.setCurrentIndex(widget.currentIndex() + 1)

#https://www.youtube.com/watch?v=NrijKenny3Y
    def passinginfos(self):
        self.second_window.textBrowser.setText(self.bus_name)
        self.second_window.textBrowser_2.setText(self.etaa)
        self.second_window.textBrowser_3.setText(self.passs)
        self.gotoscreen2()



class Display(QMainWindow, Ui_display):
    def __init__(self):
        super(Display, self).__init__()
        #uic.loadUi("display.ui", self)
        self.setupUi(self)
        self.pushButton_4.clicked.connect(self.gotofirst)

    @staticmethod
    def gotofirst():
        mainwindow = MyGui()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        #kokokokoko


widget = QtWidgets.QStackedWidget

if __name__ == '__main__':
    app = QApplication([])
    window = MyGui()
    window.show()
    sys.exit(app.exec_())
