import os
os.chdir(os.path.dirname(__file__))
from sortedcontainers import SortedList
from itertools import chain
from math import lcm


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  P = [[int((n + '>')[n.find('=') + 1:n.find('>')]) for n in s.split(', ')]
       for s in reader()]
  A = [SortedList([(t[j], 0, i) for i, t in enumerate(P)]) for j in range(3)]

  for _ in range(1000):
    A = [
      SortedList([(p + v - L.bisect_left((p, -float('inf'), -1)) + len(L) - L.bisect_right((p, float('inf'), len(L))),
                   v - L.bisect_left((p, -float('inf'), -1)) + len(L) -
                   L.bisect_right((p, float('inf'), len(L))), i) for p, v, i in L])
      for L in A
    ]

  print(sum(sum(abs(p) if j == i else 0 for p, _, j in chain(*A)) * sum(abs(v)
        if j == i else 0 for _, v, j in chain(*A)) for i in range(len(P))))


def part2():
  P = [[int((n + '>')[n.find('=') + 1:n.find('>')]) for n in s.split(', ')]
       for s in reader()]
  A = [SortedList([(t[j], 0, i) for i, t in enumerate(P)]) for j in range(3)]
  a = 1
  for L in A:
    S = set()
    while tuple(L) not in S:
      S.add(tuple(L))
      L = SortedList([(p + v - L.bisect_left((p, -float('inf'), -1)) + len(L) - L.bisect_right((p, float('inf'), len(L))),
                       v - L.bisect_left((p, -float('inf'), -1)) + len(L) -
                       L.bisect_right((p, float('inf'), len(L))), i) for p, v, i in L])
    a = lcm(a, len(S))

  print(a)


part1()
part2()
