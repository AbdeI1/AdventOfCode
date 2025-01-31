import os
os.chdir(os.path.dirname(__file__))
from collections import defaultdict


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  s = f[0].split(": ")[1]
  s = defaultdict(int, {i: 1 for i, c in enumerate(s) if c == '#'})
  R = [0] * 32
  for i in f[2:]:
    a, b = i.replace('#', '1').replace('.', '0').split(" => ")
    R[int(a[::-1], 2)] = int(b)
  for _ in range(20):
    sn = defaultdict(int)
    for i in range(min(s.keys()) - 2, max(s.keys()) + 2):
      l = sum(2 ** j for j in range(5) if s[i - 2 + j])
      if R[l]:
        sn[i] = R[l]
    s = sn
  print(sum(s.keys()))


def part2():
  f = reader()
  s = f[0].split(": ")[1]
  s = {i for i, c in enumerate(s) if c == '#'}
  R = [0] * 32
  for i in f[2:]:
    a, b = i.replace('#', '1').replace('.', '0').split(" => ")
    R[int(a[::-1], 2)] = int(b)
  N = 50000000000
  t = 0
  while True:
    sn = set()
    for i in range(min(s) - 2, max(s) + 2):
      l = sum(2 ** j for j in range(5) if i - 2 + j in s)
      if R[l]:
        sn.add(i)
    if len(sn) == len(s) and len({x - y for x, y in zip(sorted(sn), sorted(s))}) == 1:
      break
    s = sn
    t += 1
  print(sum(s) + (N - t) * len(s))


part1()
part2()
