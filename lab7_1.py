# Завдання
# Є словник з друзями, де ключ – людина, а значення –
# список друзів. Користувач вводить імена двох людей,
# які є друзями, повторює це певну кількість разів,
# після чого дані зберігаються у файл.
# Завантажте дані назад та виведіть на екран.
import json


def save_data(data):
    with open('friends.json', 'a') as file:
        json.dump(data, file)
        file.write('\n')


def print_data():
    with open(f'friends.json', 'r') as file:
        data = file.readlines()
    for item in data:
        print(json.loads(item.strip()))


friends_list = {'John': ['Mery', 'Michael'], 'Katy': ['Andrew', 'Mery'], 'Bob': ['John', 'Andrew']}
for key, value in friends_list.items():
    print(f'{key}: {value}')

while True:
    friends = input('Input frends names (space separated):').split()

    if friends:
        if friends[0] in friends_list:
            if friends[1] in friends_list[friends[0]]:
                save_data({friends[0]: friends[1]})
    else:
        break

data = print_data()
