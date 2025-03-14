import os
os.chdir(os.path.dirname(__file__))
from collections import defaultdict


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  I = {(i - len(f) // 2, j - len(f[i]) // 2) for i, r in enumerate(f)
       for j, c in enumerate(r) if c == '#'}
  i, j, = (0, 0)
  di, dj = (-1, 0)
  c = 0
  for _ in range(10000):
    if (i, j) in I:
      di, dj = dj, -di
      I.remove((i, j))
    else:
      di, dj = -dj, di
      I.add((i, j))
      c += 1
    i, j = i + di, j + dj
  print(c)


def part2():
  f = reader()
  I = defaultdict(lambda: 'C', {(i - len(f) // 2, j - len(f[i]) // 2): 'I' for i, r in enumerate(f)
                                for j, c in enumerate(r) if c == '#'})
  i, j, = (0, 0)
  di, dj = (-1, 0)
  c = 0
  for _ in range(10000000):
    match I[(i, j)]:
      case 'C':
        di, dj = -dj, di
        I[(i, j)] = 'W'
      case 'W':
        c += 1
        I[(i, j)] = 'I'
      case 'I':
        di, dj = dj, -di
        I[(i, j)] = 'F'
      case 'F':
        di, dj = -di, -dj
        I[(i, j)] = 'C'
    i, j = i + di, j + dj
  print(c)


part1()
part2()
