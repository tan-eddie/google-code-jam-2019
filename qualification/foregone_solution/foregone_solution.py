# Split int n into two ints a and b which don't contain
# the digit 4, such that a+b=n.
# Assume that n has the digit 4.
def split_n(n):
  n_digits = str(n)
  a = 0
  b = 0

  # Iterate through each digit of n, halving if we encouter a 4.
  for i in range(len(n_digits)):
    place_value = 10 ** (len(n_digits) - i - 1)
    if n_digits[i] == "4":
      a += 2 * place_value
      b += 2 * place_value
    else:
      a += int(n_digits[i]) * place_value

  return (a, b)

def main():
  num_cases = int(input())
  for i in range(num_cases):
    n = int(input())
    a, b = split_n(n)
    print("Case #{:d}: {:d} {:d}".format(i+1, a, b))

if __name__ == "__main__":
  main()
