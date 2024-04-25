import json


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f'name: {self.name}, age: {self.age}')


person = Person('Max', 22)

with open('data.json', 'w') as file:
    json.dump(person, file)

# with open('data.json', 'r') as file:
#     read_data = json.load(file)

# print(read_data)
