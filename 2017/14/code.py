import os
os.chdir(os.path.dirname(__file__))
from functools import reduce
from operator import xor


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def hash(s):
  f = list(map(ord, s)) + [17, 31, 73, 47, 23]
  l = [i for i in range(256)]
  i, s = 0, 0
  for _ in range(64):
    for le in f:
      for j in range(le // 2):
        l[(i + j) % len(l)], l[(i + le - 1 - j) %
                               len(l)] = l[(i + le - 1 - j) % len(l)], l[(i + j) % len(l)]
      i += le + s
      i %= len(l)
      s += 1
  return ''.join(f"{n:02x}" for n in [reduce(xor, l[16 * i:16 * i + 16]) for i in range(16)])


def part1():
  f = reader()[0]
  s = 0
  for i in range(128):
    s += int(hash(f'{f}-{i}'), 16).bit_count()
  print(s)


def part2():
  f = reader()[0]
  G = [[] for _ in range(128)]
  for i in range(128):
    G[i] = list(f"{int(hash(f'{f}-{i}'), 16):0128b}")

  p = [[(i, j) for j in range(128)] for i in range(128)]

  def find(i, j):
    if (i, j) != p[i][j]:
      p[i][j] = find(*p[i][j])
    return p[i][j]

  def union(i, j, ii, jj):
    x, y = find(i, j)
    xx, yy = find(ii, jj)
    p[x][y] = p[xx][yy]

  for i in range(128):
    for j in range(128):
      if G[i][j] == '1':
        for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
          if i + di in range(128) and j + dj in range(128) and G[i + di][j + dj] == '1':
            union(i, j, i + di, j + dj)

  print(len({find(i, j) for i in range(128)
        for j in range(128) if G[i][j] == '1'}))


part1()
part2()
