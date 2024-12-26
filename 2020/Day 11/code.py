import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().split('\n')[:-1]


def reader2():
  f = reader()
  a = []
  i = 0
  while i < len(f):
    a.append([])
    for s in f[i]:
      a[i].append(s)
    i += 1
  return a


def clone(f):
  a = []
  i = 0
  while i < len(f):
    a.append([])
    for s in f[i]:
      if s == "#":
        a[i].append("#")
      if s == ".":
        a[i].append(".")
      if s == "L":
        a[i].append("L")
    i += 1
  return a


def part1():
  f = reader2()
  e = simulate(f)
  while e != simulate(e):
    e = simulate(e)
  print(countOccumpied(e))


def part2():
  f = reader2()
  e = simulate2(f)
  while e != simulate2(e):
    e = simulate2(e)
  # for i in e:
  # 	print(i)
  print(countOccumpied(e))


def simulate(f):
  e = clone(f)
  i = 0
  while i < len(f):
    j = 0
    while j < len(f[i]):
      if f[i][j] == 'L' or f[i][j] == '#':
        fullCount = 0
        if i != 0:
          if isFull(f[i - 1][j]):
            fullCount += 1
          if j != 0:
            if isFull(f[i - 1][j - 1]):
              fullCount += 1
          if j != len(f[i]) - 1:
            if isFull(f[i - 1][j + 1]):
              fullCount += 1
        if i != len(f) - 1:
          if isFull(f[i + 1][j]):
            fullCount += 1
          if j != 0:
            if isFull(f[i + 1][j - 1]):
              fullCount += 1
          if j != len(f[i]) - 1:
            if isFull(f[i + 1][j + 1]):
              fullCount += 1
        if j != 0:
          if isFull(f[i][j - 1]):
            fullCount += 1
        if j != len(f[i]) - 1:
          if isFull(f[i][j + 1]):
            fullCount += 1
        if f[i][j] == 'L' and fullCount == 0:
          e[i][j] = "#"
        if f[i][j] == '#' and fullCount >= 4:
          e[i][j] = "L"
      j += 1
    i += 1
  return (e)


def simulate2(f):
  e = clone(f)
  i = 0
  while i < len(f):
    j = 0
    while j < len(f[i]):
      if f[i][j] == 'L' or f[i][j] == '#':
        fullCount = 0
        if seesRight(i, j, f):
          fullCount += 1
        if seesLeft(i, j, f):
          fullCount += 1
        if seesUR(i, j, f):
          fullCount += 1
        if seesDR(i, j, f):
          fullCount += 1
        if seesDown(i, j, f):
          fullCount += 1
        if seesDL(i, j, f):
          fullCount += 1
        if seesUp(i, j, f):
          fullCount += 1
        if seesUL(i, j, f):
          fullCount += 1
        if f[i][j] == 'L' and fullCount == 0:
          e[i][j] = "#"
        if f[i][j] == '#' and fullCount >= 5:
          e[i][j] = "L"
      j += 1
    i += 1
  return (e)


def seesRight(i, j, f):
  jnew = j + 1
  while jnew < len(f[i]):
    if f[i][jnew] == "#":
      return True
    if f[i][jnew] == "L":
      return False
    jnew += 1
  return False


def seesLeft(i, j, f):
  jnew = j - 1
  while jnew >= 0:
    if f[i][jnew] == "#":
      return True
    if f[i][jnew] == "L":
      return False
    jnew -= 1
  return False


def seesUR(i, j, f):
  inew = i - 1
  jnew = j + 1
  while inew >= 0 and jnew < len(f[inew]):
    if f[inew][jnew] == "#":
      return True
    if f[inew][jnew] == "L":
      return False
    inew -= 1
    jnew += 1
  return False


def seesDR(i, j, f):
  inew = i + 1
  jnew = j + 1
  while inew < len(f) and jnew < len(f[inew]):
    if f[inew][jnew] == "#":
      return True
    if f[inew][jnew] == "L":
      return False
    inew += 1
    jnew += 1
  return False


def seesDown(i, j, f):
  inew = i + 1
  while inew < len(f):
    if f[inew][j] == "#":
      return True
    if f[inew][j] == "L":
      return False
    inew += 1
  return False


def seesUp(i, j, f):
  inew = i - 1
  while inew >= 0:
    if f[inew][j] == "#":
      return True
    if f[inew][j] == "L":
      return False
    inew -= 1
  return False


def seesDL(i, j, f):
  inew = i + 1
  jnew = j - 1
  while inew < len(f) and jnew >= 0:
    if f[inew][jnew] == "#":
      return True
    if f[inew][jnew] == "L":
      return False
    inew += 1
    jnew -= 1
  return False


def seesUL(i, j, f):
  inew = i - 1
  jnew = j - 1
  while inew >= 0 and jnew >= 0:
    if f[inew][jnew] == "#":
      return True
    if f[inew][jnew] == "L":
      return False
    inew -= 1
    jnew -= 1
  return False


def countOccumpied(e):
  count = 0
  for i in e:
    count += i.count("#")
  return count


def isFull(c):
  return c == "#"


part1()
part2()
