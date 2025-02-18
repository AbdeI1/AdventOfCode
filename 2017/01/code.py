import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = list(map(int, reader()[0]))
  print(sum(f[i] for i in range(len(f)) if f[i] == f[(i + 1) % len(f)]))


def part2():
  f = list(map(int, reader()[0]))
  print(sum(f[i] for i in range(len(f)) if f[i]
        == f[(i + (len(f) // 2)) % len(f)]))


part1()
part2()
