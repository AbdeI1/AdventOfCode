import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  toggle = lambda x: 1 - x
  on = lambda x: 1
  off = lambda x: 0
  f = [(lambda l: (toggle, eval(l[1]), eval(l[3])) if l[0] == 'toggle' else (on, eval(l[2]), eval(
    l[4])) if l[1] == 'on' else (off, eval(l[2]), eval(l[4])))(l.split()) for l in reader()]
  W, H = 1000, 1000
  G = [[0 for _ in range(W)] for _ in range(H)]
  for op, (sx, sy), (ex, ey) in f:
    for i in range(sx, ex + 1):
      for j in range(sy, ey + 1):
        G[i][j] = op(G[i][j])
  print(sum(map(sum, G)))


def part2():
  toggle = lambda x: x + 2
  on = lambda x: x + 1
  off = lambda x: max(0, x - 1)
  f = [(lambda l: (toggle, eval(l[1]), eval(l[3])) if l[0] == 'toggle' else (on, eval(l[2]), eval(
    l[4])) if l[1] == 'on' else (off, eval(l[2]), eval(l[4])))(l.split()) for l in reader()]
  W, H = 1000, 1000
  G = [[0 for _ in range(W)] for _ in range(H)]
  for op, (sx, sy), (ex, ey) in f:
    for i in range(sx, ex + 1):
      for j in range(sy, ey + 1):
        G[i][j] = op(G[i][j])
  print(sum(map(sum, G)))


part1()
part2()
