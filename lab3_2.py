from queue import PriorityQueue


class ClinicQueue:
    def __init__(self, capacity=5):
        self.queue = PriorityQueue()
        self._capacity = capacity

    def isEmpty(self):
        return self.queue.empty()

    def isFull(self):
        if self.queue.qsize() == self._capacity:
            return True
        else:
            return False

    def insertWithPriority(self, client, priority):
        if self.isFull():
            print('черга повна')
        else:
            self.queue.put((priority, client))

    def pullHighestPriorityElement(self):
        return self.queue.get()

    def peek(self):
        pass

    def show(self):
        temp_queue = PriorityQueue()
        while not self.queue.empty():
            client = self.queue.get()
            print(client, end=' <- ')
            temp_queue.put(client)

        print()

        self.queue = temp_queue


queue1 = ClinicQueue()

queue1.insertWithPriority(2,'Mary')
queue1.insertWithPriority(3,'Sophy')
queue1.insertWithPriority(1,'John')
print(queue1.pullHighestPriorityElement())
