import os
os.chdir(os.path.dirname(__file__))
from itertools import combinations


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = [list(map(int, l.split())) for l in reader()]
  print(sum([max(r) - min(r) for r in f]))


def part2():
  f = [list(map(int, l.split())) for l in reader()]
  print(sum([(lambda t: t[0] // t[1] if t[0] > t[1] else t[1] // t[0])
             (next(
                 filter(
                     lambda t: t[1] % t[0] == 0 or t[0] % t[1] == 0,
                     combinations(r, 2)
                 )
             )
  ) for r in f]))


part1()
part2()
