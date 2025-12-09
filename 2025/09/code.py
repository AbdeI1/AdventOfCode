import os
os.chdir(os.path.dirname(__file__))
from itertools import pairwise


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = [eval(l) for l in reader()]
  A = 0
  for i in range(len(f)):
    for j in range(i + 1, len(f)):
      a = (abs(f[i][0] - f[j][0]) + 1) * (abs(f[i][1] - f[j][1]) + 1)
      A = max(A, a)
  print(A)


def part2():
  f = [eval(l) for l in reader()]
  f.append(f[0])
  V = [(p1, (p2[0] - p1[0], p2[1] - p1[1])) for p1, p2 in pairwise(f)]
  HV = [v if v[1][0] > 0 else ((v[0][0] + v[1][0], v[0][1]), (-v[1][0], 0)) for v in V if v[1][1] == 0]
  VV = [v if v[1][1] > 0 else ((v[0][0], v[0][1] + v[1][1]), (0, -v[1][1])) for v in V if v[1][0] == 0]
  A = 0
  for i in range(len(f) - 1):
    for j in range(i + 1, len(f) - 1):
      x1 = min(f[i][0], f[j][0])
      x2 = max(f[i][0], f[j][0])
      y1 = min(f[i][1], f[j][1])
      y2 = max(f[i][1], f[j][1])
      intersect = False
      for p, d in HV:
        if p[0] + d[0] > x1 and p[0] < x2 and p[1] in range(y1 + 1, y2):
         intersect = True
      for p, d in VV:
        if p[1] + d[1] > y1 and p[1] < y2 and p[0] in range(x1 + 1, x2):
         intersect = True
      if intersect:
        continue
      a = (x2 - x1 + 1) * (y2 - y1 + 1)
      A = max(A, a)
  print(A)

part1()
part2()
