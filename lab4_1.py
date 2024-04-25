# Завдання 1
# Створіть програму роботи зі словником.
# Наприклад, англо-іспанський, французько-німецький або інша мовна пара.
# Програма має:
# ■ надавати початкове введення даних для словника;
# ■ відображати слово та його переклади;
# ■ дозволяти додавати, змінювати, видаляти переклади слова;
# ■ дозволяти додавати, змінювати, видаляти слово;
# ■ відображати топ-10 найпопулярніших слів (визначаємо популярність спираючись на лічильник звернень);
# ■ відображати топ-10 найнепопулярніших слів (визначаємо непопулярність спираючись на лічильник
# звернень).
# Використовуйте дерево для виконання цього завдання.

from bintrees import AVLTree
import random
def generate_id():
    return float(random.randint(1, 999999) / 1000000)

class Word:
    def __init__(self, word):
        self.word = word
        self.eng_translate = {}
        self.call_counter = str(generate_id())

    def __str__(self):
        return f'{self.word}: {self.eng_translate}, {self.call_counter}'


class Dictionary:
    def __init__(self):
        self.tree = AVLTree()

    def add_word(self, word, translate):
        if word in self.tree:
            word.eng_translate.update(translate)
        else:
            word = Word(word)

            self.tree.insert(word, None)

    def search(self, word):
        word = Word(word)

        # if word in self.dictionary:
        #     return True
        # else:
        #     print('word is not in the dictionary')
#------------------------------------------------------------------------------------------------------

    def add_person(self, person):
        if self.search_id(person.id):
            pass
        else:
            self.tree.insert(key=person.id, value=person)

    def penalty_add(self, person_id, penalty):
        if self.search_id(person_id):
            person = self.tree[person_id]
            self.tree.remove(person_id)
            if person.penalty is not None:
                for penalty_type, value in penalty:
                    if penalty_type not in person.penalty:
                        person.penalty[penalty_type] = value
                    else:
                        person.penalty[penalty_type].append(value)
            else:
                person.penalty = penalty
            self.add_person(person)
        else:
            print('person not exist')

    def penalty_edit(self, person_id, penalty):
        if self.search_id(person_id):
            person = self.tree[person_id]
            self.tree.remove(person_id)
            person.penalty = penalty
            self.add_person(person)
        else:
            print('person not exist')

    def search_id(self, person_id):
        if person_id in self.tree:
            return True
        else:
            return False

    def delete(self, person_id):
        if person_id in self.tree:
            self.tree.remove(person_id)
        else:
            print('no record')

    def display(self):
        for person in self.tree.values():
            print(person)

    def filter_id(self, person_id):
        for person in self.tree.values():
            if person_id == person.id:
                print(person)

    def filter_city(self, city):
        for person in self.tree.values():
            if city == person.city:
                print(person)

    def filter_city(self, city):
        for person in self.tree.values():
            if city == person.city:
                print(person)

    def filter_penalty_type(self, penalty_type):
        for person in self.tree.values():
            if person.penalty is not None:
                if penalty_type in person.penalty:
                    print(person)





#------------------------------------------------------------------------------------------------------
dictionary = Dictionary()
dictionary.add_word('запит', None)
dictionary.search('запит')

print()
#------------------------------------------------------------------------------------------------------
class Person:
    def __init__(self, name, city, penalty=None):
        self.id = str(generate_id())
        self.penalty = penalty
        self.city = city
        self.name = name

    def __call__(self, *args, **kwargs):
        pass

    def __str__(self):
        return f'name: {self.name}, id: {self.id}, city: {self.city}, penalty: {self.penalty}'


class PenaltyTree:


person1 = Person("Bob Peterson", 'NY', {'1': [100, 120], '2': [200]})
person2 = Person("Петрик Пяточкін", 'Київ')
person3 = Person("Івасик Телесик", 'Полтава')
print(person1)
print(person2)
penalty_base = PenaltyTree()
penalty_base.add_person(person1)
print(penalty_base.search_id(person1.id))
print(penalty_base.search_id(person2.id))
penalty_base.add_person(person2)
print()
penalty_base.display()
# print()
# penalty_base.filter_id(input('enter id: '))
print()
penalty_base.filter_penalty_type('1')
# print()
# penalty_base.penalty_add(input('enter id: '))
