# Завдання 2
# Створіть програму для проведення опитування або
# анкетування. Зберігайте відповіді користувачів у форматі
# JSON файлу. Кожне опитування може бути окремим
# об'єктом у файлі JSON, а відповіді кожного користувача -
# списком значень.
import json


class Client():
    def __init__(self, name, age, question_list):
        self._name = name
        self._age = age
        self._question_list = question_list
        self._answer_list = []

    def survey(self):
        answer = []
        for question in self._question_list:
            print(f'{question}: ')
            answer.append(input())
        self._answer_list = answer
        self.save_data()

    def save_data(self):
        data = {}
        for key in self.__dict__:
            data[key] = self.__dict__[key]
        with open(f'survey.json', 'a', encoding="utf-8") as file:
            json.dump(data, file)
            file.write('\n')


question_list = ['question1', 'question2', 'question3', 'question4', 'question5', 'question6']
user1 = Client('Steven', 29, question_list)
user1.survey()