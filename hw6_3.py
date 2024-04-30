from datetime import datetime
import json, pickle


# Завдання 3
# До вже реалізованого класу «Стадіон» додайте можливість
# стиснення та розпакування даних з використанням json та pickle.

# Завдання 2
#  Реалізуйте клас «Стадіон». Збережіть у класі: назву
# стадіону, дату відкриття, країну, місто, місткість. Реалізуйте
# методи класу для введення-виведення даних та інших
# операцій. До вже реалізованого класу «Стадіон» додайте
# необхідні перевантажені методи та оператори.
class Stadium:
    def __init__(self, name="", date=None, country="", city="", capacity=0):
        self.name = name
        self.date = date
        self.country = country
        self.city = city
        self.capacity = capacity

    def input_data(self):
        self.name = input("Введіть назву стадіону: ")
        while True:
            date = input("Введіть дату відкриття (дд.мм.рррр): ")
            try:
                datetime.strptime(date, "%d.%m.%Y")
                self.date = date
                break
            except ValueError:
                continue
        self.country = input("Введіть країну: ")
        self.city = input("Введіть місто: ")
        self.capacity = int(input("Введіть місткість: "))

    def save_data(self):
        data = {}
        for key in self.__dict__:
            data[key] = self.__dict__[key]
        # print(data)
        with open(f'{self.name}.json', 'w') as file:
            json.dump(data, file)

    def load_data(self, name):
        with open(f'{name}.json', 'r') as file:
            data = json.load(file)
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def __str__(self):
        return str([self.name, self.date, self.country, self.city, self.capacity])

    def show(self):
        return f"Назва: {self.name};\nДата відкриття: {self.date.strftime('%d.%m.%Y')};\nКраїна: {self.country};\nМісто: {self.city};\nCapacity: {self.capacity}."

    def __eq__(self, other):
        return self.name == other.name and self.date == other.date and self.country == other.country and self.city == other.city

    def __lt__(self, other):
        return self.capacity < other.capacity

    def __gt__(self, other):
        return self.capacity > other.capacity

    def __le__(self, other):
        return self.capacity <= other.capacity

    def __ge__(self, other):
        return self.capacity >= other.capacity

    def __ne__(self, other):
        return self.name != other.name or self.city != other.city


stadium1 = Stadium("Арена Львів", "29.10.2011", "Україна", "Львів", 34900)
stadium2 = Stadium("Чорноморець", "19.11.2011", "Україна", "Одеса", 34164)
stadium3 = Stadium()
# stadium3.input_data()
# print(stadium3.show())
# print(stadium3.__str__())
print(stadium1)
print(stadium2)
print(stadium1 == stadium2)
print(stadium1 > stadium2)
print(stadium1 < stadium2)
stadium4 = Stadium()
stadium5 = Stadium()

stadium1.save_data()
stadium4.load_data('Арена Львів')
print(f'loaded data: {stadium4}')

stadium2.save_data()
stadium5.load_data('Чорноморець')
print(f'loaded data: {stadium5}')
