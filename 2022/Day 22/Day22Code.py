import pathlib

def reader():
  f = open(f"{pathlib.Path(__file__).parent.resolve()}/Day22input.txt", 'r').read()
  f = f.split('\n')
  f = f[:-1]
  return f

D = {
  (0, 1): 0,
  (1, 0): 1,
  (0, -1): 2,
  (-1, 0): 3
}

def part1():
  f = reader()
  steps = f[-1]
  b = f[:-2]
  m = max(list(map(len, b)))
  for i in range(len(b)):
    if len(b[i]) < m:
      b[i] += ' '*(m-len(b[i]))
  d = (0, 1)
  p = (0, 0)
  for i in range(len(b[0])):
    if b[0][i] == '.':
      p = (0, i)
      break
  i = 0
  while i < len(steps):
    c = steps[i]
    if c == 'L':
      d = (-d[1], d[0])
    elif c == 'R':
      d = (d[1], -d[0])
    else:
      s = c
      while i+1 < len(steps) and steps[i+1] != 'R' and steps[i+1] != 'L':
        s += steps[i+1]
        i += 1
      m = int(s)
      while m > 0:
        op = p
        p = (p[0] + d[0], p[1] + d[1])
        while p[0] in range(len(b)) and p[1] in range(len(b[p[0]])) and b[p[0]][p[1]] == ' ':
          p = (p[0] + d[0], p[1] + d[1])
        x = (p[0] + len(b))%len(b)
        y = (p[1] + len(b[x]))%len(b[x])
        p = (x, y)
        while p[0] in range(len(b)) and p[1] in range(len(b[p[0]])) and b[p[0]][p[1]] == ' ':
          p = (p[0] + d[0], p[1] + d[1])
        if b[p[0]][p[1]] == '#':
          p = op
          break
        m -= 1
    i += 1
  print((p[0]+1)*1000 + (p[1]+1)*4 + D[d])

def part2():
  f = reader()
  steps = f[-1]
  b = f[:-2]
  m = max(list(map(len, b)))
  for i in range(len(b)):
    if len(b[i]) < m:
      b[i] += ' '*(m-len(b[i]))
  def isIn(i, j):
    return i in range(len(b)) and j in range(len(b[i]))
  T = {}
  for i in range(len(b)):
    for j in range(len(b[i])):
      if b[i][j] != ' ':
        for d in D:
          T[((i, j), d)] = None
          if isIn(i+d[0], j+d[1]) and b[i+d[0]][j+d[1]] != ' ':
            T[(i, j), d] = ((i+d[0], j+d[1]), d)
  for i in range(len(b)):
    for j in range(len(b[i])):
      if b[i][j] == ' ':
        cb = []
        cs = []
        for d in D:
          if isIn(i+d[0], j+d[1]) and b[i+d[0]][j+d[1]] == ' ':
            cb += [d]
          elif isIn(i+d[0], j+d[1]) and b[i+d[0]][j+d[1]] != ' ':
            cs += [d]
        if len(cb) == 2 and len(cs) == 2:
          p1 = (i + cs[0][0], j + cs[0][1])
          p2 = (i + cs[1][0], j + cs[1][1])
          d1 = cb[0] if cb[0][0] != cs[0][0] and cb[0][1] != cs[0][1] else cb[1]
          d2 = cb[0] if cb[0] != d1 else cb[1]
          while True:
            f = True
            if not T[(p1, (d1[1], -d1[0]))]:
              T[(p1, (d1[1], -d1[0]))] = (p2, (d2[1], -d2[0]))
              f = False
            if not T[(p1, (-d1[1], d1[0]))]:
              T[(p1, (-d1[1], d1[0]))] = (p2, (-d2[1], d2[0]))
              f = False
            if not T[(p2, (d2[1], -d2[0]))]:
              T[(p2, (d2[1], -d2[0]))] = (p1, (d1[1], -d1[0]))
              f = False
            if not T[(p2, (-d2[1], d2[0]))]:
              T[(p2, (-d2[1], d2[0]))] = (p1, (-d1[1], d1[0]))
              f = False
            if f:
              break
            p1 = (p1[0] + d1[0], p1[1] + d1[1])
            p2 = (p2[0] + d2[0], p2[1] + d2[1])
            if not (isIn(p1[0], p1[1]) and b[p1[0]][p1[1]] != ' ') and not (isIn(p2[0], p2[1]) and b[p2[0]][p2[1]] != ' '):
              break
            elif not (isIn(p1[0], p1[1]) and b[p1[0]][p1[1]] != ' '):
              p1 = (p1[0] - d1[0], p1[1]-d1[1])
              d1 = (d1[1], -d1[0])
              p1 = (p1[0] + d1[0], p1[1] + d1[1])
              if not (isIn(p1[0], p1[1]) and b[p1[0]][p1[1]] != ' '):
                p1 = (p1[0] - d1[0], p1[1]-d1[1])
                d1 = (-d1[0], -d1[1])
                p1 = (p1[0] + d1[0], p1[1] + d1[1])
              p1 = (p1[0] - d1[0], p1[1]-d1[1])
            elif not (isIn(p2[0], p2[1]) and b[p2[0]][p2[1]] != ' '):
              p2 = (p2[0] - d2[0], p2[1]-d2[1])
              d2 = (d2[1], -d2[0])
              p2 = (p2[0] + d2[0], p2[1] + d2[1])
              if not (isIn(p2[0], p2[1]) and b[p2[0]][p2[1]] != ' '):
                p2 = (p2[0] - d2[0], p2[1]-d2[1])
                d2 = (-d2[0], -d2[1])
                p2 = (p2[0] + d2[0], p2[1] + d2[1])
              p2 = (p2[0] - d2[0], p2[1]-d2[1])
  s = set()
  for k in T:
    if not T[k]:
      s.add(k)
  if len(s) != 0:
    dirs = set()
    for p, d in s:
      dirs.add(d)
    dirs = list(dirs)
    t = {}
    for d in dirs:
      t[d] = []
    for p, d in s:
      t[d].append(p)
    for d in t:
      t[d].sort()
    for i in range(len(t[dirs[0]])):
      T[(t[dirs[0]][i], dirs[0])] = (t[dirs[1]][i], dirs[0])
      T[(t[dirs[1]][i], dirs[1])] = (t[dirs[0]][i], dirs[1])
  d = (0, 1)
  p = (0, 0)
  for i in range(len(b[0])):
    if b[0][i] == '.':
      p = (0, i)
      break
  i = 0
  while i < len(steps):
    c = steps[i]
    if c == 'L':
      d = (-d[1], d[0])
    elif c == 'R':
      d = (d[1], -d[0])
    else:
      s = c
      while i+1 < len(steps) and steps[i+1] != 'R' and steps[i+1] != 'L':
        s += steps[i+1]
        i += 1
      m = int(s)
      while m > 0:
        pn, dn = T[(p, d)]
        if b[pn[0]][pn[1]] == '#':
          break
        p, d = pn, dn
        m -= 1
    i += 1
  print((p[0]+1)*1000 + (p[1]+1)*4 + D[d])
  
part1() 
part2()
