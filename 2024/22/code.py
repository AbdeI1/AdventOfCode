import os
os.chdir(os.path.dirname(__file__))
from itertools import pairwise


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = list(map(int, reader()))
  M = 16777216
  c = 0
  for n in f:
    a = n
    for _ in range(2000):
      a = (a ^ (a * 64)) % M
      a = (a ^ int(a / 32)) % M
      a = (a ^ (a * 2048)) % M
    c += a
  print(c)


def part2():
  f = list(map(int, reader()))
  M = 16777216
  P = []
  for n in f:
    a = n
    P.append([a % 10])
    for _ in range(2000):
      a = (a ^ (a * 64)) % M
      a = (a ^ int(a / 32)) % M
      a = (a ^ (a * 2048)) % M
      P[-1].append(a % 10)
  D = [[p2 - p1 for p1, p2 in pairwise(p)] for p in P]
  G = {}
  for j in range(len(D)):
    d = D[j]
    for i in range(3, len(d)):
      w, x, y, z = d[i - 3:i + 1]
      if (w, x, y, z) not in G:
        G[(w, x, y, z)] = {}
      if j not in G[(w, x, y, z)]:
        G[(w, x, y, z)][j] = P[j][i + 1]
  m = max(sum(k.values()) for k in G.values())
  print(m)


part1()
part2()
