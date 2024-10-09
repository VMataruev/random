class Enigma:
    # Модель энигмы с переменными
    alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
    user_message_array = []
    key = []
    
    class Rotor:
        alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
        beforeTurn = len(alphabet)

        def turn(self):
            self.alphabet = self.alphabet[-2:] + self.alphabet[:-2]


    # Переделываем данные пользователя в 2 массива с сообщением и ключем
    def make_arrays(user_message, key):
        for i in range(len(user_message)):
            Enigma.user_message_array.append(user_message[i])
        for i in range(len(key)):
            Enigma.key.append(key[i])     


    # def chifr_message():

    # def unchifr_message():


class Menu:
    def start():
        # Очищаем консоль
        print("\033[H\033[J", end="")

        # Предоставляем выбор пользователю
        user_choice = input("Зашифровать сообщение - '1', расшифровать сообщение - '2': ")

        if user_choice == "1":
            user_message = input("Введите сообщение для шифрования: ")
            key = input("Введите ключ: ")
            Enigma.make_arrays(user_message, key)

        elif user_choice == "2":
            user_message = input("Введите зашифрованное сообщение: ")
            key = input("Введите ключ: ")

        else:
            Menu.start()

Menu.start()