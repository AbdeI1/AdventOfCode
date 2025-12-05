import os
os.chdir(os.path.dirname(__file__))
from bisect import bisect_left


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  R, I = '\n'.join(reader()).split('\n\n')
  R = [(lambda x, y: range(int(x), int(y) + 1))(*l.split('-')) for l in R.splitlines()]
  I = [int(l) for l in I.splitlines()]
  A = 0
  for i in I:
    for r in R:
      if i in r:
        A += 1
        break
  print(A)


def part2():
  R, _ = '\n'.join(reader()).split('\n\n')
  R = [tuple(map(int, l.split('-'))) for l in R.splitlines()]
  L = []
  for r in R:
    i = bisect_left(L, r)
    if i - 1 >= 0 and L[i - 1][1] >= r[0]:
      r = (L[i - 1][0], max(r[1], L[i - 1][1]))
      L.pop(i - 1)
      i -= 1
    while i < len(L) and L[i][0] <= r[1]:
      r = (r[0], max(r[1], L[i][1]))
      L.pop(i)
    L.insert(i, r)

  print(sum(e - s + 1 for s, e in L))


part1()
part2()
