import sys

STEP_SIZE = 324

def calc_zero(cycles):
  l = [0]
  curr_index = 0
  i = 1
  out = 0
  while i < cycles + 1:
    if not i % 100:
      print i
    jump = STEP_SIZE % i
    curr_index = curr_index + jump
    if curr_index >= i:
      curr_index -= i
    if curr_index == 0:
      out = i
    curr_index += 1
    i += 1
  return out
  

def main(argv):
  print calc_zero(50000000)
  return
  l = [0]
  curr_index = 0
  i = 1
  while i < 50000001:
    if not i % 100:
      print i
    jump = STEP_SIZE % len(l)
    curr_index = curr_index + jump
    if curr_index >= len(l):
      curr_index -= len(l)
    l.insert(curr_index + 1, i)
    curr_index += 1
    i += 1
  print l[:4]


main(sys.argv)

