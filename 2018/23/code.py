import os
os.chdir(os.path.dirname(__file__))
from itertools import combinations


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = sorted([tuple(map(eval, l[5:].split(">, r=")))[::-1] for l in reader()])
  R, P = f[-1]
  a = 0
  for _, p in f:
    if sum(abs(p[i] - P[i]) for i in range(3)) <= R:
      a += 1
  print(a)


def part2():
  f = [tuple(map(eval, l[5:].split(">, r=")))[::-1] for l in reader()]
  P = set()
  for r, (x, y, z) in f:
    P |= {(x + r, y, z), (x - r, y, z), (x, y + r, z),
          (x, y - r, z), (x, y, z + r), (x, y, z - r)}
  L = []
  for p1 in P:
    t = len([p2 for r, p2 in f if sum(abs(p1[i] - p2[i])
            for i in range(3)) <= r])
    L.append((t, p1))
  L.sort(key=lambda t: (-t[0], sum(map(abs, t[1]))))
  x, y, z = L[0][1]
  P = {(x + i % 3 - 1, y + (i // 3) % 3 - 1, z + (i // (3 ** 2)) % 3 - 1)
       for i in range(3 ** 3)}
  L = []
  for p1 in P:
    t = len([p2 for r, p2 in f if sum(abs(p1[i] - p2[i])
            for i in range(3)) <= r])
    L.append((t, p1))
  L.sort(key=lambda t: (-t[0], sum(map(abs, t[1]))))
  print(sum(map(abs, L[0][1])))


part1()
part2()
