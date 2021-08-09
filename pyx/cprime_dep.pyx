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
