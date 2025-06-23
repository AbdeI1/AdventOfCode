import os
os.chdir(os.path.dirname(__file__))
from math import prod


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  i, j = 0, 0
  di, dj = 1, 3
  ans = 0
  while i in range(len(f)):
    if f[i][j] == '#': ans += 1
    i, j = i + di, (j + dj) % len(f[i])
  print(ans)


def part2():
  f = reader()

  def down(di, dj):
    i, j = 0, 0
    ans = 0
    while i in range(len(f)):
      if f[i][j] == '#': ans += 1
      i, j = i + di, (j + dj) % len(f[i])
    return ans
  print(prod(down(di, dj)
        for di, dj in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]))


part1()
part2()
