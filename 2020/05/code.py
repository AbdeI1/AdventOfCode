import os
os.chdir(os.path.dirname(__file__))
from re import sub


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  print(max([int(sub(r'B|R', '1', sub(r'F|L', '0', s)), 2) for s in reader()]))


def part2():
  f = set([int(sub(r'B|R', '1', sub(r'F|L', '0', s)), 2) for s in reader()])
  print(list(set(range(min(f), max(f) + 1)) - f)[0])


part1()
part2()
