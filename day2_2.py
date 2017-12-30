import sys

def check_div(sorted_list):
  # List should be sorted odds + sorted evenss.
  for i, val in enumerate(sorted_list):
    for v2 in sorted_list[i + 1:]:
      if v2 % val == 0:
       return v2 / val
  print "Something is wrong we didn't find a divisor"
  return None # Should never happen

def main(argv):
  with open(argv[1], 'r') as infile:
    inputs = infile.read()
  lines = inputs.split("\n")
  total = 0
  for line in lines:
    vals = [int(v) for v in line.split()]
    evens = []
    odds = []
    for val in vals:
      if val % 2 == 0:
        evens.append(val)
      else:
        odds.append(val)
    sorted_vals = sorted(odds) + sorted(evens)
    total += check_div(sorted_vals)
  print total

main(sys.argv)
