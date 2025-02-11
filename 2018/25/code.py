import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = list(map(eval, reader()))
  p = [i for i in range(len(f))]

  def find(x):
    if x == p[x]:
      return x
    p[x] = find(p[x])
    return p[x]

  for i, c1 in enumerate(f):
    for j, c2 in enumerate(f):
      if sum(abs(c1[i] - c2[i]) for i in range(4)) <= 3 and find(i) != find(j):
        p[find(i)] = p[find(j)]

  C = set()
  for i in range(len(p)):
    C.add(find(i))

  print(len(C))


def part2():
  pass


part1()
part2()
