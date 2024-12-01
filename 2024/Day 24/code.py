import pathlib


def reader():
  f = open(f"{pathlib.Path(__file__).parent.resolve()}/input.txt", 'r').read()
  f = f.split('\n')
  f = f[:-1]
  return f


def part1():
  pass


def part2():
  pass


part1()
part2()
