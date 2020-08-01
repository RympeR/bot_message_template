import sys
from PySide2.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 350, 350)
        self.setWindowTitle("Using labels")
        self.ui()

    def ui(self):
        self.text = QLabel("Hello Python", self)
        enterButton = QPushButton("Enter", self)
        exitButton = QPushButton("Exit", self)
        self.text.move(100, 50)
        enterButton.move(100, 100)
        exitButton.move(100, 200)
        enterButton.clicked.connect(self.enterFunc)
        exitButton.clicked.connect(self.exitFunc)
        self.show()

    def enterFunc(self):
        self.text.resize(150, 20)
        self.text.setText("you clicked enterEnter")

    def exitFunc(self):
        self.text.resize(150, 20)
        self.text.setText("exit")


def main():
    app = QApplication(sys.argv)
    window=Window()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()