import os
os.chdir(os.path.dirname(__file__))
from collections import defaultdict
from heapq import heappush, heappop
from sortedcontainers import SortedList


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  M = reader()
  S = next((i, j) for i in range(len(M))
           for j in range(len(M[i])) if M[i][j] == '@')
  D = [(1, 0), (-1, 0), (0, 1), (0, -1)]
  G = defaultdict(list)
  V = set()
  Q = [(S, '@', 0)]
  while Q:
    (i, j), p, d = Q.pop(0)
    if ((i, j), p) in V:
      continue
    V.add(((i, j), p))
    if M[i][j] == '#':
      continue
    if M[i][j].isalpha() and M[i][j] != p:
      G[p].append((M[i][j], d))
      p = M[i][j]
      d = 0
    for di, dj in D:
      Q.append(((i + di, j + dj), p, d + 1))
  L = len([x for x in G if x.islower()])
  Q = [(0, '@', set())]
  V = set()
  while Q:
    d, n, s = heappop(Q)
    if (n, ''.join(s)) in V:
      continue
    V.add((n, ''.join(s)))
    if n.isalpha():
      if n.islower():
        s = s | {n}
      else:
        if n.lower() not in s:
          continue
    if len(s) == L:
      print(d)
      break
    for o, od in G[n]:
      heappush(Q, (d + od, o, s))


def part2():
  M = list(map(list, reader()))
  sr, sc = next((i, j) for i in range(len(M))
                for j in range(len(M[i])) if M[i][j] == '@')
  P = [
    ['@', '#', '@'],
    ['#', '#', '#'],
    ['@', '#', '@'],
  ]
  for i in range(-1, 2):
    for j in range(-1, 2):
      M[sr + i][sc + j] = P[1 + i][1 + j]
  S = [(i, j) for i in range(len(M))
       for j in range(len(M[i])) if M[i][j] == '@']
  D = [(1, 0), (-1, 0), (0, 1), (0, -1)]
  G = [defaultdict(list) for _ in range(len(S))]
  for k in range(len(S)):
    V = set()
    Q = [(S[k], '@', 0)]
    while Q:
      (i, j), p, d = Q.pop(0)
      if ((i, j), p) in V:
        continue
      V.add(((i, j), p))
      if M[i][j] == '#':
        continue
      if M[i][j].isalpha() and M[i][j] != p:
        G[k][p].append((M[i][j], d))
        p = M[i][j]
        d = 0
      for di, dj in D:
        Q.append(((i + di, j + dj), p, d + 1))
  L = len([x for g in G for x in g if x.islower()])
  Q = SortedList([(0, ('@',) * len(S), set())])
  while Q:
    d, N, s = Q.pop(0)
    if (N, ''.join(s)) in V:
      continue
    V.add((N, ''.join(s)))
    if len(s) == L:
      print(d)
      break
    for i in range(len(S)):
      n = N[i]
      for o, od in G[i][n]:
        if o.isupper() and o.lower() not in s:
          continue
        l = list(N)
        l[i] = o
        Q.add((d + od, tuple(l), (s | {o}) if o.islower() else s))


part1()
part2()


# slow ~1 min
def original_part1():
  M = reader()
  S = next((i, j) for i in range(len(M))
           for j in range(len(M[i])) if M[i][j] == '@')
  L = len([(i, j) for i in range(len(M))
          for j in range(len(M[i])) if M[i][j].isalpha() and M[i][j].islower()])
  D = [(1, 0), (-1, 0), (0, 1), (0, -1)]
  Q = [(S, set(), 0)]
  V = set()
  while Q:
    (i, j), s, d = Q.pop(0)
    if ((i, j), ''.join(s)) in V:
      continue
    V.add(((i, j), ''.join(s)))
    if M[i][j] == '#':
      continue
    if M[i][j].isalpha():
      if M[i][j].islower():
        s = s | {M[i][j]}
      else:
        if M[i][j].lower() not in s:
          continue
    if len(s) == L:
      print(d)
      break
    for di, dj in D:
      Q.append(((i + di, j + dj), s, d + 1))
