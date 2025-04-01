import os
os.chdir(os.path.dirname(__file__))
from math import log, floor


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  n = int(reader()[0])
  s, g = 1, 1
  while n > 1:
    g *= 2
    if n % 2 == 1:
      s += g
    n //= 2
  print(s)


def viz(n, p=True):
  l = list(range(1, n + 1))
  i = 0
  while len(l) > 1:
    if p:
      print(f'[{", ".join(map(str, l[:i]))}{", " if i > 0 else ""}\x1b[32m{l[i]}\x1b[0m{", " if i < len(l)-1 else ""}{", ".join(map(str, l[i + 1:]))}]')
    j = (i + len(l) // 2) % len(l)
    l.pop(j)
    if j > i:
      i = (i + 1)
    i %= len(l)
  if p:
    print(f'[\x1b[32m{l[0]}\x1b[0m]')
  return l[0]


def part2():
  n = int(reader()[0])
  m = 3 ** floor(log(n, 3))
  print(n - m if n < 2 * m else 2 * n - 3 * m)


part1()
part2()
