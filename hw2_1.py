# Завдання 1
# Реалізуйте клас стеку для роботи з рядками (стек рядків).
# Стек має бути фіксованого розміру. Реалізуйте набір операцій
# для роботи зі стеком:
# o розміщення рядка у стек;
# o виштовхування рядка зі стеку;
# o підрахунок кількості рядків у стеку;
# o перевірку, чи порожній стек;
# o перевірку, чи повний стек;
# o очищення стеку;
# o отримання значення без виштовхування
# верхнього рядка зі стеку.
# На старті додатка відобразіть меню, в якому користувач
# може вибрати необхідну операцію.
class Stack:
    capacity = 5

    def __init__(self):
        self.stack = []
        self.stack_forward = []

    def insert(self, item):
        if len(self.stack) < Stack.capacity:
            self.stack.insert(0, item)
            return None
        else:
            self.stack.insert(0, item)
            return self.stack.pop()

    # def get_item(self):
    #     if not self.stack.is_empty():
    #         pass

    def get_len(self):
        print(len(self.stack))
        return len(self.stack)

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def is_full(self):
        if len(self.stack) == Stack.capacity:
            return True
        else:
            return False

    def clean(self):
        self.stack = []


stack1 = Stack()
print(stack1.get_len())
print(stack1.is_full())
print(stack1.is_empty())