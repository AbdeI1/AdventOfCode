import os
os.chdir(os.path.dirname(__file__))
from itertools import accumulate


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  print(sum(map(lambda c: 1 if c == '(' else -1, reader()[0])))


def part2():
  print(list(accumulate(map(lambda c: 1 if c ==
        '(' else -1, reader()[0]), initial=0)).index(-1))


part1()
part2()
