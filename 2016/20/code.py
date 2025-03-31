import os
os.chdir(os.path.dirname(__file__))
from itertools import pairwise


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = sorted([eval(l.replace('-', ',')) for l in reader()])
  if f[0][0] > 0:
    print(0)
    return
  for (_, e), (b, _) in pairwise(f):
    if b > e + 1:
      print(e + 1)
      break


def part2():
  f = sorted([eval(l.replace('-', ',')) for l in reader()])
  I = []
  s, e = f[0]
  for i, j in f[1:]:
    if i > e + 1:
      I.append((s, e))
      s, e = i, j
    e = max(e, j)
  I.append((s, e))
  A = I[0][0]
  for (_, i), (j, _) in pairwise(I):
    A += j - i - 1
  print(I)
  A += (1 << 32) - I[-1][-1] - 1
  print(A)


part1()
part2()
