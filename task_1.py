# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
import random

SIZE = 10


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


array = [random.randint(-100, 99) for i in range(SIZE)]

print(f'{array} - исходный массив')
bubble_sort(array)
print(f'{array} - отсортированный массив')
