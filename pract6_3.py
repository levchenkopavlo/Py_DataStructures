import json


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f'name: {self.name}, age: {self.age}')

    def save(self, filename='person.json'):
        dct = {'name': self.name,
               'age': self.age}

        with open(filename, 'w') as file:
            json.dump(dct, file)

    def load(self, filename='person.json'):
        with open(filename, 'r') as file:
            dct = json.load(file)

        print(dct)


person = Person('Max', 22)
person.save()
person.load()