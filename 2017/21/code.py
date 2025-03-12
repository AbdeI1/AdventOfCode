import os
os.chdir(os.path.dirname(__file__))
from functools import cache


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  R = [
    {},
    {
      (0, 0): (0, 0)
    },
    {
      (0, 0): (0, 1),
      (0, 1): (1, 1),
      (1, 1): (1, 0),
      (1, 0): (0, 0)
    },
    {
      (0, 0): (0, 2),
      (0, 1): (1, 2),
      (0, 2): (2, 2),
      (1, 0): (0, 1),
      (1, 1): (1, 1),
      (1, 2): (2, 1),
      (2, 0): (0, 0),
      (2, 1): (1, 0),
      (2, 2): (2, 0)
    }
  ]
  T = {}
  for l in f:
    a, b = l.split(' => ')
    a = tuple(a.split('/'))
    b = tuple(b.split('/'))
    for _ in range(2):
      for _ in range(4):
        T[a] = b
        a = tuple(''.join([a[R[len(a)][(i, j)][0]][R[len(a)][(i, j)][1]] for j in range(len(a))]) for i in range(len(a)))
      a = a[::-1]
  G = (
    '.#.',
    '..#',
    '###'
  )
  
  @cache
  def count(G, i = 0):
    if i <= 0:
      return sum([1 for r in G for c in r if c == '#'])
    if len(G) % 2 == 0:
      return sum(count(T[tuple([r[y:y+2] for r in G[x:x+2]])], i - 1) for x in range(0, len(G), 2) for y in range(0, len(G[x]), 2))
    elif len(G) % 3 == 0:
      return sum(count(T[tuple([r[y:y+3] for r in G[x:x+3]])], i - 1) for x in range(0, len(G), 3) for y in range(0, len(G[x]), 3))
    return 0
  
  print(count(G, 5))


def part2():
  f = reader()
  R = [
    {},
    {
      (0, 0): (0, 0)
    },
    {
      (0, 0): (0, 1),
      (0, 1): (1, 1),
      (1, 1): (1, 0),
      (1, 0): (0, 0)
    },
    {
      (0, 0): (0, 2),
      (0, 1): (1, 2),
      (0, 2): (2, 2),
      (1, 0): (0, 1),
      (1, 1): (1, 1),
      (1, 2): (2, 1),
      (2, 0): (0, 0),
      (2, 1): (1, 0),
      (2, 2): (2, 0)
    }
  ]
  T = {}
  for l in f:
    a, b = l.split(' => ')
    a = tuple(a.split('/'))
    b = tuple(b.split('/'))
    for _ in range(2):
      for _ in range(4):
        T[a] = b
        a = tuple(''.join([a[R[len(a)][(i, j)][0]][R[len(a)][(i, j)][1]] for j in range(len(a))]) for i in range(len(a)))
      a = a[::-1]
  G = (
    '.#.',
    '..#',
    '###'
  )
  
  @cache
  def count(G, i = 0):
    if i <= 0:
      return sum([1 for r in G for c in r if c == '#'])
    if len(G) % 2 == 0:
      return sum(count(T[tuple([r[y:y+2] for r in G[x:x+2]])], i - 1) for x in range(0, len(G), 2) for y in range(0, len(G[x]), 2))
    elif len(G) % 3 == 0:
      return sum(count(T[tuple([r[y:y+3] for r in G[x:x+3]])], i - 1) for x in range(0, len(G), 3) for y in range(0, len(G[x]), 3))
    return 0
  
  print(count(G, 20))


part1()
part2()
