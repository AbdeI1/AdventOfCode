import pathlib

def reader():
  f = open(f"{pathlib.Path(__file__).parent.resolve()}/Day18input.txt", 'r').read()
  f = f.split('\n')
  f = f[:-1]
  return f

def part1():
  f = reader()
  P = set()
  for l in f:
    P.add(tuple(map(int, l.split(','))))
  ans = 0
  for p1 in P:
    ans += 6
    for p2 in P:
      if abs(p2[0]-p1[0]) + abs(p2[1]-p1[1]) + abs(p2[2]-p1[2]) == 1:
        ans -= 1
  print(ans)

def part2():
  f = reader()
  P = set()
  R = [(100, -1) for _ in range(3)]
  for l in f:
    p = tuple(map(int, l.split(',')))
    P.add(p)
    for i in range(3): R[i] = (min(p[i], R[i][0]), max(p[i], R[i][1]))
  def surfArea(P):
    a = 0
    for p1 in P:
      a += 6
      for p2 in P: 
        if abs(p2[0]-p1[0]) + abs(p2[1]-p1[1]) + abs(p2[2]-p1[2]) == 1: a -= 1
    return a
  ans = surfArea(P)
  DIRS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
  V = set()
  for x in range(R[0][0], R[0][1]+1):
    for y in range(R[1][0], R[1][1]+1):
      for z in range(R[2][0], R[2][1]+1):
        if (x, y, z) in P or (x, y, z) in V: continue
        q = [(x, y, z)]
        v = set()
        while q:
          p = q.pop(0)
          if p in v or p in P: continue
          if p[0] not in range(R[0][0], R[0][1]+1) or p[1] not in range(R[1][0], R[1][1]+1) or p[2] not in range(R[2][0], R[2][1]+1): break
          v.add(p)
          for D in DIRS: q.append((p[0] + D[0], p[1] + D[1], p[2] + D[2]))
        else: ans -= surfArea(v)
        V.update(v)
  print(ans)

part1()
part2()
