# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'team_genius.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OtherWindow(object):
    def setupUi(self, OtherWindow):
        OtherWindow.setObjectName("OtherWindow")
        OtherWindow.resize(381, 520)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("micro_img.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        OtherWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(OtherWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 10, 201, 221))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logo.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 230, 271, 31))

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 290, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 320, 361, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 350, 371, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 380, 90, 90))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("C:/Users/User/Downloads/imgonline-com-ua-Resize-9cuRbWcuRWslohE.jpg"))
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(140, 380, 90, 90))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("C:/Users/User/Downloads/imgonline-com-ua-Resize-yKYf7hgIlAHf.jpg"))
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(260, 380, 90, 90))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("C:/Users/User/Downloads/imgonline-com-ua-Resize-XjM9U3pgiaL.jpg"))
        self.label_8.setObjectName("label_8")
        OtherWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(OtherWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 381, 21))
        self.menubar.setObjectName("menubar")
        OtherWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OtherWindow)
        self.statusbar.setObjectName("statusbar")
        OtherWindow.setStatusBar(self.statusbar)

        self.retranslateUi(OtherWindow)
        QtCore.QMetaObject.connectSlotsByName(OtherWindow)

    def retranslateUi(self, OtherWindow):
        _translate = QtCore.QCoreApplication.translate
        OtherWindow.setWindowTitle(_translate("OtherWindow", "Друг v1.0"))
        self.label_2.setText(_translate("OtherWindow", "Команда \"GENIUS\""))
        self.label_3.setText(_translate("OtherWindow", "Сергей Милосердов - разработчик"))
        self.label_5.setText(_translate("OtherWindow", "Константин Недилько - дизайн"))
        self.label_4.setText(_translate("OtherWindow", "Андрей Попель - разработчик граф. интерфейса"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OtherWindow = QtWidgets.QMainWindow()
    ui = Ui_OtherWindow()
    ui.setupUi(OtherWindow)
    OtherWindow.show()
    sys.exit(app.exec_())
