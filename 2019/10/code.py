import os
os.chdir(os.path.dirname(__file__))
from math import atan2
from sortedcontainers import SortedDict


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  M = reader()
  L = {(i, j) for i in range(len(M))
       for j in range(len(M[i])) if M[i][j] == '#'}
  m = 0
  for i, j in L:
    S = set()
    for ii, jj in L:
      if (ii, jj) != (i, j):
        S.add(atan2(ii - i, jj - j))
    m = max(m, len(S))
  print(m)


def part2():
  M = reader()
  L = {(i, j) for i in range(len(M))
       for j in range(len(M[i])) if M[i][j] == '#'}
  m = 0
  l = -1, -1
  for i, j in L:
    S = set()
    for ii, jj in L:
      if (ii, jj) != (i, j):
        S.add(atan2(ii - i, jj - j))
    if len(S) > m:
      m = len(S)
      l = i, j
  i, j = l
  S = SortedDict()
  for ii, jj in L:
    if (ii, jj) != (i, j):
      a = atan2(j - jj, ii - i)
      if jj == j:
        a = -a
      if a not in S:
        S[a] = []
      S[a].append((jj, ii))
  A = S.values()
  x, y = A[199][0]
  print(x * 100 + y)


part1()
part2()
