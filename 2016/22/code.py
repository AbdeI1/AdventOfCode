import os
os.chdir(os.path.dirname(__file__))
from itertools import permutations


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  l = f[-1].split('-')
  X = int(l[1][1:]) + 1
  Y = int(l[2].split()[0][1:]) + 1
  G = [[tuple(map(lambda s: int(s[:-1]), f[2 + x * Y + y].split()[2:4]))
        for x in range(X)] for y in range(Y)]
  print(len(list(((x1, y1), (x2, y2)) for (x1, y1), (x2, y2)
        in permutations(((x, y) for x in range(X) for y in range(Y)), 2)
        if G[y1][x1][0] > 0 and G[y1][x1][0] <= G[y2][x2][1])))


def part2():
  f = reader()
  l = f[-1].split('-')
  X = int(l[1][1:]) + 1
  Y = int(l[2].split()[0][1:]) + 1
  G = [[tuple(map(lambda s: int(s[:-1]), f[2 + x * Y + y].split()[2:4]))
        for x in range(X)] for y in range(Y)]
  x, y = next((x, y) for x in range(X) for y in range(Y) if G[y][x][0] == 0)
  print(x, y, X, Y)


part1()
part2()
