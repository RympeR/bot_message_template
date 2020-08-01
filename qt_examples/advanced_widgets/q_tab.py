import sys

from PySide2.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 350, 350)
        self.setWindowTitle("Using tabs")
        self.ui()

    def ui(self):
        mainLayout = QVBoxLayout()
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabs.addTab(self.tab1, "First tab")
        self.tabs.addTab(self.tab2, "Second tab")
        self.tabs.addTab(self.tab3, "Third tab")
        #######################################
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.text = QLabel("Hello python")
        self.btn1 = QPushButton("First tab")
        self.btn2 = QPushButton("Second tab")
        vbox.addWidget(self.text)
        vbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)
        self.tab1.setLayout(vbox)
        self.tab2.setLayout(hbox)

        mainLayout.addWidget(self.tabs)
        self.setLayout(mainLayout)
        self.show()

def main():
    app = QApplication(sys.argv)
    window=Window()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
