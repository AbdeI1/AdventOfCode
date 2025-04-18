import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = [(lambda a: (int(a[3]), int(a[6]), int(a[13])))(l.split())
       for l in reader()]
  T = 2503
  D = 0
  for v, rt, wt in f:
    t = rt + wt
    d = v * rt * (T // t) + v * min(T % t, rt)
    D = max(D, d)
  print(D)


def part2():
  f = [(lambda a: (int(a[3]), int(a[6]), int(a[13])))(l.split())
       for l in reader()]
  T = 2503
  D = [0 for _ in range(len(f))]
  P = [0 for _ in range(len(f))]
  for t in range(T):
    mi, md = -1, 0
    for i, (v, rt, wt) in enumerate(f):
      if t % (rt + wt) < rt:
        D[i] += v
      if D[i] > md:
        mi, md = i, D[i]
    P[mi] += 1
  print(max(P))


part1()
part2()
