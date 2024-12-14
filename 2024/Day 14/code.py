import pathlib
from PIL import Image
import numpy as np


def reader():
  return open(f"{pathlib.Path(__file__).parent.resolve()}/input.txt", 'r').read().split('\n')[:-1]


def part1():
  f = [(tuple(map(int, l[2:l.find(" ")].split(','))), tuple(
    map(int, l[l.find("v") + 2:].split(',')))) for l in reader()]
  P = []
  W, H = 101, 103
  for (x, y), (vx, vy) in f:
    P.append(((x + vx * 100) % W, (y + vy * 100) % H))
  Q = [[0, 0], [0, 0]]
  for (x, y) in P:
    if x == W // 2 or y == H // 2:
      continue
    Q[0 if x < W // 2 else 1][0 if y < H // 2 else 1] += 1
  print(Q[0][0] * Q[0][1] * Q[1][0] * Q[1][1])


def part2():
  f = [(tuple(map(int, l[2:l.find(" ")].split(','))), tuple(
    map(int, l[l.find("v") + 2:].split(',')))) for l in reader()]
  P = []
  W, H = 101, 103
  I = []
  for s in range(W * H):
    G = [[0 for _ in range(W)] for _ in range(H)]
    for (x, y), (vx, vy) in f:
      G[(y + vy * s) % H][(x + vx * s) % W] = 255
    I.append(G)
  for t, i in enumerate(I):
    Image.fromarray(np.array(i, dtype=np.uint8)).save(
      f"{pathlib.Path(__file__).parent.resolve()}/images/{t}.png")


def original_part2():
  f = [(tuple(map(int, l[2:l.find(" ")].split(','))), tuple(
    map(int, l[l.find("v") + 2:].split(',')))) for l in reader()]
  P = []
  W, H = 101, 103
  I = []
  for s in range(W * H):
    G = [[0 for _ in range(W)] for _ in range(H)]
    for (x, y), (vx, vy) in f:
      G[(y + vy * s) % H][(x + vx * s) % W] = 255
    I.append(G)
  for t, i in enumerate(I):
    Image.fromarray(np.array(i, dtype=np.uint8)).save(
      f"{pathlib.Path(__file__).parent.resolve()}/images/{t}.png")


part1()
part2()
