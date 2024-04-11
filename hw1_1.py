# Завдання
# Користувач вводить з клавіатури набір чисел. Отримані
# числа необхідно зберегти до списку (тип списку оберіть в залежності від поставленого нижче завдання).
# Після чого покажіть меню, в якому запропонуєте користувачеві набір пунктів:
# 1. Додати нове число до списку (якщо таке число існує у
# списку, потрібно вивести повідомлення про це користувачеві без додавання числа).
# 2. Видалити усі входження числа зі списку (користувач вводить з клавіатури число для видалення)
# 3. Показати вміст списку (залежно від вибору користувача, покажіть список з початку або з кінця)
# 4. Перевірити, чи є значення у списку
# 5. Замінити значення у списку (користувач визначає, чи замінити тільки перше входження, чи всі)
# Дія виконується залежно від вибору користувача, після чого меню з’являється знову.
class Node:
    def __init__(self, data):
        self.data = data  # Зберігаємо дані у вузлі
        self.next = None  # Посилання на наступний вузол у списку
        self.prev = None  # Посилання на попередній вузол у двосв'язному списку

    def __str__(self):
        # return f'data: {self.data}, next: {self.next}, prev: {self.prev}'
        return f'data: {self.data} -> next: {self.next}'

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    @classmethod
    def info(cls):
        print(f'{cls.__dict__}')

    def __str__(self):
        return f'{self.head}'

    def search(self, data):
        # search_node = Node(data)
        node = self.head
        while node is not None and node.data != data:
            node = node.next
        if node is None:
            return False
        else:
            return True

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        else:
            if self.search(data):
                print(f"{data} already in the list")
            else:
                last_node = self.tail
                self.tail = new_node
                self.tail.prev = last_node
                last_node.next = self.tail
    def delete(self,data):
        node = self.head
        while node is not None:
            if node.data==data:
                node.prev.next=node.next
                node.next.prev=
            node = node.next


my_list = LinkedList()
print(my_list.head)
print(my_list.__dict__)
my_list.append(1)
print(f'head: {my_list.head}')
print(f'tail: {my_list.tail}')
my_list.append(2)
print(f'head: {my_list.head}')
print(f'tail: {my_list.tail}')
my_list.append(3)
print(f'head: {my_list.head}')
print(f'tail: {my_list.tail}')

print(my_list.search(2))
print()

my_list.info()
