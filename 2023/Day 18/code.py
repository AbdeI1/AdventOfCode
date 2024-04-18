import pathlib
from itertools import pairwise


def reader():
  f = open(f"{pathlib.Path(__file__).parent.resolve()}/sample.txt", 'r').read()
  f = f.split('\n')
  f = f[:-1]
  return f


def part1():
  f = [(d, int(n), int(c[2:-1], 16))
       for d, n, c in [s.split() for s in reader()]]
  p = sum([n for _, n, _ in f])
  x, y = 0, 0
  coords = [(x, y)]
  for d, n, _ in f:
    match d:
      case 'R':
        x += n
      case 'L':
        x -= n
      case 'D':
        y -= n
      case 'U':
        y += n
    coords.append((x, y))
  a = 0
  for p1, p2 in pairwise(coords):
    a += (p1[0] * p2[1] - p2[0] * p1[1])
  a = abs(a) // 2
  print(a)
  print(p)
  print(coords)


def part2():
  f = reader()


part1()
part2()
