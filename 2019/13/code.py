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
  code = list(map(int, reader()[0].split(',')))
  out = compute(code, [])
  print([out[i] for i in range(2, len(out), 3)].count(2))


def part2():
  code = list(map(int, reader()[0].split(',')))
  out = compute(code, [], [])
  G = [[0 for _ in range(max(out[0::3]) + 1)]
       for _ in range(max(out[1::3]) + 1)]
  code[0] = 2
  I = []
  O = []
  T = Thread(target=compute, args=(code, I, O))
  T.start()
  while len(O) < (len(G) * len(G[0]) + 1) * 3:
    sleep(0)
  for _ in range(len(G) * len(G[0])):
    x, y, t = O.pop(0), O.pop(0), O.pop(0)
    G[y][x] = t
  _, _, score = O.pop(0), O.pop(0), O.pop(0)
  while T.is_alive():
    t = -1
    while t < len(O):
      t = len(O)
      sleep(0.0001)
    while len(O) >= 3:
      x, y, t = O.pop(0), O.pop(0), O.pop(0)
      if x == -1 and y == 0:
        score = t
      else:
        G[y][x] = t
    ball = next(x for x in range(len(G[y]))
                for y in range(len(G)) if G[y][x] == 4)
    paddle = [x for x in range(42) if G[-2][x] == 3][0]
    I.append((ball > paddle) - (ball < paddle))
  print(score)


part1()
part2()
