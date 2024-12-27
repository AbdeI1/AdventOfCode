import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  M = reader()
  p = (-1, -1)
  for i in range(len(M)):
    for j in range(len(M[i])):
      if M[i][j] == '^':
        p = (i, j)
  d = (-1, 0)
  S = set()
  while p[0] in range(len(M)) and p[1] in range(len(M[p[0]])):
    S.add(p)
    pp = p[0] + d[0], p[1] + d[1]
    while pp[0] in range(len(M)) and pp[1] in range(len(M[pp[0]])) and M[pp[0]][pp[1]] == '#':
      d = d[1], -d[0]
      pp = p[0] + d[0], p[1] + d[1]
    p = pp
  print(len(S))


def part2():
  M = list(map(list, reader()))
  p = (-1, -1)
  for i in range(len(M)):
    for j in range(len(M[i])):
      if M[i][j] == '^':
        op = (i, j)
  od = (-1, 0)
  p = op
  d = od
  C = set()
  S = set()
  Sp = set()
  while p[0] in range(len(M)) and p[1] in range(len(M[p[0]])):
    S.add((p, d))
    Sp.add(p)
    pp = p[0] + d[0], p[1] + d[1]
    while pp[0] in range(len(M)) and pp[1] in range(len(M[pp[0]])) and M[pp[0]][pp[1]] == '#':
      d = d[1], -d[0]
      pp = p[0] + d[0], p[1] + d[1]
    if pp[0] in range(len(M)) and pp[1] in range(len(M[pp[0]])) and pp not in Sp:
      M[pp[0]][pp[1]] = '#'
      SS = set()
      ppp = p
      ddd = d[1], -d[0]
      while ppp[0] in range(len(M)) and ppp[1] in range(len(M[ppp[0]])):
        if (ppp, ddd) in S or (ppp, ddd) in SS:
          C.add(pp)
          break
        SS.add((ppp, ddd))
        pppp = ppp[0] + ddd[0], ppp[1] + ddd[1]
        while pppp[0] in range(len(M)) and pppp[1] in range(len(M[pppp[0]])) and M[pppp[0]][pppp[1]] == '#':
          ddd = ddd[1], -ddd[0]
          pppp = ppp[0] + ddd[0], ppp[1] + ddd[1]
        ppp = pppp
      M[pp[0]][pp[1]] = '.'
    p = pp
  print(len(C))


part1()
part2()
