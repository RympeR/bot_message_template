import sys

from PySide2.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Horizontal layout")
        self.setGeometry(50, 50, 400, 400)
        self.UI()

    def UI(self):
        hbox = QHBoxLayout()
        button1 = QPushButton("1")
        button2 = QPushButton("2")
        button3 = QPushButton("3")
        hbox.addStretch()
        hbox.addWidget(button1)
        hbox.addWidget(button2)
        hbox.addWidget(button3)
        self.setLayout(hbox)
        self.show()



def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
