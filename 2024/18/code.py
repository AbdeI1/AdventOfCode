import os
os.chdir(os.path.dirname(__file__))
import math
import time


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = list(map(eval, reader()))
  W, H = 71, 71
  G = [['.' for _ in range(W)] for _ in range(H)]
  for x, y in f[:1024]:
    G[y][x] = '#'
  D = [(1, 0), (-1, 0), (0, 1), (0, -1)]
  q = [(0, 0, 0)]
  V = set()
  while q:
    d, x, y = q.pop(0)
    if (x, y) in V:
      continue
    V.add((x, y))
    if (x, y) == (W - 1, H - 1):
      print(d)
      break
    for dx, dy in D:
      xx, yy = x + dx, y + dy
      if yy in range(len(G)) and xx in range(len(G[yy])) and G[yy][xx] == '.':
        q.append((d + 1, xx, yy))


def part2():
  f = list(map(eval, reader()))
  W, H = 71, 71
  G = [['.' for _ in range(W)] for _ in range(H)]
  for x, y in f:
    G[y][x] = '#'
  P = [[(x, y) for x in range(W)] for y in range(H)]

  def find(x, y):
    return P[y][x] if P[y][x] == (x, y) else find(*P[y][x])

  def union(x1, y1, x2, y2):
    p1, p2 = find(x1, y1), find(x2, y2)
    P[p1[1]][p1[0]] = p2

  D = [(1, 0), (-1, 0), (0, 1), (0, -1)]
  for y in range(H):
    for x in range(W):
      if G[y][x] == '#':
        continue
      for dx, dy in D:
        xx, yy = x + dx, y + dy
        if yy in range(len(G)) and xx in range(len(G[yy])) and G[yy][xx] == '.':
          union(x, y, xx, yy)

  for x, y in f[::-1]:
    G[y][x] = '.'
    for dx, dy in D:
      xx, yy = x + dx, y + dy
      if yy in range(len(G)) and xx in range(len(G[yy])) and G[yy][xx] == '.':
        union(x, y, xx, yy)
    if find(0, 0) == find(W - 1, H - 1):
      print(','.join(map(str, (x, y))))
      break


def original_part2():
  f = list(map(eval, reader()))
  W, H = 71, 71
  G = [['.' for _ in range(W)] for _ in range(H)]
  D = [(1, 0), (-1, 0), (0, 1), (0, -1)]

  def bfs():
    q = [(0, 0, 0)]
    V = set()
    while q:
      d, x, y = q.pop(0)
      if (x, y) in V:
        continue
      V.add((x, y))
      if (x, y) == (W - 1, H - 1):
        return True
      for dx, dy in D:
        xx, yy = x + dx, y + dy
        if yy in range(len(G)) and xx in range(len(G[yy])) and G[yy][xx] == '.':
          q.append((d + 1, xx, yy))
    return False

  n = 2 ** int(math.log2(len(f)))
  s = n >> 1

  for x, y in f[:n]:
    G[y][x] = '#'

  while s:
    if bfs():
      for x, y in f[n:(n + s)]:
        G[y][x] = '#'
      n += s
    else:
      for x, y in f[(n - s):n]:
        G[y][x] = '.'
      n -= s
    s >>= 1

  print(','.join(map(str, f[n - 1])))


part1()
part2()
