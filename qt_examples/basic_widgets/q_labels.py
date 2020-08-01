import sys
from PySide2.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 350, 350)
        self.setWindowTitle("Using labels")
        self.ui()

    def ui(self):
        text1 = QLabel("Hello Python", self)
        text2 = QLabel("Hello world", self)
        text1.move(100, 50)
        text2.move(200, 50)
        self.show()

def main():
    app = QApplication(sys.argv)
    window=Window()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()