import sys
import collections

Vector = collections.namedtuple('Vector', ['x', 'y', 'z'])
Particle = collections.namedtuple('Particle', ['num', 'p', 'v', 'a'])

def get_abs_accel(particle):
  return abs(particle.a.x) + abs(particle.a.y) + abs(particle.a.z)

def get_distance(particle):
  return particle.p.x + particle.p.y + particle.p.z

def parse_vector(vector_string):
  vector_string = vector_string.strip()
  vector_string = vector_string[3:-1]
  coords = vector_string.split(",")
  return Vector(x=int(coords[0]), y=int(coords[1]), z=int(coords[2]))

def parse_particles(inputs):
  particles = []
  for i, text in enumerate(inputs):
    args = text.split(", ")
    for arg in args:
      vector = parse_vector(arg)
      if arg.startswith("p"):
        pv = vector
      elif arg.startswith("v"):
        vv = vector
      elif arg.startswith("a"):
        av = vector
    particles.append(Particle(num=i, p=pv, v=vv, a=av))
  return particles

def move_particle_tick(particle):
  npvx = particle.v.x + particle.a.x 
  npvy = particle.v.y + particle.a.y
  npvz = particle.v.z + particle.a.z 
  nppx = particle.p.x + npvx 
  nppy = particle.p.y + npvy
  nppz = particle.p.z + npvz 
  return Particle(num=particle.num, p=Vector(x=nppx, y=nppy, z=nppz), v=Vector(x=npvx, y=npvy, z=npvz), a=particle.a)

def get_collissions(particles):
  collissions = set()
  for particle in particles:
    for particle2 in particles:
      if particle.p == particle2.p and particle.num != particle2.num:
        collissions.add(particle)
        collissions.add(particle2)
  return collissions

def run_tick(particles):
  i = 0
  while i < len(particles):
    particles[i] = move_particle_tick(particles[i])
    i += 1
  collissions = get_collissions(particles)
  for cp in collissions:
    particles.remove(cp)
  return particles

def main(argv):
  with open(argv[1], "r") as handle:
    inputs = handle.read().split("\n")
  particles = parse_particles(inputs)
  min_accel_particle = particles[0]
  min_accel = get_abs_accel(min_accel_particle)
  for particle in particles[1:]:
    abs_accel = get_abs_accel(particle)
    if abs_accel < min_accel:
      min_accel = abs_accel
      min_accel_particle = particle
  while True:
    particles = run_tick(particles)
    print len(particles)

main(sys.argv)

