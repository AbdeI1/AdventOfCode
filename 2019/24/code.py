import os
os.chdir(os.path.dirname(__file__))
from functools import reduce
from operator import or_


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  G = reader()
  S = reduce(or_, (1 << (i*len(G[i]) + j) for i in range(len(G)) for j in range(len(G[i])) if G[i][j] == '#'))
  adj = {}
  for i in range(len(G)):
    for j in range(len(G[i])):
      n = i*len(G[i]) + j
      l = []
      if i > 0:
        l.append((i-1)*len(G[i]) + j)
      if i < len(G)-1:
        l.append((i+1)*len(G[i]) + j)
      if j > 0:
        l.append(i*len(G[i]) + j-1)
      if j < len(G[i])-1:
        l.append(i*len(G[i]) + j+1)
      adj[n] = l
  V = set()
  while True:
    if S in V:
      break
    V.add(S)
    S = sum(1 << n for n in adj if (S & (1 << n) and sum(1 for m in adj[n] if S & 1 << m) == 1) or (not (S & (1 << n)) and sum(1 for m in adj[n] if S & 1 << m) in (1, 2)))
  print(S)


def part2():
  pass


part1()
part2()
