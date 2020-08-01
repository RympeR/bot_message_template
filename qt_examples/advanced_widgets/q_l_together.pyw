import sys

from PySide2.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Horizontal layout")
        self.setGeometry(50, 50, 400, 400)
        self.UI()

    def UI(self):
        mainLayout = QVBoxLayout()
        tophbox = QHBoxLayout()
        tophbox.setContentsMargins(100, 10, 20, 20)#left top right bottom
        button1 = QPushButton("1")
        button2 = QPushButton("2")
        button3 = QPushButton("3")
        tophbox.addWidget(button1)
        tophbox.addWidget(button2)
        tophbox.addWidget(button3)

        bothbox = QHBoxLayout()
        button1 = QPushButton("1")
        button2 = QPushButton("2")
        button3 = QPushButton("3")
        # hbox.addStretch()
        bothbox.addWidget(button1)
        bothbox.addWidget(button2)
        bothbox.addWidget(button3)
        mainLayout.addLayout(tophbox)
        mainLayout.addLayout(bothbox)
        self.setLayout(mainLayout)
        self.show()



def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
