import os
os.chdir(os.path.dirname(__file__))
from itertools import chain, combinations


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  E = list(map(lambda s: tuple(s.split('-')), reader()))
  V = {e[0] for e in E} | {e[1] for e in E}
  G = {v: set() for v in V}
  for e in E:
    G[e[0]].add(e[1])
    G[e[1]].add(e[0])
  T = set()
  for v1 in G:
    for v2 in G[v1]:
      for v3 in G[v2]:
        if v3 in G[v1]:
          T.add(tuple(sorted([v1, v2, v3])))
  print(len(list(filter(lambda t: t[0][0] == 't' or t[1]
        [0] == 't' or t[2][0] == 't', T))))


def part2():
  E = list(map(lambda s: tuple(s.split('-')), reader()))
  V = {e[0] for e in E} | {e[1] for e in E}
  G = {v: set() for v in V}
  for e in E:
    G[e[0]].add(e[1])
    G[e[1]].add(e[0])
  L = set()
  for v in G:
    for ss in map(set, chain.from_iterable(combinations(
      G[v], r) for r in range(len(G[v]) + 1))):
      s = {v} | ss
      for v1 in s:
        for v2 in s:
          if v1 != v2 and v2 not in G[v1]:
            break
        else:
          continue
        break
      else:
        L.add(tuple(sorted(s)))
  print(','.join(list(sorted(L, key=lambda s: -len(s)))[0]))


part1()
part2()
