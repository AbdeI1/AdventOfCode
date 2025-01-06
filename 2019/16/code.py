import os
os.chdir(os.path.dirname(__file__))
import numpy as np
from functools import cache


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  l = list(map(int, reader()[0] * 4))
  T = [[0 for _ in range(len(l))] for _ in range(len(l))]
  for i in range(len(l)):
    for j in range(len(l)):
      T[i][j] = (0, 1, 0, -1)[((j + 1) // (i + 1)) % 4]

  T = np.array(T)
  l = np.array(l)
  np.set_printoptions(threshold=np.inf)

  print(T)

  def fft(l): return abs(T @ l) % 10

  print(l)
  print(fft(l))
  print(fft(fft(l)))
  print(fft(fft(fft(l))))

  for _ in range(1):
    l = fft(l)

  print(''.join(map(str, l[:8])))


def part2():
  n = list(map(int, reader()[0] * 10000))
  o = int(''.join(map(str, n[:7])))

  @cache
  def dig(l, i):
    if l == 0:
      return n[i % len(n)]
    x, m = 0, -1
    for y in range(-1, len(n), i + 1):
      m = (m + 1) % 4
      if m % 2 == 0:
        continue
      t = sum([dig(l - 1, j) for j in range(y, min(len(n), y + i + 1))])
      if m == 1:
        x += t
      else:
        x -= t
    return abs(x) % 10

  # print(dig(1, 651))
  # o = 0
  # print(''.join(map(str, [dig(100, i) for i in range(o, o + 8)])))


part1()
# part2()

5971873
65100000
