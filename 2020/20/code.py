import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def rotate(t):
  return [[t[i][-1 - j] for i in range(len(t))] for j in range(len(t[0]))]


def flip(t):
  return [t[i][::-1] for i in range(len(t))]


def part1():
  T = {int(k[:-1].split()[-1]): list(map(list, v.split('\n'))) for k, _, v in [s.partition(
    '\n') for s in '\n'.join(reader()).split('\n\n')]}
  i = min(T)
  P = {i: (0, 0)}
  Q = [i]
  while Q:
    i = Q.pop()
    t0 = T[i]
    x, y = P[i]
    for k, t in T.items():
      if k in P: continue
      for _ in range(2):
        for _ in range(4):
          if t[0] == t0[-1]: P[k] = x, y + 1
          elif t[-1] == t0[0]: P[k] = x, y - 1
          elif [r[0] for r in t] == [r[-1] for r in t0]: P[k] = x + 1, y
          elif [r[-1] for r in t] == [r[0] for r in t0]: P[k] = x - 1, y
          if k in P:
            T[k] = t
            Q.append(k)
            break
          t = rotate(t)
        else:
          t = flip(t)
          continue
        break
  X = {x for x, _ in P.values()}
  Y = {y for _, y in P.values()}
  G = [[None for _ in range(min(X), max(X) + 1)]
       for _ in range(min(Y), max(Y) + 1)]
  for i, (x, y) in P.items(): G[y - min(Y)][x - min(X)] = i
  print(G[0][0] * G[0][-1] * G[-1][0] * G[-1][-1])


def part2():
  T = {int(k[:-1].split()[-1]): list(map(list, v.split('\n'))) for k, _, v in [s.partition(
    '\n') for s in '\n'.join(reader()).split('\n\n')]}
  i = min(T)
  P = {i: (0, 0)}
  Q = [i]
  while Q:
    i = Q.pop()
    t0 = T[i]
    x, y = P[i]
    for k, t in T.items():
      if k in P: continue
      for _ in range(2):
        for _ in range(4):
          if t[0] == t0[-1]: P[k] = x, y + 1
          elif t[-1] == t0[0]: P[k] = x, y - 1
          elif [r[0] for r in t] == [r[-1] for r in t0]: P[k] = x + 1, y
          elif [r[-1] for r in t] == [r[0] for r in t0]: P[k] = x - 1, y
          if k in P:
            T[k] = t
            Q.append(k)
            break
          t = rotate(t)
        else:
          t = flip(t)
          continue
        break
  X = {x for x, _ in P.values()}
  Y = {y for _, y in P.values()}
  h, w = len(T[i]) - 2, len(T[i][0]) - 2
  I = [['.' for _ in range((max(X) - min(X) + 1) * w)]
       for _ in range((max(Y) - min(Y) + 1) * h)]
  for i, (x, y) in P.items():
    t = T[i]
    for i, r in enumerate(t[1:-1]):
      I[(y - min(Y)) * h + i][(x - min(X)) * w:(x - min(X) + 1) * w] = r[1:-1]
  M = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
     ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' '],
    ['#', ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ',
     ' ', '#', '#', ' ', ' ', ' ', ' ', '#', '#', '#'],
    [' ', '#', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ',
     '#', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ']
  ]
  for _ in range(2):
    for _ in range(4):
      c = 0
      for i in range(len(I) - len(M)):
        for j in range(len(I[i]) - len(M[0])):
          if all(I[i + ii][j + jj] == '#' for ii in range(len(M)) for jj in range(len(M[ii])) if M[ii][jj] == '#'):
            c += 1
      if c != 0:
        print(sum(r.count('#') for r in I) - c * sum(r.count('#') for r in M))
      I = rotate(I)
    I = flip(I)


part1()
part2()
