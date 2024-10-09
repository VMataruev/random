import sqlite3

# Подключение к БД
connection = sqlite3.connect("C:\\My workspace\\Programming\\InfoBez\\Lab2\\users.db")
cursor = connection.cursor()

# Проверяем существует ли пользователь в бд
def isUser(login, password):
    cursor.execute('SELECT * FROM users WHERE login = ? AND password = ?', (login, password))
    results = cursor.fetchall()
    
    # connection.close()
    
    return len(results) > 0
