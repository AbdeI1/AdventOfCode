import os
os.chdir(os.path.dirname(__file__))
from functools import reduce


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  W, H = 25, 6
  layers = (lambda d: [[d[(i + h):(i + h + W)]
            for h in range(0, W * H, W)] for i in range(0, len(d), W * H)])(list(map(int, reader()[0])))
  l = min(layers, key=lambda l: sum(x.count(0) for x in l))
  print(sum(x.count(1) for x in l) * sum(x.count(2) for x in l))


def part2():
  W, H = 25, 6
  layers = (lambda d: [[d[(i + h):(i + h + W)]
            for h in range(0, W * H, W)] for i in range(0, len(d), W * H)])(list(map(int, reader()[0])))
  img = [[reduce(lambda x, y: y if x == 2 else x, (l[i][j]
                 for l in layers), 2) for j in range(W)] for i in range(H)]
  for i in img:
    print(''.join(' ' if x == 0 else '■' for x in i))


part1()
part2()
