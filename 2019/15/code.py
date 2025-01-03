import os
os.chdir(os.path.dirname(__file__))
import sys
sys.path.append('..')
from intcode import compute
from threading import Thread
from time import sleep


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  code = list(map(int, reader()[0].split(',')))
  I, O = [], []
  T = Thread(target=compute, args=(code, I, O), daemon=True)
  T.start()
  M = {}
  D = [(0, -1), (0, 1), (-1, 0), (1, 0)]

  def dfs(P, a=1):
    x, y = P
    if (x, y) in M:
      return
    M[(x, y)] = a
    for i, (dx, dy) in enumerate(D):
      I.append(i + 1)
      while not O:
        sleep(0)
      o = O.pop(0)
      if o == 0:
        M[(x + dx, y + dy)] = 0
      else:
        dfs((x + dx, y + dy), o)
        I.append((i ^ 1) + 1)
        while not O:
          sleep(0)
        O.pop(0)

  dfs((0, 0))

  xl, xr = min(x for x, _ in M), max(x for x, _ in M)
  yd, yu = min(y for _, y in M), max(y for _, y in M)

  G = [[M[(x, y)] if (x, y) in M else 0 for x in range(xl, xr + 1)]
       for y in range(yd, yu + 1)]

  Q = [(0, (0, 0))]
  V = set()

  while Q:
    d, (x, y) = Q.pop(0)
    if (x, y) in V:
      continue
    V.add((x, y))
    if G[y - yd][x - xl] == 0:
      continue
    if G[y - yd][x - xl] == 2:
      print(d)
      break
    for dx, dy in D:
      Q.append((d + 1, (x + dx, y + dy)))


def part2():
  code = list(map(int, reader()[0].split(',')))
  I, O = [], []
  T = Thread(target=compute, args=(code, I, O), daemon=True)
  T.start()
  M = {}
  D = [(0, -1), (0, 1), (-1, 0), (1, 0)]

  def dfs(P, a=1):
    x, y = P
    if (x, y) in M:
      return
    M[(x, y)] = a
    for i, (dx, dy) in enumerate(D):
      I.append(i + 1)
      while not O:
        sleep(0)
      o = O.pop(0)
      if o == 0:
        M[(x + dx, y + dy)] = 0
      else:
        dfs((x + dx, y + dy), o)
        I.append((i ^ 1) + 1)
        while not O:
          sleep(0)
        O.pop(0)

  dfs((0, 0))

  xl, xr = min(x for x, _ in M), max(x for x, _ in M)
  yd, yu = min(y for _, y in M), max(y for _, y in M)

  G = [[M[(x, y)] if (x, y) in M else 0 for x in range(xl, xr + 1)]
       for y in range(yd, yu + 1)]

  Q = [(0, next((x, y) for x, y in M if M[(x, y)] == 2))]
  V = {}

  while Q:
    d, (x, y) = Q.pop(0)
    if (x, y) in V:
      continue
    V[(x, y)] = d
    for dx, dy in D:
      if G[y + dy - yd][x + dx - xl] != 0:
        Q.append((d + 1, (x + dx, y + dy)))

  print(max(V.values()))


part1()
part2()
