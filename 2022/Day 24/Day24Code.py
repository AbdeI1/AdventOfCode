import pathlib

def reader():
  f = open(f"{pathlib.Path(__file__).parent.resolve()}/Day24input.txt", 'r').read()
  f = f.split('\n')
  f = f[:-1]
  return f

D = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]

def gcd(x, y):
  return x if y == 0 else gcd(y, x%y)

def lcm(x, y):
  return (x*y)//gcd(x,y)

def part1():
  f = reader()
  B = set()
  for i in range(len(f)):
    for j in range(len(f[i])):
      b = f[i][j]
      if b == '>': B.add(((i, j), (0, 1)))
      if b == '<': B.add(((i, j), (0, -1)))
      if b == '^': B.add(((i, j), (-1, 0)))
      if b == 'v': B.add(((i, j), (1, 0)))
  sp = (0, 0)
  for j in range(len(f[0])):
    if f[0][j] == '.':
      sp = (0, j)
      break
  ep = (0, 0)
  for j in range(len(f[0])):
    if f[-1][j] == '.':
      ep = (len(f)-1, j)
      break
  x = len(f)-2
  y = len(f[0])-2
  M = lcm(x, y)
  S = [set() for _ in range(M)]
  for t in range(M):
    for b in B:
      bs, bd = b
      bp = ((((bs[0] + t*bd[0] - 1)%x)+x)%x + 1, (((bs[1] + t*bd[1] - 1)%y)+y)%y + 1)
      S[t].add(bp)
  V = set()
  Q = [(sp, 0)]
  while Q:
    p, t = Q.pop(0)
    if (p, t%M) in V: continue
    V.add((p, t%M))
    if p == ep:
      print(t)
      break
    t += 1
    for d in D:
      pn = (p[0] + d[0], p[1] + d[1])
      if ((pn[0] in range(1, len(f)-1) and pn[1] in range(1, len(f[0])-1)) or pn == ep or pn == sp) and pn not in S[t%M]:
        Q.append((pn, t))

def part2():
  f = reader()
  B = set()
  for i in range(len(f)):
    for j in range(len(f[i])):
      b = f[i][j]
      if b == '>': B.add(((i, j), (0, 1)))
      if b == '<': B.add(((i, j), (0, -1)))
      if b == '^': B.add(((i, j), (-1, 0)))
      if b == 'v': B.add(((i, j), (1, 0)))
  sp = (0, 0)
  for j in range(len(f[0])):
    if f[0][j] == '.':
      sp = (0, j)
      break
  ep = (0, 0)
  for j in range(len(f[0])):
    if f[-1][j] == '.':
      ep = (len(f)-1, j)
      break
  x = len(f)-2
  y = len(f[0])-2
  M = lcm(x, y)
  S = [set() for _ in range(M)]
  for t in range(M):
    for b in B:
      bs, bd = b
      bp = ((((bs[0] + t*bd[0] - 1)%x)+x)%x + 1, (((bs[1] + t*bd[1] - 1)%y)+y)%y + 1)
      S[t].add(bp)
  def bfs(start, end, time):
    V = set()
    Q = [(start, time)]
    while Q:
      p, t = Q.pop(0)
      if (p, t%M) in V: continue
      V.add((p, t%M))
      if p == end: return t
      t += 1
      for d in D:
        pn = (p[0] + d[0], p[1] + d[1])
        if ((pn[0] in range(1, len(f)-1) and pn[1] in range(1, len(f[0])-1)) or pn == ep or pn == sp) and pn not in S[t%M]:
          Q.append((pn, t))
  print(bfs(sp, ep, bfs(ep, sp, bfs(sp, ep, 0))))
  
part1() 
part2()
