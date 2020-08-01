import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import QFont

font = QFont("Times", 14)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 350, 350)
        self.setWindowTitle("Using labels")
        self.ui()

    def ui(self):
        self.editor = QTextEdit(self)
        self.editor.move(30, 30)
        self.editor.setAcceptRichText(False)
        self.editor.setFont(font)
        btn = QPushButton("submit", self)
        btn.move(200, 280)
        btn.clicked.connect(self.getValue)
        self.show()

    def getValue(self):
        value = self.editor.toPlainText()
        print(value)

def main():
    app = QApplication(sys.argv)
    window=Window()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()