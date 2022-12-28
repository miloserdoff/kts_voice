from test_1 import Ui_MainWindow
from auth_sys import Ui_Reg_Auth
import test_1
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
import sys
import pymysql

host = 'localhost'
user = 'root'
password = ''
db = 'python_app'
connection = pymysql.connect(host=host, user=user, password=password, database=db, autocommit=True)

print('База данных подключена.')
# password_list = []
bot_name_list = []
user_name_list = []


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(381, 520)
        self.ui.pushButton.clicked.connect(self.btnClicked)
        self.ui.pushButton_2.clicked.connect(self.team_g)
        self.ui.pushButton_3.clicked.connect(self.command_list)


class RegSystem(QMainWindow):
    def __init__(self):
        super(RegSystem, self).__init__()
        self.ui = Ui_Reg_Auth()
        self.ui.setupUi(self)
        self.setFixedSize(381, 520)
        self.ui.pushButton.clicked.connect(self.reg_button)
        self.ui.pushButton_2.clicked.connect(self.auth_button)

    def reg_button(self):
        with connection.cursor() as cur:
            logins = []
            user_login = self.ui.login_reg.text()
            user_password = self.ui.pas_reg.text()
            user_name = self.ui.name_reg.text()
            login = cur.execute("SELECT login FROM info")
            login_find = cur.fetchall()
            for row in login_find:
                logins.append("{0}".format(row[0]))

            if user_login in logins:
                self.ui.errors_reg.setText(f'Логин `{user_login}` занят. \nИспользуйте другой')
                logins.clear()

            else:
                cur.execute("INSERT INTO `info` (`login`, `pass`, `user_name`) VALUES (%s, %s, %s)",
                            (user_login, user_password, user_name))
                self.ui.errors_reg.setText(f'Аккаунт `{user_login}` зарегистрирован.')

    def auth_button(self):
        with connection.cursor() as cur:
            logins = []
            password_list = []
            user_login = self.ui.login_auth.text()
            user_password = self.ui.pas_auth.text()
            login = cur.execute("SELECT login FROM info")
            login_find = cur.fetchall()
            for row in login_find:
                logins.append("{0}".format(row[0]))

            if user_login not in logins:
                self.ui.errors_auth.setText(f'Логин `{user_login}` не зарегистрирован.')

            else:
                sql_pass = "SELECT `pass` FROM `info` WHERE `login` = %s"
                passwords = cur.execute(sql_pass, user_login)
                password_find = cur.fetchall()
                for row in password_find:
                    password_list.append("{0}".format(row[0]))

                if user_password not in password_list:
                    self.ui.errors_auth.setText('Пароль неверный.')

                else:
                    self.ui.errors_auth.setText(f'Добро пожаловать, {user_login}!')
                    app1 = QtWidgets.QApplication([])
                    application1 = MainWindow()
                    application1.show()
                    sys.exit(app1.exec())


app = QtWidgets.QApplication([])
application = RegSystem()
application.show()
sys.exit(app.exec())
