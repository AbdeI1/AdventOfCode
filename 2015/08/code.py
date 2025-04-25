import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  print(sum(len(l) - len(eval(l)) for l in reader()))


def part2():
  print(sum(l.count('"') + l.count('\\') + 2 for l in reader()))


part1()
part2()
