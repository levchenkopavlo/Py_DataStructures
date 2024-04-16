from queue import Queue


# ■ IsEmpty — перевірка, чи черга пуста;
# ■ IsFull — перевірка черги на заповнення;
# ■ Enqueue — додати новий елемент до черги;
# ■ Dequeue — видалення елемента з черги;
# ■ Show — відображення на екрані всіх елементів черги.

class RestaurantQueue:
    def __init__(self, capacity=5):
        self.queue = Queue()
        self._capacity = capacity

    def isEmpty(self):
        return self.queue.empty()

    def isFull(self):
        if self.queue.qsize() == self._capacity:
            return True
        else:
            return False

    def enqueue(self, client):
        self.queue.put(client)

    def dequeue(self):
        if self.queue.empty():
            print('no client')
            return
        client = self.queue.get()
        return client

    def show(self):
        temp_queue = Queue()
        while not self.queue.empty():
            client = self.queue.get()
            print(client, end=' <- ')
            temp_queue.put(client)

        print()

        self.queue = temp_queue


queue1 = RestaurantQueue()
queue1.enqueue('Mary')
queue1.enqueue('Sophy')
queue1.enqueue('John')
queue1.show()
queue1.enqueue('Kate')
queue1.show()
print(f'Замовлення для {queue1.dequeue()} готове.')
print(f'Замовлення для {queue1.dequeue()} готове.')
queue1.enqueue('Steven')
queue1.show()