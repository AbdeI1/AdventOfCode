import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  s = reader()[0]
  N = 272
  while len(s) < N:
    s = f"{s}0{s[::-1].replace('0', '2').replace('1', '0').replace('2', '1')}"
  s = s[:N]
  c = s
  while len(c) % 2 == 0:
    c = ''.join('1' if c[i] == c[i + 1] else '0' for i in range(0, len(c), 2))
  print(c)


def part2():
  s = reader()[0]
  N = 35651584
  while len(s) < N:
    s = f"{s}0{s[::-1].replace('0', '2').replace('1', '0').replace('2', '1')}"
  s = s[:N]
  c = s
  while len(c) % 2 == 0:
    c = ''.join('1' if c[i] == c[i + 1] else '0' for i in range(0, len(c), 2))
  print(c)


part1()
part2()
