import sys
import collections


def main(argv):
  depth = 0
  score = 0
  in_garbage = False
  ignored_char = False
  num_cancelled = 0
  with open(argv[1], 'r') as infile:
    inputs = infile.read()
  for c in inputs:
    if in_garbage:
      if ignored_char:
        ignored_char = False
      elif c == '!':
        ignored_char = True
      elif c == '>':
        in_garbage = False
      else:
        num_cancelled += 1
    elif c == '<':
      in_garbage = True
    elif c == '{':
      depth += 1
    elif c == '}':
      score += depth
      depth -= 1
  print score
  print num_cancelled

main(sys.argv)
