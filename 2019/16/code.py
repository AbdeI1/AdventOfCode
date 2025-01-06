import os
os.chdir(os.path.dirname(__file__))
import numpy as np
from itertools import accumulate


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  l = list(map(int, reader()[0]))
  T = [[0 for _ in range(len(l))] for _ in range(len(l))]
  for i in range(len(l)):
    for j in range(len(l)):
      T[i][j] = (0, 1, 0, -1)[((j + 1) // (i + 1)) % 4]

  T = np.array(T)
  l = np.array(l)

  def fft(l): return abs(T @ l) % 10

  for _ in range(100):
    l = fft(l)

  print(''.join(map(str, l[:8])))


def part2():
  n = list(map(int, reader()[0] * 10000))
  o = int(''.join(map(str, n[:7])))

  print(''.join(map(str, (lambda v: [v := [abs(x) % 10 for x in list(accumulate(v[::-1]))[::-1]]
                                     for _ in range(100)])(n[o:])[-1][:8])))


part1()
part2()
