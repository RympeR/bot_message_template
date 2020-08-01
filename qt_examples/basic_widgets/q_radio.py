import sys
from PySide2.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(250, 150, 500, 500)
        self.setWindowTitle("Using checkbox")
        self.ui()

    def ui(self):
        self.radio1 = QRadioButton("Choice1", self)
        self.radio2 = QRadioButton("Choice2", self)
        self.radio3 = QRadioButton("Choice3", self)
        self.radio4 = QRadioButton("Choice4", self)
        self.radio1.move(50, 50)
        self.radio2.move(50, 80)
        self.radio3.move(50, 110)
        self.radio4.move(50, 140)
        self.radio1.setChecked(True)
        print(self.radio1.isChecked())
        self.show()

    def getvalue(self):
        print(self.combo.currentText())

def main():
    app = QApplication(sys.argv)
    window=Window()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()