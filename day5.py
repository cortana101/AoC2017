import sys

def main(argv):
  with open(argv[1], 'r') as infile:
    inputs = infile.read()
  lines = [int(l) for l in inputs.split("\n")]
  ops = 0
  curr = 0
  while curr < len(lines) and curr >= 0:
    jump = lines[curr]
    if jump > 2:
      lines[curr] -= 1
    else:
      lines[curr] += 1
    curr += jump
    ops += 1
  print ops

main(sys.argv)
