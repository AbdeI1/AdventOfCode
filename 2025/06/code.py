import os
os.chdir(os.path.dirname(__file__))
from math import prod


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  N = [list(map(int, l.split())) for l in f[:-1]]
  O = f[-1].split()
  A = 0
  for i in range(len(O)):
    A += {'+': sum, '*': prod}[O[i]](map(lambda x: x[i], N))
  print(A)


def part2():
  f = reader()
  O = {'+': sum, '*': prod}
  A = 0
  j = 0
  while j < len(f[-1]):
    if f[-1][j] in O:
      o = f[-1][j]
      n = []
      while j < len(f[-1]):
        s = ''.join(map(lambda x: x[j], f[:-1])).strip()
        if s == '':
          break
        n.append(int(s))
        j += 1
      A += O[o](n)
      j += 1
  print(A)


part1()
part2()
