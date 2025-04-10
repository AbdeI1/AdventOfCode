import os
os.chdir(os.path.dirname(__file__))
from math import prod


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = [tuple(map(lambda s: int(s.split()[-1]), l.split(', ')))
       for l in reader()]

  def getMax(i, t, C):
    if i == len(f) - 1:
      return prod(max(0, C[j] + t * f[i][j]) for j in range(len(C)))
    return max(getMax(i + 1, t - k, tuple(C[j] + k * f[i][j] for j in range(len(C)))) for k in range(t + 1))

  print(getMax(0, 100, (0, 0, 0, 0)))


def part2():
  f = [tuple(map(lambda s: int(s.split()[-1]), l.split(', ')))
       for l in reader()]

  def getMax(i, t, C):
    if i == len(f) - 1:
      return prod(max(0, C[j] + t * f[i][j]) for j in range(len(C) - 1)) if t * f[i][-1] + C[-1] == 500 else 0
    return max(getMax(i + 1, t - k, tuple(C[j] + k * f[i][j] for j in range(len(C)))) for k in range(t + 1))

  print(getMax(0, 100, (0, 0, 0, 0, 0)))


part1()
part2()
