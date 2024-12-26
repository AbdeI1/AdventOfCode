import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().split('\n')[:-1]


def getNum(points, i, j):
  ans = ""
  for a in range(-1, 2):
    for b in range(-1, 2):
      if (i + a, j + b) in points:
        ans += "1"
      else:
        ans += "0"
  return int(ans, 2)


def getNum2(points, i, j):
  ans = ""
  for a in range(-1, 2):
    for b in range(-1, 2):
      if 0 <= i + a and i + a < len(points) and 0 <= j + b and j + b < len(points) and points[i + a][j + b] == '#':
        ans += "1"
      else:
        ans += "0"
  return int(ans, 2)


def getNum3(points, i, j):
  ans = ""
  for a in range(-1, 2):
    for b in range(-1, 2):
      if not (0 <= i + a and i + a < len(points) and 0 <= j + b and j + b < len(points)):
        ans += "1"
      elif 0 <= i + a and i + a < len(points) and 0 <= j + b and j + b < len(points) and points[i + a][j + b] == '#':
        ans += "1"
      else:
        ans += "0"
  return int(ans, 2)


def enhance(points, enhancement):
  res = set()
  for i in rangex:
    for j in rangey:
      ind = enhancement[getNum(points, i, j)]
      if ind == '#':
        res.add((i, j))
  return res


def enhance2(points, enhancement):
  res = [['.'] * len(points) for _ in range(len(points))]
  for i in range(len(res)):
    for j in range(len(res)):
      res[i][j] = enhancement[getNum2(points, i, j)]
  return res


def enhance3(points, enhancement):
  res = [['.'] * len(points) for _ in range(len(points))]
  for i in range(len(res)):
    for j in range(len(res)):
      res[i][j] = enhancement[getNum3(points, i, j)]
  return res


def part1():
  f = reader()
  enhancement = f[0]
  image = f[2:]
  points = set()
  for i in range(len(image)):
    for j in range(len(image[i])):
      if image[i][j] == '#':
        points.add((i, j))
  im = [['.'] * (len(image) + 10) for _ in range(len(image) + 10)]
  for i in range(5, len(im) - 5):
    for j in range(5, len(im) - 5):
      im[i][j] = image[i - 5][j - 5]
  res = enhance2(im, enhancement)
  res2 = enhance3(res, enhancement)
  count = 0
  for i in range(len(res2)):
    for j in range(len(res2[i])):
      if res2[i][j] == '#':
        count += 1
  print(count)


def part2():
  f = reader()
  enhancement = f[0]
  image = f[2:]
  points = set()
  for i in range(len(image)):
    for j in range(len(image[i])):
      if image[i][j] == '#':
        points.add((i, j))
  im = [['.'] * (len(image) + 10) for _ in range(len(image) + 10)]
  for i in range(5, len(im) - 5):
    for j in range(5, len(im) - 5):
      im[i][j] = image[i - 5][j - 5]
  res2 = image
  for _ in range(25):
    im = [['.'] * (len(res2) + 10) for _ in range(len(res2) + 10)]
    for i in range(5, len(im) - 5):
      for j in range(5, len(im) - 5):
        im[i][j] = res2[i - 5][j - 5]
    res = enhance2(im, enhancement)
    res2 = enhance3(res, enhancement)
  count = 0
  for i in range(len(res2)):
    for j in range(len(res2[i])):
      if res2[i][j] == '#':
        count += 1
  print(count)


part1()
part2()
