import os
os.chdir(os.path.dirname(__file__))
from collections import Counter


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  M = list(map(list, reader()))
  for _ in range(10):
    Mn = [['' for _ in range(len(M[i]))] for i in range(len(M))]
    for i, r in enumerate(M):
      for j, c in enumerate(r):
        a = Counter([M[i + di][j + dj] for di in range(-1, 2) for dj in range(-1, 2) if (di, dj) != (0, 0)
                     and i + di in range(len(M)) and j + dj in range(len(M[i + di]))])
        if c == '.' and a['|'] >= 3:
          Mn[i][j] = '|'
        elif c == '|' and a['#'] >= 3:
          Mn[i][j] = '#'
        elif c == '#' and not (a['#'] >= 1 and a['|'] >= 1):
          Mn[i][j] = '.'
        else:
          Mn[i][j] = c
    M = Mn
  C = sum(map(Counter, M), Counter())
  print(C['|'] * C['#'])


def part2():
  T = 1000000000
  M = list(map(list, reader()))
  L = [sum(map(Counter, M), Counter())]
  V = set()
  while True:
    Mn = [['' for _ in range(len(M[i]))] for i in range(len(M))]
    for i, r in enumerate(M):
      for j, c in enumerate(r):
        a = Counter([M[i + di][j + dj] for di in range(-1, 2) for dj in range(-1, 2) if (di, dj) != (0, 0)
                     and i + di in range(len(M)) and j + dj in range(len(M[i + di]))])
        if c == '.' and a['|'] >= 3:
          Mn[i][j] = '|'
        elif c == '|' and a['#'] >= 3:
          Mn[i][j] = '#'
        elif c == '#' and not (a['#'] >= 1 and a['|'] >= 1):
          Mn[i][j] = '.'
        else:
          Mn[i][j] = c
    M = Mn
    L.append(sum(map(Counter, M), Counter()))
    t = tuple(L[-2].items()), tuple(L[-1].items())
    if t in V:
      break
    V.add(t)
  s = L.index(L[-2])
  l = len(L) - s - 2
  C = L[T if T < s else s + ((T - s) % l)]
  print(C['|'] * C['#'])


part1()
part2()
