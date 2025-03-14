import os
os.chdir(os.path.dirname(__file__))
from collections import defaultdict
from math import sqrt


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = [l.split() for l in reader()]
  R = defaultdict(int)
  def val(x): return R[x] if x.isalpha() else int(x)
  i = 0
  c = 0
  while i in range(len(f)):
    l = f[i]
    match l[0]:
      case 'set':
        R[l[1]] = val(l[2])
      case 'sub':
        R[l[1]] -= val(l[2])
      case 'mul':
        c += 1
        R[l[1]] *= val(l[2])
      case 'jnz':
        if val(l[1]) != 0:
          i += val(l[2])
          continue
    i += 1
  print(c)


def part2():
  f = [l.split() for l in reader()]
  R = defaultdict(int)
  R['a'] = 1
  def val(x): return R[x] if x.isalpha() else int(x)
  i = 0
  while i < 10:
    l = f[i]
    match l[0]:
      case 'set':
        R[l[1]] = val(l[2])
      case 'sub':
        R[l[1]] -= val(l[2])
      case 'mul':
        R[l[1]] *= val(l[2])
      case 'jnz':
        if val(l[1]) != 0:
          i += val(l[2])
          continue
    i += 1
  A = R['b']
  B = R['c']
  s = -int(f[-2][-1])
  print(len([i for i in range(A, B + 1, s) if any(i %
        j == 0 for j in range(2, round(sqrt(i)) + 2))]))


part1()
part2()
