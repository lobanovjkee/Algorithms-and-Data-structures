from collections import deque

hex_to_dec = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
              'D': 13, 'E': 14, 'F': 15}

dec_to_hex = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
              13: 'D', 14: 'E', 15: 'F'}


def hex_sum(a, b):
    a = deque(a.upper())
    b = deque(b.upper())
    for i in a:
        if i not in hex_to_dec:
            return 'Введите только числа шестнадцатиричной система счисления'
    for i in b:
        if i not in hex_to_dec:
            return 'Введите только числа шестнадцатиричной система счисления'
    result = deque()
    if len(a) > len(b):
        eggs = len(a)
    else:
        eggs = len(b)
    counter = 0
    i = 0
    while i < eggs:
        if len(a) != 0:
            x = a.pop()
            x = hex_to_dec[x]
        else:
            x = 0
        if len(b) != 0:
            y = b.pop()
            y = hex_to_dec[y]
        else:
            y = 0
        temp = x + y + counter
        counter = 0
        while temp >= 16:
            temp -= 16
            counter += 1
        result.appendleft(dec_to_hex[temp])
        i += 1
    return result


print('Введите 2 числа в шеснадцатиричной системе счисления для их сложения: ')
x = input('Введите первое число: ')
y = input('Введите второе число: ')
print(hex_sum(x, y))
