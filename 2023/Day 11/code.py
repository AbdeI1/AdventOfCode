import pathlib

def reader():
  f = open(f"{pathlib.Path(__file__).parent.resolve()}/sample.txt", 'r').read()
  f = f.split('\n')
  f = f[:-1]
  return f

def part1():
  f = [list(s) for s in reader()]
  galaxies = [(i, j) for j in range(len(f)) for i in range(len(f)) if f[i][j] == '#']
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
      m.append(['.']*len(m[-1]))
      m.append(['.']*len(m[-1]))
    else:
      l = []
      for j in range(len(f[i])):
        if f[i][j] == '|':
          l.append('.')
          l.append('.')
        else:
          l.append(f[i][j])
      m.append(l)
  g = {}
  for i in range(len(m)):
    for j in range(len(m[i])):
      n = (i, j)
      l = []
      for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        o = (n[0] + d[0], n[1] + d[1])
        if o[0] in range(len(m)) and o[1] in range(len(m[o[0]])):
          l.append((o, 1))
      g[n] = l
  print(g)
  
def part2():
  f = reader()

part1()
part2()
