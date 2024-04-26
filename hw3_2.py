# Завдання 2
# Створіть імітаційну модель «Причал морських катерів».
# Введіть таку інформацію:
# 1. Середній час між появою пасажирів на причалі у різний час доби;
# 2. Середній час між появою катерів на причалі у різний час доби;
# 3. Тип зупинки катера (кінцева або інша).
# Визначіть:
# 1. Середній час перебування людини на зупинці;
# 2. Достатній інтервал часу між приходами катерів, коли на
# зупинці не більше N людей одночасно;
# 3. Кількість вільних місць у катері є випадковою величиною.
# Вибір необхідних структур даних визначте самостійно.
import random
from queue import Queue, PriorityQueue
import datetime, time


class Passenger:

    def __init__(self, number):
        self._id = number


class SeaBoat:
    def __init__(self):
        self._seats = Queue()
        self._free_seats = random.randint(0, 10)


class Berth:
    def __init__(self):
        self._queue = Queue()

    def isEmpty(self):
        return self.queue.empty()

    def isFull(self):
        if self.queue.qsize() == self._capacity:
            return True
        else:
            return False

    def enqueue(self, client):
        self._queue.put(client)

    def dequeue(self):
        if self.queue.empty():
            print('no client')
            return
        client = self.queue.get()
        return client


def simulate(max_pass_time, max_boat_time, simulation_time=100):
    passed_time = 0
    next_boat_time = 0
    passenger_id = 1
    while passed_time <= simulation_time:
        next_boat_time += random.uniform(0, max_boat_time)
        # time_to_boat = 0
        while passed_time <= next_boat_time:
            berth.enqueue(passenger_id)
            random.uniform(0, max_pass_time)


max_pass_time = 2
max_boat_time = 10
simulate(max_pass_time, max_boat_time)
berth = Berth()
