import sys
from PySide2.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(250, 150, 500, 500)
        self.setWindowTitle("Using checkbox")
        self.ui()

    def ui(self):
        self.combo = QComboBox(self)
        self.combo.move(150, 100)
        btn = QPushButton("Save", self)
        btn.move(150, 130)
        self.combo.addItem("1")
        self.combo.addItem("2")
        self.combo.addItem("3")
        self.combo.addItems(["4", '5', '6'])
        btn.clicked.connect(self.getvalue)
        self.show()

    def getvalue(self):
        print(self.combo.currentText())

def main():
    app = QApplication(sys.argv)
    window=Window()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()