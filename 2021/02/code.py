import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  x = 0
  y = 0
  for l in f:
    d = l.split(' ')
    dist = int(d[1])
    if d[0] == "forward":
      x += dist
    elif d[0] == "up":
      y -= dist
    elif d[0] == "down":
      y += dist
  print(x * y)


def part2():
  f = reader()
  x = 0
  y = 0
  aim = 0
  for l in f:
    d = l.split(' ')
    dist = int(d[1])
    if d[0] == "forward":
      x += dist
      y += aim * dist
    elif d[0] == "up":
      aim -= dist
    elif d[0] == "down":
      aim += dist
  print(x * y)


part1()
part2()
