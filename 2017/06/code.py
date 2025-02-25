import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = list(map(int, reader()[0].split()))
  V = set()
  while str(f) not in V:
    V.add(str(f))
    i = f.index(max(f))
    x = f[i]
    f[i] = 0
    while x > 0:
      i += 1
      i %= len(f)
      f[i] += 1
      x -= 1
  print(len(V))


def part2():
  f = list(map(int, reader()[0].split()))
  V = {}
  t = 0
  while str(f) not in V:
    V[str(f)] = t
    i = f.index(max(f))
    x = f[i]
    f[i] = 0
    while x > 0:
      i += 1
      i %= len(f)
      f[i] += 1
      x -= 1
    t += 1
  print(t - V[str(f)])


part1()
part2()
