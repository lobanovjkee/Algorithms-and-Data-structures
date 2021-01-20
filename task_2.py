# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
import random

SIZE = 10


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    first = arr[:len(arr) // 2]
    second = arr[len(arr) // 2:]

    first = merge_sort(first)
    second = merge_sort(second)

    return merge(first, second)


def merge(left, right):
    result = []

    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            result.append(left[0])
            left.remove(left[0])
        else:
            result.append(right[0])
            right.remove(right[0])

    if len(left) == 0:
        result += right
    else:
        result += left

    return result


array = [random.random() * 49 for i in range(SIZE)]

print(f'{array} - исходный массив')
print(f'{merge_sort(array)} - отсортированный массив')
