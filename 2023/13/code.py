import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = [[list(s) for s in s.split('\n')]
       for s in '\n'.join(reader()).split('\n\n')]

  def rowMatch(g, i, j):
    for k in range(len(g[i])):
      if g[i][k] != g[j][k]:
        return False
    return True

  def colMatch(g, i, j):
    for k in range(len(g)):
      if g[k][i] != g[k][j]:
        return False
    return True

  ans = 0
  for g in f:
    for i in range(len(g) - 1):
      i1 = i
      i2 = i + 1
      while i1 >= 0 and i2 < len(g) and rowMatch(g, i1, i2):
        i1 -= 1
        i2 += 1
      if i1 == -1 or i2 == len(g):
        ans += 100 * (i + 1)
        break
    for i in range(len(g[0]) - 1):
      i1 = i
      i2 = i + 1
      while i1 >= 0 and i2 < len(g[0]) and colMatch(g, i1, i2):
        i1 -= 1
        i2 += 1
      if i1 == -1 or i2 == len(g[0]):
        ans += i + 1
        break
  print(ans)


def part2():
  f = [[list(s) for s in s.split('\n')]
       for s in '\n'.join(reader()).split('\n\n')]

  def rowMatch(g, i, j):
    m = 0
    for k in range(len(g[i])):
      if g[i][k] != g[j][k]:
        m += 1
    return m

  def colMatch(g, i, j):
    m = 0
    for k in range(len(g)):
      if g[k][i] != g[k][j]:
        m += 1
    return m

  ans = 0
  for g in f:
    for i in range(len(g) - 1):
      i1 = i
      i2 = i + 1
      m = 0
      while i1 >= 0 and i2 < len(g) and m <= 1:
        m += rowMatch(g, i1, i2)
        i1 -= 1
        i2 += 1
      if m == 1 and (i1 == -1 or i2 == len(g)):
        ans += 100 * (i + 1)
        break
    for i in range(len(g[0]) - 1):
      i1 = i
      i2 = i + 1
      m = 0
      while i1 >= 0 and i2 < len(g[0]) and m <= 1:
        m += colMatch(g, i1, i2)
        i1 -= 1
        i2 += 1
      if m == 1 and (i1 == -1 or i2 == len(g[0])):
        ans += i + 1
        break
  print(ans)


part1()
part2()
