import sys
import math

DIAG = math.sqrt(3) / 2.0

def main(argv):
  x = 0.0
  y = 0.0
  with open(argv[1], 'r') as infile:
    inputs = [s.replace("\n", "") for s in infile.read().split(",")]
  furtherest = 0
  for i in range(0, len(inputs)):
    so_far = inputs[0:i]
    n = so_far.count("n")
    s = so_far.count("s")
    nw = so_far.count("nw")
    ne = so_far.count("ne") 
    sw = so_far.count("sw") 
    se = so_far.count("se")
    # Ending cell must be in this column
    ew_total = ne + se - nw - sw
    # diag_total here should be treated as half-moves vertically
    diag_total_vertical = (ne + nw - se - sw) / 2.0
    ns_total = n - s + diag_total_vertical
    total_possible_diag_vertical = abs(ew_total) * 0.5
    if abs(ns_total) < abs(total_possible_diag_vertical):
      # If there are no extra vertical movement, the steps is just the number of steps to get to the
      # correct vertical column
      movement = abs(ew_total)
    else:
      extra_ns = abs(ns_total) - abs(total_possible_diag_vertical)
      movement = abs(ew_total) + extra_ns
    if movement > furtherest:
      furtherest = movement
  print furtherest

main(sys.argv)

