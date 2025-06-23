import os
os.chdir(os.path.dirname(__file__))
from itertools import combinations
from math import prod


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = list(map(int, reader()))
  for x, y in combinations(f, 2):
    if x + y == 2020:
      print(x * y)
      break


def part2():
  f = list(map(int, reader()))
  for c in combinations(f, 3):
    if sum(c) == 2020:
      print(prod(c))
      break


part1()
part2()
