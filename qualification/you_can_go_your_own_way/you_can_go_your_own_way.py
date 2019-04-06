# Find a path through n-by-n grid from
# NW corner to SE corner, avoiding using
# any of the moves in avoid_path.
# Possible moves are S (move one cell south)
# and E (move one cell east).
# Returns a length 2*n-2 string of moves (S and E chars).
def find_path(avoid_path):
  # Let's just flip avoid_path (turn S into E and E into S).
  new_path = ""
  for i in range(len(avoid_path)):
    if (avoid_path[i] == "S"):
      new_path += "E"
    else:
      new_path += "S"
  return new_path

def main():
  num_cases = int(input())
  for i in range(num_cases):
    n = int(input()) # unusued.
    avoid_path = str(input())
    solution = find_path(avoid_path) 
    print("Case #{:d}: {:s}".format(i+1, solution))

if __name__ == "__main__":
  main()
  