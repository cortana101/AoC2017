import sys

def main(argv):
  with open(argv[1], 'r') as infile:
    inputs = infile.read()
  lines = inputs.split("\n")
  total = 0
  for line in lines:
    vals = [int(v) for v in line.split()]
    max_val = vals[0]
    min_val = vals[0]
    for val in vals:
      if val > max_val:
        max_val = val
      if val < min_val:
        min_val = val
    total += max_val - min_val
  print total

main(sys.argv)
