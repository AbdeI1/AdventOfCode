import os
os.chdir(os.path.dirname(__file__))
from itertools import permutations, pairwise


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  M = reader()
  N = {int(n): {} for r in M for n in r if n.isdigit()}
  for n, D in N.items():
    (i, j) = next((i, j) for i, r in enumerate(M)
                  for j, c in enumerate(r) if c == f'{n}')
    Q = [(i, j, 0)]
    V = set()
    while Q:
      ii, jj, d = Q.pop(0)
      if (ii, jj) in V:
        continue
      V.add((ii, jj))
      if M[ii][jj] == '#':
        continue
      if M[ii][jj].isdigit():
        D[int(M[ii][jj])] = d
      for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        Q.append((ii + di, jj + dj, d + 1))
  G = [[N[i][j] for j in range(len(N))] for i in range(len(N))]
  print(min(sum(G[x][y] for x, y in pairwise((0, ) + p))
        for p in permutations(range(1, len(N)), len(N) - 1)))


def part2():
  M = reader()
  N = {int(n): {} for r in M for n in r if n.isdigit()}
  for n, D in N.items():
    (i, j) = next((i, j) for i, r in enumerate(M)
                  for j, c in enumerate(r) if c == f'{n}')
    Q = [(i, j, 0)]
    V = set()
    while Q:
      ii, jj, d = Q.pop(0)
      if (ii, jj) in V:
        continue
      V.add((ii, jj))
      if M[ii][jj] == '#':
        continue
      if M[ii][jj].isdigit():
        D[int(M[ii][jj])] = d
      for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        Q.append((ii + di, jj + dj, d + 1))
  G = [[N[i][j] for j in range(len(N))] for i in range(len(N))]
  print(min(sum(G[x][y] for x, y in pairwise((0, ) + p + (0, )))
        for p in permutations(range(1, len(N)), len(N) - 1)))


part1()
part2()
