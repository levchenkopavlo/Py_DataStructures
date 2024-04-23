# Завдання 1
# Користувач заповнює з клавіатури список цілих.
# Стисніть отримані дані та збережіть їх у файл. Після цього
# завантажте дані з файлу в новий список.
import pickle
int_numbers = list(map(int, input('input integer space separated: ').split()))
print(int_numbers)


with open('my_list.pickle', 'wb') as file:
    pickle.dump(int_numbers, file)

with open('my_list.pickle', 'rb') as file:
    read_data = pickle.load(file)

print(type(read_data), read_data)