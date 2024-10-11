# Фулл рабочий код, сделанный через ChatGPT
# !!! Нет зеркальности у третьего ротора !!!

class Enigma:
    user_message_array = []
    key = []

    # Переделываем данные пользователя в 2 массива с сообщением и ключем
    @staticmethod
    def make_arrays(user_message, key):
        Enigma.user_message_array = list(user_message)
        Enigma.key = list(key)

    class Rotor:
        alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
        turnDelay = len(alphabet)

        def __init__(self, key):
            self.startFrom = self.alphabet[-int(key):] + self.alphabet[:-int(key)]
            self.turn_counter = 0  # Счётчик оборотов для ротора
        
        def turn(self):
            # Вращение ротора на один символ
            self.startFrom = self.startFrom[-1:] + self.startFrom[:-1]
            self.turn_counter = (self.turn_counter + 1) % len(self.alphabet)
        
        def encode_char(self, char):
            # Заменяем символ по текущему положению ротора
            index = Enigma.Rotor.alphabet.index(char)
            return self.startFrom[index]

        def decode_char(self, char):
            # Восстанавливаем исходный символ
            index = self.startFrom.index(char)
            return Enigma.Rotor.alphabet[index]

    @staticmethod
    def rotate_rotors(rotor_1, rotor_2, rotor_3):
        rotor_3.turn()
        if rotor_3.turn_counter == 0:  # Полный оборот третьего ротора
            rotor_2.turn()
            if rotor_2.turn_counter == 0:  # Полный оборот второго ротора
                rotor_1.turn()

    @staticmethod
    def chifr_message(rotor_1, rotor_2, rotor_3):
        encrypted_message = []
        for char in Enigma.user_message_array:
            if char in Enigma.Rotor.alphabet:
                char = rotor_1.encode_char(char)
                char = rotor_2.encode_char(char)
                char = rotor_3.encode_char(char)
                Enigma.rotate_rotors(rotor_1, rotor_2, rotor_3)  # Вращаем роторы
            encrypted_message.append(char)
        return ''.join(encrypted_message)

    @staticmethod
    def unchifr_message(rotor_1, rotor_2, rotor_3):
        decrypted_message = []
        for char in Enigma.user_message_array:
            if char in Enigma.Rotor.alphabet:
                char = rotor_3.decode_char(char)
                char = rotor_2.decode_char(char)
                char = rotor_1.decode_char(char)
                Enigma.rotate_rotors(rotor_1, rotor_2, rotor_3)  # Вращаем роторы
            decrypted_message.append(char)
        return ''.join(decrypted_message)

class Menu:
    @staticmethod
    def start():
        # Очищаем консоль
        print("\033[H\033[J", end="")

        # Предоставляем выбор пользователю
        user_choice = input("Зашифровать сообщение - '1', расшифровать сообщение - '2': ")

        if user_choice == "1":
            user_message = input("Введите сообщение для шифрования: ").upper()
            key = input("Введите ключ из 3 символов: ")
            Enigma.make_arrays(user_message, key)
            
            # Инициализация роторов
            rotor_1 = Enigma.Rotor(Enigma.key[0])
            rotor_2 = Enigma.Rotor(Enigma.key[1])
            rotor_3 = Enigma.Rotor(Enigma.key[2])
            
            # Шифруем сообщение
            encrypted_message = Enigma.chifr_message(rotor_1, rotor_2, rotor_3)
            print(f"Зашифрованное сообщение: {encrypted_message}")

        elif user_choice == "2":
            user_message = input("Введите зашифрованное сообщение: ").upper()
            key = input("Введите ключ из 3 символов: ")
            Enigma.make_arrays(user_message, key)
            
            # Инициализация роторов
            rotor_1 = Enigma.Rotor(Enigma.key[0])
            rotor_2 = Enigma.Rotor(Enigma.key[1])
            rotor_3 = Enigma.Rotor(Enigma.key[2])

            # Расшифровываем сообщение
            decrypted_message = Enigma.unchifr_message(rotor_1, rotor_2, rotor_3)
            print(f"Расшифрованное сообщение: {decrypted_message}")

        else:
            Menu.start()

Menu.start()
