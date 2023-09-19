from PyQt5.QtWidgets import QMainWindow, QApplication, QFrame, QLabel, QPushButton
from PyQt5 import QtCore
from PyQt5.QtCore import *
import sys

DURATION_INT = 60

def secs_to_minsec(secs: int):
    mins = secs // 60
    secs = secs % 60
    minsec = f'{mins:02}:{secs:02}'
    return minsec

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setGeometry(0,0,306,542)
        
        main_frame = QFrame(self)
        main_frame.setGeometry(0,30,306,492)
        main_frame.setStyleSheet("""
            QFrame {
                background: QLinearGradient( x1: 0, y1: 0,x2: 0, y2: 1, stop: 0 #00AFB9,stop: 1 #02536A );           
                border-radius: 13px;
            }
        """)
        
        # ??
        main_frame.setFrameShadow(10)
        
        welcome_label = QLabel(self)
        welcome_label.setText("Time to focus!")
        
        welcome_label.setAlignment(Qt.AlignCenter)
        
        welcome_label.setGeometry(98,55,111,19)
        welcome_label.setStyleSheet("""
            QLabel {
                color: white;
                font-family: arial;
                font-size: 12.03pt;
                font-weight: bold;
            }
        """)
        
        start_button = QPushButton(self)
        start_button.setText("Start Timer")
        start_button.clicked.connect(self.start_time)
        start_button.setGeometry(39,397,227,43)
        
        start_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(22,202,159, 56%);
                border-radius: 20px;
                color: white;
                font-family: arial;
                font-size: 12.03pt;
                font-weight: bold;
            }
        """)
        
        self.time_label = QLabel(self)
        self.time_label.setAlignment(Qt.AlignCenter)  
        self.time_label.setGeometry(56,145,190,82)        
        self.time_label.setStyleSheet("""
            QLabel {
                background: transparent;
                color: white;
                font-family: arial;
                font-size: 50.97pt;
            }
        """)
        self.time_label.setParent(main_frame)
        
        self.time_left_int = DURATION_INT
        
        self.update_gui()
        
    def start_time(self):
        self.time_left_int = DURATION_INT
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timer_timeout)
        self.timer.start(1000)
        
    def timer_timeout(self):
        self.time_left_int -= 1
        
        if self.time_left_int == 0:
            return
        self.update_gui()
        
    def update_gui(self):
        self.time_label.setText(str(self.time_left_int))
    
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    appWindow = MainWindow()
    appWindow.show()
    sys.exit(app.exec())
