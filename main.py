import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
import re
import datetime
from lib.youtube_Layout.py import Ui_MainWindow
from PyQt5 import QtWebEngineWidgets

# form_class=uic.loadUiType('D:/section6/ui/youtube.ui')[0]

class TestForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestForm()
    window.show()
    app.exec_()
