import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  D = 50
  A = 0
  for r in f:
    d = r[0]
    n = int(r[1:])
    if d == 'R':
      D += n
    else:
      D -= n
    D %= 100
    if D == 0:
      A += 1
  print(A)


def part2():
  f = reader()
  D = 50
  A = 0
  for r in f:
    d = r[0]
    n = int(r[1:])
    if d == 'R':
      A += ((D + n) // 100)
      D += n
    else:
      A += ((n + (-D % 100)) // 100)
      D -= n
    D %= 100
  print(A)


part1()
part2()
