from collections import deque


stack = deque()

stack.append(1)
stack.append(2)
stack.append(3)

print(f'{stack=}')

print(f'Дістанемо останній елемент {stack.pop()}')
print(f'{stack=}')