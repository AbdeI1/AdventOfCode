import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


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


def part1():
  S = [eval(f"{{'{l[l.find(': ')+2:].replace(', ', ', \'').replace(':', '\':')}}}") for l in reader()]
  for i, s in enumerate(S):
    if all(D[k] == c for k, c in s.items()):
      print(i + 1)
      break


def part2():
  S = [eval(f"{{'{l[l.find(': ')+2:].replace(', ', ', \'').replace(':', '\':')}}}") for l in reader()]
  for i, s in enumerate(S):
    if all(D[k] < c if k in {'cats', 'trees'} else D[k] > c if k in {'pomeranians', 'goldfish'} else D[k] == c for k, c in s.items()):
      print(i + 1)
      break


part1()
part2()
