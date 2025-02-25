import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = list(map(int, reader()))
  i = 0
  s = 0
  while i in range(len(f)):
    f[i] += 1
    i += (f[i] - 1)
    s += 1
  print(s)


def part2():
  f = list(map(int, reader()))
  i = 0
  s = 0
  while i in range(len(f)):
    x = f[i]
    f[i] += 1 if f[i] < 3 else -1
    i += x
    s += 1
  print(s)


part1()
part2()
