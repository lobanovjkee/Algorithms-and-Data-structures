# Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
# 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля), т.к. именно в этих
# позициях первого массива стоят четные числа.
import random

MIN_VALUE = 0
MAX_VALUE = 100
QUANTITY = 10

array = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(QUANTITY)]
even_array = []
for i, item in enumerate(array):
    if item % 2 == 0:
        even_array.append(i)

print(f'Исходный массив - {array}\nИндексы четных элементов массива - {even_array}')
