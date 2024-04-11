from queue import LifoQueue

stack = LifoQueue()

stack.put(1)
stack.put(2)
stack.put(3)

print(f'{stack=}')

print(f'Дістанемо останній елемент {stack.get()}')
print(f'{stack=}')