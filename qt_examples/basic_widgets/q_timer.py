import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import QFont
from PySide2.QtCore import QTimer

font = QFont("Times", 14)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 350, 350)
        self.setWindowTitle("Using labels")
        self.ui()

    def ui(self):
        self.colorLabel = QLabel(self)
        self.colorLabel.resize(250, 250)
        self.colorLabel.setStyleSheet("background-color:green")
        self.colorLabel.move(40, 20)
        #############################BUTTONS######################
        btn = QPushButton("start", self)
        btn.move(110, 280)
        btnStop = QPushButton("stop", self)
        btnStop.move(190, 280)
        self.timer = QTimer()
        self.timer.setInterval(2000)
        self.timer.timeout.connect(self.changeColor)
        btn.clicked.connect(self.start)
        btnStop.clicked.connect(self.stop)
        self.value = 0
        self.show()

    def changeColor(self):
        if self.value == 0:
            self.colorLabel.setStyleSheet("background-color: yellow")
            self.value = 1
        else:
            self.colorLabel.setStyleSheet("background-color: red")
            self.value = 0


    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()
        self.colorLabel.setStyleSheet("background-color:green")

def main():
    app = QApplication(sys.argv)
    window=Window()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()