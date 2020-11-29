# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
def even_odd_rec(x):
    global even, odd
    if x // 10 == 0:
        if x % 2 == 0:
            even += 1
        else:
            odd += 1
        return f'Четных цифр {even}, нечетных цифр {odd}'

    n = x % 10
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
    return even_odd_rec(x // 10)


even = odd = 0
z = int(input('Введите натуральное число: '))
print(even_odd_rec(z))
