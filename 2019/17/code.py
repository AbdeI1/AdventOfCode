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
  G = ''.join(map(chr, compute(code, [], []))).strip().splitlines()
  a = 0
  for i in range(1, len(G) - 1):
    for j in range(1, len(G[i]) - 1):
      if G[i][j] == '#' and G[i - 1][j] == '#' and G[i + 1][j] == '#' and G[i][j - 1] == '#' and G[i][j + 1] == '#':
        a += i * j
  print(a)


def part2():
  code = list(map(int, reader()[0].split(',')))
  code[0] = 2
  I, O = [], []
  T = Thread(target=compute, args=(code, I, O), daemon=True)
  T.start()
  while len(O) < 6 or ''.join(map(chr, O[-6:-1])) != 'Main:':
    sleep(0)
  G = ''.join(map(chr, O[:-6])).strip().splitlines()
  x, y = next((i, j) for i in range(len(G))
              for j in range(len(G[i])) if G[i][j] in set('^v<>'))
  dx, dy = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
  }[G[x][y]]
  V = set()
  P = []
  while (x, y) not in V:
    V.add((x, y))
    Lx, Ly = x, y
    while Lx - dy in range(len(G)) and Ly + dx in range(len(G[Lx - dy])) and G[Lx - dy][Ly + dx] == '#':
      Lx, Ly = Lx - dy, Ly + dx
    if (Lx, Ly) != (x, y):
      P.append('L')
      P.append(str(abs(x - Lx) + abs(y - Ly)))
      x, y = Lx, Ly
      dx, dy = -dy, dx
      continue
    Rx, Ry = x, y
    while Rx + dy in range(len(G)) and Ry - dx in range(len(G[Rx + dy])) and G[Rx + dy][Ry - dx] == '#':
      Rx, Ry = Rx + dy, Ry - dx
    if (Rx, Ry) != (x, y):
      P.append('R')
      P.append(str(abs(x - Rx) + abs(y - Ry)))
      x, y = Rx, Ry
      dx, dy = dy, -dx
  S = ','.join(P)
  ABC = ['', '', '']
  s, i, j = 0, 0, 2
  while j < len(P):
    t = ','.join(P[i:j])
    if len(t) > 20:
      i += ABC[s].count(',') + 1
      j = i
      S = S.replace(ABC[s], chr(ord('A') + s))
      s += 1
    if s > 2:
      break
    if S.count(t) > 1:
      ABC[s] = t
    if t in ABC[:s]:
      i = j
    j += 2
  I.extend(map(ord, '\n'.join([S] + ABC + ['n\n'])))
  sleep(0.1)
  print(O[-1])


part1()
part2()
