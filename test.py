# Python program to create a countdown timer using PyQt5  
# import all the required modules  
from PyQt5.QtWidgets import *  
from PyQt5 import QtCore, QtGui  
from PyQt5.QtGui import *  
from PyQt5.QtCore import *  
import sys  
  
class Window(QMainWindow):  
    def __init__(self):  
        super().__init__()  
  
        # set the window title  
        self.setWindowTitle("Python ")
        self.setGeometry(100, 100, 400, 600)  
        self.UiComponents()  
        self.show()  
  
    # function for the widgets  
    def UiComponents(self): 
        # create a count variable  
        self.count = 0  
        self.start = False  
        # create a push button for getting the time in seconds  
        btn = QPushButton("Set time(s)", self)  
        # set the geometry of the push button  
        btn.setGeometry(125, 100, 150, 50)  
        btn.clicked.connect(self.get_scnds)  
        self.label = QLabel("//TIMER//", self)  
        self.label.setGeometry(100, 200, 200, 50)  
        self.label.setStyleSheet("border : 3px solid black")  
        self.label.setFont(QFont('Times', 15))  
        self.label.setAlignment(Qt.AlignCenter)  
  
        start_btn = QPushButton("Start", self)  
        start_btn.setGeometry(125, 350, 150, 40)  
        start_btn.clicked.connect(self.start_actn)  
  
        pause_btn = QPushButton("Pause", self)   
        pause_btn.setGeometry(125, 400, 150, 40)  
        pause_btn.clicked.connect(self.pause_actn)  
  
        reset_btn = QPushButton("Reset", self)   
        reset_btn.setGeometry(125, 450, 150, 40)  
        reset_btn.clicked.connect(self.reset_actn)  
  
        timerClock = QTimer(self)  
        timerClock.timeout.connect(self.displayTime)  
        timerClock.start(100)  
  
    # function to be called by the timer clock  
    def displayTime(self):  
        if self.start:  
            self.count -= 1  
            if self.count == 0:  
                self.start = False  
                self.label.setText("Completed !!!! ")  
  
        if self.start:  
            txt = str(self.count / 10) + " s"  
            self.label.setText(txt)  
  
    def get_scnds(self):  
        self.start = False   
        second, done = QInputDialog.getInt(self, 'Seconds', 'Enter Seconds:')  
  
        if done:  
            self.count = second * 10  
  
            self.label.setText(str(second))  
  
    def start_actn(self):  
        self.start = True  
  
        if self.count == 0:  
            self.start = False  
  
    def pause_actn(self):  
        self.start = False  
  
    def reset_actn(self):  
  
        self.start = False  
        self.count = 0  
        self.label.setText("//TIMER//")  
  
# creating the pyqt5 application  
Base = QApplication(sys.argv)  
  
# creating an instance of the of Window created  
window = Window()  
  
# starting the application  
sys.exit(Base.exec())  