import os
os.chdir(os.path.dirname(__file__))
import sys
sys.path.append('..')
from intcode import compute
from threading import Thread
from time import sleep


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  print(sum(compute(list(map(int, reader()[0].split(','))), [
        x, y], [])[0] for x in range(50) for y in range(50)))


def part2():
  code = list(map(int, reader()[0].split(',')))
  G = [[' ' for _ in range(1500)] for _ in range(1500)]
  for y in range(20):
    for x in range(20):
      if compute(code, [x, y], [])[0]:
        G[y][x] = '#'

  lx, ly = next((x, y) for y in range(19, -1, -1)
                for x in range(20) if G[y][x] == '#')
  while ly in range(len(G)) and lx in range(len(G[ly]) - 1):
    while lx in range(len(G[ly]) - 1) and compute(code, [lx, ly + 1], [])[0] == 0:
      lx += 1
      if compute(code, [lx + 99, ly - 99], [])[0] == 1:
        print(lx * 10000 + ly - 99)
        return
      G[ly][lx] = '#'
    while ly in range(len(G) - 1) and compute(code, [lx, ly + 1], [])[0]:
      ly += 1
      if compute(code, [lx + 99, ly - 99], [])[0] == 1:
        print(lx * 10000 + ly - 99)
        return
      G[ly][lx] = '#'


part1()
part2()
