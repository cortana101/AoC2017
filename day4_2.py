import sys
import collections

def is_anagram(wa, wb):
  if len(wa) != len(wb):
    return False
  wbc = [c for c in wb]
  for c in wa:
    if c not in wbc:
      return False
    wbc.remove(c)
  return len(wbc) == 0
       

def line_valid(line):
  words = line.split()
  seen = []
  for word in words:
    for seen_word in seen:
      if is_anagram(word, seen_word):
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
