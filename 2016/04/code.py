import os
os.chdir(os.path.dirname(__file__))
from collections import Counter


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = [(lambda t: (''.join(c for _, c in sorted([(y, x) for x, y in Counter(t[0].replace('-', '')).most_common()],
        key=lambda t: (-t[0], t[1]))[:5]), t[-1].split("[")[1][:-1], int(t[-1].split("[")[0])))(l.rpartition('-')) for l in reader()]
  print(sum(z for x, y, z in f if x == y))


def part2():
  f = [(lambda t: (' '.join(''.join(chr((ord(c) - ord('a') + t[1]) % 26 + ord('a')) for c in s)
        for s in t[0].split('-')), t[1]))((lambda t: (t[0], int(t[-1].split("[")[0])))(l.rpartition('-'))) for l in reader()]
  print(sum([i for s, i in f if "north" in s]))


part1()
part2()
