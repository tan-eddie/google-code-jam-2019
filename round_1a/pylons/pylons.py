# Return [] if IMPOSSIBLE.
# Else, return [(r0, c0), (r1, c1), ...] of the path.
def pylons(rows, cols):
  # Limits:
  # Test Set 1: 2 <= rows, cols <= 5.
  # Test Set 2: 2 <= rows, cols, <= 20.

  # Generate grid.
  grid = []
  for r in range(rows):
    for c in range(cols):
      grid.append((r, c))

  # Generate possible cells to visit from each cell.
  grid_paths = {}
  for r in range(rows):
    for c in range(cols):
      possible_cells = [x for x in grid if (x[0] != r) and (x[1] != c) and (x[0]-x[1] != r-c) and (x[0]+x[1] != r+c)]
      grid_paths[(r, c)] = possible_cells

  # Now work out the path...
  # This is a Hamiltonian path problem??

  # Start at cell with least number of jumps, and jump to next least number of jumps.
  least_jumps = 0
  path = []
  for cell in grid_paths:
    num_jumps = len(grid_paths[cell])
    if num_jumps == 0:
      return []
    elif least_jumps == 0 or num_jumps < least_jumps:
      least_jumps = num_jumps
      path = [cell]

  while len(path) < (rows * cols):
    # Choose the next jump.
    current_cell = path[-1]
    possible_jumps = [x for x in grid_paths[current_cell] if x not in path]
    if len(possible_jumps) == 0:
      # We stuck!
      return []
    else:
      least_jumps = 0 # placeholder.
      next_jump = (0, 0) # placeholder.
      for jump in possible_jumps:
        next_possible_paths = [x for x in grid_paths[jump] if x not in path]
        num_jumps = len(next_possible_paths)
        if least_jumps == 0 or num_jumps < least_jumps:
          least_jumps = num_jumps
          next_jump = jump

      # Make the jump
      path.append(next_jump)

  return path

def main():
  num_cases = int(input())
  for i in range(num_cases):
    params = input().split()
    rows = int(params[0])
    cols = int(params[1])
    result = pylons(rows, cols)
    if len(result) == 0:
      print("Case #{:d}: IMPOSSIBLE".format(i+1))
    else:
      print("Case #{:d}: POSSIBLE".format(i+1))
      for move in result:
        print("{:d} {:d}".format(move[0]+1, move[1]+1)) # 1-indexed rows and columns.

if __name__ == "__main__":
  main()