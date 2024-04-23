import pickle, gzip


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f'name: {self.name}, age: {self.age}')


person1 = Person('John', 33)

with open('person.pickle', 'wb') as file:
    pickle.dump(person1, file)

with open('person.pickle', 'rb') as file:
    read_person = pickle.load(file)

print((type(read_person)), read_person)
read_person.print_info()
