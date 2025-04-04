import os
os.chdir(os.path.dirname(__file__))
from hashlib import md5


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  p = reader()[0]

  def dirs(s):
    L = []
    for l, d in zip(md5(s.encode()).hexdigest()[:4], [('U', (-1, 0)), ('D', (1, 0)), ('L', (0, -1)), ('R', (0, 1))]):
      if l in 'bcdef':
        L.append(d)
    return L

  Q = [(p, (0, 0))]
  while Q:
    s, (y, x) = Q.pop(0)
    if (y, x) == (3, 3):
      print(s[8:])
      break
    for d, (dy, dx) in dirs(s):
      if x + dx in range(0, 4) and y + dy in range(0, 4):
        Q.append((s + d, (y + dy, x + dx)))


def part2():
  p = reader()[0]

  def dirs(s):
    L = []
    for l, d in zip(md5(s.encode()).hexdigest()[:4], [('U', (-1, 0)), ('D', (1, 0)), ('L', (0, -1)), ('R', (0, 1))]):
      if l in 'bcdef':
        L.append(d)
    return L

  def dfs(s, y, x):
    if (y, x) == (3, 3):
      return len(s) - 8
    return max((dfs(s + d, y + dy, x + dx) for d, (dy, dx) in dirs(s) if x + dx in range(0, 4) and y + dy in range(0, 4)), default=0)

  print(dfs(p, 0, 0))


part1()
part2()
