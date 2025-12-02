import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  R = [tuple(map(int, r.split('-'))) for r in f[0].split(',')]
  A = 0
  for r in R:
    for n in range(r[0], r[1] + 1):
      s = str(n)
      if len(s) % 2 == 0 and s[:len(s)//2] == s[len(s)//2:]:
        A += n
  print(A)


def part2():
  f = reader()
  R = [tuple(map(int, r.split('-'))) for r in f[0].split(',')]
  A = 0
  for r in R:
    for n in range(r[0], r[1] + 1):
      s = str(n)
      for l in range(1, len(s) // 2 + 1):
        if len(s) % l == 0 and s == s[:l] * (len(s) // l):
          A += n
          break
  print(A)

part1()
part2()
