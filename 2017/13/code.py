import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  print(sum(t * d for t, d in eval(f'{{{', '.join(reader())}}}').items() if t % (2 * (d - 1)) == 0))


def part2():
  f = eval(f'{{{', '.join(reader())}}}')
  M = [(2 * (d - 1)) for _, d in f.items()]
  l = [t % (2 * (d - 1)) for t, d in f.items()]
  D = 0
  while 0 in [(t + D) % (2 * (d - 1)) for t, d in f.items()]:
    D += 2
  print(D)


part1()
part2()
