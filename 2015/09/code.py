import os
os.chdir(os.path.dirname(__file__))
from collections import defaultdict
from itertools import permutations, pairwise


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = [(lambda t: (t[0], t[2], int(t[4])))(l.split()) for l in reader()]
  G = defaultdict(lambda: defaultdict(int))
  for n1, n2, d in f:
    G[n1][n2] = G[n2][n1] = d
  ans = float('inf')
  for p in permutations(G, len(G)):
    ans = min(ans, sum(G[n1][n2] for n1, n2 in pairwise(p)))
  print(ans)


def part2():
  f = [(lambda t: (t[0], t[2], int(t[4])))(l.split()) for l in reader()]
  G = defaultdict(lambda: defaultdict(int))
  for n1, n2, d in f:
    G[n1][n2] = G[n2][n1] = d
  ans = 0
  for p in permutations(G, len(G)):
    ans = max(ans, sum(G[n1][n2] for n1, n2 in pairwise(p)))
  print(ans)


part1()
part2()
