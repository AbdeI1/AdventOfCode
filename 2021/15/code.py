import heapq


import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def getM(g, i, j):
  if i >= 100 or j >= 100 or i < 0 or j < 0:
    return 100000000
  return g[i][j]


def part1():
  f = reader()
  g = list(map(lambda x: list(map(int, x)), f))
  q = [(0, (0, 0))]
  v = set()
  while len(q) > 0:
    (w, (i, j)) = heapq.heappop(q)
    if (i, j) in v:
      continue
    v.add((i, j))
    if (i, j) == (99, 99):
      print(w)
      break
    up = (w + getM(g, i - 1, j), (i - 1, j))
    down = (w + getM(g, i + 1, j), (i + 1, j))
    right = (w + getM(g, i, j + 1), (i, j + 1))
    left = (w + getM(g, i, j - 1), (i, j - 1))
    if down[0] - w < 10:
      heapq.heappush(q, down)
    if right[0] - w < 10:
      heapq.heappush(q, right)
    if up[0] - w < 10:
      heapq.heappush(q, up)
    if left[0] - w < 10:
      heapq.heappush(q, left)


def getM2(g, i, j):
  if i >= 500 or j >= 500 or i < 0 or j < 0:
    return 100000000
  return (g[i % 100][j % 100] + i // 100 + j // 100 - 1) % 9 + 1


def part2():
  f = reader()
  g = list(map(lambda x: list(map(int, x)), f))
  q = [(0, (0, 0))]
  v = set()
  while len(q) > 0:
    (w, (i, j)) = heapq.heappop(q)
    if (i, j) in v:
      continue
    v.add((i, j))
    if (i, j) == (499, 499):
      print(w)
      break
    up = (w + getM2(g, i - 1, j), (i - 1, j))
    down = (w + getM2(g, i + 1, j), (i + 1, j))
    right = (w + getM2(g, i, j + 1), (i, j + 1))
    left = (w + getM2(g, i, j - 1), (i, j - 1))
    if down[0] - w < 10:
      heapq.heappush(q, down)
    if right[0] - w < 10:
      heapq.heappush(q, right)
    if up[0] - w < 10:
      heapq.heappush(q, up)
    if left[0] - w < 10:
      heapq.heappush(q, left)


part1()
part2()
