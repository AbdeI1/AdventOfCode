import pathlib

def reader():
  f = open(f"{pathlib.Path(__file__).parent.resolve()}/sample.txt", 'r').read()
  f = f.split('\n')
  f = f[:-1]
  return f

def part1():
  f = [[x.split()[0]] + [list(map(int, x.split()[1].split(',')))] for x in reader()]
  print(f)
  m = 0
  for s, n in f:
    s2 = '.'.join(['#'*x for x in n])
    print(s, len(s))
    print(s2, len(s2))
    diff = len(s) - len(s2)
    print(diff)
    m = max(m, diff)
  print(m)
  
def part2():
  f = reader()

part1()
part2()
