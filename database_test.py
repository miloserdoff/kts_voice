import pymysql
import speech_recognition as sr


host = 'localhost'
user = 'root'
password = ''
db = 'python_app'
connection = pymysql.connect(host=host, user=user, password=password, database=db, autocommit=True)
# logins = []
# password_list = []
# user_login = input('Введите логин: ')
#
# with connection.cursor() as cur:
#     login = cur.execute("SELECT login FROM info")
#     login_find = cur.fetchall()
#     for row in login_find:
#         logins.append("{0}".format(row[0]))
#
#     if user_login in logins:
#         print(f'Логин `{user_login}` найден!')
#         user_password = input(f'Введите пароль от аккаунта {user_login}: ')
#         sql_pass = "SELECT `pass` FROM `info` WHERE `login` = %s"
#         passwords = cur.execute(sql_pass, (user_login))
#         password_find = cur.fetchall()
#         for row in password_find:
#             password_list.append("{0}".format(row[0]))
#
#         if user_password in password_list:
#             print(f'Вам разрешен доступ к аккаунту `{user_login}`!')
#         else:
#             print(f'Вам запрещен доступ к аккаунту `{user_login}`!')
#     else:
#         print(f'Логин `{user_login}` не найден!')
#
# with connection.cursor() as cur:
#     # sql = "INSERT INTO `info` (`login`, `pass`) VALUES (`%s`, `%s`)"
#     log = 'victor'
#     pas = 'ff'
#     cur.execute("INSERT INTO `info` (`login`, `pass`) VALUES (%s, %s)", (log, pas))
#     print('Success')
