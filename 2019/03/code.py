import os
os.chdir(os.path.dirname(__file__))
from itertools import accumulate, pairwise


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  w1, w2 = [l.split(',') for l in reader()]
  D = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
  p1 = list(accumulate(w1, lambda a, b: (a[0] +
            D[b[0]][0] * int(b[1:]), a[1] + D[b[0]][1] * int(b[1:])), initial=(0, 0)))
  p2 = list(accumulate(w2, lambda a, b: (a[0] +
            D[b[0]][0] * int(b[1:]), a[1] + D[b[0]][1] * int(b[1:])), initial=(0, 0)))
  c = float('inf')
  for ((p11x, p11y), (p12x, p12y)) in pairwise(p1[1:]):
    for ((p21x, p21y), (p22x, p22y)) in pairwise(p2[1:]):
      (p1lx, p1rx), (p1dy, p1uy) = sorted((p11x, p12x)), sorted((p11y, p12y))
      (p2lx, p2rx), (p2dy, p2uy) = sorted((p21x, p22x)), sorted((p21y, p22y))
      if p11x == p12x and p21x == p22x and p11x == p21x and p1dy <= p2uy and p2dy <= p2uy:
        c = min(c, abs(p11x) + min(abs(max(p1dy, p2dy)), abs(min(p1uy, p2uy))))
      elif p11y == p12y and p21y == p22y and p11y == p21y and p1lx <= p2rx and p2lx <= p2rx:
        c = min(c, abs(p11y) + min(abs(max(p1lx, p2lx)), abs(min(p1rx, p2rx))))
      elif (p11y == p12y and p21x in range(p1lx, p1rx + 1) and p11y in range(p2dy, p2uy + 1)) or (p21y == p22y and p11x in range(p2lx, p2rx + 1) and p21y in range(p1dy, p1uy + 1)):
        c = min(c, abs(p21x) + abs(p11y) if p11y ==
                p12y else abs(p11x) + abs(p21y))
  print(c)


def part2():
  w1, w2 = [l.split(',') for l in reader()]
  D = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
  p1 = list(accumulate(w1, lambda a, b: (a[0] +
            D[b[0]][0] * int(b[1:]), a[1] + D[b[0]][1] * int(b[1:])), initial=(0, 0)))
  p2 = list(accumulate(w2, lambda a, b: (a[0] +
            D[b[0]][0] * int(b[1:]), a[1] + D[b[0]][1] * int(b[1:])), initial=(0, 0)))
  c = float('inf')
  s1 = abs(p1[1][0]) + abs(p1[1][1])
  for ((p11x, p11y), (p12x, p12y)) in pairwise(p1[1:]):
    (p1lx, p1rx), (p1dy, p1uy) = sorted((p11x, p12x)), sorted((p11y, p12y))
    s2 = abs(p2[1][0]) + abs(p2[1][1])
    for ((p21x, p21y), (p22x, p22y)) in pairwise(p2[1:]):
      (p2lx, p2rx), (p2dy, p2uy) = sorted((p21x, p22x)), sorted((p21y, p22y))
      if p11x == p12x and p21x == p22x and p11x == p21x and p1dy <= p2uy and p2dy <= p2uy:
        pass
      elif p11y == p12y and p21y == p22y and p11y == p21y and p1lx <= p2rx and p2lx <= p2rx:
        pass
      elif (p11y == p12y and p21x in range(p1lx, p1rx + 1) and p11y in range(p2dy, p2uy + 1)) or (p21y == p22y and p11x in range(p2lx, p2rx + 1) and p21y in range(p1dy, p1uy + 1)):
        ix, iy = (p21x, p11y) if p11y == p12y else (p11x, p21y)
        c = min(c, s1 + s2 + abs(ix - p11x) + abs(ix -
                p21x) + abs(iy - p11y) + abs(iy - p21y))
      s2 += abs(p21x - p22x) + abs(p21y - p22y)
    s1 += abs(p11x - p12x) + abs(p11y - p12y)
  print(c)


part1()
part2()
