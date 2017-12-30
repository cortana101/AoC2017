import sys


def do_spin(spin_index, l):
  out = l[-spin_index:] + l[:len(l) - spin_index]
  return out

def do_swap(indicies, l):
  tmp = l[indicies[0]]
  l[indicies[0]] = l[indicies[1]]
  l[indicies[1]] = tmp
  return l

def do_swap_chars(chars, l):
  indicies = []
  indicies.append(l.index(chars[0]))
  indicies.append(l.index(chars[1]))
  return do_swap(indicies, l)

def dance(action, l):
  if action[0] == "s":
    spin_index = int(action[1:])
    l = do_spin(spin_index, l)
  elif action[0] == "x":
    indicies = [int(a) for a in action[1:].split("/")]
    l = do_swap(indicies, l)
  elif action[0] == "p":
    chars = action[1:].split("/")
    l = do_swap_chars(chars, l)
  else:
    raise Error("Unknown action " + action)
  return l

def dance_with_moves(actions, l):
  for action in actions:
    l = dance(action, l)
  return l

def main(argv):
  orig = [chr(i) for i in range(97, 113)]
  l = list(orig)
  with open(argv[1], "r") as handle:
    inputs = handle.read().split(",")
  i = 0
  cycle = 0
  while True:
    i += 1
    l = dance_with_moves(inputs, l)
    if l == orig:
      cycle = i
      break
  extras = 1000000000 % cycle
  i = 0
  while i < extras:
    i += 1
    l = dance_with_moves(inputs, l)
  print "".join(l)


main(sys.argv)

