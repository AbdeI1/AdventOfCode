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
  G = reader()
  h, w = len(G), len(G[0])
  V = {(i, j, 0) for i in range(h) for j in range(w) if G[i][j] == '#'}
  for _ in range(200):
    nV = set()
    for i, j, l in V:
      adj = []
      
      if i == 0:
        adj.append((h // 2 - 1, w // 2, l + 1))
      elif i == h // 2 + 1:
        adj.extend((h-1, k, l-1) for k in range(w))
      else:
        adj.append((i-1, j, l))
        
      if i == h-1:
        adj.append((h // 2 + 1, w // 2, l + 1))
      elif i == h // 2 - 1:
        adj.extend((0, k, l-1) for k in range(w))
      else:
        adj.append((i+1, j, l))
        
      if j == 0:
        adj.append((h // 2, w // 2 - 1, l + 1))
      elif j == w // 2 + 1:
        adj.extend((k, w-1, l-1) for k in range(h))
      else:
        adj.append((i, j-1, l))
        
      if j == w - 1:
        adj.append((h // 2, w // 2 + 1, l + 1))
      elif j == w // 2 - 1:
        adj.extend((k, 0, l-1) for k in range(h))
      else:
        adj.append((i, j+ 1, l))
      
      c = sum(1 for x, y, z in adj if (x, y, z) in V) in (1, 2)
      


part1()
part2()
