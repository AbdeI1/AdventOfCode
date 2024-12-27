import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  t = 0
  for l in reader():
    r, n = l.split(": ")
    r = int(r)
    n = list(map(int, n.split(" ")))
    for i in range(1 << (len(n) - 1)):
      x = n[0]
      for b in range(len(n) - 1):
        if ((i >> b) & 1):
          x += n[b + 1]
        else:
          x *= n[b + 1]
      if x == r:
        t += r
        break
  print(t)


def part2():
  t = 0
  for l in reader():
    r, n = l.split(": ")
    r = int(r)
    n = list(map(int, n.split(" ")))
    for i in range(3 ** (len(n) - 1)):
      x = n[0]
      for b in range(len(n) - 1):
        a = (i // (3 ** b))
        if a % 3 == 0:
          x += n[b + 1]
        elif a % 3 == 1:
          x *= n[b + 1]
        else:
          x = int(str(x) + str(n[b + 1]))
      if x == r:
        t += r
        break
  print(t)


part1()
part2()
