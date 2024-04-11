examples = ['((0', '()[]{}']


def naive(text):
    num_type1 = 0
    num_type2 = 0
    num_type3 = 0

    for char in text:
        if char == '(':
            num_type1 += 1
        elif char == '{':
            num_type1 += 1
        elif char == '[':
            num_type1 += 1

        if char == ')':
            if num_type1 == 0:
                return False
            else:
                num_type1 -= 1
        if char == '}':
            if num_type1 == 0:
                return False
            else:
                num_type1 -= 1
        if char == ']':
            if num_type1 == 0:
                return False
            else:
                num_type1 -= 1
    return num_type1 == 0 and num_type2 == 0 and num_type3 == 0
