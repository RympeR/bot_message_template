import sys
from PySide2.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 350, 350)
        self.setWindowTitle("Using line edits")
        self.ui()

    def ui(self):
        self.nameTextBox = QLineEdit(self)
        self.nameTextBox.setPlaceholderText("Please enter your name")
        self.nameTextBox.move(120, 50)
        self.passwordTextBox = QLineEdit(self)
        self.passwordTextBox.setPlaceholderText("Enter your password")
        self.passwordTextBox.setEchoMode(QLineEdit.Password)
        self.passwordTextBox.move(120, 80)


        btn = QPushButton("Submit", self)
        btn.clicked.connect(self.output)
        btn.move(120, 120)
        self.show()

    def output(self):
        print(self.nameTextBox.text())
        print(self.passwordTextBox.text())

def main():
    app = QApplication(sys.argv)
    window=Window()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()