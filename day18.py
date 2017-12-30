import sys

def get_val(regs, val_literal):
  try:
    val = int(val_literal)
    return val
  except:
    if val_literal in regs:
      return regs[val_literal]
    else:
      return 0

def recover_freq(inputs, regs):
  i = 0
  print inputs
  last_sound = 0
  while True:
    inst = inputs[i]
    args = inst.split()
    target = args[1]
    if target not in regs:
      regs[target] = 0
    if len(args) == 3:
      val = get_val(regs, args[2])
    if inst.startswith("set"):
      regs[target] = val
    elif inst.startswith("add"):
      regs[target] += val
    elif inst.startswith("mul"):
      regs[target] *= val
    elif inst.startswith("mod"):
      regs[target] %= val
    elif inst.startswith("snd"):
      last_sound = regs[target]
    elif inst.startswith("rcv"):
      if regs[target]:
        return last_sound
    elif inst.startswith("jgz"):
      if regs[target] > 0:
        i += val
        continue
    else:
      raise Error
    i += 1


def main(argv):
  regs = {}
  with open(argv[1], "r") as handle:
    inputs = [s.strip() for s in handle.read().split("\n")]
  print recover_freq(inputs, regs)

main(sys.argv)

