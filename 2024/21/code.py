import os
os.chdir(os.path.dirname(__file__))
from itertools import pairwise
from functools import cache


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def getPT(G, chars):
  P = {c: (i, j) for i, r in enumerate(G) for j, c in enumerate(r)}
  T = {c1: {c2: set() for c2 in chars} for c1 in chars}
  for c1 in T:
    for c2 in T[c1]:
      (x1, y1), (x2, y2) = P[c1], P[c2]
      v, vc = 'v' if x1 < x2 else '^', abs(x2 - x1)
      h, hc = '>' if y1 < y2 else '<', abs(y2 - y1)
      if G[x1][y2] in chars:
        T[c1][c2].add(h * hc + v * vc)
      if G[x2][y1] in chars:
        T[c1][c2].add(v * vc + h * hc)
  return P, T


def part1():
  f = reader()
  G0 = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['#', '0', 'A'],
  ]
  G1 = [
    ['#', '^', 'A'],
    ['<', 'v', '>']
  ]
  G2 = [
    ['#', '^', 'A'],
    ['<', 'v', '>']
  ]

  _, G0T = getPT(G0, '0123456789A')
  _, G1T = getPT(G1, '<^>vA')
  _, G2T = getPT(G2, '<^>vA')

  def r(T, s, i=0, c='A'):
    return [[t1] + t2 for t1 in T[c][s[i]] for t2 in r(T, s, i + 1, s[i])] if i < len(s) else [[]]

  ans = 0
  for s0 in f:
    l = float('inf')
    t0 = list(map(lambda l: 'A'.join(l) + 'A', r(G0T, s0)))
    for s1 in t0:
      t1 = list(map(lambda l: 'A'.join(l) + 'A', r(G1T, s1)))
      for s2 in t1:
        t2 = list(map(lambda l: 'A'.join(l) + 'A', r(G2T, s2)))
        for s3 in t2:
          l = min(l, len(s3))
    ans += l * int(s0[:-1])
  print(ans)


def part2():
  f = reader()
  G0 = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['#', '0', 'A'],
  ]
  GC = [
    ['#', '^', 'A'],
    ['<', 'v', '>']
  ]

  _, G0T = getPT(G0, '0123456789A')
  _, GCT = getPT(GC, '<^>vA')

  def r(T, s, i=0, c='A'):
    return [[t1] + t2 for t1 in T[c][s[i]] for t2 in r(T, s, i + 1, s[i])] if i < len(s) else [[]]

  @cache
  def count(c1, c2, M):
    return min(sum(count(cc1, cc2, M - 1)
                   for cc1, cc2 in pairwise('A' + t + 'A')) for t in GCT[c1][c2]) if M > 0 else 1

  ans = 0
  for s0 in f:
    l = min(sum(count(cc1, cc2, 25)
                for cc1, cc2 in pairwise('A' + t + 'A')) for t in map(lambda l: 'A'.join(l), r(G0T, s0)))
    ans += l * int(s0[:-1])
  print(ans)


part1()
part2()
