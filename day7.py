import sys
import collections

Node = collections.namedtuple("Node", ['weight', 'children'])

def get_root(target_node, nodes):
  for node in nodes:
    if target_node in nodes[node].children:
      return node
  return None

def find_root(nodes):
  root = nodes.keys()[0]
  while True:
    rooter_node = get_root(root, nodes)
    if not rooter_node:
      break
    root = rooter_node
  return root

def get_total_weight(node, nodes):
  if not nodes[node].children:
    return nodes[node].weight
  total_weight = nodes[node].weight
  child_weights = collections.defaultdict(list)
  for child in nodes[node].children:
    child_weights[child] = get_total_weight(child, nodes)
    total_weight += child_weights[child]
  child_weights_unique = set(child_weights.values())
  if len(child_weights_unique) > 1:
    print "Uneven weights found: " + str(child_weights)
    print "Current node is: " + str(node)
  return total_weight

def main(argv):
  with open(argv[1], 'r') as infile:
    inputs = infile.read()
  lines = inputs.split("\n")
  nodes = collections.defaultdict(list)
  for line in lines:
    elems = [l.replace(",", "") for l in line.split()]
    weight = int(elems[1].replace("(", "").replace(")", ""))
    children = []
    if len(elems) > 3:
      children = elems[3:]
    nodes[elems[0]] = Node(weight, children)
  root = find_root(nodes)
  get_total_weight(root, nodes)

main(sys.argv)
