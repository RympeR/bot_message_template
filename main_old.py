# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
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
                                "    background-color: rgb(192, 211, 210);\n"
                                "}")
        self.tabs.setObjectName("tabs")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.id_profile = QtWidgets.QLabel(self.tab)
        self.id_profile.setGeometry(QtCore.QRect(20, 10, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(12)
        self.id_profile.setFont(font)
        self.id_profile.setObjectName("id_profile")
        self.online = QtWidgets.QPushButton(self.tab)
        self.online.setGeometry(QtCore.QRect(20, 70, 93, 28))
        self.online.setStyleSheet("#online{\n"
                                  "    background-color: green;\n"
                                  "}")
        self.online.setObjectName("online")
        self.message = QtWidgets.QLineEdit(self.tab)
        self.message.setGeometry(QtCore.QRect(20, 160, 471, 22))
        self.message.setStyleSheet("#message{\n"
                                   "    background-color: #FFFFFF;\n"
                                   "}")
        self.message.setObjectName("message")
        self.start_message = QtWidgets.QPushButton(self.tab)
        self.start_message.setGeometry(QtCore.QRect(150, 190, 61, 31))
        self.start_message.setStyleSheet("#start_message{\n"
                                         "    background-color: green;\n"
                                         "}")
        self.start_message.setObjectName("start_message")
        self.stop_message = QtWidgets.QPushButton(self.tab)
        self.stop_message.setGeometry(QtCore.QRect(220, 190, 71, 31))
        self.stop_message.setStyleSheet("#stop_message{\n"
                                        "    background-color: red;\n"
                                        "}")
        self.stop_message.setObjectName("stop_message")
        self.moderation = QtWidgets.QPushButton(self.tab)
        self.moderation.setGeometry(QtCore.QRect(710, 190, 131, 51))
        self.moderation.setStyleSheet("#moderation{\n"
                                      "    background-color:yellow;\n"
                                      "}")
        self.moderation.setObjectName("moderation")
        self.stop_ice = QtWidgets.QPushButton(self.tab)
        self.stop_ice.setGeometry(QtCore.QRect(850, 190, 161, 51))
        self.stop_ice.setStyleSheet("#stop_ice{\n"
                                    "    background-color:red;\n"
                                    "}")
        self.stop_ice.setObjectName("stop_ice")
        self.send_ice = QtWidgets.QPushButton(self.tab)
        self.send_ice.setGeometry(QtCore.QRect(550, 190, 141, 51))
        self.send_ice.setStyleSheet("#send_ice{\n"
                                    "    background-color:green;\n"
                                    "}")
        self.send_ice.setObjectName("send_ice")
        self.icebreaker = QtWidgets.QLineEdit(self.tab)
        self.icebreaker.setGeometry(QtCore.QRect(550, 160, 461, 22))
        self.icebreaker.setStyleSheet("#icebreaker{\n"
                                      "    background-color: #FFFFFF;\n"
                                      "}")
        self.icebreaker.setObjectName("icebreaker")
        self.message_label = QtWidgets.QLabel(self.tab)
        self.message_label.setGeometry(QtCore.QRect(180, 100, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(12)
        self.message_label.setFont(font)
        self.message_label.setObjectName("message_label")
        self.iceBreaker = QtWidgets.QLabel(self.tab)
        self.iceBreaker.setGeometry(QtCore.QRect(720, 100, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(12)
        self.iceBreaker.setFont(font)
        self.iceBreaker.setObjectName("iceBreaker")
        self.tabs.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabs.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1068, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLog_in = QtWidgets.QAction(MainWindow)
        self.actionLog_in.setObjectName("actionLog_in")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu.addAction(self.actionLog_in)
        self.menu_2.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.id_profile.setText(_translate("MainWindow", "id profile"))
        self.online.setText(_translate("MainWindow", "Онлайн"))
        self.message.setPlaceholderText(_translate("MainWindow", "рассылка"))
        self.start_message.setText(_translate("MainWindow", "Пуск"))
        self.stop_message.setText(_translate("MainWindow", "Стоп"))
        self.moderation.setText(_translate("MainWindow", "На модерацию"))
        self.stop_ice.setText(_translate("MainWindow", "Отменить текущий"))
        self.send_ice.setText(_translate("MainWindow", "Отправить новый"))
        self.icebreaker.setPlaceholderText(
            _translate("MainWindow", "icebreaker"))
        self.message_label.setText(_translate("MainWindow", "Рассылка"))
        self.iceBreaker.setText(_translate("MainWindow", "IceBreaker"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab),
                             _translate("MainWindow", "Tab 1"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_2),
                             _translate("MainWindow", "Tab 2"))
        self.menu.setTitle(_translate("MainWindow", "Вход"))
        self.menu_2.setTitle(_translate("MainWindow", "Шаблоны"))
        self.actionLog_in.setText(_translate("MainWindow", "Log in"))
        self.action.setText(_translate("MainWindow", "Управление шаблонами"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
