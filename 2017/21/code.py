import os
os.chdir(os.path.dirname(__file__))


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
    a = a.split('/')
    b = b.split('/')
    for _ in range(2):
      for _ in range(4):
        T[tuple(a)] = b
        a = [''.join([a[R[len(a)][(i, j)][0]][R[len(a)][(i, j)][1]] for j in range(len(a))]) for i in range(len(a))]
      a = a[::-1]
  print(len(T.keys()))


def part2():
  pass


part1()
part2()
