import os
os.chdir(os.path.dirname(__file__))
from collections import Counter
from itertools import combinations


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  print(len(list(filter(lambda l: 2 in set(Counter(l).values()), f)))
        * len(list(filter(lambda l: 3 in set(Counter(l).values()), f))))


def part2():
  f = reader()
  for s1, s2 in combinations(f, 2):
    s = set(enumerate(s1)) & set(enumerate(s2))
    if len(s) == len(s1) - 1:
      print(''.join([c for i, c in sorted(s)]))
      break


part1()
part2()
