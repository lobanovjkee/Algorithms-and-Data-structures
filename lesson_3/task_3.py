# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

MIN_VALUE = 0
MAX_VALUE = 100
SIZE = 10

array = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(SIZE)]
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
array.remove(maximum)
array.remove(minimum)
if index_max > index_min:
    array.insert(index_min, maximum)
    array.insert(index_max, minimum)
else:
    array.insert(index_max, minimum)
    array.insert(index_min, maximum)

print(array)
print(f'Максимальный элемент - {maximum}\nМинимальный элемент - {minimum}')
