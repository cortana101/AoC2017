import sys
import math

def total_capacity(rn):
  # Returns the number of values that exist in a ring that is rn distance from 1.
  capacity = 8 * ((rn / 2) * (rn + 1) + (rn % 2) * (rn + 1) / 2) + 1
  return capacity

def get_ring(val):
  # Returns the ring number tha val must be in, basically solve rn for capacity given val.
  i = 1
  while val > total_capacity(i):
    i += 1
  return i

def get_axial_values(rn):
  # Retrns a tuple (e, n, w, s) of the axial values at a given ring. Axial values are the
  # values on the ring whose distance to 1 is exactly equal to the ring number. ie exactly the
  # values that are on the axies at the ring.
  e = rn + total_capacity(rn - 1)
  n = rn * 2 + e
  w = rn * 2 + n
  s = rn * 2 + w
  return e, n, w, s

def get_offset(val):
  rn = get_ring(val)  
  axvs = get_axial_values(rn)
  # Distance from axial value to the target value
  min_dist = math.fabs(axvs[0] - val)
  for axv in axvs[1:]:
    dist = math.fabs(axv - val)
    if dist < min_dist:
      min_dist = dist
  return int(rn + min_dist)

def main(argv):
  # Seems like the main approach is the mathematically work out, which "ring" the target number is
  # in, then find its distance from axes. The numbers on the axes are always R blocks from 1, where 
  # R is the ring number.
  for i in [12, 23, 1024, 368078]:
    print str(i) + " " + str(get_offset(i))

main(sys.argv)
