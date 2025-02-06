import os
os.chdir(os.path.dirname(__file__))
import sys
sys.setrecursionlimit(10000)
from functools import cache


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = [tuple(range(int(c[2:]), int(c[2:]) + 1) if '..' not in c else range(int(c[2:c.index('..')]), int(c[c.index('..') + 2:]) + 1)
             for c in sorted(l.split(', '))) for l in reader()]
  Ymm = min(ry.start for _, ry in f)
  Ym = max(ry.stop for _, ry in f)

  B = {(x, y) for xr, yr in f for x in xr for y in yr}
  V = {}

  def flow(x, y):
    if (x, y) in V:
      return V[(x, y)]
    if (x, y) in B:
      return 0
    if y >= Ym:
      return -1
    d = flow(x, y + 1)
    if d == -1:
      V[(x, y)] = -1
      return -1
    l = x - 1
    while (l, y) not in B:
      V[(l, y)] = -1
      if flow(l, y + 1) != 0:
        break
      l -= 1
    r = x + 1
    while (r, y) not in B:
      V[(r, y)] = -1
      if flow(r, y + 1) != 0:
        break
      r += 1
    if (l, y) in B and (r, y) in B:
      for xx in range(l + 1, r):
        V[(xx, y)] = 0
      return 0
    V[(x, y)] = -1
    return -1

  flow(500, 0)
  print(len([y for _, y in V if y in range(Ymm, Ym + 1)]))


def part2():
  f = [tuple(range(int(c[2:]), int(c[2:]) + 1) if '..' not in c else range(int(c[2:c.index('..')]), int(c[c.index('..') + 2:]) + 1)
             for c in sorted(l.split(', '))) for l in reader()]
  Ymm = min(ry.start for _, ry in f)
  Ym = max(ry.stop for _, ry in f)

  B = {(x, y) for xr, yr in f for x in xr for y in yr}
  V = {}

  def flow(x, y):
    if (x, y) in V:
      return V[(x, y)]
    if (x, y) in B:
      return 0
    if y >= Ym:
      return -1
    d = flow(x, y + 1)
    if d == -1:
      V[(x, y)] = -1
      return -1
    l = x - 1
    while (l, y) not in B:
      V[(l, y)] = -1
      if flow(l, y + 1) != 0:
        break
      l -= 1
    r = x + 1
    while (r, y) not in B:
      V[(r, y)] = -1
      if flow(r, y + 1) != 0:
        break
      r += 1
    if (l, y) in B and (r, y) in B:
      for xx in range(l + 1, r):
        V[(xx, y)] = 0
      return 0
    V[(x, y)] = -1
    return -1

  flow(500, 0)
  print(len([y for x, y in V if V[(x, y)] == 0 and y in range(Ymm, Ym + 1)]))


part1()
part2()
