import sys
import collections

def line_valid(line):
  words = line.split()
  seen = []
  for word in words:
    if word in seen:
      return False
    seen.append(word)
  return True

def main(argv):
  with open(argv[1], 'r') as infile:
    inputs = infile.read()
  lines = inputs.split("\n")
  valids = 0
  for line in lines:
    if line_valid(line):
      valids += 1
  print valids

main(sys.argv)
