# Определить, какое число в массиве встречается чаще всего.
import random

MIN_VALUE = 0
MAX_VALUE = 5
QUANTITY = 100

array = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(QUANTITY)]
max_dict = {}
for i in array:
    if i in max_dict:
        max_dict[i] += 1
    else:
        max_dict[i] = 1
# print(max_dict)
m = 0
n = 0
for i in max_dict:
    print(max_dict[i], end='|')
    if max_dict[i] >= m:
        m = max_dict[i]
        n = i

print(f'\n{n} - {m}')
