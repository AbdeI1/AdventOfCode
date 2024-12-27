import os
os.chdir(os.path.dirname(__file__))
import re


def reader():
  return open(f"input.txt", 'r').read().splitlines()


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
  print((lambda f: len(re.findall(
    f'(?=(M.M.{{{len(f[0]) - 2}}}A.{{{len(f[0]) - 2}}}S.S|M.S.{{{len(f[0]) - 2}}}A.{{{len(f[0]) - 2}}}M.S|S.M.{{{len(f[0]) - 2}}}A.{{{len(f[0]) - 2}}}S.M|S.S.{{{len(f[0]) - 2}}}A.{{{len(f[0]) - 2}}}M.M))', ''.join(f))))(reader()))


part1()
part2()
