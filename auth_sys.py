# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'auth_sys.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Reg_Auth(object):
    def setupUi(self, MainMenu):
        MainMenu.setObjectName("MainMenu")
        MainMenu.resize(381, 445)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("micro_img1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainMenu.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 20, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 70, 381, 351))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.login_reg = QtWidgets.QLineEdit(self.tab)
        self.login_reg.setGeometry(QtCore.QRect(130, 30, 113, 20))
        self.login_reg.setObjectName("login_reg")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pas_reg = QtWidgets.QLineEdit(self.tab)
        self.pas_reg.setGeometry(QtCore.QRect(130, 70, 113, 20))
        self.pas_reg.setObjectName("pas_reg")
        self.name_reg = QtWidgets.QLineEdit(self.tab)
        self.name_reg.setGeometry(QtCore.QRect(130, 110, 113, 20))
        self.name_reg.setObjectName("name_reg")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(40, 210, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.errors_reg = QtWidgets.QLabel(self.tab)
        self.errors_reg.setGeometry(QtCore.QRect(20, 260, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.errors_reg.setFont(font)
        self.errors_reg.setText("")
        self.errors_reg.setObjectName("errors_reg")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(230, 210, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(10, 30, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.login_auth = QtWidgets.QLineEdit(self.tab_2)
        self.login_auth.setGeometry(QtCore.QRect(130, 30, 113, 20))
        self.login_auth.setObjectName("login_auth")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(10, 70, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pas_auth = QtWidgets.QLineEdit(self.tab_2)
        self.pas_auth.setGeometry(QtCore.QRect(130, 70, 113, 20))
        self.pas_auth.setObjectName("pas_auth")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 210, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.errors_auth = QtWidgets.QLabel(self.tab_2)
        self.errors_auth.setGeometry(QtCore.QRect(20, 270, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.errors_auth.setFont(font)
        self.errors_auth.setText("")
        self.errors_auth.setObjectName("errors_auth")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 210, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.tabWidget.addTab(self.tab_2, "")
        MainMenu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainMenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 381, 21))
        self.menubar.setObjectName("menubar")
        MainMenu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainMenu)
        self.statusbar.setObjectName("statusbar")
        MainMenu.setStatusBar(self.statusbar)

        self.retranslateUi(MainMenu)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainMenu)

    def retranslateUi(self, MainMenu):
        _translate = QtCore.QCoreApplication.translate
        MainMenu.setWindowTitle(_translate("MainMenu", "Voice KTS"))
        self.label.setText(_translate("MainMenu", "Голосовой помощник"))
        self.label_2.setText(_translate("MainMenu", "Логин"))
        self.label_3.setText(_translate("MainMenu", "Пароль"))
        self.label_4.setText(_translate("MainMenu", "Ваше имя"))
        self.pushButton.setText(_translate("MainMenu", "Регистрация"))
        self.pushButton_4.setText(_translate("MainMenu", "Далее"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainMenu", "Регистрация"))
        self.label_5.setText(_translate("MainMenu", "Логин"))
        self.label_6.setText(_translate("MainMenu", "Пароль"))
        self.pushButton_2.setText(_translate("MainMenu", "Авторизация"))
        self.pushButton_3.setText(_translate("MainMenu", "Далее"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainMenu", "Авторизация"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainMenu = QtWidgets.QMainWindow()
    ui = Ui_Reg_Auth()
    ui.setupUi(MainMenu)
    MainMenu.show()
    sys.exit(app.exec_())
