import os
os.chdir(os.path.dirname(__file__))
from collections import defaultdict


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  R = defaultdict(int)
  for l in f:
    r, op, n, _, cr, comp, cn = l.split()
    if eval(f'{cr} {comp} {cn}', locals=R):
      R[r] += int(n) * (1 if op == 'inc' else -1)
  print(max(R.values()))


def part2():
  f = reader()
  R = defaultdict(int)
  m = 0
  for l in f:
    r, op, n, _, cr, comp, cn = l.split()
    if eval(f'{cr} {comp} {cn}', locals=R):
      R[r] += int(n) * (1 if op == 'inc' else -1)
    m = max(m, max(R.values()))
  print(m)


part1()
part2()
