import pathlib


def reader():
  return open(f"{pathlib.Path(__file__).parent.resolve()}/input.txt", 'r').read().split('\n')[:-1]


def part1():
  print(sum(abs(n2 - n1) for n1, n2 in zip(*map(lambda t: sorted(list(t)), zip(
    *[map(int, s.split('   ')) for s in reader()])))))


def part2():
  (lambda l1, l2: print(sum(a * l2.count(a) for a in l1)))(*map(list, zip(
    *[map(int, s.split('   ')) for s in reader()])))


part1()
part2()
