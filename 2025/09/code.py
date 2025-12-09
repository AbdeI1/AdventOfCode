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
      a = abs(f[i][0] - f[j][0] + 1) * abs(f[i][1] - f[j][1] + 1)
      A = max(A, a)
  print(A)


def part2():
  f = [eval(l) for l in reader()]
  f.append(f[0])
  V = [(p1, (p2[0] - p1[0], p2[1] - p1[1])) for p1, p2 in pairwise(f)]
  HV = [v if v[1][0] > 0 else ((v[0][0] + v[1][0], v[0][1]), (-v[1][0], 0)) for v in V if v[1][1] == 0]
  VV = [v if v[1][1] > 0 else ((v[0][0], v[0][1] + v[1][1]), (0, -v[1][1])) for v in V if v[1][0] == 0]
  # print(HV)
  # print(VV)
  A = 0
  for i in range(len(f)):
    for j in range(i + 1, len(f)):
      x1 = min(f[i][0], f[j][0])
      x2 = max(f[i][0], f[j][0])
      y1 = min(f[i][1], f[j][1])
      y2 = max(f[i][1], f[j][1])
      intersect = False
      icc = 0
      icd = 0
      for p, d in HV:
        if x1 in range(p[0] + 1, p[0] + d[0]) and p[1] in range(y1 + 1, y2):
          intersect = True
        if x2 in range(p[0] + 1, p[0] + d[0]) and p[1] in range(y1 + 1, y2):
          intersect = True
      for p, d in VV:
        if y1 in range(p[1] + 1, p[1] + d[1]) and p[0] in range(x1 + 1, x2):
          intersect = True
        if y2 in range(p[1] + 1, p[1] + d[1]) and p[0] in range(x1 + 1, x2):
          intersect = True
        if p[0] >= f[i][0] and f[j][1] in range(p[1], p[1] + d[1] + 1):
          icc += 1
        if p[0] >= f[j][0] and f[i][1] in range(p[1], p[1] + d[1] + 1):
          icd += 1
      if icc % 2 == 0 or icd % 2 == 0:
        intersect = True
      if intersect:
        break
      a = abs(f[i][0] - f[j][0] + 1) * abs(f[i][1] - f[j][1] + 1)
      A = max(A, a)
  print(A)


part1()
part2()
