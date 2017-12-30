import sys

DIVISOR = 2147483647

def generateB(prev):
  out = prev * 48271 % DIVISOR
  while out % 8:
    prev = out
    out = prev * 48271 % DIVISOR
  return out

def generateA(prev):
  out = prev * 16807 % DIVISOR
  while out % 4:
    prev = out
    out = prev * 16807 % DIVISOR
  return out

def get_binary(num):
  return "{0:b}".format(num)

def calc_matches(a_start, b_start, cycles):
  a = a_start
  b = b_start
  matches = 0
  i = 0
  while i < cycles:
    a = generateA(a)
    b = generateB(b)
    bin_a = get_binary(a)[-16:]
    bin_b = get_binary(b)[-16:]
    if bin_a == bin_b:
      matches += 1
      print matches
    i += 1
  print matches


def main(argv):
  calc_matches(512, 191, 5000000)


main(sys.argv)

