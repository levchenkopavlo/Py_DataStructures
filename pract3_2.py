from queue import PriorityQueue

queue1 = PriorityQueue()

queue1.put((1, 'Mary'))
queue1.put((1, 'Sofie'))
queue1.put((1, 'John'))

while not queue1.empty():
    priority, client = queue1.get()
    print(client, priority)


class TaskSolver:
    def __init__(self):
        self.queue = PriorityQueue()

    def add_task(self, task, priority):
        self.queue.put((priority, task))

    def solve_next_task(self):
        if self.queue.empty():
            print('no more task')
            return

        priority, task = self.queue.get()

        print(f'виконую {task}')

solver=TaskSolver()

solver.add_task('task 2',2)
solver.add_task('task 3',3)
solver.add_task('task 1',1)

solver.solve_next_task()
solver.solve_next_task()
solver.solve_next_task()

