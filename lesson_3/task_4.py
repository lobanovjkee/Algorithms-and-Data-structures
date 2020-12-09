# Определить, какое число в массиве встречается чаще всего.
import random

MIN_VALUE = 0
MAX_VALUE = 10
QUANTITY = 1000
m = 0
n = 0

array = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(QUANTITY)]
print(array)
max_dict = {}
for i in array:
    if i in max_dict:
        max_dict[i] += 1
    else:
        max_dict[i] = 1

for i in max_dict:
    if max_dict[i] >= m:
        m = max_dict[i]
        n = i

del max_dict[n]
temp = [[n, m]]

for i in max_dict:
    if max_dict[i] == m:
        temp.append([i, m])

for i in temp:
    if 2 <= i[1] % 10 <= 4 and (i[1] % 100 < 10 or i[1] % 100 > 20):
        print(f'Чаще всего встречаются число {i[0]}, {i[1]} раза')
    else:
        print(f'Чаще всего встречаются число {i[0]}, {i[1]} раз')
