x = int(input('Введите целое положительное число: '))

if x % 400 == 0 or (x % 4 == 0 and x % 100 != 0):
    print('Год високосный')
else:
    print('Год не високосный')
