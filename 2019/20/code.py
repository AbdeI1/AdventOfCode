import os
os.chdir(os.path.dirname(__file__))
from collections import defaultdict


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  M = reader()
  P = [(''.join(l for l in [M[i][j], M[i + 1][j], M[i][j + 1]] if l.isalpha()), (i, j)) for i in range(len(M) - 1)
       for j in range(len(M[i]) - 1) if M[i][j].isalpha() and (M[i + 1][j].isalpha() or M[i][j + 1].isalpha())]
  Pd = defaultdict(list)
  for p, c in P:
    Pd[p].append(c)

  def cd(i, j):
    d = 0
    while True:
      for k in range(-d, d + 1):
        for ii, jj in [(i + k, j + d - abs(k)), (i + k, j - d + abs(k))]:
          if ii in range(len(M)) and jj in range(len(M[ii])) and M[ii][jj] == '.':
            return (ii, jj)
      d += 1

  E = {}

  for l in Pd.values():
    if len(l) != 2:
      continue
    (x1, y1), (x2, y2) = l
    (cx1, cy1), (cx2, cy2) = cd(x1, y1), cd(x2, y2)
    E[(x1, y1) if abs(cx1 - x1) <= 1 and abs(cy1 - y1) <=
      1 else ((cx1 + x1) // 2, (cy1 + y1) // 2)] = (cx2, cy2)
    E[(x2, y2) if abs(cx2 - x2) <= 1 and abs(cy2 - y2) <=
      1 else ((cx2 + x2) // 2, (cy2 + y2) // 2)] = (cx1, cy1)

  S = cd(*Pd['AA'][0])
  F = cd(*Pd['ZZ'][0])
  D = [(1, 0), (-1, 0), (0, 1), (0, -1)]

  Q = [(0, S)]
  V = set()
  while Q:
    d, (i, j) = Q.pop(0)
    if (i, j) in E:
      i, j = E[(i, j)]
    if (i, j) in V:
      continue
    V.add((i, j))
    if M[i][j] != '.':
      continue
    if (i, j) == F:
      print(d)
      break
    for di, dj in D:
      Q.append((d + 1, (i + di, j + dj)))


def part2():
  M = reader()
  P = [(''.join(l for l in [M[i][j], M[i + 1][j], M[i][j + 1]] if l.isalpha()), (i, j)) for i in range(len(M) - 1)
       for j in range(len(M[i]) - 1) if M[i][j].isalpha() and (M[i + 1][j].isalpha() or M[i][j + 1].isalpha())]
  Pd = defaultdict(list)
  for p, c in P:
    Pd[p].append(c)

  def cd(i, j):
    d = 0
    while True:
      for k in range(-d, d + 1):
        for ii, jj in [(i + k, j + d - abs(k)), (i + k, j - d + abs(k))]:
          if ii in range(len(M)) and jj in range(len(M[ii])) and M[ii][jj] == '.':
            return (ii, jj)
      d += 1

  E = {}

  for l in Pd.values():
    if len(l) != 2:
      continue
    (x1, y1), (x2, y2) = l
    (cx1, cy1), (cx2, cy2) = cd(x1, y1), cd(x2, y2)
    E[(x1, y1) if abs(cx1 - x1) <= 1 and abs(cy1 - y1) <=
      1 else ((cx1 + x1) // 2, (cy1 + y1) // 2)] = (cx2, cy2)
    E[(x2, y2) if abs(cx2 - x2) <= 1 and abs(cy2 - y2) <=
      1 else ((cx2 + x2) // 2, (cy2 + y2) // 2)] = (cx1, cy1)

  S = cd(*Pd['AA'][0])
  F = cd(*Pd['ZZ'][0])
  D = [(1, 0), (-1, 0), (0, 1), (0, -1)]

  Q = [(0, S, 0)]
  V = set()
  while Q:
    d, (i, j), l = Q.pop(0)
    if (i, j) in E:
      if i == 1 or j == 1 or i == len(M) - 2 or j == len(M[i]) - 2:
        l -= 1
      else:
        l += 1
      if l >= 0:
        i, j = E[(i, j)]
    if ((i, j), l) in V:
      continue
    V.add(((i, j), l))
    if M[i][j] != '.':
      continue
    if (i, j) == F and l == 0:
      print(d)
      break
    for di, dj in D:
      Q.append((d + 1, (i + di, j + dj), l))


part1()
part2()
