import sys
import collections

def main(argv):
  wall = {}
  with open(argv[1], 'r') as infile:
    inputs = infile.read().split("\n")
  for i in inputs:
    line = i.split(":")
    wall[int(line[0])] = int(line[1].replace("\n", ""))
  delay = 0
  sev = 0
  while True:
    caught = False
    for layer in wall:
      if not (layer + delay) % ((wall[layer] - 1) * 2):
        # implies a catch
        sev += layer * wall[layer]
        caught = True
        break
    if not caught:
      print delay
      break
    delay += 1




main(sys.argv)

