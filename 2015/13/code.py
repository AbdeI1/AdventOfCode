import os
os.chdir(os.path.dirname(__file__))
from collections import defaultdict
from itertools import permutations


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  D = defaultdict(lambda: defaultdict(int))
  for l in map(str.split, f):
    D[l[0]][l[10][:-1]] = int(l[3]) * {'gain': 1, 'lose': -1}[l[2]]
  M = 0
  for s in permutations(D, len(D)):
    sc = sum(D[s[i]][s[i - 1]] + D[s[i]][s[(i + 1) % len(s)]]
             for i in range(len(s)))
    M = max(M, sc)
  print(M)


def part2():
  f = reader()
  D = defaultdict(lambda: defaultdict(int))
  D['yourself'] = defaultdict(int)
  for l in map(str.split, f):
    D[l[0]][l[10][:-1]] = int(l[3]) * {'gain': 1, 'lose': -1}[l[2]]
  M = 0
  for s in permutations(D, len(D)):
    sc = sum(D[s[i]][s[i - 1]] + D[s[i]][s[(i + 1) % len(s)]]
             for i in range(len(s)))
    M = max(M, sc)
  print(M)


part1()
part2()
