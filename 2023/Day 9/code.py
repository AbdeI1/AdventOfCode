import pathlib
from itertools import pairwise

def reader():
  f = open(f"{pathlib.Path(__file__).parent.resolve()}/input.txt", 'r').read()
  f = f.split('\n')
  f = f[:-1]
  return f

def pred(a):
  hist = [a]
  while not all([n == 0 for n in hist[-1]]):
    l = [y - x for x, y in pairwise(hist[-1])]
    hist.append(l)
  hist[-1].append(0)
  for i in range(2, len(hist)+1):
    hist[-i].append(hist[-i][-1] + hist[-i+1][-1])
  return hist[0][-1]
      

def part1():
  f = [[int(n) for n in a.split()] for a in reader()]
  print(sum(map(pred, f)))
  
def part2():
  f = [[int(n) for n in reversed(a.split())] for a in reader()]
  print(sum(map(pred, f)))

part1()
part2()
