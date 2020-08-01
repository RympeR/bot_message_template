import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import QFont
from PySide2.QtCore import QTimer

font = QFont("Times", 14)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle("Using labels")
        self.ui()

    def ui(self):
        self.addRecord = QLineEdit(self)
        self.addRecord.move(100, 50)
        self.listWidget = QListWidget(self)
        self.listWidget.move(100, 80)
        #################################################
        list_s = ["batman", "superman", "spiderman"]
        self.listWidget.addItems(list_s)
        self.listWidget.addItem("human")
        #################################################
        btn_add = QPushButton("add", self)
        btn_add.move(360, 80)
        btn_add.clicked.connect(self.add)
        btn_delete = QPushButton("delete", self)
        btn_delete.move(360, 110)
        btn_delete.clicked.connect(self.delete)
        btn_get = QPushButton("get", self)
        btn_get.move(360, 140)
        btn_get.clicked.connect(self.select)
        btn_del_all = QPushButton("delete_all", self)
        btn_del_all.move(360, 170)
        btn_del_all.clicked.connect(self.delete_all)
        # for num in range(5, 11):
        #     self.listWidget.addItem(str(num))

        self.show()

    def add(self):
        value = self.addRecord.text()
        self.listWidget.addItem(value)
        self.addRecord.setText("")

    def select(self):
        value = self.listWidget.currentItem().text()
        print(value)

    def delete_all(self):
        self.listWidget.clear()

    def delete(self):
        id_=self.listWidget.currentRow()
        self.listWidget.takeItem(id_)

def main():
    app = QApplication(sys.argv)
    window=Window()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()