import pathlib


def reader():
  f = open(f"{pathlib.Path(__file__).parent.resolve()}/sample.txt", 'r').read()
  f = f.split('\n')
  f = f[:-1]
  return f


def part1():
  f = reader()
  d = 64
  s = (0, 0)
  for i in range(len(f)):
    for j in range(len(f[i])):
      if f[i][j] == 'S':
        s = (i, j)
        break
    else:
      continue
    break
  q = [(s, 0)]
  v = set()
  ans = 0
  while q:
    (i, j), s = q.pop(0)
    if s > d or i not in range(len(f)) or j not in range(len(f[i])) or f[i][j] == '#':
      continue
    if (i, j) in v:
      continue
    v.add((i, j))
    if s % 2 == 0:
      ans += 1
    for d1, d2 in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
      q.append(((i + d1, j + d2), s + 1))
  print(ans)


def part2():
  f = reader()
  d = 10
  s = (0, 0)
  for i in range(len(f)):
    for j in range(len(f[i])):
      if f[i][j] == 'S':
        s = (i, j)
        break
    else:
      continue
    break
  q = [(s, 0)]
  v = set()
  a = {}
  b = {}
  ans = 0
  while q:
    (i, j), st = q.pop(0)
    ii, jj = i % len(f), j % len(f[i % len(f)])
    if st > d or f[ii][jj] == '#':
      continue
    if (i, j) in v:
      continue
    v.add((i, j))
    if (ii, jj) not in a:
      a[(ii, jj)] = []
    a[(ii, jj)].append(st)
    if st not in b:
      b[st] = set()
    b[st].add((ii, jj))
    if st % 2 == d % 2:
      ans += 1
    for d1, d2 in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
      q.append(((i + d1, j + d2), st + 1))
  print(a)
  print(b)


part1()
part2()
