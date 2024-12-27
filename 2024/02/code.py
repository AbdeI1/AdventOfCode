import os
os.chdir(os.path.dirname(__file__))
from itertools import pairwise


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def check(l):
  return all(abs(n1 - n2) in range(1, 4) for n1, n2 in pairwise(l)) and len(set((n1 - n2) / abs(n1 - n2) for n1, n2 in pairwise(l))) == 1 and l[1] - l[0] != 0


def part1():
  print(sum(check(list(map(int, l.split()))) for l in reader()))


def part2():
  print(sum(check(n) or any(check(n[:i] + n[i + 1:]) for i in range(len(n)))
        for n in [list(map(int, l.split())) for l in reader()]))


part1()
part2()
