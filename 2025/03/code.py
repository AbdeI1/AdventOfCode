import os
os.chdir(os.path.dirname(__file__))
from functools import cache


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = [list(map(int, l)) for l in reader()]
  A = 0
  for b in f:
    M = 0
    for i in range(len(b) - 1):
      M = max(M, b[i] * 10 + max(b[(i + 1):]))
    A += M
  print(A)


def part2():
  f = [list(map(int, l)) for l in reader()]
  A = 0

  for b in f:
    M = 0

    @cache
    def get_max(i, d):
      if d <= 0:
        return 0
      if i < 0:
        return 0
      return max(get_max(i - 1, d), get_max(i - 1, d - 1) * 10 + b[i])

    M = get_max(len(b) - 1, 12)
    A += M
  print(A)


part1()
part2()
