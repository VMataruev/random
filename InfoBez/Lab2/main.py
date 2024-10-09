from register import insertIntoTable
from login import isUser
from time import sleep

class Menu:
    # Очищаем консоль
    print("\033[H\033[J", end="")
    # Вход пользователя
    def login():
        # Количество попыток входа
        logTry = 3
        logDelay = 10

        # Даёт попытку ввода, пока есть количество попыток входа
        while logTry > 0:
            print("\nВход в аккаунт")
            login = input("Введите логин: ")
            password = input("Введите пароль: ")

            # Смог ли войти пользователь?
            if isUser(login, password):
                print(f"Добро пожаловать, {login}!")
                break
            else:
                print(f"Вход запрещён, осталось попыток: {logTry}, следующая попытка будет доступна через {logDelay} секунд")
                logTry -= 1
                sleep(logDelay)



    # Регистрация пользователя
    def register():
        print("\nРегистрация")
        login = input("Введите логин: ")
        password = input("Введите пароль: ")

        # Переменные
        passwordCheck = []
        passwordCheckLetters = 0
        passwordCheckNumbers = 0
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        # Пароль расскладываем на отдельные символы
        for i in range(len(password)):
            passwordCheck.append(password[i])
        
        # Записываем количество цифр и букв в пароле
        for i in range(len(passwordCheck)):
            if passwordCheck[i] in numbers:
                passwordCheckNumbers += 1
            else:
                passwordCheckLetters += 1 

        # Если цифр и букв меньше нужного, то отправляем пользователя придумывать новый пароль
        if passwordCheckLetters < 3:
            print("Пароль должен содержать как минимум 3 буквы")
            Menu.register()
        if passwordCheckNumbers < 2:
            print("Пароль должен содержать как минимум 2 цифры")
            Menu.register()

        # Если все проверки пройдены, то добавляем пользователя в таблицу
        insertIntoTable(login, password)


 

    # Запустить меню выбора для пользователя
    def start():
        userChoice = input("Напишите '1', если хотите войти или напишите '2', если хотите зарегестрироваться: ")
        if userChoice == "1":
            Menu.login()
        elif userChoice == "2":
            Menu.register()
        else:
            print("Неверный ввод")


Menu.start()
