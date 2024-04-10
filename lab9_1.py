# Завдання 1
# Користувач вводить з клавіатури набір чисел. Збережіть отримані числа до однозв’язного списку. Після
# чого покажіть меню, в якому запропонуєте користувачеві
# набір пунктів:
# 1. Додати елемент до списку.
# 2. Видалити елемент зі списку.
# 3. Показати вміст списку.
# 4. Перевірити, чи є значення у списку.
# 5. Замінити значення у списку.
# Дія виконується залежно від вибору користувача,
# після чого меню з’являється знову.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f'{self.data} -> {self.next}'


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        return str(self.head)

    def print(self):
        node = self.head

        while node is not None:
            print(node.data, end='->')
            node = node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def delete(self, data):
        # Знайти node з потрібним data
        node = self.head
        prev = Node
        while node is not None and node.data != data:
            prev = node
            node = node.next
        if node is None:
            print('Не знайдено')
            return
        prev.next = node.next

    def search(self, data):
        node = self.head
        while node is not None and node.data != data:
            node = node.next
        if node is None:
            print('Не знайдено')
            return
        else:
            print('Знайдено')

    def replace(self, data, new_data):
        node = self.head
        while node is not None and node.data != data:
            node = node.next
        if node is None:
            print('Не знайдено')
            return
        node.data = new_data


my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)

my_list.print()

print()
my_list.search(3)

print()
my_list.replace(3, 99)
my_list.print()
print()
my_list.delete(99)
my_list.print()
print()


# my_list2 = LinkedList()
# data_list = input("input data (space separated): ").split()
# print(data_list)
# for i in data_list:
#     my_list2.append(int(i))
# my_list2.print()