import pathlib

def reader():
  f = open(f"{pathlib.Path(__file__).parent.resolve()}/sample.txt", 'r').read()
  f = f.split('\n')
  f = f[:-1]
  return f

def part1():
  f = [list(s) for s in reader()]
  galaxies = [(i, j) for j in range(len(f)) for i in range(len(f)) if f[i][j] == '#']
  for i in range(len(f)):
    a = all(map(lambda x: x == '.', f[i]))
    if a:
      for j in range(len(f)):
        f[i][j] = '-'
    b = all([f[j][i] == '.' for j in range(len(f))])
    if b:
      for j in range(len(f)):
        f[j][i] = '*' if f[j][i] == '-' else '|'
  g = {}
  for i in range(len(f)):
    for j in range(len(f[i])):
      n = (i, j)
      l = []
      for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        o = (n[0] + d[0], n[1] + d[1])
        if o[0] in range(len(f)) and o[1] in range(len(f[o[0]])):
          match f[n[0]], [n[1]], f[o[0]][o[1]]:
            case '*', '*':
              l.append((o, 1.5))
      g[n] = l
            
  print(g)
  
def part2():
  f = reader()

part1()
part2()
