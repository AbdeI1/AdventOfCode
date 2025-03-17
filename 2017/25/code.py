import os
os.chdir(os.path.dirname(__file__))
from collections import defaultdict


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  s = f[0][-2]
  I = int(f[1].split()[-2])
  S = {}
  for l in '\n'.join(f).split('\n\n')[1:]:
    ll = l.splitlines()
    ss = ll[0][-2]
    S[ss] = tuple((int(ll[i][-2]), {'right': 1, 'left': -1}
                  [ll[i + 1].split()[-1][:-1]], ll[i + 2][-2]) for i in (2, 6))
  T = defaultdict(int)
  i = 0
  for _ in range(I):
    v, m, ns = S[s][T[i]]
    T[i] = v
    i += m
    s = ns
  print(sum(T.values()))


def part2():
  pass


part1()
part2()
