# Завдання 1
# Створіть два окремих "мікросервіси" (дві окремі
# програми). Одна програма створює та експортує дані у
# форматі JSON, а інша програма завантажує та обробляє ці
# дані. Це може бути, наприклад, система, яка створює та
# обробляє замовлення.
import json
from queue import Queue


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

def save(data, filename='task.json'):
    with open(filename, 'w') as file:
        json.dump(data, file)


def load(filename='task.json'):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

# Завдання 1
# Розробіть додаток, що імітує чергу запитів до сервера.
# Мають бути клієнти, які надсилають запити на сервер, кожен
# з яких має свій пріоритет. Кожен новий клієнт потрапляє у
# чергу залежно від свого пріоритету. Зберігайте статистику
# запитів (користувач, час) в окремій черзі.
# Передбачте виведення статистики на екран. Вибір необхідних структур даних визначте самостійно.
import random
from queue import Queue, PriorityQueue
import datetime, time


class Task:
    def __init__(self, request, priority, timestamp):
        self.request = request
        self.priority = priority
        self.timestamp = timestamp

    def __str__(self):
        return f'{self.request}, {self.priority}, {self.timestamp}'

    def __lt__(self, other):
        if self.request < other.request:
            return True
        else:
            return False


class ServerQueue:
    def __init__(self):
        self.queue = PriorityQueue()
        self._statistic = Queue()

    def enqueue(self, request, priority, timestamp):
        task = Task(request, priority, timestamp)
        print(f'{task} income')
        self.queue.put((priority, task))
        self._statistic.put(task)

    def dequeue(self):
        if self.isEmpty():
            print('queue is empty')
        else:
            return self.queue.get()

    def peek(self):
        # print(self.queue.queue[0][1].request)
        return self.queue.queue[0][1]

    def isEmpty(self):
        return self.queue.empty()

    def statistic_print(self):
        while not self._statistic.empty():
            print(self._statistic.get())


server_queue = ServerQueue()
counter = 1
while True:
    for _ in range(4):  # add task to queue
        server_queue.enqueue(f'task_{counter}', random.randint(1, 9), datetime.datetime.now().timestamp())
        time.sleep(random.randint(1, 10) / 6)
        # print(server_queue.peek().timestamp)
        counter += 1
    for _ in range(5):  # process task
        if server_queue.isEmpty():
            print(f'all task executed')
            break
        exec_task = server_queue.dequeue()
        exec_time = random.randint(1, 10) / 7
        print(f'{exec_task[1].request} executed')
        if not server_queue.isEmpty():
            if server_queue.peek().timestamp - exec_task[1].timestamp > exec_time:
                print(f'all task executed')
                break

    if counter > 11:
        break
while not server_queue.isEmpty():
    exec_task = server_queue.dequeue()
    exec_time = random.randint(1, 10) / 7
    print(f'{exec_task[1].request} executed')
print()
server_queue.statistic_print()