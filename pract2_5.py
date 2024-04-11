examples = ['2 + (1-5)', '(2*[10-5] + (8-4))*(2-1)']


def naive(text):
    num_type1 = 0
    num_type2 = 0
    num_type3 = 0

    for char in text:
        if char == '(': num_type1 += 1
        elif char == '{': num_type2 += 1
        elif char == '[': num_type3 += 1

        if char == ')':
            if num_type1 == 0:
                return False
            else:
                num_type1 -= 1

        elif char == '}':
            if num_type2 == 0:
                return False
            else:
                num_type2 -= 1

        elif char == ']':
            if num_type3 == 0:
                return False
            else:
                num_type3 -= 1

    return num_type1 == 0 and num_type2 == 0 and num_type3 == 0


def check_with_stack(text):
    stack = []

    for char in text:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if len(stack) == 0:
                return False
            item = stack.pop()
            pair = item + char

            if pair not in ('()', '{}', '[]'):
                return False

    return len(stack) == 0


for example in examples:
    print(f'{example} - {check_with_stack(example)}')