import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  n = int(reader()[0])
  print(n)


def part2():
  pass


part1()
part2()
