first = ord(input('Введите первую английскую букву от a до z: '))
second = ord(input('Введите вторую английскую букву от a до z: '))

first = first - ord('a') + 1
second = second - ord('a') + 1

diff = first - second

print(
    f'Позиция первой буквы {first},\nПозиция второй буквы {second}'
    f'\nРастояние между этими буквами равно {abs(diff)}')
