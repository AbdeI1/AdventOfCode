import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  G = [list(s) for s in reader()]
  for _ in range(100):
    G = [
      [
        ('#' if [G[ii][jj] for ii in range(max(0, i - 1), min(len(G), i + 2))
         for jj in range(max(0, j - 1), min(len(G[ii]), j + 2)) if (ii, jj) != (i, j)].count('#') in range(2, 4) else '.')
        if G[i][j] == '#' else
        ('#' if [G[ii][jj] for ii in range(max(0, i - 1), min(len(G), i + 2))
         for jj in range(max(0, j - 1), min(len(G[ii]), j + 2)) if (ii, jj) != (i, j)].count('#') == 3 else '.')
        for j in range(len(G[i]))
      ]
      for i in range(len(G))
    ]
  print(sum(l.count('#') for l in G))


def part2():
  G = [list(s) for s in reader()]
  for _ in range(100):
    G = [
      [
        ('#' if [G[ii][jj] for ii in range(max(0, i - 1), min(len(G), i + 2))
         for jj in range(max(0, j - 1), min(len(G[ii]), j + 2)) if (ii, jj) != (i, j)].count('#') in range(2, 4) else '.')
        if G[i][j] == '#' else
        ('#' if [G[ii][jj] for ii in range(max(0, i - 1), min(len(G), i + 2))
         for jj in range(max(0, j - 1), min(len(G[ii]), j + 2)) if (ii, jj) != (i, j)].count('#') == 3 else '.')
        for j in range(len(G[i]))
      ]
      for i in range(len(G))
    ]
    for i, j in [(0, 0), (-1, 0), (-1, -1), (0, -1)]:
      G[i][j] = '#'
  print(sum(l.count('#') for l in G))


part1()
part2()
