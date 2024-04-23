# Завдання 2
# При старті програми з’являється меню з наступними пунктами:
# 1. Завантаження даних;
# 2. Збереження даних;
# 3. Додавання даних;
# 4. Видалення даних.
# Використайте список цілих як сховища даних. Також застосуйте стиснення/розпакування даних.

import pickle
import gzip


def dump_data(data, file_name):
    with gzip.open(file_name, 'wb') as file:
        serialized_data = pickle.dumps(data)
        file.write(serialized_data)


def read_data(file_name):
    with gzip.open(file_name, 'rb') as file:
        serialized_data = file.read()
        read_data = pickle.loads(serialized_data)
        return read_data


print(type(read_data), read_data)

file_name = "my_list.gz"
try:
    while True:
        print(f"\033[33m1\033[0m. Завантаження даних")
        print(f"\033[33m2\033[0m. Збереження даних")
        print(f"\033[33m3\033[0m. Додавання даних")
        print(f"\033[33m4\033[0m. Видалення даних")
        userChoice = input("Виберіть необхідний пункт меню або \033[33mEnter\033[0m для виходу: ")
        print("\033[32m------------------------------------------------------\033[0m")
        match userChoice:
            case "":
                break
            case "1":
                int_numbers = read_data(file_name)
                print('data loaded', int_numbers)
            case "2":
                dump_data(int_numbers, file_name)
                print('data saved')
            case "3":
                int_numbers = list(map(int, input('input integer space separated: ').split()))
                print(int_numbers)
            case "4":
                print(int_numbers)
                del_value = int(input('enter index of value for delete: '))
                if del_value in range(len(int_numbers) - 1):
                    del int_numbers[del_value]
            case _:
                print("\033[33mзробіть правильний вибір...\033[0m")
                continue
except(Exception) as e:
    print(e)
