from test_1 import Ui_MainWindow
from auth_sys import Ui_Reg_Auth
import test_1
from PyQt5 import QtWidgets
import speech_recognition as sr
import pyttsx3
import sys
import pymysql
from pyowm import OWM
import webbrowser
import datetime
import requests
from bs4 import BeautifulSoup


# from command_list import Ui_Other_Win2


def speak(text):
    print(text)
    speak_engine.say(text)
    speak_engine.runAndWait()
    speak_engine.stop()


host = 'localhost'
user = 'root'
password = ''
db = 'python_app'
connection = pymysql.connect(host=host, user=user, password=password, database=db, autocommit=True)

print('База данных подключена.')
# password_list = []
bot_name_list = []
user_name_list = []


class Currency:
    dollar_rub = 'https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw%3A1584716087546&source=hp&ei=N9l0XtDXHs716QTcuaXoAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131l4.3044.4178..5294...1.0..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4'
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 Safari/537.36'
    }
    current_conv_price = 0

    def __init__(self):
        self.current_conv_price = float(self.get_currency_price().replace(',', '.'))

    def get_currency_price(self):
        full_page = requests.get(self.dollar_rub, headers=self.HEADERS)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.find_all("span", {'class': 'DFlfde SwHCTb', 'data-precision': 2})
        return convert[0].text

    def check_cur(self):
        currency = float(self.get_currency_price().replace(",", "."))
        today = datetime.datetime.now()
        return f'На момент {today.day}.{today.month}.{today.year} {today.hour}:{today.minute} \n1 доллар = ' + str(
            currency) + ' рублей'


class RegSystem(QtWidgets.QMainWindow):
    def __init__(self):
        super(RegSystem, self).__init__()
        self.ui = Ui_Reg_Auth()
        self.ui.setupUi(self)
        self.setFixedSize(381, 520)
        self.ui.pushButton_3.hide()
        self.ui.pushButton_4.hide()
        self.ui.pushButton.clicked.connect(self.reg_button)
        self.ui.pushButton_2.clicked.connect(self.auth_button)
        self.ui.pushButton_3.clicked.connect(self.OpenWindowIntro)
        self.ui.pushButton_4.clicked.connect(self.OpenWindowIntro)

    def OpenWindowIntro(self):
        self.another_window = Voice()
        self.another_window.show()
        self.close()

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
                self.ui.pushButton.hide()
                self.ui.pushButton_4.show()

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
                    sql_name = "SELECT `user_name` FROM `info` WHERE `login` = %s"
                    user_name_sql = cur.execute(sql_name, user_login)
                    user_name_sql_find = cur.fetchall()
                    for rows in user_name_sql_find:
                        user_name_list.append("{0}".format(rows[0]))
                    self.ui.pushButton_3.show()
                    self.ui.pushButton_2.hide()


class Voice(QtWidgets.QMainWindow):

    def __init__(self):
        # test_1.Ui_MainWindow.auth_system(self)
        super(Voice, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(381, 520)
        self.ui.pushButton.clicked.connect(self.btnClicked)
        self.ui.pushButton_2.clicked.connect(self.team_g)
        self.ui.pushButton_3.clicked.connect(self.command_list)

    def command_list(self):
        test_1.Ui_MainWindow.openWindow_command(self)

    def team_g(self):
        test_1.Ui_MainWindow.openWindow(self)

    def btnClicked(self):
        try:
            speak('Слушаю Вас!')
            r = sr.Recognizer()
            m = sr.Microphone(device_index=1)
            with m as sourse:
                r.adjust_for_ambient_noise(sourse)
                audio_command = r.listen(sourse)
                voice = r.recognize_google(audio_command, language='ru-RU').lower()
                self.ui.label_2.setText('[Вы]: ' + voice)
                print(f'[LOG]: {voice}')

                if 'привет' in voice:
                    speak('Приветствую!')
                    self.ui.label_3.setText('[' + name + '] Приветствую!')


                elif 'тебя зовут' in voice:
                    speak('Меня зовут ' + name)
                    self.ui.label_3.setText('[' + name + '] Меня зовут ' + name)

                elif 'меня зовут' in voice:
                    speak('Вас зовут ' + user_name_list[0])
                    self.ui.label_3.setText('[' + name + '] Вас зовут ' + user_name_list[0])

                elif 'погода' in voice:
                    self.ui.label_3.setText('[' + name + '] Назовите город!')
                    speak('Назовите город.')
                    audio1 = r.listen(sourse)
                    city = r.recognize_google(audio1, language='ru-RU').lower()
                    self.ui.label_2.setText('[Вы]: ' + city)
                    observation = mgr.weather_at_place(city)
                    w = observation.weather
                    temperatre = w.temperature('celsius')['temp']
                    tmp = 'Температура в городе ' + city + ' : \n' + str(temperatre) + ' °C'
                    speak(tmp)
                    self.ui.label_3.setText('[' + name + ']: ' + tmp)
                elif 'браузер' in voice:
                    speak('Открываю браузер')
                    self.ui.label_3.setText('[' + name + '] Открываю браузер!')
                    webbrowser.open('https://yandex.ru/')
                elif 'новости' in voice:
                    speak('Одну секунду, перевожу вас на новостной портал!')
                    self.ui.label_3.setText('[' + name + '] Одну секунду, \nперевожу вас на новостной портал!')
                    webbrowser.open('https://yandex.ru/news')
                elif 'время' in voice:
                    today = datetime.datetime.now()
                    now = 'Сейчас ' + str(today.hour) + ':' + str(today.minute)
                    speak(now)
                    self.ui.label_3.setText('[' + name + '] Сейчас ' + str(today.hour) + ':' + str(today.minute))
                elif 'доллар' in voice:
                    currency = Currency()
                    speak(currency.check_cur())
                    self.ui.label_3.setText('[' + name + ']: ' + str(currency.check_cur()))
                else:
                    speak('Я не знаю такой команды')
                    self.ui.label_3.setText('[' + name + '] Я не знаю такой команды')




        except sr.UnknownValueError:
            print('Проверьте свой микрофон')
            # speak('Не могу распознать ваш запрос. Проверьте свой микрофон!')
        except sr.RequestError:
            # speak('Ошибка подключения к Интернету. Проверьте соединение.')
            print('Проверьте соединение с Интернетом')


speak_engine = pyttsx3.init()
print('[GENIUS] Голосовой помощник "Друг"')
speak('Для удобства использования дайте имя Вашему помощнику!')
print('[LOG] Распознавание...')
try:
    r = sr.Recognizer()
    m = sr.Microphone(device_index=1)
    with m as voices:
        audio = r.listen(voices)
        name = r.recognize_google(audio, language='ru-RU').lower()
        print(f'Имя вашего помощника: {name}')
except sr.UnknownValueError:
    print('Проверьте свой микрофон')
except sr.RequestError:
    print('Проверьте соединение с Интернетом')

owm = OWM('c7328c552ccb5360670b6fda8ea08f50')
mgr = owm.weather_manager()
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = RegSystem()
    application.show()
    sys.exit(app.exec_())
