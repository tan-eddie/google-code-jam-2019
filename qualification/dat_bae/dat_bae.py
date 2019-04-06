import sys

def test_store(bits):
  print(bits)
  sys.stdout.flush()
  return input()

# Positions must be a sorted list of 0-indexed positions of the broken workers.
def send_answer(positions):
  out = ""
  for position in positions:
    out += str(position) + " "
  print(out)
  sys.stdout.flush()

def generate_0_1_str(length, section_size):
  out = ""
  i = -1 # To handle the case where section_size > length.
  for i in range(length // section_size):
    out += str(i % 2) * section_size
  i += 1
  out += str(i % 2) * (length % section_size)
  return out

# Parse result1 to determine which sections the broken workers are in.
def get_broken_workers_by_section(result1, section_sizes):
  num_broken_workers_in_section = [0] * len(section_sizes)

  i = 0
  for section in range(len(section_sizes)):
    bit = section % 2
    for k in range(section_sizes[section]):
      if (i >= len(result1)) or (int(result1[i]) != bit):
        # Section ended early due to reaching end of result1 or non-matching bit.
        num_broken_workers_in_section[section] = section_sizes[section] - k
        break
      else:
        i += 1

  return num_broken_workers_in_section

# Get number of bits needed to represent numbers from 0 to num (inclusive (?))
def get_bits_needed_for_int(num):
  bits = 0
  max_for_bits = 1
  while (max_for_bits <= num):
    bits += 1
    max_for_bits = 2 * max_for_bits
  return bits

# Determine broken worker positions.
def get_broken_worker_positions(result2, section_sizes, num_broken_workers_in_section):
  section_ids = [int(''.join(x), 2) for x in zip(*result2)]
  broken_worker_positions = []
  i = 0
  virtual_offset = 0
  for section in range(len(section_sizes)):
    actual_section_size = section_sizes[section] - num_broken_workers_in_section[section]

    # For each section with broken workers, we want to find the worker IDs and find those that are missing.
    if num_broken_workers_in_section[section] > 0:
      full_section_ids = list(range(section_sizes[section]))
      missing_section_ids = [x + virtual_offset for x in full_section_ids if x not in section_ids[i:i+actual_section_size]]
      broken_worker_positions = broken_worker_positions + missing_section_ids
    
    i += actual_section_size
    virtual_offset += section_sizes[section]

  return broken_worker_positions

def process_test_case(num_workers, num_broken_workers, max_calls):
  # Step 1: Break down the workers into sections; each section having size of num_broken_workers.
  # Send a string of alternating 000...111...000... with each 0 or 1 section having num_broken_workers bits.
  section_sizes = [num_broken_workers] * (num_workers // num_broken_workers)
  if (num_workers % num_broken_workers != 0):
    section_sizes.append(num_workers % num_broken_workers)

  result1 = test_store(generate_0_1_str(num_workers, num_broken_workers)) # CALL 1

  # Parse result1 to determine which sections the broken workers are in.
  num_broken_workers_in_section = get_broken_workers_by_section(result1, section_sizes)

  # Step 1.5: Check if all broken workers were in one section. If yes, then we can send the answer and stop.
  if num_broken_workers in num_broken_workers_in_section:
    start_index = num_broken_workers * num_broken_workers_in_section.index(num_broken_workers)
    send_answer(list(range(start_index, start_index + num_broken_workers)))
    return

  # Step 2: Determine broken worker positions for each section.
  # We have 4 calls to test_store left (for test set 2).
  # Now we can treat each section independently.
  # Note that each section has max. 15 workers (test limit of max. 15 broken workers).
  # So we can uniquely ID each worker in a section using max. 4 calls, because we only need 4 bits to represent
  # ints from 0 to 15.
  bits_needed = get_bits_needed_for_int(num_broken_workers - 1) # 0-indexed worker IDs.

  result2 = []
  for bit_place in range(bits_needed-1, -1, -1):
    out = ""
    for section_size in section_sizes:
      out += generate_0_1_str(section_size, 2 ** bit_place) # ... 2nd bit -> 00001111, 1st bit -> 00110011, 0th bit -> 01010101

    result2.append(test_store(out)) # CALL 2 up to 5.

  broken_worker_positions = get_broken_worker_positions(result2, section_sizes, num_broken_workers_in_section)
  
  # Send the final answer.
  send_answer(broken_worker_positions)

def main():
  num_cases = int(input())
  for i in range(num_cases):
    parameters = [int(x) for x in input().split()]
    process_test_case(parameters[0], parameters[1], parameters[2])
    input() # Read and ignore the response (fingers crossed it was right!)

if __name__ == "__main__":
  main()
