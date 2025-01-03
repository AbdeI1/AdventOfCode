import os
os.chdir(os.path.dirname(__file__))
from itertools import chain


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  recipes = [tuple(tuple((r.split(' ')[1], int(r.split(' ')[0])) for r in l.split(', '))
             for l in s.split(' => ')) for s in reader()]
  I = {i for i, n in chain(*chain(*recipes))}
  D = {r[0][0]: (i, r[0][1]) for i, r in recipes}
  S = {i: 0 for i in I}
  S['FUEL'] = 1
  while any(S[i] > 0 and i != 'ORE' for i in I):
    for s in S:
      c = S[s]
      if c > 0 and s != 'ORE':
        l, r = D[s]
        n = (c + r - 1) // r
        for i, m in l:
          S[i] += m * n
        S[s] -= n * r
  print(S['ORE'])


def part2():
  recipes = [tuple(tuple((r.split(' ')[1], int(r.split(' ')[0])) for r in l.split(', '))
             for l in s.split(' => ')) for s in reader()]
  I = {i for i, n in chain(*chain(*recipes))}
  D = {r[0][0]: (i, r[0][1]) for i, r in recipes}

  def f(n):
    S = {i: 0 for i in I}
    S['FUEL'] = n
    while any(S[i] > 0 and i != 'ORE' for i in I):
      for s in S:
        c = S[s]
        if c > 0 and s != 'ORE':
          l, r = D[s]
          n = (c + r - 1) // r
          for i, m in l:
            S[i] += m * n
          S[s] -= n * r
    return S['ORE']

  T = 1e12

  i = 1
  while f(i) < T:
    i <<= 1
  s = i >> 1

  while s > 0:
    i += s if f(i) < T else -s
    s >>= 1

  print(i if f(i) <= T else i - 1)


part1()
part2()
