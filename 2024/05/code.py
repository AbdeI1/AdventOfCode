import os
os.chdir(os.path.dirname(__file__))
from functools import cmp_to_key


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = list(map(lambda s: tuple(map(int, s.split('|'))),
           '\n'.join(reader()).split('\n\n')[0].split('\n')))
  n = set(a for a, b in f).union(set(b for a, b in f))
  o = {x: {y: True for y in n} for x in n}
  for a, b in f:
    o[b][a] = False
  L = list(map(lambda s: list(map(int, s.split(','))),
           '\n'.join(reader()).split('\n\n')[1].split('\n')))
  c = 0
  for l in L:
    if all(all(o[l[i]][l[j]] for j in range(i + 1, len(l))) for i in range(len(l))):
      c += l[len(l) // 2]
  print(c)


def part2():
  f = list(map(lambda s: tuple(map(int, s.split('|'))),
           '\n'.join(reader()).split('\n\n')[0].split('\n')))
  n = set(a for a, b in f).union(set(b for a, b in f))
  o = {x: {y: True for y in n} for x in n}
  for a, b in f:
    o[b][a] = False
  L = list(map(lambda s: list(map(int, s.split(','))),
           '\n'.join(reader()).split('\n\n')[1].split('\n')))
  c = 0
  for l in L:
    if not all(all(o[l[i]][l[j]] for j in range(i + 1, len(l))) for i in range(len(l))):
      l = sorted(l, key=lambda x: sum(o[x][y] for y in l))
      c += l[len(l) // 2]
  print(c)


part1()
part2()
