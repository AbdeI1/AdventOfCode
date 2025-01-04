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
  I = [[i] for i in range(50)]
  O = [[] for _ in range(50)]
  T = [Thread(target=compute, args=(code, I[i], O[i], False), daemon=True)
       for i in range(50)]
  for t in T:
    t.start()

  while True:
    for i in range(50):
      while O[i]:
        a, x, y = O[i].pop(0), O[i].pop(0), O[i].pop(0)
        if a == 255:
          print(y)
          return
        I[a].extend([x, y])
    sleep(0)


def part2():
  code = list(map(int, reader()[0].split(',')))
  I = [[i] for i in range(50)]
  O = [[] for _ in range(50)]
  T = [Thread(target=compute, args=(code, I[i], O[i], False), daemon=True)
       for i in range(50)]
  for t in T:
    t.start()

  X, Y = -1, -1
  Yp = -1

  while True:
    c = 0
    for i in range(50):
      if O[i]:
        while O[i]:
          a, x, y = O[i].pop(0), O[i].pop(0), O[i].pop(0)
          if a == 255:
            X, Y = x, y
            continue
          I[a].extend([x, y])
      else:
        c += 1
    if c == 50:
      if Y == Yp:
        print(Y)
        return
      Yp = Y
      I[0].extend([X, Y])
    sleep(0.2)


part1()
part2()
