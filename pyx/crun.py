import cProfile
from cprime import count_primes

cProfile.run("count_primes(35)")


# OUTPUT FROM BENCHMARK
'''
61673363
         4 function calls in 3.208 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    3.208    3.208 <string>:1(<module>)
        1    0.000    0.000    3.208    3.208 {built-in method builtins.exec}
        1    3.208    3.208    3.208    3.208 {cprime.count_primes}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
