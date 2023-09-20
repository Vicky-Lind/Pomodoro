from PyQt5.QtWidgets import QMainWindow, QApplication, QFrame, QLabel, QPushButton, QGraphicsDropShadowEffect
from PyQt5 import QtCore
from PyQt5.QtCore import *
import sys
from PyQt5.QtGui import QCursor, QPalette, QBrush, QColor
import time
from PyQt5.QtGui import QPainter, QBrush, QPen, QPixmap
from PyQt5.QtCore import Qt
from qroundprogressbar import QRoundProgressBar

# TODO: Add a progress bar
# TODO: Add a settings button
# TODO: Add a settings window
# TODO: Add a close button
# TODO: Add a minimize button
# TODO: Add a pause button
# TODO: Add a reset button
# TODO: Add dictionary to store welcome_label texts

WORK_TIME_INT =  5
REST_TIME_INT = 2

def secs_to_minsec(secs: int):
    mins = secs // 60
    secs = secs % 60
    minsec = f'{mins:02}:{secs:02}'
    return minsec

class MainWindow(QMainWindow):
    WORK_TIME = True
    
    def __init__(self):
        super().__init__()
        
        
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setGeometry(0,0,320,542)
        
        main_frame = QFrame(self)
        main_frame.setGeometry(0,30,306,492)
        main_frame.setStyleSheet("""
            QFrame {
                background: QLinearGradient( x1: 0, y1: 0,x2: 0, y2: 1, stop: 0 #00AFB9,stop: 1 #02536A );           
                border-radius: 13px;
            }
        """)
        
        # ??
        main_frame.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=20, xOffset=2, yOffset=2))
        
        self.welcome_label = QLabel(self)
        self.welcome_label.setText("Time to focus!")
        self.welcome_label.setGeometry(75,55,160,19)
        self.welcome_label.setAlignment(Qt.AlignCenter)
        self.welcome_label.setStyleSheet("""
            QLabel {
                color: white;
                font-family: arial;
                font-size: 12.03pt;
                font-weight: bold;
            }
        """)
        
        start_button = QPushButton(self)
        start_button.setText("Start Timer")
        start_button.clicked.connect(self.startTimer)
        start_button.setGeometry(39,397,227,43)
        start_button.setCursor(QCursor(Qt.PointingHandCursor))
        start_button.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=12, xOffset=0, yOffset=8))
        
        start_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(22,202,159, 56%);
                border-radius: 20px;
                color: white;
                font-family: arial;
                font-size: 12.03pt;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: rgba(136, 228, 205, 56%);
            }

            QPushButton:pressed {
                background-color: rgba(14, 130, 102, 56%);     
            }
        """)
        
        self.info_label_1 = QLabel(self)
        self.info_label_1.setAlignment(Qt.AlignCenter)
        self.info_label_1.setText("Now: Work")
        self.info_label_1.setGeometry(39, 450, 227, 19)
        self.info_label_1.setStyleSheet("""
            QLabel {
                background: transparent;
                color: white;
                font-family: arial;
                font-size: 7.4399999999999995pt;
                font-weight: bold;
            }
        """)
        
        self.info_label_2 = QLabel(self)
        self.info_label_2.setAlignment(Qt.AlignCenter)
        self.info_label_2.setText("Up Next: Rest Time")
        self.info_label_2.setGeometry(39, 470, 227, 19)
        self.info_label_2.setStyleSheet("""
            QLabel {
                background: transparent;
                color: white;
                font-family: arial;
                font-size: 7.4399999999999995pt;
                font-weight: bold;
            }
        """)
        # self.progress = QRoundProgressBar(self)
        # self.progress.setBarStyle(QRoundProgressBar.BarStyle.DONUT)

        # # style accordingly via palette
        # self.palette = QPalette()
        # brush = QBrush(QColor(0, 0, 255))
        # brush.setStyle(Qt.SolidPattern)
        # self.palette.setBrush(QPalette.Active, QPalette.Highlight, brush)

        # self.progress.setPalette(self.palette)
        # self.setCentralWidget(self.progress)
        
        self.time_label = QLabel(self)
        self.time_label.setAlignment(Qt.AlignCenter)  
        self.time_label.setText("01:00")
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
        
        self.time_left_int = WORK_TIME_INT
        
        self.timer = QTimer(self)
        self.update_gui()
        
        
        self.paint = QPainter(self)
    
        self.label = QLabel(self)
        self.label.setStyleSheet
        canvas = QPixmap(400, 300)
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_something()

    def draw_something(self):
        painter = QPainter(self.label.pixmap())
        painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
        painter.drawEllipse(40, 40, 400, 400)
        painter.end()
    
    def startTimer(self):
        if self.WORK_TIME:
            self.time_left_int = WORK_TIME_INT
        else:
            self.time_left_int = REST_TIME_INT
        
        self.timer.timeout.connect(self.timerTimeout)
        self.timer.start(1000)
        
    def timerTimeout(self):
        self.time_left_int -= 1
        
        if self.time_left_int == 0:
            if self.WORK_TIME:
                self.WORK_TIME = False
                self.time_left_int = REST_TIME_INT
                self.welcome_label.setText("Sit back and relax 😎")
                self.info_label_1.setText("Now: Rest")
                self.info_label_2.setText("Up Next: Work Time")
            else:
                self.WORK_TIME = True
                self.time_left_int = WORK_TIME_INT
                self.welcome_label.setText("Time to focus!")
                self.info_label_1.setText("Now: Work")
                self.info_label_2.setText("Up Next: Rest Time")
        self.update_gui()
        
    def update_gui(self):
        minsec = secs_to_minsec(self.time_left_int)
        self.time_label.setText(minsec)
    
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

    # for i in range(0, 100, 5):
    #     appWindow.progress.setValue(i)
    #     app.processEvents()
    #     time.sleep(0.1)

    sys.exit(app.exec())
