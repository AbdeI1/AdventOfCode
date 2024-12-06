import pathlib


def reader():
  return open(f"{pathlib.Path(__file__).parent.resolve()}/input.txt", 'r').read().split('\n')[:-1]


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

  def r(p, d):
    if M[p[0]][p[1]] == '#':
      return False
    S = set()
    l = 0
    while p[0] in range(len(M)) and p[1] in range(len(M[p[0]])):
      if (p, d) in S:
        return True
      S.add((p, d))
      pp = p[0] + d[0], p[1] + d[1]
      while pp[0] in range(len(M)) and pp[1] in range(len(M[pp[0]])) and M[pp[0]][pp[1]] == '#':
        d = d[1], -d[0]
        pp = p[0] + d[0], p[1] + d[1]
      p = pp
      l += 1
    return False

  p = op
  d = od
  C = set()
  while p[0] in range(len(M)) and p[1] in range(len(M[p[0]])):
    M[p[0]][p[1]] = '#'
    if r(op, od):
      C.add(p)
    M[p[0]][p[1]] = '.'
    pp = p[0] + d[0], p[1] + d[1]
    if pp[0] in range(len(M)) and pp[1] in range(len(M[pp[0]])) and M[pp[0]][pp[1]] == '#':
      d = d[1], -d[0]
    p = p[0] + d[0], p[1] + d[1]
  print(len(C))


part1()
part2()
