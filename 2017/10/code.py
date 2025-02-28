import os
os.chdir(os.path.dirname(__file__))
from functools import reduce
from operator import xor


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = eval(reader()[0])
  l = [i for i in range(256)]
  i, s = 0, 0
  for le in f:
    for j in range(le // 2):
      l[(i + j) % len(l)], l[(i + le - 1 - j) %
                             len(l)] = l[(i + le - 1 - j) % len(l)], l[(i + j) % len(l)]
    i += le + s
    i %= len(l)
    s += 1
  print(l[0] * l[1])


def part2():
  f = list(map(ord, reader()[0])) + [17, 31, 73, 47, 23]
  l = [i for i in range(256)]
  i, s = 0, 0
  for _ in range(64):
    for le in f:
      for j in range(le // 2):
        l[(i + j) % len(l)], l[(i + le - 1 - j) %
                               len(l)] = l[(i + le - 1 - j) % len(l)], l[(i + j) % len(l)]
      i += le + s
      i %= len(l)
      s += 1
  print(
    ''.join(f"{n:02x}" for n in [reduce(xor, l[16 * i:16 * i + 16]) for i in range(16)]))


part1()
part2()
