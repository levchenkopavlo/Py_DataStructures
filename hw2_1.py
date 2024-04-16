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
    def __init__(self, capacity=5):
        self._stack = []
        self._capacity = capacity

    def insert(self, item):
        if len(self._stack) < self._capacity:
            self._stack.insert(0, item)
            return None
        else:
            self._stack.insert(0, item)
            return self._stack.pop()

    def get_item(self):
        if not self._stack:
            print("stack is empty")
            return None
        else:
            return self._stack[-1]

    def get_len(self):
        return len(self._stack)

    def is_empty(self):
        return bool(not self._stack)

    def is_full(self):
        if len(self._stack) == self._capacity:
            return True
        else:
            return False

    def clean(self):
        self._stack = []

    def __str__(self):
        return str(self._stack)


stack1 = Stack()
try:
    while True:
        print(f"\033[33m1\033[0m. Додати рядок в стек")
        print(f"\033[33m2\033[0m. Виштовхнути рядок з стеку")
        print(f"\033[33m3\033[0m. Кількість елементів стеку")
        print(f"\033[33m4\033[0m. Стек порожній?")
        print(f"\033[33m5\033[0m. Стек повний?")
        print(f"\033[33m6\033[0m. Очистити стек")
        print(f"\033[33m7\033[0m. Отримати значення без виштовхування")
        print(f"\033[33m8\033[0m. Переглянути вміст стеку")
        userChoice = input("Виберіть необхідний пункт меню або \033[33mEnter\033[0m для виходу: ")
        print("\033[32m------------------------------------------------------\033[0m")
        match userChoice:
            case "":
                break
            case "1":
                print("Введіть рядок для додавання в стек: ")
                string_for_stack = input()
                stack1.insert(string_for_stack)

            case "2":
                print(stack1.insert(None))
            case "3":
                print(stack1.get_len())
            case "4":
                print(stack1.is_empty())
            case "5":
                print(stack1.is_full())
            case "6":
                stack1.clean()
            case "7":
                print(stack1.get_item())
            case "8":
                print(stack1)
            case _:
                print("\033[33mзробіть правильний вибір...\033[0m")
                continue

except(Exception) as e:
    print(e)
