import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  n = len(f)
  p = [i for i in range(n)]

  def find(x):
    if x != p[x]:
      p[x] = find(p[x])
    return p[x]

  def union(x, y):
    p[find(x)] = p[find(y)]

  for l in f:
    i, ii = l.split(' <-> ')
    for o in ii.split(','):
      union(int(i), int(o))

  print(sum(1 for x in p if find(x) == find(p[0])))


def part2():
  f = reader()
  n = len(f)
  p = [i for i in range(n)]

  def find(x):
    if x != p[x]:
      p[x] = find(p[x])
    return p[x]

  def union(x, y):
    p[find(x)] = p[find(y)]

  for l in f:
    i, ii = l.split(' <-> ')
    for o in ii.split(','):
      union(int(i), int(o))

  print(len({find(x) for x in p}))


part1()
part2()
