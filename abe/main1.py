import sys
from first import *
from display import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication

widget = QtWidgets.QStackedWidget()


class first_window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(first_window, self).__init__()
        self.setupUi()

        self.pushButton.clicked.connect(self.gotoscreen2)
        self.pushButton_2.clicked.connect(self.gotoscreen2)
        self.pushButton_3.clicked.connect(self.gotoscreen2)

    def gotoscreen2(self):
        jojo = second_window()
        widget.addWidget(jojo)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class second_window(QDialog, Ui_display):
    def __init__(self):
        super(second_window, self).__init__()
        self.setupUi()

        self.pushButton_4.clicked.connect(self.gotofirst)


    def gotofirst(self):
        koala = first_window()
        widget.addWidget(koala)
        widget.setCurrentIndex(widget.currentIndex() + 1)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = first_window()
    window.show()
    sys.exit(app.exec_())