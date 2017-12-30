import sys
import binascii
import collections

Coord = collections.namedtuple('Coord', ['col', 'row'])

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
  return [hex(v)[2:].zfill(2) for v in output]

def calc_hash(in_string):
  print in_string
  skip_size = 0
  current_index = 0
  asci = [ord(c) for c in in_string] + [17, 31, 73, 47, 23]
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
  return "".join(densify(l))

def hex_to_bin(h):
  output = ""
  for c in h:
    output += format(int(c, 16), "0=4b")
  return [int(i) for i in output]

def convert_to_blocks(hashed_string):
  output = hex_to_bin(hashed_string)
  actual = []
  for o in output:
    if o:
      actual.append(0)
    else:
      actual.append(None)
  return actual

def count_used(bin_hash):
  return bin_hash.count(0)

def get_next_region_index(array):
  for row_num, row in enumerate(array):
    for col_num, val in enumerate(row):
      if val == 0:
        return Coord(col_num, row_num)
  return None

def add_neighbour(target_coord, remainders, array):
  if target_coord not in remainders and array[target_coord.row][target_coord.col] == 0:
    remainders.append(target_coord)
  return remainders

def add_neighbours(coord, remainders, array):
  remainders = add_neighbour(coord, remainders, array)
  if coord.col > 0:
    left = Coord(coord.col - 1, coord.row)
    remainders = add_neighbour(left, remainders, array)
  if coord.row > 0:
    top = Coord(coord.col, coord.row - 1)
    remainders = add_neighbour(top, remainders, array)
  if coord.col < len(array[coord.row]) - 1:
    right = Coord(coord.col + 1, coord.row)
    remainders = add_neighbour(right, remainders, array)
  if coord.row < len(array) - 1:
    bottom = Coord(coord.col, coord.row + 1)
    remainders = add_neighbour(bottom, remainders, array)
  return remainders

def fill_one_region(array, region_counter, starting_coord):
  remainders = []
  remainders = add_neighbours(starting_coord, remainders, array)
  while remainders:
    coord = remainders[0]
    if array[coord.row][coord.col] == 0:
      array[coord.row][coord.col] = region_counter
      remainders = add_neighbours(coord, remainders, array)
    remainders.remove(coord)
  return array

def count_regions(array):
  region_counter = 1
  starting_coord = get_next_region_index(array)
  while starting_coord:
    array = fill_one_region(array, region_counter, starting_coord)
    starting_coord = get_next_region_index(array)
    region_counter += 1
  return array, region_counter

def main(argv):
  in_string = argv[1]
  total = 0
  array = []
  for i in range(0, 128):
    output = calc_hash(in_string + "-" + str(i))
    blocks = convert_to_blocks(output)
    array.append(blocks)
    used = count_used(blocks)
    total += used
  counted, tot = count_regions(array)
  retotal = 0
  for row in counted:
    print row
  print tot


main(sys.argv)

