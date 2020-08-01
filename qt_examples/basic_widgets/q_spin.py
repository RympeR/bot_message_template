import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import QFont

font = QFont("Times", 16)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 350, 350)
        self.setWindowTitle("Using labels")
        self.ui()

    def ui(self):
        self.spin = QSpinBox(self)
        self.spin.move(150, 100)
        self.spin.setFont(font)
        # self.spin.setMinimum(25)
        # self.spin.setMaximum(110)
        self.spin.setRange(25, 110)
        # self.spin.setPrefix("$ ")
        self.spin.setSuffix(" km")
        self.spin.setSingleStep(5)
        # self.spin.valueChanged.connect(self.getValue)
        btn = QPushButton("submit", self)
        btn.move(25, 150)
        btn.clicked.connect(self.getSpinValue)
        self.show()

    def getSpinValue(self):
        print(self.spin.value())

    def getValue(self):
        value = self.spin.value()
        print(value)

def main():
    app = QApplication(sys.argv)
    window=Window()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()