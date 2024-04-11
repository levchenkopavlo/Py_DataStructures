priority = {'+': 1, '-': 1, '*': 2, '/': 2, '(': -100}


def infix_to_postfix(text):
    # priority = {'+': 1, '-': 1, '*': 2, '/': 2, '(': -100}
    charecters = text.split()
    stack = []
    result = ''

    for char in charecters:
        if char.isdigit():
            result += ' ' + char

        elif char == '(':
            stack.append(char)

        elif char == ')':
            while stack[-1] != '(':
                result += ' ' + stack.pop()

            stack.pop()

        else:
            while stack and priority[stack[-1]] >= priority[char]:
                result += ' ' + stack.pop()

            stack.append(char)

    result += ' ' + ' '.join(stack)

    return result


def action(sign, num1, num2):
    if sign == '+':
        return num1 + num2
    elif sign == '-':
        return num1 - num2
    elif sign == '*':
        return num1 * num2
    elif sign == '/':
        return int(num1 / num2)
    else:
        raise AttributeError('unknown action')


def my_calc(postfix_text):
    postfix_list = postfix_text.split()
    print(postfix_list)
    stack = []
    for char in postfix_list:
        if char not in priority:
            stack.append(int(char))
        else:
            operand1 = stack.pop()
            # print(operand1)
            operand2 = stack.pop()
            # print(operand2)
            stack.append(action(char, operand1, operand2))
    return stack[0]


example = '3 + 4 * ( 2 - 5 )'
print(infix_to_postfix(example))
print(my_calc(infix_to_postfix(example)))
