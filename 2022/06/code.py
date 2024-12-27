import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  l = f[0]
  for i in range(len(l)):
    s = set()
    for j in range(4):
      s.add(l[i + j])
    if len(s) >= 4:
      print(i + 4)
      break


def part2():
  f = reader()
  l = f[0]
  for i in range(len(l)):
    s = set()
    for j in range(14):
      s.add(l[i + j])
    if len(s) >= 14:
      print(i + 14)
      break


part1()
part2()
