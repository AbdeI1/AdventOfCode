import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  A, B = map(lambda s: int(s.split()[-1]), reader())

  s = 0
  for _ in range(40000000):
    A = (A * 16807) % 2147483647
    B = (B * 48271) % 2147483647
    if (A & 0xffff) == (B & 0xffff):
      s += 1

  print(s)


def part2():
  A, B = map(lambda s: int(s.split()[-1]), reader())

  s = 0
  for _ in range(5000000):
    A = (A * 16807) % 2147483647
    while A % 4 != 0:
      A = (A * 16807) % 2147483647
    B = (B * 48271) % 2147483647
    while B % 8 != 0:
      B = (B * 48271) % 2147483647
    if (A & 0xffff) == (B & 0xffff):
      s += 1

  print(s)


# part1()
part2()
