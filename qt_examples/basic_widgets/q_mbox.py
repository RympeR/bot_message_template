import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import QFont

font = QFont("Times")

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 350, 350)
        self.setWindowTitle("Using labels")
        self.ui()

    def ui(self):
        enterButton = QPushButton("Enter", self)
        enterButton.setFont(font)
        enterButton.move(100, 100)
        enterButton.clicked.connect(self.enterFunc)
        self.show()

    def enterFunc(self):
        mbox = QMessageBox.question(self, "warn", "Are you sure to exit?",
                QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)

        print(string)
        if mbox == QMessageBox.Yes:
            sys.exit()
        else:
            print("not exit")

def main():
    app = QApplication(sys.argv)
    window=Window()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()