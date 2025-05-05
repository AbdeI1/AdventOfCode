import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = [(l[0], int(l[1:])) for l in reader()[0].split(', ')]
  x, y = 0, 0
  dx, dy = 0, 1
  for r, d in f:
    match r:
      case 'R': dx, dy = dy, -dx
      case 'L': dx, dy = -dy, dx
    x, y = x + d * dx, y + d * dy
  print(abs(x) + abs(y))


def part2():
  f = [(l[0], int(l[1:])) for l in reader()[0].split(', ')]
  x, y = 0, 0
  dx, dy = 0, 1
  V = {(x, y)}
  for r, d in f:
    match r:
      case 'R': dx, dy = dy, -dx
      case 'L': dx, dy = -dy, dx
    for _ in range(d):
      x, y = x + dx, y + dy
      if (x, y) in V:
        print(abs(x) + abs(y))
        break
      V.add((x, y))
    else:
      continue
    break


part1()
part2()
