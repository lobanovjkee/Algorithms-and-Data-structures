# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве. Примечание к
# задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.
import random

MIN_VALUE = -10
MAX_VALUE = 10
QUANTITY = 10

array = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(QUANTITY)]
print(array)
negative_array = []
for i in array:
    if i < 0:
        negative_array.append(i)
j = MIN_VALUE - 1
for i in negative_array:
    if j < i:
        j = i
print(f'Максимальный минимальный элемент {j} с индексом {array.index(j)}')
