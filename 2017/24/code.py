import os
os.chdir(os.path.dirname(__file__))
from collections import defaultdict
from functools import cache


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = [eval(l.replace("/", ",")) for l in reader()]
  C = defaultdict(list)
  S = []
  I = {}
  for i, p1 in enumerate(f):
    I[p1] = i
    for _, p2 in enumerate(f[i + 1:]):
      if p1[0] in p2 or p1[1] in p2:
        C[p1].append(p2)
        C[p2].append(p1)
    if 0 in p1:
      S.append(p1)

  @cache
  def exp(c, U):
    m = 0
    for p in C[c]:
      if (1 << I[p]) & U == 0:
        m = max(m, sum(p) + exp(p, U | (1 << I[p])))
    return m

  print(max(exp(s, (1 << I[s])) for s in S))


def part2():
  pass


part1()
part2()
