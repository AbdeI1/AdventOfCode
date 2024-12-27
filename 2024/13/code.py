import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = list(map(lambda s: s.split('\n'), '\n'.join(reader()).split('\n\n')))
  M = []
  for l in f:
    Ax = int(l[0][(l[0].find('X+') + 2):l[0].find(',')])
    Ay = int(l[0][(l[0].find('Y+') + 2):])
    Bx = int(l[1][(l[1].find('X+') + 2):l[1].find(',')])
    By = int(l[1][(l[1].find('Y+') + 2):])
    X = int(l[2][(l[2].find('X=') + 2):l[2].find(',')])
    Y = int(l[2][(l[2].find('Y=') + 2):])
    M.append([(Ax, Ay), (Bx, By), (X, Y)])
  t = 0
  for m in M:
    l = -1, 0
    for i in range(101):
      for j in range(101):
        cost = 3 * i + j
        pos = i * m[0][0] + j * m[1][0], i * m[0][1] + j * m[1][1]
        if pos == m[2]:
          l = (0, cost) if l[0] == -1 else (0, min(l[1], cost))
    if l[0] == 0:
      t += l[1]
  print(t)


def part2():
  f = list(map(lambda s: s.split('\n'), '\n'.join(reader()).split('\n\n')))
  M = []
  for l in f:
    Ax = int(l[0][(l[0].find('X+') + 2):l[0].find(',')])
    Ay = int(l[0][(l[0].find('Y+') + 2):])
    Bx = int(l[1][(l[1].find('X+') + 2):l[1].find(',')])
    By = int(l[1][(l[1].find('Y+') + 2):])
    X = int(l[2][(l[2].find('X=') + 2):l[2].find(',')])
    Y = int(l[2][(l[2].find('Y=') + 2):])
    M.append([(Ax, Ay), (Bx, By), (X + 10000000000000, Y + 10000000000000)])
  t = 0
  for m in M:
    d = m[0][0] * m[1][1] - m[1][0] * m[0][1]
    if d != 0:
      i, j = (m[2][0] * m[1][1] - m[2][1] * m[1][0]) / d, (m[2]
                                                            [1] * m[0][0] - m[2][0] * m[0][1]) / d
      if i == int(i) and j == int(j):
        t += int(3 * i + j)
  print(t)


part1()
part2()
