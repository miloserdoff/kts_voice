import pymysql
from test_1 import Ui_MainWindow
from auth_sys import Ui_Reg_Auth
from app import MainWindow
import test_1
import sys
from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5 import QtWidgets

host = 'localhost'
user = 'root'
password = ''
db = 'python_app'
connection = pymysql.connect(host=host, user=user, password=password, database=db, autocommit=True)

print('База данных подключена.')


class VoiceAs(QMainWindow):

    def __init__(self):
        # test_1.Ui_MainWindow.auth_system(self)
        super(VoiceAs, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(381, 520)
        # self.ui.pushButton.clicked.connect(self.btnClicked)
        self.ui.pushButton_2.clicked.connect(self.team_g)
        self.ui.pushButton_3.clicked.connect(self.command_list)

    def command_list(self):
        test_1.Ui_MainWindow.openWindow_command(self)

    def team_g(self):
        test_1.Ui_MainWindow.openWindow(self)



app = QtWidgets.QApplication([])
application = VoiceAs()
application.show()
sys.exit(app.exec())
