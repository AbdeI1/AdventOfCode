import os
os.chdir(os.path.dirname(__file__))
from functools import cache


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = [[c for c in s] for s in reader()]
  s = [(0, 1, 0, 0)]
  ids = {(0, 1): 0}
  v = set()
  al = [[]]
  while s:
    i, j, n, d = s.pop()
    if (i, j) in v:
      continue
    v.add((i, j))
    if f[i][j] in {'>', '<', 'v', '^'}:
      match f[i][j]:
        case '>':
          if (i, j + 1) in ids and d > 1:
            al[n].append((ids[(i, j + 1)], d + 1))
        case '<':
          if (i, j - 1) in ids and d > 1:
            al[n].append((ids[(i, j - 1)], d + 1))
        case 'v':
          if (i + 1, j) in ids and d > 1:
            al[n].append((ids[(i + 1, j)], d + 1))
        case '^':
          if (i - 1, j) in ids and d > 1:
            al[n].append((ids[(i - 1, j)], d + 1))
    else:
      c = 0
      for d1, d2 in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ii, jj = (i + d1, j + d2)
        if ii in range(len(f)) and jj in range(len(f[ii])) and f[ii][jj] in {'>', '<', 'v', '^'}:
          c += 1
      if c > 1:
        al[n].append((len(al), d))
        d = 0
        n = len(al)
        ids[(i, j)] = n
        al.append([])
      for d1, d2 in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ii, jj = (i + d1, j + d2)
        if (ii not in range(len(f)) or jj not in range(len(f[ii]))) and (i, j) not in ids:
          al[n].append((len(al), d))
          n = len(al)
          al.append([])
          ids[(i, j)] = n
    for d1, d2 in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
      ii, jj = (i + d1, j + d2)
      if ii in range(len(f)) and jj in range(len(f[ii])) and f[ii][jj] != '#':
        if f[ii][jj] in {'>', '<', 'v', '^'} and {'>': (0, -1), '<': (0, 1), 'v': (-1, 0), '^': (1, 0)}[f[ii][jj]] == (d1, d2):
          continue
        s.append((ii, jj, n, d + 1))

  def dist(a, b):
    if a == b:
      return 0
    return max([d + dist(n, b) for n, d in al[a]])

  print(dist(ids[(0, 1)], ids[(len(f) - 1, len(f[-1]) - 2)]))


def part2():
  f = [[c for c in s] for s in reader()]
  s = [(0, 1, 0, 0)]
  ids = {(0, 1): 0}
  v = set()
  al = [[]]
  while s:
    i, j, n, d = s.pop()
    if (i, j) in v:
      continue
    v.add((i, j))
    if f[i][j] in {'>', '<', 'v', '^'}:
      match f[i][j]:
        case '>':
          if (i, j + 1) in ids and d > 1:
            al[n].append((ids[(i, j + 1)], d + 1))
        case '<':
          if (i, j - 1) in ids and d > 1:
            al[n].append((ids[(i, j - 1)], d + 1))
        case 'v':
          if (i + 1, j) in ids and d > 1:
            al[n].append((ids[(i + 1, j)], d + 1))
        case '^':
          if (i - 1, j) in ids and d > 1:
            al[n].append((ids[(i - 1, j)], d + 1))
    else:
      c = 0
      for d1, d2 in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ii, jj = (i + d1, j + d2)
        if ii in range(len(f)) and jj in range(len(f[ii])) and f[ii][jj] in {'>', '<', 'v', '^'}:
          c += 1
      if c > 1:
        al[n].append((len(al), d))
        d = 0
        n = len(al)
        ids[(i, j)] = n
        al.append([])
      for d1, d2 in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ii, jj = (i + d1, j + d2)
        if (ii not in range(len(f)) or jj not in range(len(f[ii]))) and (i, j) not in ids:
          al[n].append((len(al), d))
          n = len(al)
          al.append([])
          ids[(i, j)] = n
    for d1, d2 in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
      ii, jj = (i + d1, j + d2)
      if ii in range(len(f)) and jj in range(len(f[ii])) and f[ii][jj] != '#':
        if f[ii][jj] in {'>', '<', 'v', '^'} and {'>': (0, -1), '<': (0, 1), 'v': (-1, 0), '^': (1, 0)}[f[ii][jj]] == (d1, d2):
          continue
        s.append((ii, jj, n, d + 1))

  al2 = [[] for l in al]
  for i, l in enumerate(al):
    for n, d in l:
      al2[i].append((n, d))
      al2[n].append((i, d))

  @cache
  def dist(a, b, v):
    if a == b:
      return 0
    return max([-float('inf')] + [d + dist(n, b, v | (1 << a)) for n, d in al2[a] if ((v & (1 << n)) == 0)])

  print(dist(ids[(0, 1)], ids[(len(f) - 1, len(f[-1]) - 2)], 0))


part1()
part2()
