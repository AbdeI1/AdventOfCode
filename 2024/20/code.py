import os
os.chdir(os.path.dirname(__file__))
from collections import defaultdict


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  G = reader()
  S = next((i, j) for i in range(len(G))
           for j in range(len(G[i])) if G[i][j] == 'S')
  E = next((i, j) for i in range(len(G))
           for j in range(len(G[i])) if G[i][j] == 'E')
  D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
  Dg = {(dx1 + dx2, dy1 + dy2) for dx1, dy1 in D for dx2, dy2 in D}
  De = {}
  q = [(E, 0)]
  while q:
    (i, j), d = q.pop(0)
    if (i, j) in De:
      continue
    De[(i, j)] = d
    for dx, dy in D:
      ii, jj = (i + dx, j + dy)
      if G[ii][jj] != '#':
        q.append(((ii, jj), d + 1))
  L = De[S]
  q = [(S, 0)]
  V = set()
  saves = defaultdict(lambda: 0)
  while q:
    (i, j), d = q.pop(0)
    if (i, j) in V:
      continue
    V.add((i, j))
    for dx, dy in Dg:
      ii, jj = (i + dx, j + dy)
      if ii in range(len(G)) and jj in range(len(G[ii])) and G[ii][jj] != '#':
        c = d + 2 + De[(ii, jj)]
        if c < L:
          saves[L - c] += 1
    for dx, dy in D:
      ii, jj = (i + dx, j + dy)
      if G[ii][jj] != '#':
        q.append(((ii, jj), d + 1))
  print(sum(map(lambda x: x[1] if x[0] >= 100 else 0, saves.items())))


def part2():
  G = reader()
  S = next((i, j) for i in range(len(G))
           for j in range(len(G[i])) if G[i][j] == 'S')
  E = next((i, j) for i in range(len(G))
           for j in range(len(G[i])) if G[i][j] == 'E')
  D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
  Dg = {(0, 0)}
  for _ in range(20):
    Dg |= {(dx1 + dx2, dy1 + dy2) for dx1, dy1 in Dg for dx2, dy2 in D}
  De = {}
  q = [(E, 0)]
  while q:
    (i, j), d = q.pop(0)
    if (i, j) in De:
      continue
    De[(i, j)] = d
    for dx, dy in D:
      ii, jj = (i + dx, j + dy)
      if G[ii][jj] != '#':
        q.append(((ii, jj), d + 1))
  L = De[S]
  q = [(S, 0)]
  V = set()
  saves = defaultdict(lambda: 0)
  while q:
    (i, j), d = q.pop(0)
    if (i, j) in V:
      continue
    V.add((i, j))
    for dx, dy in Dg:
      ii, jj = (i + dx, j + dy)
      if ii in range(len(G)) and jj in range(len(G[ii])) and G[ii][jj] != '#':
        c = d + abs(dx) + abs(dy) + De[(ii, jj)]
        if c < L:
          saves[L - c] += 1
    for dx, dy in D:
      ii, jj = (i + dx, j + dy)
      if G[ii][jj] != '#':
        q.append(((ii, jj), d + 1))
  print(sum(map(lambda x: x[1] if x[0] >= 100 else 0, saves.items())))


part1()
part2()
