import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def step(pos, vel):
  pos[0] += vel[0]
  pos[1] += vel[1]
  if vel[0] > 0:
    vel[0] -= 1
  elif vel[0] < 0:
    vel[0] += 1
  vel[1] -= 1


def inTarget(pos, tx, ty):
  return tx[0] <= pos[0] and pos[0] <= tx[1] and ty[0] <= pos[1] and pos[1] <= ty[1]


def part1():
  f = reader()
  xs = f[0][(f[0].index('x') + 2):(f[0].index(','))].split('..')
  ys = f[0][(f[0].index('y') + 2):].split('..')
  xs = list(map(int, xs))
  ys = list(map(int, ys))
  gm = -1
  for x in range(1, xs[1] + 1):
    for y in range(400):
      m = -1
      pos = [0, 0]
      vel = [x, y]
      while pos[1] > ys[1] and pos[0] < xs[1]:
        step(pos, vel)
        m = max(m, pos[1])
      if inTarget(pos, xs, ys):
        gm = max(gm, m)
  print(gm)


def part2():
  f = reader()
  xs = f[0][(f[0].index('x') + 2):(f[0].index(','))].split('..')
  ys = f[0][(f[0].index('y') + 2):].split('..')
  xs = list(map(int, xs))
  ys = list(map(int, ys))
  s = 0
  for x in range(17, xs[1] + 1):
    for y in range(ys[0], 400):
      pos = [0, 0]
      vel = [x, y]
      while pos[0] <= xs[1] and pos[1] >= ys[0]:
        step(pos, vel)
        if inTarget(pos, xs, ys):
          s += 1
          break
  print(s)


part1()
part2()
