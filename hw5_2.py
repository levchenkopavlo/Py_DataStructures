# Завдання 2
# Маємо певний словник з назвами музичних груп (виконавців) та альбомів. Назва групи використовується як ключ,
# назва альбомів — як значення. Реалізуйте: додавання, видалення, пошук, редагування, збереження та завантаження
# даних (використовуючи стиснення та розпакування).

import pickle
import gzip


class ArtistData:

    def __init__(self, file_name):
        self._file_name = file_name
        self.artist_info = {}

    def menu(self):
        try:
            while True:
                print(f"\033[33m1\033[0m. Завантаження даних")
                print(f"\033[33m2\033[0m. Збереження даних")
                print(f"\033[33m3\033[0m. Додавання/редагування даних")
                print(f"\033[33m4\033[0m. Видалення даних")
                print(f"\033[33m5\033[0m. Пошук")
                userChoice = input("Виберіть необхідний пункт меню або \033[33mEnter\033[0m для виходу: ")
                print("\033[32m------------------------------------------------------\033[0m")
                match userChoice:
                    case "":
                        break
                    case "1":
                        self.artist_info = self.read_data(self._file_name)
                        print('data loaded', self.artist_info)
                    case "2":
                        self.dump_data(self.artist_info, self._file_name)
                        print('data saved')
                    case "3":
                        artist = input('Введіть назву гурту/виконавця: ')
                        album = input('введіть альбоми: ')
                        self.artist_info[artist] = album
                        print(self.artist_info)
                    case "4":
                        artist = input('Введіть назву гурту/виконавця для видалення: ')
                        if artist in self.artist_info:
                            del self.artist_info[artist]
                        print(self.artist_info)
                    case "5":
                        artist = input('Введіть назву назву гурту/виконавця: ')
                        if artist in self.artist_info:
                            print(f'Альбоми: {self.artist_info[artist]}')
                    case _:
                        print("\033[33mзробіть правильний вибір...\033[0m")
                        continue
        except(Exception) as e:
            print(e)

    @staticmethod
    def dump_data(data, file_name):
        with gzip.open(file_name, 'wb') as file:
            serialized_data = pickle.dumps(data)
            file.write(serialized_data)

    @staticmethod
    def read_data(file_name):
        with gzip.open(file_name, 'rb') as file:
            serialized_data = file.read()
            read_data = pickle.loads(serialized_data)
            return read_data


base1 = ArtistData("artist_data.gz")
base1.menu()
