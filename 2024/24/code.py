import os
os.chdir(os.path.dirname(__file__))
from functools import cache
import re
from itertools import chain


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = '\n'.join(reader()).split('\n\n')
  B = {}
  for l in f[0].split('\n'):
    v, b = l.split(': ')
    B[v] = int(b)
  F = {}
  D = {}
  for l in f[1].split('\n'):
    f, v = l.split(' -> ')
    v1, op, v2 = f.split(' ')
    D[v] = {v1, v2}
    op = {'XOR': '^', 'AND': '&', 'OR': '|'}[op]
    F[v] = f"{v1} {op} {v2}"
    for vv in [v, v1, v2]:
      if vv not in B:
        B[vv] = None

  def r(v):
    if B[v] is None:
      for dv in D[v]:
        r(dv)
      B[v] = eval(F[v], None, B)
    return B[v]

  for v in B:
    r(v)

  print(int(''.join(map(lambda t: str(t[1]), sorted(
    filter(lambda t: t[0][0] == 'z', B.items()), reverse=True))), base=2))


def part2():
  f = '\n'.join(reader()).split('\n\n')
  B = {}
  for l in f[0].split('\n'):
    v, b = l.split(': ')
    B[v] = int(b)
  F = {}
  D = {}
  for l in f[1].split('\n'):
    f, v = l.split(' -> ')
    v1, op, v2 = f.split(' ')
    v1, v2 = sorted((v1, v2))
    D[v] = {v1, v2}
    op = {'XOR': '^', 'AND': '&', 'OR': '|'}[op]
    F[v] = f"{v1} {op} {v2}"
    for vv in [v, v1, v2]:
      if vv not in B:
        B[vv] = None

  def swap(s1, s2):
    F[s1], F[s2] = F[s2], F[s1]
    D[s1], D[s2] = D[s2], D[s1]

  # swap('z15', 'jgc')
  # swap('z22', 'drg')
  # swap('z35', 'jbp')
  # swap('qjb', 'gvw')

  def r(v):
    if B[v] is None:
      for dv in D[v]:
        r(dv)
      B[v] = eval(F[v], None, B)
    return B[v]

  def getNum(s): return int(''.join(map(lambda t: str(t[1]), sorted(
    filter(lambda t: t[0][0] == s, B.items()), reverse=True))), base=2)

  for v in B:
    r(v)

  @cache
  def getFullFormula(v):
    if v[0] in {'x', 'y'}:
      return v
    v1, op, v2 = F[v].split(' ')
    v1, v2 = sorted((v1, v2))
    return f"({getFullFormula(v1)}) {op} ({getFullFormula(v2)})"

  FD = {}
  for v in D:
    formula = getFullFormula(v)
    FD[v] = set(re.findall(r'x\d{2}|y\d{2}', formula))

  problems = []
  for i in range(1, len(list(filter(lambda t: t[0][0] == 'z', B.items()))) - 1):
    p = f'((x{i:02}) ^ (y{i:02}))'
    formula = getFullFormula(f'z{i:02}')
    if f'{p} ^' not in formula and f'^ {p}' not in formula:
      problems.append(i)

  swaps = []
  for p in problems:
    x = f'x{p:02}'
    y = f'y{p:02}'
    z = f'z{p:02}'
    start = f'{x} ^ {y}'
    p1 = next(filter(lambda t: t[1] == start, F.items()))[0]
    v1, op, v2 = F[z].split(' ')
    if op != '^':
      p2 = next(
        filter(lambda t: f'^ {p1}' in t[1] or f'{p1} ^' in t[1], F.items()))[0]
      swaps.append((z, p2))
    else:
      swaps.append(
        (p1, sorted((v1, v2), key=lambda v: len(getFullFormula(v)))[0]))

  print(','.join(sorted(chain(*swaps))))


part1()
part2()
