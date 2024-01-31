import pathlib

def reader():
  f = open(f"{pathlib.Path(__file__).parent.resolve()}/sample.txt", 'r').read()
  f = f.split('\n')
  f = f[:-1]
  return f

def part1():
  f = reader()
  
def part2():
  f = reader()

part1()
part2()
