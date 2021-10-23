from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('calculator')
        self.setGeometry(100,100,300,350)
        self.UiComponents()
        self.show()
    def UiComponents(self):
        self.label = QLabel(self)
        self.label.setGeometry(5,5,350,70)
        self.label.setWordWrap(True)
        
        
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())

