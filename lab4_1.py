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


class Word:
    def __init__(self, word):
        self.word = word
        self.eng_translate = {}
        self.call_counter = 0

    def __str__(self):
        return f'{self.word}: {self.eng_translate}, {self.call_counter}'


class Dictionary:
    def __init__(self):
        self.dictionary = AVLTree()

    def add_word(self, word, translate):
        if word in self.dictionary:
            word.eng_translate.update(translate)
        else:
            word = Word(word)

            self.dictionary.insert(word, None)

    def search(self, word):
        word = Word(word)

        # if word in self.dictionary:
        #     return True
        # else:
        #     print('word is not in the dictionary')


dictionary = Dictionary()
dictionary.add_word('запит', None)
dictionary.search('запит')

print()
