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
        f[i][j] = '*'
    b = all([f[j][i] == '.' for j in range(len(f))])
    if b:
      for j in range(len(f)):
        f[j][i] = '*'
  print(f)
  print(len(galaxies))
  
def part2():
  f = reader()

part1()
part2()
