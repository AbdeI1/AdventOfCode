import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  P = list(map(eval, reader()))
  Q = [(p, i, 0) for i, p in enumerate(P)]
  V = {}
  D = [(0, 1), (1, 0), (-1, 0), (0, -1)]
  R = range(
      min(x for x, _ in P), max(x for x, _ in P) + 1
  ), range(
      min(y for _, y in P), max(y for _, y in P) + 1
  )
  while Q:
    (i, j), ii, d = Q.pop(0)
    if i not in R[0] or j not in R[1]:
      continue
    if (i, j) in V:
      p, dd = V[(i, j)]
      if d == dd and p != ii:
        V[(i, j)] = (-1, dd)
      continue
    else:
      V[(i, j)] = (ii, d)
    for di, dj in D:
      Q.append(((i + di, j + dj), ii, d + 1))
  A = [len(list(filter(lambda t: t[0] == i, V.values())))
       for i in range(len(P))]
  B = ({V[(i, j)][0] for i in R[0] for j in [R[1].start, R[1].stop - 1]}
       | {V[(i, j)][0] for i in [R[0].start, R[0].stop - 1] for j in R[1]}) - {-1}
  print(max(a for i, a in enumerate(A) if i not in B))


def part2():
  P = list(map(eval, reader()))
  R = range(
      min(x for x, _ in P), max(x for x, _ in P) + 1
  ), range(
      min(y for _, y in P), max(y for _, y in P) + 1
  )
  D = 10000
  print(len([(i, j) for i in R[0] for j in R[1] if sum(
    abs(i - ii) + abs(j - jj) for ii, jj in P) < D]))


part1()
part2()
