import os
os.chdir(os.path.dirname(__file__))
from re import split
from math import sqrt
from itertools import product


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = [tuple(eval(t) for t in split(r'>, [v|a]=<', l[3:-1])) for l in reader()]
  T = 100000
  mi, md = -1, float('inf')
  for i, ((px, py, pz), (vx, vy, vz), (ax, ay, az)) in enumerate(f):
    Px = ax * T * T / 2 + (vx + (ax / 2)) * T + px
    Py = ay * T * T / 2 + (vx + (ay / 2)) * T + py
    Pz = az * T * T / 2 + (vx + (az / 2)) * T + pz
    d = sum(abs(n) for n in [Px, Py, Pz])
    if d < md:
      mi, md = i, d
  print(mi)


def part2():
  f = [tuple(eval(t) for t in split(r'>, [v|a]=<', l[3:-1])) for l in reader()]
  C = []
  for i, (P1, V1, A1) in enumerate(f):
    for j, (P2, V2, A2) in enumerate(f):
      if j <= i:
        continue
      T = []
      for (p1, v1, a1), (p2, v2, a2) in zip(zip(P1, V1, A1), zip(P2, V2, A2)):
        a = (a2 - a1) / 2
        b = (v2 - v1) + a
        c = p2 - p1
        if a == 0 and b == 0 and c == 0:
          T.append((None,))
        elif a == 0 and b != 0:
          T.append((-c / b, ))
        elif a != 0 and (b * b - 4 * a * c) == 0:
          T.append((-b / (2 * a), ))
        elif a != 0 and (b * b - 4 * a * c) > 0:
          disc = sqrt(b * b - 4 * a * c)
          t1 = (-b + disc) / (2 * a)
          t2 = (-b - disc) / (2 * a)
          T.append((t1, t2))
        else:
          T.append(())
      for (t1, t2, t3) in product(*T):
        tt = t1 if t1 is not None else t2 if t2 is not None else t3
        if all(t is None or (t >= 0 and abs(t - tt) <= 1e-4) for t in (t1, t2, t3)) and tt == round(tt):
          c = (round(tt), i, j)
          if c not in C:
            C.append(c)
  R = {}
  for t, c1, c2 in C:
    if c1 in R and c2 in R:
      continue
    elif c1 not in R and c2 not in R:
      R[c1] = t
      R[c2] = t
    elif c1 in R:
      if R[c1] == t:
        R[c2] = t
    elif c2 in R:
      if R[c2] == t:
        R[c1] = t
  print(len(f) - len(R))


part1()
part2()
