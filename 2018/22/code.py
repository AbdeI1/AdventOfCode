import os
os.chdir(os.path.dirname(__file__))
from functools import cache
from heapq import heappop, heappush


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  depth = int(f[0].split(": ")[1])
  tx, ty = eval(f[1].split(": ")[1])
  M = 20183
  E = [[0 for _ in range(tx + 1)] for _ in range(ty + 1)]
  for y in range(ty + 1):
    for x in range(tx + 1):
      if y == 0:
        E[y][x] = (x * 16807 + depth) % M
      elif x == 0:
        E[y][x] = (y * 48271 + depth) % M
      else:
        E[y][x] = (E[y - 1][x] * E[y][x - 1] + depth) % M
  E[-1][-1] = depth % M
  print(sum(i % 3 for r in E for i in r))


def part2():
  f = reader()
  depth = int(f[0].split(": ")[1])
  tx, ty = eval(f[1].split(": ")[1])
  M = 20183

  @cache
  def E(x, y):
    if (x, y) == (tx, ty):
      return depth % M
    elif y == 0:
      return (x * 16807 + depth) % M
    elif x == 0:
      return (y * 48271 + depth) % M
    else:
      return (E(x - 1, y) * E(x, y - 1) + depth) % M

  Q = [(0, (0, 0, 1))]
  V = set()
  while Q:
    d, (x, y, t) = heappop(Q)
    if x < 0 or y < 0:
      continue
    if E(x, y) % 3 == t:
      continue
    if (x, y, t) in V:
      continue
    V.add((x, y, t))
    # print(d, (x, y, t))
    if (x, y, t) == (tx, ty, 1):
      print(d)
      break
    heappush(Q, (d + 7, (x, y, (t + 1) % 3)))
    heappush(Q, (d + 7, (x, y, (t + 2) % 3)))
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
      heappush(Q, (d + 1, (x + dx, y + dy, t)))


part1()
part2()
