# Завдання 1
# Маємо певний словник з назвами країн і столиць. Назва
# країни використовується як ключ, назва столиці — як значення. Реалізуйте: додавання, видалення, пошук, редагування,
# збереження та завантаження даних (використовуючи стиснення та розпакування).


import pickle
import gzip


class CountryData:

    def __init__(self, file_name):
        self._file_name = file_name
        self.country_info = {}

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
                        self.country_info = self.read_data(self._file_name)
                        print('data loaded', self.country_info)
                    case "2":
                        self.dump_data(self.country_info, self._file_name)
                        print('data saved')
                    case "3":
                        country = input('Введіть назву Країни: ')
                        capital = input('введіть столицю: ')
                        self.country_info[country] = capital
                        print(self.country_info)
                    case "4":
                        country = input('Введіть країну для видалення: ')
                        if country in self.country_info:
                            del self.country_info[country]
                        print(self.country_info)
                    case "5":
                        country = input('Введіть назву Країни: ')
                        if country in self.country_info:
                            print(f'Столиця: {self.country_info[country]}')
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


base1 = CountryData("country_data.gz")
base1.menu()
