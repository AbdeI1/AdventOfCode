import os
os.chdir(os.path.dirname(__file__))
from collections import defaultdict


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()[0]
  i = 1

  def parse(D):
    nonlocal i
    md = -1
    d = 0
    while f[i] != '$':
      if f[i] == '(':
        i += 1
        d += parse(D + d)
      elif f[i] == ')':
        if f[i - 1] == '|':
          return 0
        else:
          break
      elif f[i] == '|':
        md = max(md, d)
        d = 0
      else:
        d += 1
      i += 1
    md = max(md, d)
    return md

  x = parse(0)
  print(x)


def part2():
  f = reader()[0]
  M = 1000
  i = 1

  def parse():
    nonlocal i
    s = ""
    O = []
    L = ()
    while f[i] != '$':
      if f[i] == '(':
        i += 1
        if len(s):
          L += (s,)
        s = ""
        l = parse()
        L += (l,)
      elif f[i] == ')':
        if f[i - 1] == '|':
          # for j in range(len(O)):
          #   O[j] //= 2
          O.append("")
        break
      elif f[i] == '|':
        if len(s):
          L += (s, )
        if L:
          O.append(L if len(L) > 1 else L[0])
        s = ""
        L = ()
      else:
        s += f[i]
      i += 1
    if len(s):
      L += (s,)
    if L:
      O.append(L if len(L) > 1 else L[0])
    return O if len(O) > 1 else O[0]

  D = defaultdict(lambda: float('inf'))
  D[(0, 0)] = 0
  MOVE = {
    'E': (1, 0),
    'N': (0, 1),
    'W': (-1, 0),
    'S': (0, -1)
  }

  def count(o, P):
    p = set()
    if type(o) is str:
      for x, y in P:
        d = D[(x, y)]
        for c in o:
          x, y = x + MOVE[c][0], y + MOVE[c][1]
          d += 1
          D[(x, y)] = min(D[(x, y)], d)
        p.add((x, y))
    elif type(o) is tuple:
      y = P
      for x in o:
        y = count(x, y)
      p = y
    elif type(o) is list:
      if o[-1] == 0:
        for s in o[:-1]:
          for x, y in P:
            d = D[(x, y)]
            for c in s:
              x, y = x + MOVE[c][0], y + MOVE[c][1]
              d += 1
              D[(x, y)] = min(D[(x, y)], d)
        p = P
      else:
        for x in o:
          p |= count(x, P)
    return p

  count(parse(), {(0, 0)})
  print(len([p for p in D if D[p] >= M]))


part1()
part2()
