import os
os.chdir(os.path.dirname(__file__))
from itertools import chain
from collections import Counter


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  W, C = {}, {}
  for l in f:
    p = l.split(' -> ')
    c = []
    if len(p) > 1:
      p, c = p[0], p[1].split(', ')
    else:
      p = p[0]
    p, w = p.split(' (')
    w = int(w[:-1])
    W[p] = w
    C[p] = c
  print(next(iter(set(W) - set(chain(*C.values())))))


def part2():
  f = reader()
  W, C = {}, {}
  for l in f:
    p = l.split(' -> ')
    c = []
    if len(p) > 1:
      p, c = p[0], p[1].split(', ')
    else:
      p = p[0]
    p, w = p.split(' (')
    w = int(w[:-1])
    W[p] = w
    C[p] = c
  S = next(iter(set(W) - set(chain(*C.values()))))

  def dfs(n):
    if len(C[n]) == 0:
      return W[n]
    w = list(map(dfs, C[n]))
    if len(set(w)) > 1:
      (n1, _), (n2, _) = Counter(w).most_common()
      for i in range(len(w)):
        if w[i] == n2:
          print(W[C[n][i]] + (n1 - n2))
          w[i] = n1
    return W[n] + sum(w)

  dfs(S)


part1()
part2()
