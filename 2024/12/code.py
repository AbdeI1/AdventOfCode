import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  M = reader()
  c = 0
  V = set()
  D = [(1, 0), (-1, 0), (0, 1), (0, -1)]
  for i in range(len(M)):
    for j in range(len(M[0])):
      if (i, j) in V:
        continue
      l = M[i][j]
      q = [(i, j)]
      s = set()
      while q:
        (ii, jj) = q.pop()
        if (ii, jj) in s:
          continue
        s.add((ii, jj))
        for d in D:
          x, y = ii + d[0], jj + d[1]
          if x in range(len(M)) and y in range(len(M[x])) and M[x][y] == l:
            q.append((x, y))
      A = len(s)
      P = 0
      for p in s:
        for d in D:
          if (p[0] + d[0], p[1] + d[1]) not in s:
            P += 1
      c += A * P
      V.update(s)
  print(c)


def part2():
  M = reader()
  c = 0
  V = set()
  D = [(1, 0), (-1, 0), (0, 1), (0, -1)]
  for i in range(len(M)):
    for j in range(len(M[0])):
      if (i, j) in V:
        continue
      l = M[i][j]
      q = [(i, j)]
      s = set()
      while q:
        (ii, jj) = q.pop()
        if (ii, jj) in s:
          continue
        s.add((ii, jj))
        for d in D:
          x, y = ii + d[0], jj + d[1]
          if x in range(len(M)) and y in range(len(M[x])) and M[x][y] == l:
            q.append((x, y))
      A = len(s)
      sides = set()
      for p in s:
        for d in D:
          pp = p
          if (p[0] + d[0], p[1] + d[1]) not in s:
            while pp in s and (pp[0] + d[0], pp[1] + d[1]) not in s:
              pp = pp[0] - d[1], pp[1] + d[0]
            sides.add((pp, d))
      c += A * (len(sides))
      V.update(s)
  print(c)


part1()
part2()
