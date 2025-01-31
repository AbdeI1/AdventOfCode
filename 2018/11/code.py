import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  n = int(reader()[0])
  G = [[int(f'{((x + 10) * y + n) * (x + 10):03}'[-3]) -
        5 for x in range(1, 301)] for y in range(1, 301)]
  Gp = [[0] * 301 for _ in range(301)]
  for y in range(1, 301):
    for x in range(1, 301):
      Gp[y][x] = Gp[y - 1][x] + Gp[y][x - 1] - \
        Gp[y - 1][x - 1] + G[y - 1][x - 1]
  m = -float('inf')
  r = (-1, -1)
  for y in range(1, 298):
    for x in range(1, 298):
      s = Gp[y + 3][x + 3] - Gp[y + 3][x] - Gp[y][x + 3] + Gp[y][x]
      if s > m:
        m = s
        r = (x + 1, y + 1)
  print(','.join(map(str, r)))


def part2():
  n = int(reader()[0])
  G = [[int(f'{((x + 10) * y + n) * (x + 10):03}'[-3]) -
        5 for x in range(1, 301)] for y in range(1, 301)]
  Gp = [[0] * 301 for _ in range(301)]
  for y in range(1, 301):
    for x in range(1, 301):
      Gp[y][x] = Gp[y - 1][x] + Gp[y][x - 1] - \
        Gp[y - 1][x - 1] + G[y - 1][x - 1]
  m = -float('inf')
  r = (-1, -1, -1)
  for y in range(1, 301):
    for x in range(1, 301):
      for s in range(1, 301 - max(x, y)):
        p = Gp[y + s][x + s] - Gp[y + s][x] - Gp[y][x + s] + Gp[y][x]
        if p > m:
          m = p
          r = (x + 1, y + 1, s)
  print(','.join(map(str, r)))


part1()
part2()
