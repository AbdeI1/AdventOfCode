import os
os.chdir(os.path.dirname(__file__))
from math import sqrt, floor
from collections import defaultdict


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  n = int(reader()[0])
  s = floor(sqrt(n - 1))
  s -= (1 - (s % 2))
  p = (s // 2 + 1, s // 2 + 1)
  d = n - (s * s)
  D = [(0, -1), (-1, 0), (0, 1), (1, 0)]
  for dx, dy in D:
    m = min(d, s + 1)
    p = p[0] + dx * m, p[1] + dy * m
    d -= m
    if d == 0:
      break
  print(sum(map(abs, p)))


def part2():
  n = int(reader()[0])
  V = defaultdict(int)
  px, py = (0, 0)
  dx, dy = (0, 0)
  V[(px, py)] = 1
  while V[(px, py)] < n:
    if px == py and px >= 0:
      px, py = px + 1, py + 1
      dx, dy = (0, -1)
    elif abs(px) == abs(py):
      dx, dy = dy, -dx
    px, py = px + dx, py + dy
    V[(px, py)] = sum([V[(px + i, py + j)]for i in range(-1, 2)
                       for j in range(-1, 2) if (i, j) != (0, 0)])
  print(V[(px, py)])


part1()
part2()
