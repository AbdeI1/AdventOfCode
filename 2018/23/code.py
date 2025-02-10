import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = sorted([tuple(map(eval, l[5:].split(">, r=")))[::-1] for l in reader()])
  R, P = f[-1]
  a = 0
  for _, p in f:
    if sum(abs(p[i] - P[i]) for i in range(3)) <= R:
      a += 1
  print(a)


def part2():
  pass


part1()
part2()
