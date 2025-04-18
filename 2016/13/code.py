import os
os.chdir(os.path.dirname(__file__))
from collections import deque


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  n = int(reader()[0])
  S = (1, 1)
  E = (31, 39)
  Q = deque([(S, 0)])
  V = set()
  while Q:
    (x, y), d = Q.popleft()
    if (x, y) in V:
      continue
    V.add((x, y))
    if (x, y) == E:
      print(d)
      break
    if x < 0 or y < 0:
      continue
    if (x * x + 3 * x + 2 * x * y + y + y * y + n).bit_count() % 2 == 1:
      continue
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      Q.append(((x + dx, y + dy), d + 1))


def part2():
  n = int(reader()[0])
  S = (1, 1)
  E = (31, 39)
  Q = deque([(S, 0)])
  V = set()
  while Q:
    (x, y), d = Q.popleft()
    if d > 50:
      break
    if x < 0 or y < 0:
      continue
    if (x * x + 3 * x + 2 * x * y + y + y * y + n).bit_count() % 2 == 1:
      continue
    if (x, y) in V:
      continue
    V.add((x, y))
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      Q.append(((x + dx, y + dy), d + 1))
  print(len(V))


part1()
part2()
