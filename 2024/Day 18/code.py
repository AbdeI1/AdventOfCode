import pathlib


def reader():
  return open(f"{pathlib.Path(__file__).parent.resolve()}/input.txt", 'r').read().split('\n')[:-1]


def part1():
  f = list(map(eval, reader()))
  W, H = 71, 71
  G = [['.' for _ in range(W)] for _ in range(H)]
  for x, y in f[:1024]:
    G[y][x] = '#'
  D = [(1, 0), (-1, 0), (0, 1), (0, -1)]
  q = [(0, 0, 0)]
  V = set()
  while q:
    d, x, y = q.pop(0)
    if (x, y) in V:
      continue
    V.add((x, y))
    if (x, y) == (W - 1, H - 1):
      print(d)
      break
    for dx, dy in D:
      xx, yy = x + dx, y + dy
      if yy in range(len(G)) and xx in range(len(G[yy])) and G[yy][xx] == '.':
        q.append((d + 1, xx, yy))


def part2():
  f = list(map(eval, reader()))
  W, H = 71, 71
  G = [['.' for _ in range(W)] for _ in range(H)]
  D = [(1, 0), (-1, 0), (0, 1), (0, -1)]

  def bfs():
    q = [(0, 0, 0)]
    V = set()
    while q:
      d, x, y = q.pop(0)
      if (x, y) in V:
        continue
      V.add((x, y))
      if (x, y) == (W - 1, H - 1):
        return True
      for dx, dy in D:
        xx, yy = x + dx, y + dy
        if yy in range(len(G)) and xx in range(len(G[yy])) and G[yy][xx] == '.':
          q.append((d + 1, xx, yy))
    return False

  n = len(f)

  for x, y in f:
    G[x][y] = '#'
    if not bfs():
      print(x, y)
      break


part1()
part2()
