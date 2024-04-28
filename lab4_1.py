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


class Dictionary:
    def __init__(self):
        self.tree = AVLTree()
        self.call_counter = {}

    def show(self, word):
        if word in self.tree:
            self.call_counter[word] += 1
            return f'{word}: {self.tree[word]}'
        else:
            return None

    def show_all(self):
        for word in self.tree:
            print(f'{word}: {self.tree[word]}')

    def add_word(self, new_word, *translate):
        if new_word in self.tree:
            self.tree[new_word] |= set(translate)
        else:
            self.tree.insert(key=new_word, value=set(translate))
            self.call_counter[new_word] = 0

    def edit_word(self, word, new_word):
        if word in self.tree:
            self.add_word(new_word, *self.tree[word])
            self.tree.remove(word)
        else:
            print('no record in base')

    def edit_translate(self, word, *translate):
        if word in self.tree:
            self.tree[word] = set(translate)
        else:
            self.tree.insert(key=word, value=set(translate))

    def remove_word(self, word):
        if word in self.tree:
            self.tree.remove(word)
        else:
            pass

    def search(self, search_word):
        if search_word in self.tree:
            return True
        else:
            return False

    def show_statistic(self):
        print(f'статистика запитів: {self.call_counter}')

    def get_statistic(self):
        return {self.call_counter}

    def show_most_usable(self, number=0):
        sorted_dict_values = sorted(self.call_counter.items(), key=lambda x: x[1], reverse=True)
        if number:
            print(*sorted_dict_values[0:number])
        else:
            print(*sorted_dict_values)


# ------------------------------------------------------------------------------------------------------
dictionary = Dictionary()
dictionary.add_word('запит', 'request')
print(dictionary.search('запит'))
print(dictionary.show('запит'))
dictionary.add_word('запит', 'question')
print(dictionary.show('запит'))
dictionary.add_word('стіл', 'table')
print(dictionary.show('стіл'))
dictionary.add_word('кран', 'crane', 'tap')
print()
dictionary.show_all()
dictionary.edit_translate('запит', 'request')
print(dictionary.show('кран'))
print(dictionary.show('кран'))
print(dictionary.show('кран'))
print()
dictionary.show_all()
print()
dictionary.show_statistic()
dictionary.edit_word('стіл', 'столище')
dictionary.show_all()

print()
dictionary.show_most_usable()
dictionary.show_most_usable(2)