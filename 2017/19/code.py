import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  M = reader()
  x, y = (0, next(j for j in range(len(M[0])) if M[0][j] == '|'))
  dx, dy = (1, 0)
  s = ""
  while M[x][y] != ' ':
    if M[x][y].isalpha():
      s += M[x][y]
    if M[x][y] == '+':
      dx, dy = (dy, -dx) if M[x + dy][y - dx] != ' ' else (-dy, dx)
    x, y = x + dx, y + dy
  print(s)


def part2():
  M = reader()
  x, y = (0, next(j for j in range(len(M[0])) if M[0][j] == '|'))
  dx, dy = (1, 0)
  s = 0
  while M[x][y] != ' ':
    s += 1
    if M[x][y] == '+':
      dx, dy = (dy, -dx) if M[x + dy][y - dx] != ' ' else (-dy, dx)
    x, y = x + dx, y + dy
  print(s)


part1()
part2()
