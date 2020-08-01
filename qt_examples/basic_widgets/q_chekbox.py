import sys
from PySide2.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 350, 350)
        self.setWindowTitle("Using checkbox")
        self.ui()

    def ui(self):
        self.name = QLineEdit(self)
        self.name.setPlaceholderText("Name")
        self.surname = QLineEdit(self)
        self.surname.setPlaceholderText("Surname")
        self.name.move(150, 50)
        self.surname.move(150, 80)
        self.remember = QCheckBox("Remember me", self)
        self.remember.move(150, 110)
        btn = QPushButton("Submit", self)
        btn.clicked.connect(self.getvalue)
        btn.move(200, 140)

        self.show()

    def getvalue(self):
        print(self.name.text())
        print(self.surname.text())
        print(self.remember.isChecked())

def main():
    app = QApplication(sys.argv)
    window=Window()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()