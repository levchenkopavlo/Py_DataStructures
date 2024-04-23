# Завдання 3
# Маємо певний словник з логінами і паролями користувачів. Логін використовується як ключ, пароль —
# як значення. Реалізуйте: додавання, видалення, пошук,
# редагування, збереження та завантаження даних (використовуючи стиснення та розпакування)
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


file_name = "login_data.gz"
user_info = {}
try:
    while True:
        print(f"\033[33m1\033[0m. Завантаження даних")
        print(f"\033[33m2\033[0m. Збереження даних")
        print(f"\033[33m3\033[0m. Додавання даних")
        print(f"\033[33m4\033[0m. Видалення даних")
        print(f"\033[33m5\033[0m. Пошук")
        userChoice = input("Виберіть необхідний пункт меню або \033[33mEnter\033[0m для виходу: ")
        print("\033[32m------------------------------------------------------\033[0m")
        match userChoice:
            case "":
                break
            case "1":
                user_info = read_data(file_name)
                print('data loaded', user_info)
            case "2":
                dump_data(user_info, file_name)
                print('data saved')
            case "3":
                login = input('введіть логін: ')
                password = input('введіть пароль: ')
                user_info[login] = password
                print(user_info)
            case "4":
                login = input('введіть логін для видалення: ')
                if login in user_info:
                    del user_info[login]
                print(user_info)
            case "5":
                login = input('введіть логін: ')
                if login in user_info:
                    print(f'Пароль: {user_info[login]}')
            case _:
                print("\033[33mзробіть правильний вибір...\033[0m")
                continue
except(Exception) as e:
    print(e)
