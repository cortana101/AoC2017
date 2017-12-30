import sys
import collections

def process_condition(line, registers):
  key = line[4]
  op = line[5]
  val = int(line[6])
  if op == ">":
    return registers[key] > val
  elif op == "<":
    return registers[key] < val
  elif op == "<=":
    return registers[key] <= val
  elif op == ">=":
    return registers[key] >= val
  elif op == "==":
    return registers[key] == val
  else:
    return registers[key] != val

def get_modifier(line):
  if line[1] == 'inc':
    return int(line[2])
  else:
    return int(line[2]) * -1

def get_max(registers):
  biggest = 0
  biggest_v = registers[0]
  for v in registers:
    if registers[v] > biggest:
      biggest = registers[v]
      biggest_v = v
  return biggest, biggest_v


def main(argv):
  registers = collections.defaultdict(int)
  with open(argv[1], 'r') as infile:
    inputs = infile.read()
  lines = inputs.split("\n")
  for line in lines:
    key = line.split()[0]
    if key not in registers:
      registers[key] = 0
  highest_val = 0
  for line in lines:
    vals = line.split()
    modifier = get_modifier(vals)
    if process_condition(vals, registers):
      registers[vals[0]] += modifier
      if registers[vals[0]] > highest_val:
        highest_val = registers[vals[0]]
  print get_max(registers)
  print highest_val

main(sys.argv)
