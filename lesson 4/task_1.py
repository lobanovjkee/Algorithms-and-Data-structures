import timeit
import cProfile
import math


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
    return array[-1]


print(timeit.timeit('prime_slow(2**0)', number=1, globals=globals()))  # 5.512999990742173e-06
print(timeit.timeit('prime_slow(2**1)', number=1, globals=globals()))  # 4.71900000320602e-06
print(timeit.timeit('prime_slow(2**2)', number=1, globals=globals()))  # 8.398000005627182e-06
print(timeit.timeit('prime_slow(2**3)', number=1, globals=globals()))  # 1.2337000001139131e-05
print(timeit.timeit('prime_slow(2**4)', number=1, globals=globals()))  # 4.506300000173269e-05
print(timeit.timeit('prime_slow(2**5)', number=1, globals=globals()))  # 9.083000000487118e-05
print(timeit.timeit('prime_slow(2**6)', number=1, globals=globals()))  # 0.00034246299999551866
print(timeit.timeit('prime_slow(2**7)', number=1, globals=globals()))  # 0.0012431319999990365
print(timeit.timeit('prime_slow(2**8)', number=1, globals=globals()))  # 0.003191821999990907
print(timeit.timeit('prime_slow(2**9)', number=1, globals=globals()))  # 0.010495851000001721
print(timeit.timeit('prime_slow(2**10)', number=1, globals=globals()))  # 0.040063185999997586
print(timeit.timeit('prime_slow(2**11)', number=1, globals=globals()))  # 0.13075546199999621
print(timeit.timeit('prime_slow(2**12)', number=1, globals=globals()))  # 0.5246515759999966
print(timeit.timeit('prime_slow(2**13)', number=1, globals=globals()))  # 2.053379313999997
cProfile.run('prime_slow(2**13)')
"""     92213 function calls in 5.680 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    5.665    5.665    5.680    5.680 1.py:6(prime_slow)
        1    0.000    0.000    5.680    5.680 <string>:1(<module>)
        1    0.000    0.000    5.680    5.680 {built-in method builtins.exec}
    84017    0.013    0.000    0.013    0.000 {built-in method builtins.len}
     8192    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""
print(timeit.timeit('prime_slow(2**14)', number=1, globals=globals()))  # 8.141807283999995
print(timeit.timeit('prime_slow(2**15)', number=1, globals=globals()))  # 32.25709891300001
cProfile.run('prime_slow(2**15)')
"""          418865 function calls in 110.199 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1  110.123  110.123  110.198  110.198 1.py:6(prime_slow)
        1    0.000    0.000  110.199  110.199 <string>:1(<module>)
        1    0.000    0.000  110.199  110.199 {built-in method builtins.exec}
   386093    0.063    0.000    0.063    0.000 {built-in method builtins.len}
    32768    0.013    0.000    0.013    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""
print(timeit.timeit('prime_slow(2**16)', number=1, globals=globals()))  # 129.30836898700002
cProfile.run('prime_slow(2**16)')
"""            887181 function calls in 468.289 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1  468.102  468.102  468.288  468.288 1.py:6(prime_slow)
        1    0.001    0.001  468.288  468.288 <string>:1(<module>)
        1    0.000    0.000  468.289  468.289 {built-in method builtins.exec}
   821641    0.143    0.000    0.143    0.000 {built-in method builtins.len}
    65536    0.042    0.000    0.042    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""
print(timeit.timeit('prime_slow(2**17)', number=1, globals=globals()))  # 530.756379348
print(timeit.timeit('prime_slow(2**18)', number=1, globals=globals()))  # 2104.9647049630003
print(timeit.timeit('prime_slow(2**19)', number=1, globals=globals()))  # 8400.967965877
print(timeit.timeit('prime_slow(2**20)', number=1, globals=globals()))  # 33596.984215657782
"""Делал 1 замер, потому что алгоритм получился слишком медленный и для 100 замеров ушло бы примерно 53 дня."""


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
    return array[-1]


print(timeit.timeit('prime_fast(2**0)', number=100, globals=globals()))  # 8.558999979868531e-05
print(timeit.timeit('prime_fast(2**1)', number=100, globals=globals()))  # 0.0004907789989374578
print(timeit.timeit('prime_fast(2**2)', number=100, globals=globals()))  # 0.0008297910026158206
print(timeit.timeit('prime_fast(2**3)', number=100, globals=globals()))  # 0.003426547998969909
print(timeit.timeit('prime_fast(2**4)', number=100, globals=globals()))  # 0.006953569001780124
print(timeit.timeit('prime_fast(2**5)', number=100, globals=globals()))  # 0.026168877000600332
print(timeit.timeit('prime_fast(2**6)', number=100, globals=globals()))  # 0.060051453998312354
print(timeit.timeit('prime_fast(2**7)', number=100, globals=globals()))  # 0.15562041500015766
print(timeit.timeit('prime_fast(2**8)', number=100, globals=globals()))  # 0.3770045650016982
print(timeit.timeit('prime_fast(2**9)', number=100, globals=globals()))  # 0.8102384359990538
print(timeit.timeit('prime_fast(2**10)', number=100, globals=globals()))  # 1.9470252219980466
print(timeit.timeit('prime_fast(2**11)', number=100, globals=globals()))  # 5.025789350998821
print(timeit.timeit('prime_fast(2**12)', number=100, globals=globals()))  # 12.19042905400056
print(timeit.timeit('prime_fast(2**13)', number=100, globals=globals()))  # 30.86421935600083
print(timeit.timeit('prime_fast(2**14)', number=100, globals=globals()))  # 76.17566047299988
print(timeit.timeit('prime_fast(2**15)', number=100, globals=globals()))  # 188.6322771209998
cProfile.run('prime_fast(2**15)')
"""            418865 function calls in 2.511 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    2.447    2.447    2.510    2.510 1.py:6(prime_fast)
        1    0.000    0.000    2.511    2.511 <string>:1(<module>)
        1    0.000    0.000    2.511    2.511 {built-in method builtins.exec}
   386093    0.058    0.000    0.058    0.000 {built-in method builtins.len}
    32768    0.005    0.000    0.005    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""
print(timeit.timeit('prime_fast(2**16)', number=100, globals=globals()))  # 491.39433880700017
print(timeit.timeit('prime_fast(2**17)', number=100, globals=globals()))  # 1278.278321900998
print(timeit.timeit('prime_fast(2**18)', number=100, globals=globals()))  # 3317.9590933819964
cProfile.run('prime_fast(2**18)')
"""      3943279 function calls in 46.266 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1   45.646   45.646   46.262   46.262 1.py:6(prime_fast)
        1    0.003    0.003   46.265   46.265 <string>:1(<module>)
        1    0.000    0.000   46.266   46.266 {built-in method builtins.exec}
  3681131    0.568    0.000    0.568    0.000 {built-in method builtins.len}
   262144    0.048    0.000    0.048    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""
print(timeit.timeit('prime_fast(2**19)', number=100, globals=globals()))  # 8203.409648888002
print(timeit.timeit('prime_fast(2**20)', number=100, globals=globals()))  # 20807.209826399992
cProfile.run('prime_fast(2**20)')
"""       17338627 function calls in 324.265 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1  321.563  321.563  324.254  324.254 1.py:6(prime_fast)
        1    0.011    0.011  324.265  324.265 <string>:1(<module>)
        1    0.000    0.000  324.265  324.265 {built-in method builtins.exec}
 16290047    2.491    0.000    2.491    0.000 {built-in method builtins.len}
  1048576    0.200    0.000    0.200    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""


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


print(timeit.timeit('sieve(2**0)', number=100, globals=globals()))  # 0.0001396100000192746
print(timeit.timeit('sieve(2**1)', number=100, globals=globals()))  # 0.00035088800001403797
print(timeit.timeit('sieve(2**2)', number=100, globals=globals()))  # 0.0005928030000177387
print(timeit.timeit('sieve(2**3)', number=100, globals=globals()))  # 0.0025378119999572846
print(timeit.timeit('sieve(2**4)', number=100, globals=globals()))  # 0.0020120880000149555
print(timeit.timeit('sieve(2**5)', number=100, globals=globals()))  # 0.004469399000015528
print(timeit.timeit('sieve(2**6)', number=100, globals=globals()))  # 0.009678479000001516
print(timeit.timeit('sieve(2**7)', number=100, globals=globals()))  # 0.0364676579999923
print(timeit.timeit('sieve(2**8)', number=100, globals=globals()))  # 0.07250016300002926
print(timeit.timeit('sieve(2**9)', number=100, globals=globals()))  # 0.15904368500002874
print(timeit.timeit('sieve(2**10)', number=100, globals=globals()))  # 0.32730351900005417
print(timeit.timeit('sieve(2**11)', number=100, globals=globals()))  # 0.734719956000049
print(timeit.timeit('sieve(2**12)', number=100, globals=globals()))  # 1.6039371609999762
print(timeit.timeit('sieve(2**13)', number=100, globals=globals()))  # 3.4899148900000228
print(timeit.timeit('sieve(2**14)', number=100, globals=globals()))  # 14.042919586000039
print(timeit.timeit('sieve(2**15)', number=100, globals=globals()))  # 32.40838812700002
cProfile.run('sieve(2**15)')
"""    418870 function calls in 0.595 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.058    0.058    0.058    0.058 1.py:12(<listcomp>)
        1    0.470    0.470    0.589    0.589 1.py:6(sieve)
        1    0.005    0.005    0.595    0.595 <string>:1(<module>)
        1    0.000    0.000    0.595    0.595 {built-in method builtins.exec}
   386093    0.057    0.000    0.057    0.000 {built-in method builtins.len}
        4    0.000    0.000    0.000    0.000 {built-in method math.log}
    32768    0.005    0.000    0.005    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""
print(timeit.timeit('sieve(2**16)', number=100, globals=globals()))  # 68.537813588
print(timeit.timeit('sieve(2**17)', number=100, globals=globals()))  # 144.053649177
print(timeit.timeit('sieve(2**18)', number=100, globals=globals()))  # 306.634830093
cProfile.run('sieve(2**18)')
"""        3943284 function calls in 5.363 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.523    0.523    0.523    0.523 1.py:12(<listcomp>)
        1    4.224    4.224    5.325    5.325 1.py:6(sieve)
        1    0.037    0.037    5.363    5.363 <string>:1(<module>)
        1    0.000    0.000    5.363    5.363 {built-in method builtins.exec}
  3681131    0.538    0.000    0.538    0.000 {built-in method builtins.len}
        4    0.000    0.000    0.000    0.000 {built-in method math.log}
   262144    0.039    0.000    0.039    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""
print(timeit.timeit('sieve(2**19)', number=100, globals=globals()))  # 640.0585276239999
print(timeit.timeit('sieve(2**20)', number=100, globals=globals()))  # 1355.275537991
cProfile.run('sieve(2**20)')
"""    17338632 function calls in 23.254 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    2.045    2.045    2.045    2.045 1.py:12(<listcomp>)
        1   18.431   18.431   23.111   23.111 1.py:6(sieve)
        1    0.143    0.143   23.254   23.254 <string>:1(<module>)
        1    0.000    0.000   23.254   23.254 {built-in method builtins.exec}
 16290047    2.462    0.000    2.462    0.000 {built-in method builtins.len}
        4    0.000    0.000    0.000    0.000 {built-in method math.log}
  1048576    0.173    0.000    0.173    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""

"""
Замеры timeit делал параллельно в google collab, потому что не расчитал со временем, поэтому время cProfile может отличаться.

У алгоритма prime_slow квадратная асимптотика O(n**2), потому что используются 2 вложенных цикла, 
так же как и у алгоритма prime_fast, но из-за оптимизации алгоритма он работает в среднем в 63 раза быстрее.
У алгоритма sieve линейная асимптотика O(n), так как при увеличении искомого числа в 2 раза время возрастает примерно в 2 раза.

Построил графики для наглядности.
https://docs.google.com/spreadsheets/d/1k50FcVeU6e-ugheAQPDT2VY_8bHH3RAPd_1Vr8ZgaAU/edit?usp=sharing
"""
