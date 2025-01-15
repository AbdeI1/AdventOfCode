import os
os.chdir(os.path.dirname(__file__))
from itertools import accumulate


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  print(sum(map(int, reader())))


def part2():
  l = list(map(int, reader()))
  V = set()
  i = 0
  n = 0
  while True:
    if n in V:
      print(n)
      break
    V.add(n)
    n += l[i % len(l)]
    i += 1


part1()
part2()
