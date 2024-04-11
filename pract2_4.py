class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        self.size += 1

        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            raise IndexError('stack is empty')

        self.size -= 1

        data = self.head.data
        self.head = self.head.next

        return data

    def peek(self):
        if self.head is None:
            raise IndexError('stack is empty')

        return self.head.data

    def get_size(self):
        return self.size

    def print(self):
        node = self.head

        while node:
            print(node.data, end=' ')
            node = node.next
        print()


stack = Stack()

stack.append(1)
stack.append(2)
stack.append(3)

stack.print()

print(f'Дістанемо останній елемент {stack.pop()}')
stack.print()

print(f'Подивемось на останній елемент {stack.peek()}')
stack.print()
