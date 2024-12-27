import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()  # just reads input from txt file, don't want to show directory names
  cubes = {}
  i = 0
  while i < len(f):
    j = 0
    while j < len(f[i]):
      if f[i][j] == '#':
        cubes[(j, i, 0)] = '#'
      else:
        cubes[(j, i, 0)] = '.'
      j += 1
    i += 1
  i = 0
  while i < 6:
    cubes = simulate(cubes)
    i += 1
  total = 0
  for x in cubes:
    if cubes[x] == '#':
      total += 1
  print(total)


def simulate(cubes):
  new = {}
  for c in cubes:
    x = checkNeighbors(c, cubes)
    if cubes[c] == '#':
      if x == 2 or x == 3:
        new[c] = '#'
      else:
        new[c] = '.'
      n = findNeighbors(c)
      for x in n:
        if x not in cubes:
          k = checkNeighbors(x, cubes)
          if k == 3:
            new[x] = '#'
    elif cubes[c] == '.':
      if x == 3:
        new[c] = '#'
      else:
        new[c] = '.'
  return new


def findNeighbors(c):
  n = []
  i = -1
  while i < 2:
    j = -1
    while j < 2:
      k = -1
      while k < 2:
        if not (i == 0 and j == 0 and k == 0):
          n.append((c[0] + i, c[1] + j, c[2] + k))
        k += 1
      j += 1
    i += 1
  return n


def checkNeighbors(c, cubes):
  n = findNeighbors(c)
  total = 0
  for x in n:
    if x in cubes:
      if cubes[x] == '#':
        total += 1
  return total


def part2():
  f = reader()
  cubes = {}
  i = 0
  while i < len(f):
    j = 0
    while j < len(f[i]):
      if f[i][j] == '#':
        cubes[(j, i, 0, 0)] = '#'
      else:
        cubes[(j, i, 0, 0)] = '.'
      j += 1
    i += 1
  i = 0
  while i < 6:
    cubes = simulate4d(cubes)
    i += 1
  total = 0
  for x in cubes:
    if cubes[x] == '#':
      total += 1
  print(total)


def simulate4d(cubes):
  new = {}
  for c in cubes:
    x = checkNeighbors4d(c, cubes)
    if cubes[c] == '#':
      if x == 2 or x == 3:
        new[c] = '#'
      else:
        new[c] = '.'
      n = findNeighbors4d(c)
      for x in n:
        if x not in cubes:
          k = checkNeighbors4d(x, cubes)
          if k == 3:
            new[x] = '#'
    elif cubes[c] == '.':
      if x == 3:
        new[c] = '#'
      else:
        new[c] = '.'
  return new


def findNeighbors4d(c):
  n = []
  i = -1
  while i < 2:
    j = -1
    while j < 2:
      k = -1
      while k < 2:
        w = -1
        while w < 2:
          if not (i == 0 and j == 0 and k == 0 and w == 0):
            n.append((c[0] + i, c[1] + j, c[2] + k, c[3] + w))
          w += 1
        k += 1
      j += 1
    i += 1
  return n


def checkNeighbors4d(c, cubes):
  n = findNeighbors4d(c)
  total = 0
  for x in n:
    if x in cubes:
      if cubes[x] == '#':
        total += 1
  return total


part1()
part2()
