import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
import first


class MyGui(QMainWindow):

    def __init__(self):
        super(MyGui,self).__init__()
        uic.loadUi("first.ui",self)
   #     self.show()                                      # ni just display ui
        self.pushButton.clicked.connect(self.gotoscreen2)   #fuction for clicked button (and kena tambah lagi untuk bas lain)
    #    self.pushButton_2.clicked.connect(self.gotoscreen2) #kena ejas dekat 1. gotoscreen2 or 2. class Display
    #    self.pushButton_3.clicked.connect(self.gotoscreen2)

    def gotoscreen2(self):
        display = Display()
        widget.addWidget(display)
        widget.setCurrentIndex(widget.currentIndex()+1)


class Display(QMainWindow):
    def __init__(self):
        super(Display,self).__init__()
        uic.loadUi("display.ui",self)
        #self.show()
        self.pushButton.clicked.connect(self.gotoscreen1())

    def gotoscreen1(self):
        jojo = MyGui()
        widget.addWidget(jojo)
        widget.setCurrentIndex(widget.currentIndex()+1)

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
mainwindow = MyGui()
widget.addWidget(mainwindow)
widget.setFixedHeight(527)
widget.setFixedWidth(360)
widget.show()


class main():
    app = QApplication([])
    window = MyGui()
    app.exec_()

     #if __name__== '__main__':


