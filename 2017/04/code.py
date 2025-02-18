import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  print(len(list(filter(lambda s: len(set(s.split())) == len(s.split()), reader()))))


def part2():
  print(len(list(filter(lambda s: len(
    set(map(lambda w: str(sorted(w)), s.split()))) == len(s.split()), reader()))))


part1()
part2()
