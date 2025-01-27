import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = [tuple(eval(x) for x in l[len('position=<'):-1].split('> velocity=<'))
       for l in reader()]
  a = float('inf')
  T = 0
  for t in range(10100):
    P = {(x + t * vx, y + t * vy) for (x, y), (vx, vy) in f}
    X = range(min(x for x, _ in P), max(x for x, _ in P) + 1)
    Y = range(min(y for _, y in P), max(y for _, y in P) + 1)
    A = (X.stop - X.start) * (Y.stop - Y.start)
    if A > a:
      T = t - 1
      break
    a = A
  P = {(x + T * vx, y + T * vy) for (x, y), (vx, vy) in f}
  X = range(min(x for x, _ in P), max(x for x, _ in P) + 1)
  Y = range(min(y for _, y in P), max(y for _, y in P) + 1)
  for y in Y:
    print(''.join('@' if (x, y) in P else ' ' for x in X))


def part2():
  f = [tuple(eval(x) for x in l[len('position=<'):-1].split('> velocity=<'))
       for l in reader()]
  a = float('inf')
  T = 0
  for t in range(10100):
    P = {(x + t * vx, y + t * vy) for (x, y), (vx, vy) in f}
    X = range(min(x for x, _ in P), max(x for x, _ in P) + 1)
    Y = range(min(y for _, y in P), max(y for _, y in P) + 1)
    A = (X.stop - X.start) * (Y.stop - Y.start)
    if A > a:
      T = t - 1
      break
    a = A
  print(T)


part1()
part2()
