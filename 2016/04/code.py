import os
os.chdir(os.path.dirname(__file__))
from collections import Counter


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = [(lambda t: Counter(t[0].replace('-', '')).most_common(5))(l.rpartition('-'))
       for l in reader()]
  print(f)


def part2():
  pass


part1()
part2()
