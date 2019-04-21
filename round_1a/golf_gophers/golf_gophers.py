import sys
from functools import reduce

# Send num_blades = [B0, B1, ..., B17] for each windmill.
# Note that 2 <= B0, ... B17 <= 18
# Returns [b0, b1, ..., b17], the blade number (0-indexed) of the downward pointing blade.
def interact(num_blades):
  print(*num_blades)
  sys.stdout.flush()
  result = input().split()
  return [int(x) for x in result]

def golf_gophers(N, M):
  # Limits:
  # Test Set 1: N = 365, M = 100.
  # Test Set 2: N = 7, M = 10^6.
  # Each night we can form 19 equations.

  # Solution for worst-case (7 nights).
  # Each night, send next largest relatively prime number in below set (where gcd of set is 1)
  # to ALL windmills.
  # So each night j, we have:
  # b_i = m_i mod B_j, where num_gophers = sum(m_i) for 0 <= i <= 17.
  # Rearrange to get num_gophers mod B_j = sum(b_i) mod B_j.
  # Then use Chinese Remainder Theorem to find number of gophers.
  # Note that Chinese Remainder Theorem gives us a solution unique
  # mod product(relative_primes), so we need to choose the primes such that the product
  # is bigger than M = 10^6.
  relative_primes = [3, 5, 7, 11, 13, 16, 17]
  b_sum = []
  for B in relative_primes:
    result = interact([B] * 18)
    b_sum.append(sum(result))

  num_gophers = chinese_remainder(relative_primes, b_sum) 
  # Send solution
  print(num_gophers)
  sys.stdout.flush()

# From https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def main():
  params = input().split()
  num_cases = int(params[0])
  N = int(params[1]) # Number of nights per test case.
  M = int(params[2]) # Max. number of gophers.
  for i in range(num_cases):
    golf_gophers(N, M)
    result = int(input())
    if result == -1:
      # Wrong answer, so exit.
      return

if __name__ == "__main__":
  main()
