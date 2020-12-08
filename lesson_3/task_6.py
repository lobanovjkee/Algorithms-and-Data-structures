# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.
import random

MIN_VALUE = -25
MAX_VALUE = 100
QUANTITY = 10
j = 0

array = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(QUANTITY)]
print(array)
minimum = MAX_VALUE + 1
maximum = MIN_VALUE - 1

for i in array:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i

index_max = array.index(maximum)
index_min = array.index(minimum)

if index_max > index_min:
    for i in range(index_min + 1, index_max):
        j += array[i]
else:
    for i in range(index_max + 1, index_min):
        j += array[i]
print(f'Максимальный элемент - {maximum}, минимальный элемент - {minimum}')
print(f'Сумма между максимальным и минимальным элементами - {j}')
