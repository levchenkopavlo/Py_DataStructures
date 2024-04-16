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
        pass

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


clinic1 = ClinicQueue()


class TaskSolver:
    def __init__(self):
        self.queue = PriorityQueue()

    def solve_next_task(self):
        if self.queue.empty():
            print('no more task')
            return

        priority, task = self.queue.get()

        print(f'виконую {task}')
