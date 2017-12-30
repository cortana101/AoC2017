import sys

LIST_MAX = 255
ITERATIONS = 64

def get_wrapped_index(index):
  return index % (LIST_MAX + 1)

def densify(h):
  output = []
  for i in range(0, 255, 16):
    sublist = h[i:(i + 16)]
    val = sublist[0]
    for v in sublist[1:]:
      val ^= v
    output.append(val)
  print output
  return [hex(v)[2:] for v in output]

def main(argv):
  skip_size = 0
  current_index = 0
  with open(argv[1], 'r') as infile:
    inputs = infile.read()
  asci = [ord(c) for c in inputs] + [17, 31, 73, 47, 23]
  l = range(0, LIST_MAX + 1)
  for j in range(0, ITERATIONS):
    for move in asci:
      end_index = current_index + move
      if end_index > LIST_MAX:
        sublist = list(l[current_index:] + l[:get_wrapped_index(end_index)])
      else:
        sublist = list(l[current_index:end_index])
      for i, val in enumerate(sublist[::-1], current_index):
        l[get_wrapped_index(i)] = val
      current_index = get_wrapped_index(end_index + skip_size)
      skip_size += 1
  print l
  print "".join(densify(l))

main(sys.argv)

