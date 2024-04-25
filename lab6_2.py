# Завдання 2
# Реалізація програми для додавання, видалення та
# відстеження завдань/заміток. Зберігати ці завдання у
# форматі JSON у файлі. Можливість завантаження
# раніше збережених завдань для подальшої роботи з ними.
import json


class Task:
    def __init__(self):
        self._task = []

    def task_add(self, task):
        self._task += task

    def task_save(self, filename='task.json'):
        with open(filename, 'w') as file:
            json.dump(self._task, file)

    def task_load(self, filename='task.json'):
        with open(filename, 'r') as file:
            self._task = json.load(file)
    def get_tasks(self):
        return self._task



tasklist1 = Task()
tasklist1.task_add(['1', '2'])
print(tasklist1.get_tasks())

tasklist1.task_save()
tasklist1.task_add(['3', '4'])
tasklist1.task_save()
tasklist1.task_load()
print(tasklist1.get_tasks())
tasklist1.task_load()
print(tasklist1.get_tasks())