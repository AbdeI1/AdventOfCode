import os
os.chdir(os.path.dirname(__file__))
from itertools import accumulate
from functools import reduce
from collections import Counter


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  print(Counter(accumulate(reader(), lambda d, r: (d + {'R': 1, 'L': -1}[r[0]] * int(r[1:])) % 100, initial=50))[0])


def part2():
  print(reduce(lambda d, r: ((d[0] + {'R': 1, 'L': -1}[r[0]] * int(r[1:])) % 100, d[1] + (int(r[1:]) + {'R': 1, 'L': -1}[r[0]] * d[0] % 100) // 100), reader(),initial=(50, 0))[1])


part1()
part2()
