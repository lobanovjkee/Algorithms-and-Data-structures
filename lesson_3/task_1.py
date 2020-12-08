# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

START = 2
FINISH = 100

array = [_ for _ in range(START, FINISH)]
even_dict = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
for i in array:
    for j in even_dict:
        if i % j == 0:
            even_dict[j] += 1

for i in even_dict:
    print(f'Кратных {i} - {even_dict[i]}')
