# Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
from hashlib import sha256


def substring_counter(text):
    letters = list(text)
    substrings = []

    for letter in range(len(letters)):

        n = letter + 1
        spam = letters[letter]

        while n <= len(letters):
            if sha256(spam.encode('utf-8')).hexdigest() not in substrings and spam != text:
                substrings.append(sha256(spam.encode('utf-8')).hexdigest())
            if n == len(letters):
                break
            spam += letters[n]
            n += 1

    return len(substrings)


string = 'test'

print(substring_counter(string))
