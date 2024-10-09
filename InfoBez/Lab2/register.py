import sqlite3

try:
    # Подключение к бд
    sqlite_connection = sqlite3.connect("C:\\My workspace\\Programming\\InfoBez\\Lab2\\users.db")
    cursor = sqlite_connection.cursor()
    print("Подключен к SQLite")

    # Функция добавления пользователя в таблицу
    def insertIntoTable(login, password):
        sqlite_insert_query = """INSERT INTO users
                              (login, password)
                              VALUES
                              (?, ?);"""
        count = cursor.execute(sqlite_insert_query, (login, password))
        sqlite_connection.commit()
        print("Пользователь успешно зарегестрирован")
        cursor.close()

# Вывод ошибок
except sqlite3.Error as error:
    print("Ошибка при работе с SQLite", error)
