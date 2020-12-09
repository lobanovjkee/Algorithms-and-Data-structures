# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными), так и различаться.
import random

MIN_VALUE = 0
MAX_VALUE = 10
SIZE = 10
second_minimum = MAX_VALUE
second_minimum_index = 0  # Переменная для проверки при одинаковых минимальных элементах

array = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(SIZE)]
print(array)
minimum = MAX_VALUE + 1

for i in array:
    if i < minimum:
        minimum = i
print(f'Минимальный элемент {minimum}[{array.index(minimum)}]')

for i, item in enumerate(array):
    if i != array.index(minimum) and item < second_minimum:
        second_minimum = item
        second_minimum_index = i
print(f'Второй минимальный элемент {second_minimum}[{second_minimum_index}]')
