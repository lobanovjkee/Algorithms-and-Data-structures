# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
def printer(start, finish):
    while start <= finish:
        if start % 10 == 1:
            print(f'|{start} - {chr(start)}|')
        else:
            print(f'|{start} - {chr(start)}|', end=' ')
        start += 1


printer(32, 127)
