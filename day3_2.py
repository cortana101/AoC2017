import sys
import math

def get_capacity(rn):
  if rn == 0:
    return 1
  return 8 * rn

def main(argv):
  # Since the goal here is to get the first value that is larger, we don't really have a choice
  # but to keep producing the sum. We can try to iteratively fill in arrays and generate the value.

  # There seems to be special handling necessary for the corners, and the first value of each ring.
  rn = 2
  l = [1, 1, 2, 4, 5, 10, 11, 23, 25] # List of all values per index
  width = 4 # Width of current ring
  x = 0 # the "Side factor"
  w = 0 # index in current side
  while l[len(l) - 1] < 368078:
    i = len(l)
    v = l[i - 1]
    direct_neighbour = i - get_capacity(rn - 1) - 1 - x
    print "i: " + str(i) + " x: " + str(x) + " direct_neighbour: " + str(direct_neighbour)
    if w == (width - 1):
      v += l[direct_neighbour - 1]
      w = 0
      if x == 6:
        v += l[direct_neighbour]
        x = 0
        rn += 1
        width += 2
      else:
        x += 2
    elif w == (width - 2):
      v += l[direct_neighbour]
      v += l[direct_neighbour - 1]
      if x == 6:
        v += l[direct_neighbour + 1]
      w += 1
    elif w == 0:
      if x != 0:
        # In a new ring for sure
        v += l[direct_neighbour]
        v += l[i - 2]
      v += l[direct_neighbour + 1]
      w += 1
    elif w == 1 and x == 0:
      # Second element of a new ring
      v += l[i - 2]
      v += l[direct_neighbour]
      v += l[direct_neighbour + 1]
      w += 1
    else:
      # General case:
      v += l[direct_neighbour]
      v += l[direct_neighbour + 1]
      v += l[direct_neighbour - 1]
      w += 1
    l.append(v)

  print l 

main(sys.argv)
