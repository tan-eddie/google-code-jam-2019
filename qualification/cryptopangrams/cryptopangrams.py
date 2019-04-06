import math

# Insert element into a in a sorted fashion, but only if it doesn't
# already exist in the list.
def insort_unique(a, element):
  for i in range(len(a)):
    if element < a[i]:
      # Insert element into the list.
      a[i:i] = [element]
      return
    elif element == a[i]:
      return
  a.append(element)

# Ciphertext is list of int.
# The plaintext contains each English alphabet letter at least once.
def decrypt(prime_ceiling, ciphertext):
  # Store the found primes in this sorted list.
  # Should end up with 26 elements in this list (one for each char)
  # if all goes well.
  primes = []
  # Plaintext in prime number form.
  plaintext_primes = [0] * (len(ciphertext) + 1)

  # Find gcd of first two adjacent and unique ciphertext elements.
  found_first_prime = False
  for i in range(len(ciphertext) - 1):
    if (ciphertext[i] != ciphertext[i+1]):
      # Find the first prime!
      # ciphertext[i] = left_prime * right_prime
      # ciphertext[i+1] = right_prime * x
      right_prime = math.gcd(ciphertext[i], ciphertext[i+1])
      left_prime = ciphertext[i] // right_prime

      primes.append(left_prime)
      insort_unique(primes, right_prime)

      plaintext_primes[i] = left_prime
      plaintext_primes[i+1] = right_prime

      found_first_prime = True
      break

  if (found_first_prime):
    # Go forwards from i to find remaining primes.
    for j in range(i+1, len(ciphertext)):
      right_prime = ciphertext[j] // right_prime
      insort_unique(primes, right_prime)
      plaintext_primes[j+1] = right_prime

    # Go backwards from i to find remaining primes.
    for j in range(i-1, -1, -1):
      left_prime = ciphertext[j] // left_prime
      insort_unique(primes, left_prime)
      plaintext_primes[j] = left_prime

    # Match plaintext prime numbers to letters.
    plaintext = ""
    for plaintext_prime in plaintext_primes:
      plaintext += chr(ord('A') + primes.index(plaintext_prime))

    return plaintext

  else:
    # This shouldn't occur with the given assumptions.
    return ""

def main():
  num_cases = int(input())
  for i in range(num_cases):
    prime_ceiling = int(input().split()[0])
    ciphertext = [int(x) for x in input().split()]
    plaintext = decrypt(prime_ceiling, ciphertext)
    print("Case #{:d}: {:s}".format(i+1, plaintext))

if __name__ == "__main__":
  main()
