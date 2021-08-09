import cProfile

def count_primes(max_num: int):
  '''this func counts prime numbers below the input value
  Input vals are in thousands, i.e. - 40 is 40,000'''

  count: int = 0
  for num in range(max_num * 1000 +1):
    if num > 1:
      for i in range(2, num):
        if num % i == 0:
          break
        else:
          count += 1

  print(count)
  return count

cProfile.run("count_primes(35)")

# OUTPUT FROM BENCHMARK
'''
61673363
         5 function calls in 5.576 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    5.576    5.576 <string>:1(<module>)
        1    5.576    5.576    5.576    5.576 prime_run.py:3(count_primes)
        1    0.000    0.000    5.576    5.576 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
