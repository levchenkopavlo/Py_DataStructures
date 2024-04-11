from collections import deque
stack=deque


from queue import LifoQueue
stack=LifoQueue()
stack.put(1)
stack.put(2)
stack.put(3)

print(f'{stack=}')

print(f'дістанемо останній елемент {stack.get()}')
print(f'{stack=}')
print(f'дістанемо останній елемент {stack.get()}')