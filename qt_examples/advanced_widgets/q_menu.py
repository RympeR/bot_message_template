import sys

from PySide2.QtWidgets import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 350, 350)
        self.setWindowTitle("Using menus")
        self.ui()

    def ui(self):
        ################MAIN MENU####################
        menubar = self.menuBar()
        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")
        code = menubar.addMenu("Code")
        help_ = menubar.addMenu("Help")
        ###################SUB MENU###################
        new = QAction("&New Project", self)
        open_ = QAction("&open", self)
        exit = QAction("&quit", self)
        exit.setShortcut("Ctrl+Q")
        exit.triggered.connect(self.close)
        file.addAction(new)
        new.setShortcut("Ctrl+N")
        file.addAction(open_)
        file.addSeparator()
        file.addAction(exit)

        self.show()

    def close(self):
        mbox = QMessageBox.question(
            self, "Warning", "You sure?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            sys.exit()


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
