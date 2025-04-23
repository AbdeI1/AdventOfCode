import os
os.chdir(os.path.dirname(__file__))
from itertools import groupby


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  s = reader()[0]
  for _ in range(40):
    s = ''.join(f'{len(list(i))}{c}' for c, i in groupby(s))
  print(len(s))


def part2():
  s = reader()[0]
  for _ in range(50):
    s = ''.join(f'{len(list(i))}{c}' for c, i in groupby(s))
  print(len(s))


part1()
part2()
