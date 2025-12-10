import os
os.chdir(os.path.dirname(__file__))
from collections import deque
from heapq import heappop, heappush
import numpy
from pulp import *


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = [(l[1:l.find(']')], list(map(lambda x: eval(f'{{{x[1:-1]}}}'), l[l.find('('):l.find('{')-1].split())), eval(f'[{l[l.find('{')+1:-1]}]')) for l in reader()]
  A = 0
  for E, B, _ in f:
    E = tuple(1 if c == '#' else 0 for c in E)
    S = (0,) * len(E)
    Q = deque([(S, 0)])
    V = set()
    while len(Q) > 0:
      s, d = Q.popleft()
      if s in V:
        continue
      V.add(s)
      if s == E:
        A += d
        break
      for b in B:
        ns = tuple(s[i] if i not in b else (1 - s[i]) for i in range(len(s)))
        Q.append((ns, d + 1))
  print(A)


def part2():
  f = [(l[1:l.find(']')], list(map(lambda x: eval(f'{{{x[1:-1]}}}'), l[l.find('('):l.find('{')-1].split())), eval(f'({l[l.find('{')+1:-1]})')) for l in reader()]
  A = 0
  for _, B, E in f:
    M = numpy.array([[1 if i in b else 0 for i in range(len(E))] for b in B]).T
    Y = numpy.array(E)
    # X = M.T @ numpy.linalg.inv(M @ M.T) @ Y
    X = [LpVariable(f"x{i}", 0, cat=LpInteger) for i in range(len(B))]
    prob = LpProblem("problem", LpMinimize)
    for i in range(len(M)):
      prob += sum(X[j] if M[i][j] == 1 else 0 for j in range(len(M[i]))) == Y[i]
    prob += sum(X)
    prob.solve(PULP_CBC_CMD(msg=0))
    s = int(sum(value(x) for x in X))
    A += s
    # print(s)
  print(A)


part1()
part2()
