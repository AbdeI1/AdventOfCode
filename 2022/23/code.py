import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


D = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def part1():
  f = reader()
  elves = set()
  for i in range(len(f)):
    for j in range(len(f[i])):
      if f[i][j] == '#':
        elves.add((i, j))
  di = 0
  for _ in range(10):
    d = {}
    counts = {}
    for e in elves:
      c = 0
      for i in range(-1, 2):
        for j in range(-1, 2):
          if (i, j) == (0, 0):
            continue
          if (e[0] + i, e[1] + j) in elves:
            c += 1
      if c == 0:
        d[e] = e
        counts[e] = 1
        continue
      i = di
      for _ in range(len(D)):
        md = D[i]
        b = 0 if md[0] == 0 else 1
        c = [md[0], md[1]]
        ce = 0
        for a in range(-1, 2):
          c[b] = a
          if (e[0] + c[0], e[1] + c[1]) in elves:
            ce += 1
        if ce == 0:
          pn = (e[0] + md[0], e[1] + md[1])
          d[e] = pn
          if pn in counts:
            counts[pn] += 1
          else:
            counts[pn] = 1
          break
        i += 1
        i %= len(D)
      else:
        d[e] = e
        counts[e] = 1
    ne = set()
    for e in elves:
      if counts[d[e]] == 1:
        ne.add(d[e])
      else:
        ne.add(e)
    elves = ne
    di += 1
    di %= len(D)
  a = (lambda l1, l2: (max(l1) - min(l1) + 1) * (max(l2) - min(l2) + 1)
       )(list(map(lambda t: t[0], elves)), list(map(lambda t: t[1], elves)))
  print(a - len(elves))


def part2():
  f = reader()
  elves = set()
  for i in range(len(f)):
    for j in range(len(f[i])):
      if f[i][j] == '#':
        elves.add((i, j))
  r = 0
  while True:
    d = {}
    counts = {}
    for e in elves:
      c = 0
      for i in range(-1, 2):
        for j in range(-1, 2):
          if (i, j) == (0, 0):
            continue
          if (e[0] + i, e[1] + j) in elves:
            c += 1
      if c == 0:
        d[e] = e
        counts[e] = 1
        continue
      i = r % len(D)
      for _ in range(len(D)):
        md = D[i]
        b = 0 if md[0] == 0 else 1
        c = [md[0], md[1]]
        ce = 0
        for a in range(-1, 2):
          c[b] = a
          if (e[0] + c[0], e[1] + c[1]) in elves:
            ce += 1
        if ce == 0:
          pn = (e[0] + md[0], e[1] + md[1])
          d[e] = pn
          if pn in counts:
            counts[pn] += 1
          else:
            counts[pn] = 1
          break
        i += 1
        i %= len(D)
      else:
        d[e] = e
        counts[e] = 1
    ne = set()
    m = 0
    for e in elves:
      if counts[d[e]] == 1:
        ne.add(d[e])
        if e != d[e]:
          m += 1
      else:
        ne.add(e)
    elves = ne
    r += 1
    if m == 0:
      break
  print(r)


part1()
part2()
