import pickle
import gzip


class UserData:

    def __init__(self):
        self.file_name = "login_data.gz"
        self.user_info = {}

    def menu(self):
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
                        self.user_info = self.read_data(self.file_name)
                        print('data loaded', self.user_info)
                    case "2":
                        self.dump_data(self.user_info, self.file_name)
                        print('data saved')
                    case "3":
                        login = input('введіть логін: ')
                        password = input('введіть пароль: ')
                        self.user_info[login] = password
                        print(self.user_info)
                    case "4":
                        login = input('введіть логін для видалення: ')
                        if login in self.user_info:
                            del self.user_info[login]
                        print(self.user_info)
                    case "5":
                        login = input('введіть логін: ')
                        if login in self.user_info:
                            print(f'Пароль: {self.user_info[login]}')
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


base1 = UserData()
base1.menu()
