import os
os.chdir(os.path.dirname(__file__))
from collections import defaultdict

def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  S = {f[0].index('S')}
  A = 0
  for l in f:
    for j in range(len(l)):
      if l[j] == '^' and j in S:
        S.remove(j)
        S.add(j - 1)
        S.add(j + 1)
        A += 1
  print(A)


def part2():
  f = reader()
  S = defaultdict(int, {f[0].index('S'): 1})
  A = 1
  for l in f:
    for j in range(len(l)):
      if l[j] == '^' and j in S:
        S[j - 1] += S[j]
        S[j + 1] += S[j]
        A += S[j]
        S[j] = 0
  print(A)


part1()
part2()
