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
    def __init__(self, boat_id):
        self._boat_id = boat_id
        self._seats = Queue()
        self._free_seats = random.randint(0, 14)

    def enqueue(self, client):
        self._seats.put(client)

    def isFull(self):
        if self._seats.qsize() == self._free_seats:
            return True
        else:
            return False

    def get_boat_free_seats(self):
        return self._free_seats

    def get_queue_size(self):
        return self._seats.qsize()


class Berth:
    def __init__(self):
        self._queue = Queue()
        self._all_passenger = Queue()
        self._all_boat = Queue()

    def isEmpty(self):
        return self._queue.empty()

    def enqueue(self, client):
        self._queue.put(client)
        self._all_passenger.put(client)

    def dequeue(self):
        if self._queue.empty():
            print('no client')
            return
        client = self._queue.get()
        return client

    def peak(self):
        return self._queue.queue[0]
    def get_queue_size(self):
        return self._queue.qsize()
    def get_all_passengers(self):
        return self._all_passenger.qsize()


def simulate(max_pass_time, max_boat_time, min_simulation_time=100):
    passed_time = 0
    next_boat_time = 0
    passenger_id = 1
    boat_id = 1
    delay = 0
    while passed_time <= min_simulation_time:
        next_boat_time += random.uniform(min_boat_time, max_boat_time)
        # time_to_boat = 0
        while passed_time <= next_boat_time:
            berth.enqueue(passenger_id)
            passed_time += random.uniform(0, max_pass_time)
            print(f'пасажир {passenger_id} прибув')
            passenger_id += 1
            time.sleep(delay)
        print(f'{passed_time=}')
        boat = SeaBoat(boat_id)
        print(f'Човен {boat_id} прибув, вільних місць: {boat.get_boat_free_seats()}')
        while not boat.isFull() and not berth.isEmpty():
            passenger = berth.dequeue()
            boat.enqueue(passenger)
            print(f'пасажир {passenger} сів на човен')
            time.sleep(delay)
        print(
            f'Човен {boat_id} відплив. На борту {boat.get_queue_size()} пасажирів з {boat.get_boat_free_seats()}')
        boat_id += 1
    print()
    print(f'На причалі залишилось пасажирів {berth.get_queue_size()}')
    print(f'Середній час очікування човна {round(next_boat_time/(boat_id-1),3)}')
    print(f'Середній час між появою пасажирів {round(passed_time/berth.get_all_passengers(),3)}')


max_pass_time = 3
min_boat_time = 6
max_boat_time = 10
berth = Berth()
simulate(max_pass_time, max_boat_time)




