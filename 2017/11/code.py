import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()[0].split(',')
  x, y = 0, 0
  M = {
    'n': (0, 2),
    's': (0, -2),
    'ne': (1, 1),
    'nw': (-1, 1),
    'se': (1, -1),
    'sw': (-1, -1)
  }
  for c in f:
    dx, dy = M[c]
    x, y = x + dx, y + dy
  print(abs(abs(y) - abs(x)) // 2 + min(abs(x), abs(y)))


def part2():
  f = reader()[0].split(',')
  x, y = 0, 0
  M = {
    'n': (0, 2),
    's': (0, -2),
    'ne': (1, 1),
    'nw': (-1, 1),
    'se': (1, -1),
    'sw': (-1, -1)
  }
  md = 0
  for c in f:
    dx, dy = M[c]
    x, y = x + dx, y + dy
    d = abs(abs(y) - abs(x)) // 2 + min(abs(x), abs(y))
    md = max(d, md)
  print(md)


part1()
part2()
