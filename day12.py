import sys

def merge_groups(groups):
  i = 0
  while i < len(groups):
    j = i + 1
    while j < len(groups):
      if groups[i].intersection(groups[j]):
        groups[i] = groups[i].union(groups[j])
        del groups[j]
      else:
        j += 1
    i += 1
  return groups

def insert_into_groups(groups, x, y):
  added = None
  for group in groups:
    if x in group:
      group.add(y)
      added = True
  if not added:
    groups.append(set([x, y]))
  return groups

def insert_line_into_groups(groups, node, connected):
  for c in connected:
    groups = insert_into_groups(groups, node, c)
    groups = merge_groups(groups)
  return groups

def get_group_containing(target, groups):
  for group in groups:
    if target in group:
      return group
  return None

def main(argv):
  with open(argv[1], 'r') as infile:
    inputs = infile.read().split("\n")
  groups = []
  for i in inputs:
    elems = i.split()
    if not elems:
      continue
    node = int(elems[0])
    connected = [int(e.replace(",", "")) for e in elems[2:]]
    groups = insert_line_into_groups(groups, node, connected)
  print len(get_group_containing(0, groups))
  s = 0
  for group in groups:
    s += len(group)
  print s
  print len(groups)

main(sys.argv)
