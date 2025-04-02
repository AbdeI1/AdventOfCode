import os
os.chdir(os.path.dirname(__file__))
from collections import defaultdict
from re import finditer, search


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  S = set()
  M = f[-1]
  for l in f[:-2]:
    b, e = l.split(' => ')
    for m in finditer(b, M):
      S.add(M[:m.start()] + e + M[m.end():])
  print(len(S))


def part2():
  f = reader()
  R = sorted((tuple(l.split(' => ')[::-1])
             for l in f[:-2]), key=lambda t: -len(t[0]))
  M = f[-1]
  A = 0
  while M != 'e':
    m, rr = next((search(r, M), rr) for r, rr in R if r in M)
    M = M[:m.start()] + rr + M[m.end():]
    A += 1
  print(A)


part1()
part2()
