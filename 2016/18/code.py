import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()[0]

  def triwise(l):
    a, b = l[:2]
    for c in l[2:]:
      yield a, b, c
      a, b = b, c

  A = 0
  for _ in range(40):
    A += f.count('.')
    f = ''.join('^' if (a, b, c) in {('^', '^', '.'), ('.', '^', '^'), (
      '^', '.', '.'), ('.', '.', '^')} else '.' for a, b, c in triwise(f'.{f}.'))

  print(A)


def part2():
  f = reader()[0]

  def triwise(l):
    a, b = l[:2]
    for c in l[2:]:
      yield a, b, c
      a, b = b, c

  A = 0
  for _ in range(400000):
    A += f.count('.')
    f = ''.join('^' if (a, b, c) in {('^', '^', '.'), ('.', '^', '^'), (
      '^', '.', '.'), ('.', '.', '^')} else '.' for a, b, c in triwise(f'.{f}.'))

  print(A)


part1()
part2()
