import sys
import math


def sizeof(*args):
    _sum = 0
    for i in args:
        _sum += sys.getsizeof(i)
    return _sum


def prime_slow(n):
    array = []
    u = 2
    while len(array) < n:
        for i in range(u, u + 1):
            for j in array:
                if i % j == 0:
                    break
            else:
                array.append(i)
        u += 1
    return array[-1], sizeof(n, array, u, i, j, array[-1])


def prime_fast(n):
    array = []
    u = 2
    while len(array) < n:
        for i in range(u, u + 1):
            if (i > 10) and (i % 10 == 5):
                continue
            for j in array:
                if j ** 2 - 1 > i:
                    array.append(i)
                    break
                if i % j == 0:
                    break
            else:
                array.append(i)
        u += 1
    return array[-1], sizeof(n, array, u, i, j, array[-1])


def sieve(n):
    array = []
    k = n * 3
    while k / math.log(k) <= n:
        k += k
    end = k
    a = [i for i in range(0, end)]
    a[1] = 0
    u = 2
    while len(array) < n:
        if a[u] != 0:
            array.append(a[u])
            for j in range(a[u], end, a[u]):
                a[j] = 0
        u += 1
    return array[-1], sizeof(n, array, u, k, end, a, j, array[-1])


print(prime_slow(2)[1])  # 114
print(prime_slow(4)[1])  # 114
print(prime_slow(8)[1])  # 130
print(prime_slow(16)[1])  # 162
print(prime_slow(32)[1])  # 238
print(prime_slow(64)[1])  # 386
print(prime_slow(128)[1])  # 690
print(prime_slow(256)[1])  # 1174
print(prime_slow(512)[1])  # 2202
print(prime_slow(1024)[1])  # 4578

print('*' * 30)

print(prime_fast(2)[1])  # 114
print(prime_fast(4)[1])  # 114
print(prime_fast(8)[1])  # 130
print(prime_fast(16)[1])  # 162
print(prime_fast(32)[1])  # 238
print(prime_fast(64)[1])  # 386
print(prime_fast(128)[1])  # 690
print(prime_fast(256)[1])  # 1174
print(prime_fast(512)[1])  # 2202
print(prime_fast(1024)[1])  # 4578

print('*' * 30)

print(sieve(2)[1])  # 188
print(sieve(4)[1])  # 220
print(sieve(8)[1])  # 404
print(sieve(16)[1])  # 628
print(sieve(32)[1])  # 1084
print(sieve(64)[1])  # 2048
print(sieve(128)[1])  # 7204
print(sieve(256)[1])  # 14552
print(sieve(512)[1])  # 29496
print(sieve(1024)[1])  # 53900

"""
ОС Windows 10 x64
Python 3.8.3 x32

Программы prime_slow и prime_fast используют идентичное количество памяти, но меньше, чем программа sieve.
Поэтому если имеются ограничения по памяти на машине, которая выполняет программы, то разумнее будет использовать prime_slow или prime_fast,
но лучше prime_fast, так как она более оптимизирована и работает быстрее.
"""
