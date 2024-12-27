import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = [tuple(map(eval, s.split('~'))) for s in reader()]
  ranges = [0, 0, 0]
  for i in range(3):
    ranges[i] = max([t1[i] for t1, _ in f] + [t2[i] for _, t2 in f]) + 1
  grid = [[[0 for _ in range(ranges[2])] for _ in range(ranges[1])]
          for _ in range(ranges[0])]
  support = {}
  for n, ((x1, y1, z1), (x2, y2, z2)) in enumerate(f, 1):
    support[n] = set()
    for i in range(x1, x2 + 1):
      for j in range(y1, y2 + 1):
        for k in range(z1, z2 + 1):
          grid[i][j][k] = n
  for z in range(ranges[2]):
    for x in range(ranges[0]):
      for y in range(ranges[1]):
        if grid[x][y][z]:
          n = grid[x][y][z]
          h = z
          flag = 0
          while h > 1:
            for i in range(f[n - 1][0][0], f[n - 1][1][0] + 1):
              for j in range(f[n - 1][0][1], f[n - 1][1][1] + 1):
                if grid[i][j][h - 1] != 0:
                  if grid[i][j][h - 1] != n:
                    support[n].add(grid[i][j][h - 1])
                  flag = 1
            if flag == 0:
              h -= 1
            else:
              break
          for i in range(f[n - 1][0][0], f[n - 1][1][0] + 1):
            for j in range(f[n - 1][0][1], f[n - 1][1][1] + 1):
              grid[i][j][z] = 0
              grid[i][j][h] = n
    required = set()
    for n in support:
      if len(support[n]) == 1:
        required = required.union(support[n])
  print(len(f) - len(required))


def part2():
  f = [tuple(map(eval, s.split('~'))) for s in reader()]
  ranges = [0, 0, 0]
  for i in range(3):
    ranges[i] = max([t1[i] for t1, _ in f] + [t2[i] for _, t2 in f]) + 1
  grid = [[[0 for _ in range(ranges[2])] for _ in range(ranges[1])]
          for _ in range(ranges[0])]
  support = {}
  reverse_map = {}
  for n, ((x1, y1, z1), (x2, y2, z2)) in enumerate(f, 1):
    support[n] = set()
    reverse_map[n] = set()
    for i in range(x1, x2 + 1):
      for j in range(y1, y2 + 1):
        for k in range(z1, z2 + 1):
          grid[i][j][k] = n
  for z in range(ranges[2]):
    for x in range(ranges[0]):
      for y in range(ranges[1]):
        if grid[x][y][z]:
          n = grid[x][y][z]
          h = z
          flag = 0
          while h > 1:
            for i in range(f[n - 1][0][0], f[n - 1][1][0] + 1):
              for j in range(f[n - 1][0][1], f[n - 1][1][1] + 1):
                if grid[i][j][h - 1] != 0:
                  if grid[i][j][h - 1] != n:
                    support[n].add(grid[i][j][h - 1])
                    reverse_map[grid[i][j][h - 1]].add(n)
                  flag = 1
            if flag == 0:
              h -= 1
            else:
              break
          for i in range(f[n - 1][0][0], f[n - 1][1][0] + 1):
            for j in range(f[n - 1][0][1], f[n - 1][1][1] + 1):
              grid[i][j][z] = 0
              grid[i][j][h] = n
    required = set()
    for n in support:
      if len(support[n]) == 1:
        required = required.union(support[n])
  ans = 0
  for n in range(1, len(f) + 1):
    s = {k: {i for i in v} for k, v in support.items()}
    q = [n]
    while q:
      b = q.pop(0)
      for o in reverse_map[b]:
        s[o].remove(b)
        if len(s[o]) == 0:
          ans += 1
          q.append(o)
  print(ans)


part1()
part2()
