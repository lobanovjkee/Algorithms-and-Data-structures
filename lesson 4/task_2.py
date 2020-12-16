import math


def prime(n):
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
    return array[-1]


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
    return array[-1]


print(prime(10000))
print(sieve(10000))
