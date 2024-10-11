# class Enigma:
#     # Модель энигмы с переменными
#     user_message_array = []
#     key = []

#     # Переделываем данные пользователя в 2 массива с сообщением и ключем
#     def make_arrays(user_message, key):
#         for i in range(len(user_message)):
#             Enigma.user_message_array.append(user_message[i])
#         for i in range(len(key)):
#             Enigma.key.append(key[i])  
#         # print(Enigma.user_message_array, Enigma.key)
        
    
#     class Rotor:
#         alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
#         turnDelay = len(alphabet)

#         def __init__(self, key):
#             self.startFrom = self.alphabet[-int(key):] + self.alphabet[:-int(key)]
#             # print(self.alphabet)
            
#         def turn(self):
#             self.startFrom = self.startFrom[-1:] + self.startFrom[:-1]


#     def chifr_message(rotor_1, rotor_2, rotor_3):


#     # def unchifr_message():






# class Menu:
#     def start():
#         # Очищаем консоль
#         print("\033[H\033[J", end="")
#         # Предоставляем выбор пользователю
#         user_choice = input("Зашифровать сообщение - '1', расшифровать сообщение - '2': ")

#         if user_choice == "1":
#             user_message = input("Введите сообщение для шифрования: ")
#             key = input("Введите ключ: ")
#             Enigma.make_arrays(user_message, key)

#             # Инициализируем роторы
#             rotor_1 = Enigma.Rotor(Enigma.key[0])
#             rotor_2 = Enigma.Rotor(Enigma.key[1])
#             rotor_3 = Enigma.Rotor(Enigma.key[2])
#             # print(rotor_1.startFrom, "\n" , rotor_2.startFrom, "\n" , rotor_3.startFrom)

#         elif user_choice == "2":
#             user_message = input("Введите зашифрованное сообщение: ")
#             key = input("Введите ключ: ")

#         else:
#             Menu.start()

Menu.start()