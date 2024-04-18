# Завдання 1
# Розробіть додаток, що імітує чергу запитів до сервера.
# Мають бути клієнти, які надсилають запити на сервер, кожен
# з яких має свій пріоритет. Кожен новий клієнт потрапляє у
# чергу залежно від свого пріоритету. Зберігайте статистику
# запитів (користувач, час) в окремій черзі.
# Передбачте виведення статистики на екран. Вибір необхідних структур даних визначте самостійно.

from queue import PriorityQueue


class ServerQueue:
    def __init__(self):
        self._queue = PriorityQueue()
        self._statistic = []
        # self._capacity = capacity

    def enqueue(self, request, priority, time):
        pass

    def dequeue(self):
        return self._queue.get()
