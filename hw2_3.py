# Завдання 3
# Дано три вежі та n дисків різного розміру, відсортованих
# за зростанням, розміщених на першій вежі у вигляді піраміди.
# Потрібно перемістити всі диски на третю вежу,
# використовуючи проміжну вежу, за умови, що можна
# переміщати тільки один диск за раз та диск завжди можна
# покласти лише на диск більшого розміру або на порожню вежу.
# Ця задача може бути вирішена за допомогою
# рекурсивного алгоритму, використовуючи стек для
# зберігання проміжних ходів при переміщенні дисків між
# вежами
def move_disk(*args):
    last_element = args[0]
    stack1 = args[1]
    stack2 = args[2]
    stack3 = args[3]
    counter = args[4]
    print(counter)
    if len(stack1) == num_disk and last_element != 0:
        return
    if len(stack3) == num_disk:
        print(stack3)
        print(counter)
        quit()
    if stack1:  # стек1 не порожній
        if stack1[-1] != last_element:
            if stack2:  # стек2 не порожній
                if stack1[-1] < stack2[-1]:
                    stack2.append(stack1.pop())
                    move_disk(stack2[-1], stack1, stack2, stack3, counter+1)
            else:
                stack2.append(stack1.pop())
                move_disk(stack2[-1], stack1, stack2, stack3, counter+1)

    if stack1:  # стек1 не порожній
        if stack1[-1] != last_element:
            if stack3:  # стек3 не порожній
                if stack1[-1] < stack3[-1]:
                    stack3.append(stack1.pop())
                    move_disk(stack3[-1], stack1, stack2, stack3, counter+1)
            else:
                stack3.append(stack1.pop())
                move_disk(stack3[-1], stack1, stack2, stack3, counter+1)
    # ====================================================================================
    if stack2:  # стек2 не порожній
        if stack2[-1] != last_element:
            if stack1:  # стек1 не порожній
                if stack2[-1] < stack1[-1]:
                    stack1.append(stack2.pop())
                    move_disk(stack1[-1], stack1, stack2, stack3, counter+1)
            else:
                stack1.append(stack2.pop())
                move_disk(stack1[-1], stack1, stack2, stack3, counter+1)

    if stack2:  # стек2 не порожній
        if stack2[-1] != last_element:
            if stack3:  # стек3 не порожній
                if stack2[-1] < stack3[-1]:
                    stack3.append(stack2.pop())
                    move_disk(stack3[-1], stack1, stack2, stack3, counter+1)
            else:
                stack3.append(stack2.pop())
                move_disk(stack3[-1], stack1, stack2, stack3, counter+1)
    # ====================================================================================
    if stack3:  # стек3 не порожній
        if stack3[-1] != last_element:
            if stack1:  # стек1 не порожній
                if stack3[-1] < stack1[-1]:
                    stack1.append(stack3.pop())
                    move_disk(stack1[-1], stack1, stack2, stack3, counter+1)
            else:
                stack1.append(stack3.pop())
                move_disk(stack1[-1], stack1, stack2, stack3, counter+1)

    if stack3:  # стек3 не порожній
        if stack3[-1] != last_element:
            if stack2:  # стек2 не порожній
                if stack3[-1] < stack2[-1]:
                    stack2.append(stack3.pop())
                    move_disk(stack2[-1], stack1, stack2, stack3, counter+1)
            else:
                stack2.append(stack3.pop())
                move_disk(stack2[-1], stack1, stack2, stack3, counter+1)
    return


stack1 = []
stack2 = []
stack3 = []
num_disk = 2
for i in range(num_disk, 0, -1):
    stack1.append(i)
print(stack1)
move_disk(0, stack1, stack2, stack3, 1)
