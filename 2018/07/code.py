import os
os.chdir(os.path.dirname(__file__))
from heapq import heappop, heappush
from collections import defaultdict


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  G = defaultdict(list)
  Gr = defaultdict(int)
  for l in map(lambda x: x.split(), reader()):
    G[l[1]].append(l[7])
    Gr[l[7]] += 1
  Q = []
  V = set()
  s = ""
  for C in set(G) - set(Gr):
    heappush(Q, C)
  while Q:
    n = heappop(Q)
    if n in V:
      continue
    s += n
    V.add(n)
    for m in G[n]:
      Gr[m] -= 1
      if Gr[m] == 0:
        heappush(Q, m)
  print(s)


def part2():
  G = defaultdict(list)
  Gr = defaultdict(int)
  for l in map(lambda x: x.split(), reader()):
    G[l[1]].append(l[7])
    Gr[l[7]] += 1
  W = [0 for _ in range(5)]
  Wl = ['.' for _ in range(len(W))]
  Q = []
  s = ""
  T = 0
  for C in set(G) - set(Gr):
    heappush(Q, C)
  i = 0
  while max(W) > 0 or Q:
    for i in range(len(W)):
      if W[i] == 0:
        if Q:
          n = heappop(Q)
          W[i] = ord(n) - 4
          Wl[i] = n
        else:
          Wl[i] = '.'
    i = W.index(min(set(W) - {0}))
    t = W[i]
    T += t
    for j in range(len(W)):
      if W[j] > 0:
        W[j] -= t
    s += Wl[i]
    for m in G[Wl[i]]:
      Gr[m] -= 1
      if Gr[m] == 0:
        heappush(Q, m)
    Wl[i] = '.'
  print(T)


part1()
part2()
