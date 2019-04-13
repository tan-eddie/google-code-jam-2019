def alien_rhyme(words):
  # Store indices of words with the given rhyming suffix as key.
  rhyming_suffix = {}
  for i in range(len(words)):
    word = words[i]
    for j in range(len(word)):
      suffix = word[j:len(word)]
      if suffix in rhyming_suffix: 
        rhyming_suffix[suffix].append(i)
      else:
        rhyming_suffix[suffix] = [i]

  # Now remove all key value pairs that only have one index in the value
  # (nothing will rhyme with them).
  rhyming_suffix = {suffix: rhyming_suffix[suffix] for suffix in rhyming_suffix if len(rhyming_suffix[suffix]) > 1}

  pairs_formed = []
  for suffix in sorted(rhyming_suffix, key=len, reverse=True):
    # Remove any already formed pairs from this suffix.
    for pair in pairs_formed:
      for p in pair:
        if p in rhyming_suffix[suffix]:
          rhyming_suffix[suffix].remove(p)

    # Take one pair from each suffix (just take the first 2 for convenience)
    if len(rhyming_suffix[suffix]) >= 2:
      rhyming_suffix[suffix] = rhyming_suffix[suffix][0:2]
      pairs_formed.append(rhyming_suffix[suffix])
    else:
      # But if not enough, then we need to remove all possible pair candidates from this suffix.
      rhyming_suffix[suffix] = []

  # Now work out how many elements remain.
  count = 0
  for suffix in rhyming_suffix:
    count += len(rhyming_suffix[suffix])
  return count

def main():
  num_cases = int(input())
  for i in range(num_cases):
    num_words = int(input())
    words = []
    for n in range(num_words):
      words.append(input())
    result = alien_rhyme(words)
    print("Case #{:d}: {:d}".format(i+1, result))

if __name__ == "__main__":
  main()
