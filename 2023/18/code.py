import os
os.chdir(os.path.dirname(__file__))
from itertools import pairwise


def reader():
  return open(f"input.txt", 'r').read().splitlines()


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
  print(a + (p // 2) + 1)


def part2():
  f = [({'0': 'R', '1': 'D', '2': 'L', '3': 'U'}[c[-2]], int(c[2:-2], 16), int(c[2:-1], 16))
       for _, _, c in [s.split() for s in reader()]]
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
  print(a + (p // 2) + 1)


part1()
part2()
