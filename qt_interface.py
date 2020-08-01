from bot_logic import DriverLogic
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
import sys

from PySide2.QtWidgets import *

from PySide2.QtGui import *

# from bot_logic import *


MESSAGES = {}
PROFILES = {}


MESSAGES = {}
PROFILES = {}


class MessageThread(QThread):
    __slots__ = [
        'driver',
        'message',
        'chat_id',
        'id_profile',
        'index_method',
        'amount'
    ]
    # message = ''
    # s1 = QtCore.pyqtSignal(str)

    def __init__(self, driver, parent=None):
        QThread.__init__(self, parent)
        # drive = DriverLogic()
        self.driver = driver

    def set_message(self, new_message: str):
        self.message = new_message

    def set_index(self, index_: int):
        self.index_method = index_

    def set_chat_id(self, id_: int):
        self.chat_id = id_

    def set_id_profile(self, id_: int):
        self.id_profile = id_

    def set_send(self, amount: int):
        self.amount = amount

    def call_send_message(self):
        self.driver.send_chat_message(
            self.id_profile,
            self.message,
            self.amount
        )

    def call_send_icebreaker(self):
        self.driver.send_icebreaker(self.id_profile)

    def call_send_icebreaker_to_moderation(self):
        self.driver.send_icebreaker_to_moderation(
            self.id_profile, self.message)

    def call_answertounread(self):
        self.driver.answertounread(self.message)

    def call_login(self):
        self.driver.login()

    def run(self):
        methods = [
            self.login,
            self.call_send_message,
            self.call_send_icebreaker_to_moderation,
            self.call_send_icebreaker,
        ]
        try:
            methods[self.index_method]()
        except Exception as identifier:
            pass


class Window(QMainWindow):
    tabs_arr = []
    thread_arr = []

    labels_message_arr = []
    labels_ice_arr = []
    labels_id_arr = []

    new_ice_btn_arr = []
    moder_ice_btn_arr = []
    reset_curr_ice_btn_arr = []

    online_buttons_arr = []

    entry_ice_arr = []
    entry_message_arr = []

    begin_message_buttons_arr = []
    stop_message_buttons_arr = []

    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 1040, 456)
        self.setWindowTitle("ПраймБот")
        self.ui()

    def ui(self):
        self.mainLayout = QVBoxLayout()
        self.menu()
        self.main_tab()
        
        self.setLayout(self.mainLayout)
        self.show()

    def menu(self):
        menubar = self.menuBar()
        template = menubar.addMenu("Шаблоны")
        enter = menubar.addMenu("Вход")
        login = QAction("&Log in", self)
        login.setShortcut("Ctrl+L")
        login.triggered.connect(self.login_form)
        add_template = QAction("&Template", self)
        add_template.setShortcut("Ctrl+T")
        add_template.triggered.connect(self.template_window)
        enter.addAction(login)
        template.addAction(add_template)

    def main_tab(self):
        self.login = QtWidgets.QLineEdit(self)
        self.login.setGeometry(QRect(420, 130, 171, 22))
        self.login.setObjectName("login")
        self.login.setPlaceholderText("Login")
        self.password = QtWidgets.QLineEdit(self)
        self.password.setGeometry(QRect(420, 240, 171, 22))
        self.password.setObjectName("password")
        self.password.setPlaceholderText("Password")
        self.login_label = QLabel("Логин", self)
        self.login_label.setGeometry(QRect(470, 80, 71, 31))
        font = QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(12)
        self.login_label.setFont(font)
        self.login_label.setObjectName("login_label")
        self.pass_label = QLabel("Пароль", self)
        self.pass_label.setGeometry(QRect(460, 200, 91, 21))
        self.pass_label.setFont(font)
        self.pass_label.setObjectName("pass_label")
        self.enter_btn = QPushButton("Войти", self)
        self.enter_btn.setGeometry(QRect(460, 300, 111, 41))
        self.enter_btn.setObjectName("enter_btn")
        self.enter_btn.clicked.connect(self.login_form)

    def create_tab(self, id_profile):
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(12)

        # self.thread_arr.append(MessageThread('driver'))

        ##################tabs####################
        self.tabs_arr.append(QtWidgets.QWidget())
        self.tabs_arr[-1].setObjectName("tab")
        self.tabs.addTab(self.tabs_arr[-1], str(id_profile))
        self.setCentralWidget(self.tabs)

        ###############Label id##########################
        self.labels_id_arr.append(QtWidgets.QLabel(
            str(id_profile), self.tabs_arr[-1]))
        self.labels_id_arr[-1].setGeometry(QtCore.QRect(20, 10, 101, 51))
        self.labels_id_arr[-1].setFont(font)
        self.labels_id_arr[-1].setObjectName("id_profile")

        ############Online btn##########################
        self.online_buttons_arr.append(
            QtWidgets.QPushButton("Онлайн", self.tabs_arr[-1]))
        self.online_buttons_arr[-1].setGeometry(QtCore.QRect(20, 70, 93, 28))
        self.online_buttons_arr[-1].setStyleSheet("#online{\n"
                                                  "background-color: green;\n"
                                                  "}")
        self.online_buttons_arr[-1].setObjectName("online")

        ##################Message entry field###############
        self.entry_message_arr.append(QtWidgets.QLineEdit(self.tabs_arr[-1]))
        self.entry_message_arr[-1].setGeometry(QtCore.QRect(20, 160, 471, 22))
        self.entry_message_arr[-1].setStyleSheet("#message{\n"
                                                 "background-color: #FFFFFF;\n"
                                                 "}")
        self.entry_message_arr[-1].setObjectName("message")
        self.entry_message_arr[-1].setPlaceholderText("рассылка")

        ###################Start mesage btn################
        self.begin_message_buttons_arr.append(
            QtWidgets.QPushButton("Пуск", self.tabs_arr[-1]))
        self.begin_message_buttons_arr[-1].setGeometry(
            QtCore.QRect(150, 190, 61, 31))
        self.begin_message_buttons_arr[-1].setStyleSheet("#start_message{\n"
                                                         "background-color: green;\n"
                                                         "}")
        self.begin_message_buttons_arr[-1].setObjectName("start_message")

        ###################Stop mesage btn################
        self.stop_message_buttons_arr.append(
            QtWidgets.QPushButton("Стоп", self.tabs_arr[-1]))
        self.stop_message_buttons_arr[-1].setGeometry(
            QtCore.QRect(220, 190, 71, 31))
        self.stop_message_buttons_arr[-1].setStyleSheet("#stop_message{\n"
                                                        "background-color: red;\n"
                                                        "}")
        self.stop_message_buttons_arr[-1].setObjectName("stop_message")

        ###############Send to moderation btn#############
        self.moder_ice_btn_arr.append(
            QtWidgets.QPushButton("На модерацию", self.tabs_arr[-1]))
        self.moder_ice_btn_arr[-1].setGeometry(QtCore.QRect(710, 190, 131, 51))
        self.moder_ice_btn_arr[-1].setStyleSheet("#moderation{\n"
                                                 "background-color:yellow;\n"
                                                 "}")
        self.moder_ice_btn_arr[-1].setObjectName("moderation")

        ###############Reset curr ice from send btn#############
        self.reset_curr_ice_btn_arr.append(
            QtWidgets.QPushButton("Отменить текущий", self.tabs_arr[-1]))
        self.reset_curr_ice_btn_arr[-1].setGeometry(
            QtCore.QRect(850, 190, 161, 51))
        self.reset_curr_ice_btn_arr[-1].setStyleSheet("#stop_ice{\n"
                                                      "background-color:red;\n"
                                                      "}")
        self.reset_curr_ice_btn_arr[-1].setObjectName("stop_ice")

        ###############Send new ice btn#############
        self.new_ice_btn_arr.append(
            QtWidgets.QPushButton("Отправить новый", self.tabs_arr[-1]))
        self.new_ice_btn_arr[-1].setGeometry(QtCore.QRect(550, 190, 141, 51))
        self.new_ice_btn_arr[-1].setStyleSheet("#send_ice{\n"
                                               "background-color:green;\n"
                                               "}")
        self.new_ice_btn_arr[-1].setObjectName("send_ice")

        ###############IceBreaker entry field#############
        self.entry_ice_arr.append(QtWidgets.QLineEdit(self.tabs_arr[-1]))
        self.entry_ice_arr[-1].setGeometry(QtCore.QRect(550, 160, 461, 22))
        self.entry_ice_arr[-1].setStyleSheet("#icebreaker{\n"
                                             "background-color: #FFFFFF;\n"
                                             "}")
        self.entry_ice_arr[-1].setObjectName("icebreaker")
        self.entry_ice_arr[-1].setPlaceholderText("icebreaker")

        ####################Message label##################
        self.labels_message_arr.append(
            QtWidgets.QLabel("Рассылка", self.tabs_arr[-1]))
        self.labels_message_arr[-1].setGeometry(
            QtCore.QRect(180, 100, 111, 51))
        self.labels_message_arr[-1].setFont(font)
        self.labels_message_arr[-1].setObjectName("message_label")

        ####################IceBreaker label##################
        self.labels_ice_arr.append(
            QtWidgets.QLabel("IceBreker", self.tabs_arr[-1]))
        self.labels_ice_arr[-1].setGeometry(QtCore.QRect(720, 100, 101, 41))
        self.labels_ice_arr[-1].setFont(font)
        self.labels_ice_arr[-1].setObjectName("iceBreaker_lbl")

    def login_form(self):
        self.tabs = QTabWidget()
        self.tabs.setGeometry(QRect(0, 0, 1061, 421))
        self.tabs.setStyleSheet("QWidget{\n"
                                "    background-color: rgb(192, 211, 210);\n"
                                "}")
        self.tabs.move(0, 20)
        self.setCentralWidget(self.tabs)
        self.tabs_arr.clear()
        ''' logic from bot_logic '''
        for i in range(2):
            self.create_tab(i)
        self.mainLayout.addWidget(self.tabs)
        self.show()
        self.mainLayout.addWidget(self.tabs)

    def template_window(self):
        print('templates')


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()


class Window(QMainWindow):
    tabs_arr = []
    online_buttons_arr = []
    online_labels_arr = []
    begin_message_buttons_arr = []
    stop_message_buttons_arr = []
    entry_message_arr = []

    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 500, 750)
        self.setWindowTitle("ПраймБот")
        self.ui()

    def ui(self):
        self.mainLayout = QVBoxLayout()
        self.menu()
        self.main_tab()
        self.mainLayout.addWidget(self.tabs)
        self.setLayout(self.mainLayout)
        self.show()

    def menu(self):
        menubar = self.menuBar()
        template = menubar.addMenu("Шаблоны")
        enter = menubar.addMenu("Вход")
        login = QAction("&Log in", self)
        login.setShortcut("Ctrl+L")
        login.triggered.connect(self.login_form)
        add_template = QAction("&Template", self)
        add_template.setShortcut("Ctrl+T")
        add_template.triggered.connect(self.template_window)
        enter.addAction(login)
        template.addAction(add_template)

    def main_tab(self):
        self.tabs = QTabWidget()
        self.tabs.resize(500, 730)
        self.tabs.move(0, 20)
        self.setCentralWidget(self.tabs)

    def create_tab(self, id_profile):
        self.tabs_arr.append(QWidget())
        self.online_buttons_arr.append(
            QPushButton("Оффлайн", self.tabs_arr[-1]))
        self.online_buttons_arr[-1].move(100, 100)
        self.tabs.addTab(self.tabs_arr[-1], str(id_profile))
        print(self.tabs.currentIndex())

    def login_form(self):
        self.tabs_arr.clear()
        ''' logic from bot_logic '''
        for i in range(2):
            self.create_tab(i)
        self.mainLayout.addWidget(self.tabs)
        self.show()

    def template_window(self):
        print('templates')


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
