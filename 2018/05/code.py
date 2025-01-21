import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()[0]
  i = 0
  while i < len(f):
    j = 0
    while i - 1 - j >= 0 and i + j < len(f):
      a, b = f[i - 1 - j], f[i + j]
      if a.upper() != b.upper() or a == b:
        break
      j += 1
    f = f[:i - j] + f[i + j:]
    i = (i - j) + 1
  print(len(f))


def part2():
  f = reader()[0]

  def react(f):
    i = 0
    while i < len(f):
      j = 0
      while i - 1 - j >= 0 and i + j < len(f):
        a, b = f[i - 1 - j], f[i + j]
        if a.upper() != b.upper() or a == b:
          break
        j += 1
      f = f[:i - j] + f[i + j:]
      i = (i - j) + 1
    return len(f)

  print(min(react(f.replace(l, '').replace(l.lower(), ''))
        for l in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))


part1()
part2()
