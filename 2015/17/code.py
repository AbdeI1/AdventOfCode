import os
os.chdir(os.path.dirname(__file__))
from itertools import chain, combinations


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  N = list(map(int, reader()))
  print(len(list(s for s in chain.from_iterable(combinations(N, r)
        for r in range(len(N) + 1)) if sum(s) == 150)))


def part2():
  N = list(map(int, reader()))
  L = list(s for s in chain.from_iterable(combinations(N, r)
                                          for r in range(len(N) + 1)) if sum(s) == 150)
  L = list(filter(lambda l: len(l) == len(L[0]), L))
  print(len(L))


part1()
part2()
