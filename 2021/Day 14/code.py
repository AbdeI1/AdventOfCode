import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().split('\n')[:-1]


def insert(p, r):
  l = len(p)
  n = p
  last = 1
  for i in range(l - 1):
    n = n[:last] + r[p[i] + p[i + 1]] + n[last:]
    last += 2
  return n


def part1():
  f = reader()
  polymer = f[0]
  rules = f[2:]
  d = {}
  for r in rules:
    t = r.split(' -> ')
    d[t[0]] = t[1]
  n = polymer
  for i in range(10):
    n = insert(n, d)
  ma = -1
  mi = 1000000000
  for i in n:
    ma = max(n.count(i), ma)
    mi = min(n.count(i), mi)
  print(ma - mi)


def insert2(p, r):
  pn = p.copy()
  for k in p:
    k1 = k[0] + r[k]
    k2 = r[k] + k[1]
    if k1 in pn:
      pn[k1] += p[k]
    else:
      pn[k1] = p[k]
    if k2 in pn:
      pn[k2] += p[k]
    else:
      pn[k2] = p[k]
    pn[k] -= p[k]
  return pn


def part2():
  f = reader()
  p = f[0]
  rules = f[2:]
  d = {}
  for r in rules:
    t = r.split(' -> ')
    d[t[0]] = t[1]
  pairs = {}
  for i in range(len(p) - 1):
    k = p[i] + p[i + 1]
    if k in pairs:
      pairs[k] += 1
    else:
      pairs[k] = 1
  pn = pairs.copy()
  for i in range(40):
    pn = insert2(pn, d)
  ma = -1
  mi = 10000000000000000
  d = {}
  for k in pn:
    d[k[0]] = 0
    d[k[1]] = 0
  for k in pn:
    d[k[0]] += pn[k] / 2
    d[k[1]] += pn[k] / 2
  d[p[0]] += 0.5
  d[p[-1]] += 0.5
  for k in d:
    ma = max(ma, d[k])
    mi = min(mi, d[k])
  print(int(ma - mi))


part1()
part2()
