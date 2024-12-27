import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  print(sum((x // 3) - 2 for x in map(int, reader())))


def part2():
  f = map(int, reader())
  c = 0
  for x in f:
    while (x := (x // 3) - 2) > 0:
      c += x
  print(c)


part1()
part2()
