import os
os.chdir(os.path.dirname(__file__))
import heapq


def reader():
  return open(f"input.txt", 'r').read().split('\n')[:-1]


DIRS = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def part1():
  f = reader()
  m = list(map(list, f))
  s = (-1, -1)
  e = (-1, -1)
  for i in range(len(m)):
    for j in range(len(m[i])):
      if m[i][j] == 'S':
        s = (i, j)
        m[i][j] = 'a'
      if m[i][j] == 'E':
        e = (i, j)
        m[i][j] = 'z'
  m = list(map(lambda a: list(map(lambda c: ord(c) - ord('a'), a)), m))
  q = [(0, s)]
  v = set()
  while q:
    d, p = heapq.heappop(q)
    if p in v:
      continue
    v.add(p)
    if p == e:
      print(d)
      break
    for D in DIRS:
      pn = (p[0] + D[0], p[1] + D[1])
      if pn[0] in range(len(m)) and pn[1] in range(len(m[pn[0]])) and m[pn[0]][pn[1]] <= m[p[0]][p[1]] + 1:
        heapq.heappush(q, (d + 1, pn))


def part2():
  f = reader()
  m = list(map(list, f))
  q = []
  e = (-1, -1)
  for i in range(len(m)):
    for j in range(len(m[i])):
      if m[i][j] == 'S' or m[i][j] == 'a':
        q.append((0, (i, j)))
        m[i][j] = 'a'
      if m[i][j] == 'E':
        e = (i, j)
        m[i][j] = 'z'
  m = list(map(lambda a: list(map(lambda c: ord(c) - ord('a'), a)), m))
  v = set()
  while q:
    d, p = heapq.heappop(q)
    if p in v:
      continue
    v.add(p)
    if p == e:
      print(d)
      break
    for D in DIRS:
      pn = (p[0] + D[0], p[1] + D[1])
      if pn[0] in range(len(m)) and pn[1] in range(len(m[pn[0]])) and m[pn[0]][pn[1]] <= m[p[0]][p[1]] + 1:
        heapq.heappush(q, (d + 1, pn))


part1()
part2()
