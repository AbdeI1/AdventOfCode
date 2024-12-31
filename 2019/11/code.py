import os
os.chdir(os.path.dirname(__file__))
import sys
sys.path.append('..')
from intcode import compute
from threading import Thread
from time import sleep
from collections import defaultdict
import threading


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  code = list(map(int, reader()[0].split(',')))
  I, O = [], []
  T = Thread(target=compute, args=(code, I, O))
  T.start()
  P = 0, 0
  D = (0, 1)
  M = defaultdict(int)
  M[P] = 0
  while T.is_alive():
    I.append(M[P])
    while len(O) < 2:
      sleep(0)
    c, t = O.pop(0), O.pop(0)
    M[P] = c
    D = (D[1], -D[0]) if t else (-D[1], D[0])
    P = P[0] + D[0], P[1] + D[1]
  print(len(M))


def part2():
  code = list(map(int, reader()[0].split(',')))
  I, O = [], []
  T = Thread(target=compute, args=(code, I, O))
  T.start()
  P = 0, 0
  D = (0, 1)
  M = defaultdict(int)
  M[P] = 1
  while T.is_alive():
    I.append(M[P])
    while len(O) < 2:
      sleep(0)
    c, t = O.pop(0), O.pop(0)
    M[P] = c
    D = (D[1], -D[0]) if t else (-D[1], D[0])
    P = P[0] + D[0], P[1] + D[1]
  X, Y = zip(*M.keys())
  xl, xr = min(X), max(X)
  yd, yu = min(Y), max(Y)
  A = [['■' if M[(x, y)] else ' ' for x in range(xl, xr + 1)]
       for y in range(yu, yd - 1, -1)]
  for r in A:
    print(''.join(r))


part1()
part2()
