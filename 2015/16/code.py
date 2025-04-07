import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  S = [eval(f"{{'{l[l.find(': ')+2:].replace(', ', ', \'').replace(':', '\':')}}}") for l in reader()]
  D = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
  }
  print(D)


def part2():
  pass


part1()
part2()
