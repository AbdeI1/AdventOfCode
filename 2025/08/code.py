import os
os.chdir(os.path.dirname(__file__))
from math import sqrt, prod
from collections import defaultdict


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = [eval(l) for l in reader()]
  C = 1000
  L = []
  for i in range(len(f)):
    for j in range(i + 1, len(f)):
      d = sqrt(sum((f[j][k] - f[i][k]) ** 2 for k in range(3)))
      L.append((d, (i, j)))
  L.sort()
  P = [i for i in range(len(f))]

  def find(x):
    if x != P[x]:
      P[x] = find(P[x])
    return P[x]

  for _, (i, j) in L[:C]:
    if find(i) != find(j):
      P[find(i)] = P[find(j)]
      C -= 1
    if C <= 1:
      break

  D = defaultdict(int)
  for i in range(len(f)):
    D[find(i)] += 1

  print(prod(sorted(D.values(), reverse=True)[:3]))


def part2():
  f = [eval(l) for l in reader()]
  L = []
  for i in range(len(f)):
    for j in range(i + 1, len(f)):
      d = sqrt(sum((f[j][k] - f[i][k]) ** 2 for k in range(3)))
      L.append((d, (i, j)))
  L.sort()
  P = [i for i in range(len(f))]

  def find(x):
    if x != P[x]:
      P[x] = find(P[x])
    return P[x]

  C = 0
  for _, (i, j) in L:
    if find(i) != find(j):
      P[find(i)] = P[find(j)]
      C += 1
    if C == len(P) - 1:
      print(f[i][0] * f[j][0])
      break


part1()
part2()
