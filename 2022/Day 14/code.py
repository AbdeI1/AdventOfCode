import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().split('\n')[:-1]


def part1():
  f = reader()
  grid = [['.' for _ in range(550)] for _ in range(170)]
  for l in f:
    points = l.split(' -> ')
    k = 0
    for k in range(1, len(points)):
      p0 = points[k - 1]
      p1 = points[k]
      x1, y1 = tuple(map(int, p0.split(',')))
      x2, y2 = tuple(map(int, p1.split(',')))
      if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2) + 1):
          grid[i][x1] = '#'
      else:
        for j in range(min(x1, x2), max(x1, x2) + 1):
          grid[y1][j] = '#'
  ans = 0
  while True:
    i, j = 0, 500
    while True:
      if i >= len(grid) - 1:
        break
      if grid[i + 1][j] != '#':
        i += 1
      elif grid[i + 1][j - 1] != '#':
        i += 1
        j -= 1
      elif grid[i + 1][j + 1] != '#':
        i += 1
        j += 1
      else:
        grid[i][j] = '#'
        ans += 1
        break
    if i >= len(grid) - 1:
      break
  print(ans)


def part2():
  f = reader()
  grid = [['.' for _ in range(750)] for _ in range(170)]
  maxy = 0
  for l in f:
    points = l.split(' -> ')
    k = 0
    for k in range(1, len(points)):
      p0 = points[k - 1]
      p1 = points[k]
      x1, y1 = tuple(map(int, p0.split(',')))
      x2, y2 = tuple(map(int, p1.split(',')))
      maxy = max(maxy, y1, y2)
      if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2) + 1):
          grid[i][x1] = '#'
      else:
        for j in range(min(x1, x2), max(x1, x2) + 1):
          grid[y1][j] = '#'
  ans = 0
  while True:
    i, j = 0, 500
    if grid[i][j] == '#':
      break
    while True:
      if i == maxy + 2:
        grid[i][j] = '#'
        break
      if grid[i + 1][j] != '#':
        i += 1
      elif grid[i + 1][j - 1] != '#':
        i += 1
        j -= 1
      elif grid[i + 1][j + 1] != '#':
        i += 1
        j += 1
      else:
        grid[i][j] = '#'
        ans += 1
        break
  print(ans)


part1()
part2()
