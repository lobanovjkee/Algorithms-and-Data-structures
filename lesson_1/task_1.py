# https://drive.google.com/file/d/1qcMrfRdUam6zyVPNnAIvJ3sfUv-U-ei8/view?usp=sharing
x = int(input('Введите целое трёхзначное число: '))
a = x // 100
b = x % 10
c = x // 10
c = c % 10

d = a + b + c
e = a * b * c

print(f'Сумма цифр числа {x} = {d} \nПроизведение цифр числа {x} = {e}')
