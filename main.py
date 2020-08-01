import sys

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtWidgets import *

from bot_logic import DriverLogic
from styles import *

MESSAGES = {}
PROFILES = {}


class MessageThread(QtCore.QThread):
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


class Ui_MainWindow(object):
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

    def create_tab(self, id_profile, MainWindow):
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(12)

        self.thread_arr.append(MessageThread('driver'))

        ##################tabs####################
        self.tabs_arr.append(QtWidgets.QWidget())
        self.tabs_arr[-1].setObjectName("tab")
        self.tabs.addTab(self.tabs_arr[-1])
        MainWindow.setCentralWidget(self.centralwidget)

        ###############Label id##########################
        self.labels_id_arr.append(QtWidgets.QLabel(id_profile, self.tab))
        self.labels_id_arr[-1].setGeometry(QtCore.QRect(20, 10, 101, 51))
        self.labels_id_arr[-1].setFont(font)
        self.labels_id_arr[-1].setObjectName("id_profile")

        ############Online btn##########################
        self.online_buttons_arr.append(
            QtWidgets.QPushButton("Онлайн", self.tab))
        self.online_buttons_arr[-1].setGeometry(QtCore.QRect(20, 70, 93, 28))
        self.online_buttons_arr[-1].setStyleSheet("#online{\n"
                                                  "background-color: green;\n"
                                                  "}")
        self.online_buttons_arr[-1].setObjectName("online")

        ##################Message entry field###############
        self.entry_message_arr.append(QtWidgets.QLineEdit(self.tab))
        self.entry_message_arr[-1].setGeometry(QtCore.QRect(20, 160, 471, 22))
        self.entry_message_arr[-1].setStyleSheet("#message{\n"
                                                 "background-color: #FFFFFF;\n"
                                                 "}")
        self.entry_message_arr[-1].setObjectName("message")
        self.entry_message_arr[-1].setPlaceholderText("рассылка")

        ###################Start mesage btn################
        self.begin_message_buttons_arr.append(
            QtWidgets.QPushButton("Пуск", self.tab))
        self.begin_message_buttons_arr[-1].setGeometry(
            QtCore.QRect(150, 190, 61, 31))
        self.begin_message_buttons_arr[-1].setStyleSheet("#start_message{\n"
                                                         "background-color: green;\n"
                                                         "}")
        self.begin_message_buttons_arr[-1].setObjectName("start_message")

        ###################Stop mesage btn################
        self.stop_message_buttons_arr.append(
            QtWidgets.QPushButton("Стоп", self.tab))
        self.stop_message_buttons_arr[-1].setGeometry(
            QtCore.QRect(220, 190, 71, 31))
        self.stop_message_buttons_arr[-1].setStyleSheet("#stop_message{\n"
                                                        "background-color: red;\n"
                                                        "}")
        self.stop_message_buttons_arr[-1].setObjectName("stop_message")

        ###############Send to moderation btn#############
        self.moder_ice_btn_arr.append(
            QtWidgets.QPushButton("На модерацию", self.tab))
        self.moder_ice_btn_arr[-1].setGeometry(QtCore.QRect(710, 190, 131, 51))
        self.moder_ice_btn_arr[-1].setStyleSheet("#moderation{\n"
                                                 "background-color:yellow;\n"
                                                 "}")
        self.moder_ice_btn_arr[-1].setObjectName("moderation")

        ###############Reset curr ice from send btn#############
        self.reset_curr_ice_btn_arr.append(
            QtWidgets.QPushButton("Отменить текущий", self.tab))
        self.reset_curr_ice_btn_arr[-1].setGeometry(
            QtCore.QRect(850, 190, 161, 51))
        self.reset_curr_ice_btn_arr[-1].setStyleSheet("#stop_ice{\n"
                                                      "background-color:red;\n"
                                                      "}")
        self.reset_curr_ice_btn_arr[-1].setObjectName("stop_ice")

        ###############Send new ice btn#############
        self.new_ice_btn_arr.append(
            QtWidgets.QPushButton("Отправить новый", self.tab))
        self.new_ice_btn_arr[-1].setGeometry(QtCore.QRect(550, 190, 141, 51))
        self.new_ice_btn_arr[-1].setStyleSheet("#send_ice{\n"
                                               "background-color:green;\n"
                                               "}")
        self.new_ice_btn_arr[-1].setObjectName("send_ice")

        ###############IceBreaker entry field#############
        self.entry_ice_arr.append(QtWidgets.QLineEdit(self.tab))
        self.entry_ice_arr[-1].setGeometry(QtCore.QRect(550, 160, 461, 22))
        self.entry_ice_arr[-1].setStyleSheet("#icebreaker{\n"
                                             "background-color: #FFFFFF;\n"
                                             "}")
        self.entry_ice_arr[-1].setObjectName("icebreaker")
        self.entry_ice_arr[-1].setPlaceholderText("icebreaker")

        ####################Message label##################
        self.labels_message_arr.append(QtWidgets.QLabel("Рассылка", self.tab))
        self.labels_message_arr[-1].setGeometry(
            QtCore.QRect(180, 100, 111, 51))
        self.labels_message_arr[-1].setFont(font)
        self.labels_message_arr[-1].setObjectName("message_label")

        ####################IceBreaker label##################
        self.labels_ice_arr.append(QtWidgets.QLabel("IceBreker", self.tab))
        self.labels_ice_arr[-1].setGeometry(QtCore.QRect(720, 100, 101, 41))
        self.labels_ice_arr[-1].setFont(font)
        self.labels_ice_arr[-1].setObjectName("iceBreaker_lbl")

    def ui(self, MainWindow):
        self.setupUi(MainWindow)
        self.menu(MainWindow)

    def login_form(self, MainWindow):
        self.tabs_arr.clear()
        ''' logic from bot_logic '''
        for i in range(2):
            self.create_tab(i, MainWindow)
        self.mainLayout.addWidget(self.tabs)
        # self.show()

    def menu(self, MainWindow):
        menubar = QtWidgets.QMenuBar(MainWindow)
        menubar.setGeometry(QtCore.QRect(0, 0, 1068, 26))
        template = menubar.addMenu("Шаблоны")
        enter = menubar.addMenu("Вход")
        login = QAction("&Log in", MainWindow)
        login.setShortcut("Ctrl+L")
        login.triggered.connect(lambda x: self.login_form(MainWindow))
        add_template = QAction("&Template", MainWindow)
        add_template.setShortcut("Ctrl+T")
        # add_template.triggered.connect(self.template_window)
        enter.addAction(login)
        template.addAction(add_template)
        MainWindow.setMenuBar(menubar)
        self.login_form(MainWindow)

    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setStyleSheet(u"#MainWindow, #centralWidget{\n"
                                 "	background-color: rgb(192, 211, 210);\n"
                                 "}\n"
                                 "")
        MainWindow.resize(1068, 476)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.tabs.setGeometry(QtCore.QRect(0, 0, 1061, 421))

        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(12)

        self.tabs.setFont(font)
        self.tabs.setStyleSheet("QWidget{\n"
                                "background-color: rgb(192, 211, 210);\n"
                                "}")
        self.tabs.setObjectName("tabs")

        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.ui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
