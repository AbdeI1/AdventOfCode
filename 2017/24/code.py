import os
os.chdir(os.path.dirname(__file__))
from collections import defaultdict
from functools import cache


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = [eval(l.replace("/", ",")) for l in reader()]
  C = defaultdict(set)
  I = {}
  for i, p1 in enumerate(f):
    I[p1] = i
    C[p1[0]].add(p1)
    C[p1[1]].add(p1)

  @cache
  def exp(c, U):
    m = 0
    for p in C[c]:
      if (1 << I[p]) & U == 0:
        m = max(m, sum(p) + exp(p[0] if p[0] != c else p[1], U | (1 << I[p])))
    return m

  print(exp(0, 0))


def part2():
  f = [eval(l.replace("/", ",")) for l in reader()]
  C = defaultdict(set)
  I = {}
  for i, p1 in enumerate(f):
    I[p1] = i
    C[p1[0]].add(p1)
    C[p1[1]].add(p1)

  L = []

  def expL(c, U, l):
    nonlocal L
    for p in C[c]:
      if (1 << I[p]) & U == 0:
        expL(p[0] if p[0] != c else p[1], U | (1 << I[p]), l + [p])
    L.append(l)

  expL(0, 0, [])
  bs = max(map(len, L))
  Ls = list(filter(lambda l: len(l) == bs, L))
  print(max(sum(sum(l, ())) for l in Ls))


part1()
part2()
