import sys

from PySide2.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Horizontal layout")
        self.setGeometry(50, 50, 400, 400)
        self.UI()

    def UI(self):
        mainLayout = QFormLayout()
        # mainLayout.setRowWrapPolicy(QFormLayout.WrapAllRows)
        name_txt = QLabel("name: ")
        name_input = QLineEdit()
        name_input.setPlaceholderText("Input name: ")
        pass_txt = QLabel("pass: ")
        pass_input = QLineEdit()
        hbox = QHBoxLayout()
        hbox.addWidget(QPushButton("Enter: "))
        hbox.addWidget(QPushButton("Exit: "))
        mainLayout.addRow(name_txt, name_input)
        mainLayout.addRow(pass_txt, pass_input)
        mainLayout.addRow(QLabel("Country: "), QComboBox())
        mainLayout.addRow(hbox)
        self.setLayout(mainLayout)
        self.show()



def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
