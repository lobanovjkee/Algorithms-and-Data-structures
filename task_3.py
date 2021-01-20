#  Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
#  Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
import random

SIZE = int(input('Введите целое положительное число: '))


def gnome_sort(arr):
    i, size = 1, len(arr)

    while i < size:
        if arr[i - 1] <= arr[i]:
            i += 1
        else:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            if i > 1:
                i -= 1

    return arr


array = [random.randint(0, 100) for i in range(2 * SIZE + 1)]

print(f'{array} - исходный массив')
gnome_sort(array)
print(f'{array[len(array) // 2:][0]} - медиана')
