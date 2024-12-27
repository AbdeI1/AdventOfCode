import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


DIR = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}


def sign(x):
  if x == 0:
    return 0
  if x < 0:
    return -1
  return 1


def part1():
  f = reader()
  tailPos = set()
  ph = (0, 0)
  pt = (0, 0)
  tailPos.add(pt)
  for l in f:
    m = l.split()
    D = DIR[m[0]]
    for _ in range(int(m[1])):
      ph = (ph[0] + D[0], ph[1] + D[1])
      dx = ph[0] - pt[0]
      dy = ph[1] - pt[1]
      dt = (0, 0)
      if dx == 0 or dy == 0:
        dt = (sign(dx - sign(dx)), sign(dy - sign(dy)))
      elif abs(dx) > 1 or abs(dy) > 1:
        dt = (sign(dx), sign(dy))
      pt = (pt[0] + dt[0], pt[1] + dt[1])
      tailPos.add(pt)
  print(len(tailPos))


def part2():
  f = reader()
  tailPos = set()
  numKnots = 10
  p = [(0, 0) for _ in range(numKnots)]
  tailPos.add(p[-1])
  for l in f:
    m = l.split()
    D = DIR[m[0]]
    for _ in range(int(m[1])):
      p[0] = (p[0][0] + D[0], p[0][1] + D[1])
      for j in range(1, len(p)):
        dx = p[j - 1][0] - p[j][0]
        dy = p[j - 1][1] - p[j][1]
        dt = (0, 0)
        if dx == 0 or dy == 0:
          dt = (sign(dx - sign(dx)), sign(dy - sign(dy)))
        elif abs(dx) > 1 or abs(dy) > 1:
          dt = (sign(dx), sign(dy))
        p[j] = (p[j][0] + dt[0], p[j][1] + dt[1])
      tailPos.add(p[-1])
  print(len(tailPos))


part1()
part2()
