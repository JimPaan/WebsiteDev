import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from first import Ui_MainWindow
from display import Ui_display


class MyGui(QMainWindow,Ui_MainWindow):

    def __init__(self):
        super(MyGui, self).__init__()
        self.pushButton = None
        uic.loadUi("first.ui", self)
        self.second_window = Display()
        self.pushButton.clicked.connect(self.gotoscreen2)
        self.pushButton_2.clicked.connect(self.gotoscreen2)
        self.pushButton_3.clicked.connect(self.gotoscreen2)

        if self.pushButton_2.clicked is True:
            self.bus_name = 'T789'

    @staticmethod
    def gotoscreen2():
        display = Display()
        widget.addWidget(display)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def passinginfos(self):
        self.second_window.textBrowser.setText(self.bus_name)
        self.second_window.textBrowser_2.setText()


class Display(QMainWindow, Ui_display):
    def __init__(self):
        super(Display,self).__init__()
        uic.loadUi("display.ui",self)
        self.pushButton_4.clicked.connect(self.gotofirst)
        self.bus_name =

    def gotofirst(self):
        mainwindow = MyGui()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
        #kokokokoko



app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
mainwindow = MyGui()
widget.addWidget(mainwindow)
widget.setFixedHeight(527)
widget.setFixedWidth(360)
widget.show()

def main():
    app = QApplication([])
    window = MyGui()
    app.exec_()

if __name__ == '__main__':
    main()