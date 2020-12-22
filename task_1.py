from collections import deque

avg = 0
b = []
company_counter = int(input('Введите кол-во компаний: '))

for i in range(company_counter):
    name = input('Название компании: ')
    q1 = int(input('Прибыль за 1 квартал: '))
    q2 = int(input('Прибыль за 2 квартал: '))
    q3 = int(input('Прибыль за 3 квартал: '))
    q4 = int(input('Прибыль за 4 квартал: '))
    f = [name, q1, q2, q3, q4]
    c = deque(f)
    b.append(c)
    print('-' * 30)

for i in b:
    profit = 0
    for j in range(1, 5):
        profit += i[j]
        avg += i[j]
    i.append(profit)

avg = round(avg / company_counter)
print(f'Средняя прибыль для всех компаний {avg}')

less = []
more = []

for i in b:
    if i.pop() < avg:
        less.append(i.popleft())
    else:
        more.append(i.popleft())

print('Прибыль ниже среднего:')
for i in less:
    print(i, end=' ')

print('\nПрибыль выше среднего:')
for i in more:
    print(i, end=' ')
