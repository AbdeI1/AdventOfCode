import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


D = {
  '^': (0, 1),
  'v': (0, -1),
  '<': (-1, 0),
  '>': (1, 0)
}


def part1():
  f = reader()[0]
  x, y = 0, 0
  V = {(x, y)}
  for c in f:
    dx, dy = D[c]
    x, y = x + dx, y + dy
    V.add((x, y))
  print(len(V))


def part2():
  f = reader()[0]
  P = [(0, 0), (0, 0)]
  V = set(P)
  for C in zip(f[::2], f[1::2]):
    P = [tuple(x + d for x, d in zip(p, D[c])) for p, c in zip(P, C)]
    V.update(P)
  print(len(V))


part1()
part2()
