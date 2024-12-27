import os
os.chdir(os.path.dirname(__file__))
from heapq import *


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = [[int(c) for c in s] for s in reader()]
  q = [(-f[0][0], (0, 0, 'e', 0))]
  v = set()
  while q:
    hl, (i, j, d, s) = heappop(q)
    if i not in range(len(f)) or j not in range(len(f[i])) or s > 3:
      continue
    if (i, j, d, s) in v:
      continue
    v.add((i, j, d, s))
    hl += f[i][j]
    if (i, j) == (len(f) - 1, len(f[i]) - 1):
      print(hl)
      break
    match d:
      case 'n':
        heappush(q, (hl, (i - 1, j, 'n', s + 1)))
        heappush(q, (hl, (i, j + 1, 'e', 1)))
        heappush(q, (hl, (i, j - 1, 'w', 1)))
      case 'e':
        heappush(q, (hl, (i, j + 1, 'e', s + 1)))
        heappush(q, (hl, (i - 1, j, 'n', 1)))
        heappush(q, (hl, (i + 1, j, 's', 1)))
      case 's':
        heappush(q, (hl, (i + 1, j, 's', s + 1)))
        heappush(q, (hl, (i, j + 1, 'e', 1)))
        heappush(q, (hl, (i, j - 1, 'w', 1)))
      case 'w':
        heappush(q, (hl, (i, j - 1, 'w', s + 1)))
        heappush(q, (hl, (i - 1, j, 'n', 1)))
        heappush(q, (hl, (i + 1, j, 's', 1)))


def part2():
  f = [[int(c) for c in s] for s in reader()]
  q = [(-f[0][0], (0, 0, 'e', 0))]
  v = set()
  while q:
    hl, (i, j, d, s) = heappop(q)
    if i not in range(len(f)) or j not in range(len(f[i])) or s > 10:
      continue
    if (i, j, d, s) in v:
      continue
    v.add((i, j, d, s))
    hl += f[i][j]
    if (i, j) == (len(f) - 1, len(f[i]) - 1) and s > 3:
      print(hl)
      break
    match d:
      case 'n':
        heappush(q, (hl, (i - 1, j, 'n', s + 1)))
        if s >= 4:
          heappush(q, (hl, (i, j + 1, 'e', 1)))
          heappush(q, (hl, (i, j - 1, 'w', 1)))
      case 'e':
        heappush(q, (hl, (i, j + 1, 'e', s + 1)))
        if s >= 4:
          heappush(q, (hl, (i - 1, j, 'n', 1)))
          heappush(q, (hl, (i + 1, j, 's', 1)))
      case 's':
        heappush(q, (hl, (i + 1, j, 's', s + 1)))
        if s >= 4:
          heappush(q, (hl, (i, j + 1, 'e', 1)))
          heappush(q, (hl, (i, j - 1, 'w', 1)))
      case 'w':
        heappush(q, (hl, (i, j - 1, 'w', s + 1)))
        if s >= 4:
          heappush(q, (hl, (i - 1, j, 'n', 1)))
          heappush(q, (hl, (i + 1, j, 's', 1)))


part1()
part2()
