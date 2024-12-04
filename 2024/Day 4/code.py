import pathlib
import re


def reader():
  return open(f"{pathlib.Path(__file__).parent.resolve()}/input.txt", 'r').read().split('\n')[:-1]


def part1():
  f = reader()
  c = 0
  D = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
  word = "XMAS"
  for i in range(len(f)):
    for j in range(len(f[i])):
      for d in D:
        ii, jj = i, j
        wi = 0
        while wi < len(word) and ii in range(len(f)) and jj in range(len(f[ii])) and f[ii][jj] == word[wi]:
          wi += 1
          ii, jj = ii + d[0], jj + d[1]
        if wi == len(word):
          c += 1
  print(c)


def part2():
  f = reader()
  c = 0
  for i in range(1, len(f) - 1):
    for j in range(1, len(f[i]) - 1):
      if f[i][j] == 'A':
        if ((f[i - 1][j - 1] == 'M' and f[i + 1][j + 1] == 'S') or (f[i - 1][j - 1] == 'S' and f[i + 1][j + 1] == 'M')) and ((f[i + 1][j - 1] == 'M' and f[i - 1][j + 1] == 'S') or (f[i + 1][j - 1] == 'S' and f[i - 1][j + 1] == 'M')):
          c += 1
  print(c)


part1()
part2()
