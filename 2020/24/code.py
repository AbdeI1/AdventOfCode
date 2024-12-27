import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  flippedTiles = []
  for line in f:
    i = 0
    pos = [0, 0]
    while i < len(line):
      direction = ""
      if line[i] == 's' or line[i] == 'n':
        direction = line[i] + line[i + 1]
        i += 1
      else:
        direction = line[i]
      if direction == "ne":
        pos = [pos[0] + 0.5, pos[1] + 0.5]
      elif direction == "nw":
        pos = [pos[0] - 0.5, pos[1] + 0.5]
      elif direction == "se":
        pos = [pos[0] + 0.5, pos[1] - 0.5]
      elif direction == "sw":
        pos = [pos[0] - 0.5, pos[1] - 0.5]
      elif direction == "e":
        pos = [pos[0] + 1, pos[1]]
      elif direction == "w":
        pos = [pos[0] - 1, pos[1]]
      i += 1
    if pos not in flippedTiles:
      flippedTiles.append(pos)
    else:
      flippedTiles.remove(pos)
  print(len(flippedTiles))


def part2():
  f = reader()
  D = (2000, 2000)
  grid = [[1 for _ in range(D[0])] for _ in range(D[1])]
  for l in f:
    x, y = D[0] // 2, D[1] // 2
    i = 0
    while i < len(l):
      d = ""
      if l[i] == 's' or l[i] == 'n':
        d = l[i] + l[i + 1]
        i += 1
      else:
        d = l[i]
      if d == "ne":
        x += 1
        y += 1
      elif d == "nw":
        x += 1
        y -= 1
      elif d == "se":
        x -= 1
        y += 1
      elif d == "sw":
        x -= 1
        y -= 1
      elif d == "e":
        y += 2
      elif d == "w":
        y -= 2
      i += 1
    grid[x][y] = 1 - grid[x][y]
  for _ in range(100):
    grid = simulate(grid)
  ans = 0
  for i in grid:
    for j in i:
      if j == 0:
        ans += 1
  print(ans)


def simulate(grid):
  ng = [[1 for _ in range(len(grid[i]))] for i in range(len(grid))]
  for i in range(2, len(grid) - 2):
    for j in range(3 if i % 2 == 1 else 2, len(grid[i]) - 2, 2):
      ng[i][j] = grid[i][j]
      c = 6
      c -= grid[i + 1][j + 1]
      c -= grid[i + 1][j - 1]
      c -= grid[i - 1][j + 1]
      c -= grid[i - 1][j - 1]
      c -= grid[i][j + 2]
      c -= grid[i][j - 2]
      if grid[i][j] == 1 and c == 2:
        ng[i][j] = 0
      if grid[i][j] == 0 and (c == 0 or c > 2):
        ng[i][j] = 1
  return ng


part1()
part2()
