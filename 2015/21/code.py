import os
os.chdir(os.path.dirname(__file__))
from math import ceil
from itertools import combinations, product


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  hp = int(f[0].split()[-1])
  dmg = int(f[1].split()[-1])
  arm = int(f[2].split()[-1])
  php = 100
  W = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]
  A = [(0, 0, 0), (13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)]
  R = [(0, 0, 0), (25, 1, 0), (50, 2, 0), (100, 3, 0),
       (20, 0, 1), (40, 0, 2), (80, 0, 3)]
  L = list(product(W, A, [((0, 0, 0), (0, 0, 0))] + list(combinations(R, 2))))
  G = float('inf')
  for w, a, (r1, r2) in L:
    g, d, a = (sum(t[i] for t in (w, a, r1, r2)) for i in range(3))
    pd = max(1, d - arm)
    ed = max(1, dmg - a)
    if ceil(hp / pd) <= ceil(php / ed):
      G = min(G, g)
  print(G)


def part2():
  f = reader()
  hp = int(f[0].split()[-1])
  dmg = int(f[1].split()[-1])
  arm = int(f[2].split()[-1])
  php = 100
  W = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]
  A = [(0, 0, 0), (13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)]
  R = [(0, 0, 0), (25, 1, 0), (50, 2, 0), (100, 3, 0),
       (20, 0, 1), (40, 0, 2), (80, 0, 3)]
  L = list(product(W, A, [((0, 0, 0), (0, 0, 0))] + list(combinations(R, 2))))
  G = 0
  for w, a, (r1, r2) in L:
    g, d, a = (sum(t[i] for t in (w, a, r1, r2)) for i in range(3))
    pd = max(1, d - arm)
    ed = max(1, dmg - a)
    if ceil(hp / pd) > ceil(php / ed):
      G = max(G, g)
  print(G)


part1()
part2()
