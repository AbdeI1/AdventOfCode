import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().split('\n')[:-1]


def foldu(p, y):
  pn = [[0] * (len(p[0])) for i in range(y)]
  for i in range(y):
    for j in range(len(p[0])):
      if p[i][j] == 1 or p[-i - 1][j] == 1:
        pn[i][j] = 1
  return pn


def foldl(p, x):
  pn = [[0] * (x) for i in range(len(p))]
  for i in range(len(p)):
    for j in range(x):
      if p[i][j] == 1 or p[i][-j - 1] == 1:
        pn[i][j] = 1
  return pn


def part1():
  f = reader()
  coords = f[:1004]
  folds = f[1005:]
  points = [[0] * (1311) for i in range(895)]
  for c in coords:
    nums = c.split(',')
    points[int(nums[1])][int(nums[0])] = 1
  fold1 = int(folds[0].split('=')[1])
  res = foldl(points, fold1)
  s = 0
  for i in range(len(res)):
    for j in range(len(res[i])):
      if res[i][j] == 1:
        s += 1
  print(s)


def part2():
  f = reader()
  coords = f[:1004]
  folds = f[1005:]
  points = [[0] * (1311) for i in range(895)]
  for c in coords:
    nums = c.split(',')
    points[int(nums[1])][int(nums[0])] = 1
  for f in folds:
    t = f.split('=')
    num = int(t[1])
    l = t[0][-1]
    if l == 'x':
      points = foldl(points, num)
    else:
      points = foldu(points, num)
  for i in range(len(points)):
    for j in range(len(points[i])):
      if points[i][j] == 1:
        print('@', end='')
      else:
        print(' ', end='')
    print()


part1()
part2()
