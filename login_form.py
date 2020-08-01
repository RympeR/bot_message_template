from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1040, 456)
        MainWindow.setStyleSheet(u"#MainWindow, #centralWidget{\n"
        "	background-color: rgb(192, 211, 210);\n"
        "}\n"
        "")
        self.actionLog_in = QAction(MainWindow)
        self.actionLog_in.setObjectName(u"actionLog_in")
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.login = QLineEdit(self.centralwidget)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(420, 130, 171, 22))
        self.password = QLineEdit(self.centralwidget)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(420, 240, 171, 22))
        self.login_label = QLabel(self.centralwidget)
        self.login_label.setObjectName(u"login_label")
        self.login_label.setGeometry(QRect(470, 80, 71, 31))
        font = QFont()
        font.setFamily(u"Bahnschrift Light")
        font.setPointSize(12)

        self.login_label.setFont(font)
        self.pass_label = QLabel(self.centralwidget)
        self.pass_label.setObjectName(u"pass_label")
        self.pass_label.setGeometry(QRect(460, 200, 91, 21))
        self.pass_label.setFont(font)
        self.enter_btn = QPushButton(self.centralwidget)
        self.enter_btn.setObjectName(u"enter_btn")
        self.enter_btn.setGeometry(QRect(460, 300, 111, 41))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1040, 26))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.actionLog_in)
        self.menu_2.addAction(self.action)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
    def log_in(self):
        pass

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionLog_in.setText(QCoreApplication.translate("MainWindow", u"Log in", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0448\u0430\u0431\u043b\u043e\u043d\u0430\u043c\u0438", None))
        self.login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"login", None))
        self.password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"password", None))
        self.login_label.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.pass_label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.enter_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0428\u0430\u0431\u043b\u043e\u043d\u044b", None))
    # retranslateUi


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
