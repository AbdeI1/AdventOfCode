import pathlib
from itertools import pairwise
from functools import cache


def reader():
  return open(f"{pathlib.Path(__file__).parent.resolve()}/input.txt", 'r').read().split('\n')[:-1]


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

  def getPT(G, chars, banned):
    P = {c: (i, j) for i, r in enumerate(G) for j, c in enumerate(r)}
    T = {c1: {c2: [] for c2 in chars} for c1 in chars}
    for c1 in T:
      for c2 in T[c1]:
        x1, y1 = P[c1]
        x2, y2 = P[c2]
        v = 'v' if x1 < x2 else '^'
        h = '>' if y1 < y2 else '<'
        vc = abs(x2 - x1)
        hc = abs(y2 - y1)
        v * vc + h * hc
        q = [(vc, hc, '', x1, y1, 0)]
        while q:
          vcc, hcc, s, x, y, m = q.pop(0)
          if (x, y) in banned:
            continue
          if vcc == 0 or hcc == 0:
            m = 0
          if m >= 0 and vcc > 0:
            q.append((vcc - 1, hcc, s + v, x + (1 if x1 < x2 else -1), y, 1))
          if m <= 0 and hcc > 0:
            q.append((vcc, hcc - 1, s + h, x, y + (1 if y1 < y2 else -1), -1))
          if vcc == 0 and hcc == 0:
            T[c1][c2].append(s)
    return P, T

  G0P, G0T = getPT(G0, '0123456789A', {(3, 0)})
  G1P, G1T = getPT(G1, '<^>vA', {(0, 0)})
  G2P, G2T = getPT(G2, '<^>vA', {(0, 0)})

  def r(T, s, i, c):
    if i >= len(s):
      return [[]]
    return [[t1] + t2 for t1 in T[c][s[i]] for t2 in r(T, s, i + 1, s[i])]

  ans = 0
  for s0 in f:
    l = float('inf')
    t0 = list(map(lambda l: 'A'.join(l) + 'A', r(G0T, s0, 0, 'A')))
    for s1 in t0:
      t1 = list(map(lambda l: 'A'.join(l) + 'A', r(G1T, s1, 0, 'A')))
      for s2 in t1:
        t2 = list(map(lambda l: 'A'.join(l) + 'A', r(G2T, s2, 0, 'A')))
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

  def getPT(G, chars, banned):
    P = {c: (i, j) for i, r in enumerate(G) for j, c in enumerate(r)}
    T = {c1: {c2: [] for c2 in chars} for c1 in chars}
    for c1 in T:
      for c2 in T[c1]:
        x1, y1 = P[c1]
        x2, y2 = P[c2]
        v = 'v' if x1 < x2 else '^'
        h = '>' if y1 < y2 else '<'
        vc = abs(x2 - x1)
        hc = abs(y2 - y1)
        v * vc + h * hc
        q = [(vc, hc, '', x1, y1, 0)]
        while q:
          vcc, hcc, s, x, y, m = q.pop(0)
          if (x, y) in banned:
            continue
          if vcc == 0 or hcc == 0:
            m = 0
          if m >= 0 and vcc > 0:
            q.append((vcc - 1, hcc, s + v, x + (1 if x1 < x2 else -1), y, 1))
          if m <= 0 and hcc > 0:
            q.append((vcc, hcc - 1, s + h, x, y + (1 if y1 < y2 else -1), -1))
          if vcc == 0 and hcc == 0:
            T[c1][c2].append(s)
    return P, T

  G0P, G0T = getPT(G0, '0123456789A', {(3, 0)})
  GCP, GCT = getPT(GC, '<^>vA', {(0, 0)})

  def r(T, s, i, c):
    if i >= len(s):
      return [[]]
    return [[t1] + t2 for t1 in T[c][s[i]] for t2 in r(T, s, i + 1, s[i])]

  @cache
  def count(c1, c2, M):
    if M <= 0:
      return 1
    l = float('inf')
    for t in GCT[c1][c2]:
      l = min(l, sum(count(cc1, cc2, M - 1)
              for cc1, cc2 in pairwise('A' + t + 'A')))
    return l

  ans = 0
  for s0 in f:
    t0 = list(map(lambda l: 'A'.join(l) + 'A', r(G0T, s0, 0, 'A')))
    l = float('inf')
    for t in t0:
      l = min(l, sum(count(cc1, cc2, 25)
              for cc1, cc2 in pairwise('A' + t)))
    ans += l * int(s0[:-1])
  print(ans)


part1()
part2()
