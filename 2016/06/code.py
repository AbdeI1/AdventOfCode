import os
os.chdir(os.path.dirname(__file__))
from collections import Counter


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  C = [Counter(l[i] for l in f) for i in range(len(f[0]))]
  print(''.join(c.most_common(1)[0][0] for c in C))


def part2():
  f = reader()
  C = [Counter(l[i] for l in f) for i in range(len(f[0]))]
  print(''.join(c.most_common()[-1][0] for c in C))


part1()
part2()
