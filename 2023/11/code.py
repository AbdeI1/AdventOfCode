import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = [list(s) for s in reader()]
  count_h = 0
  count_v = 0
  for i in range(len(f)):
    a = all(map(lambda x: x in {'.', '|', '-'}, f[i]))
    if a:
      for j in range(len(f)):
        f[i][j] = '-'
      count_v += 1
    b = all([f[j][i] in {'.', '-', '|'} for j in range(len(f))])
    if b:
      for j in range(len(f)):
        f[j][i] = '*' if f[j][i] == '-' else '|'
      count_h += 1
  m = []
  for i in range(len(f)):
    if f[i][0] == '-':
      m.append(['.'] * len(m[-1]))
      m.append(['.'] * len(m[-1]))
    else:
      l = []
      for j in range(len(f[i])):
        if f[i][j] == '|':
          l.append('.')
          l.append('.')
        else:
          l.append(f[i][j])
      m.append(l)
  galaxies = [(i, j) for j in range(len(m[0]))
              for i in range(len(m)) if m[i][j] == '#']
  s = 0
  for g1 in galaxies:
    for g2 in galaxies:
      s += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
  print(s // 2)


def part2():
  f = [list(s) for s in reader()]
  scale = 1000000
  for i in range(len(f)):
    a = all(map(lambda x: x in {'.', '|', '-'}, f[i]))
    if a:
      for j in range(len(f)):
        f[i][j] = '-'
    b = all([f[j][i] in {'.', '-', '|'} for j in range(len(f))])
    if b:
      for j in range(len(f)):
        f[j][i] = '*' if f[j][i] == '-' else '|'
  galaxies = []
  r, c = 0, 0
  for i in range(len(f)):
    c = 0
    if f[i][0] == '-':
      r += scale
      continue
    for j in range(len(f[i])):
      if f[i][j] == '#':
        galaxies.append((r, c))
      elif f[i][j] == '|':
        c += scale
        continue
      c += 1
    r += 1
  s = 0
  for g1 in galaxies:
    for g2 in galaxies:
      s += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
  print(s // 2)


part1()
part2()
