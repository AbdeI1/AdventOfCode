import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().split('\n')[:-1]


DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def part1():
  f = reader()
  m = list(map(lambda s: list(map(int, list(s))), f))
  ans = 0
  for i in range(len(m)):
    for j in range(len(m[i])):
      s = m[i][j]
      for D in DIRS:
        a, b = i + D[0], j + D[1]
        while a in range(len(m)) and b in range(len(m[a])):
          if m[a][b] >= s:
            break
          a += D[0]
          b += D[1]
        else:
          ans += 1
          break
  print(ans)


def part2():
  f = reader()
  m = list(map(lambda s: list(map(int, list(s))), f))
  ans = 0
  for i in range(len(m)):
    for j in range(len(m[i])):
      s = m[i][j]
      score = 1
      for D in DIRS:
        a, b = i + D[0], j + D[1]
        v = 0
        while a in range(len(m)) and b in range(len(m[a])):
          v += 1
          if m[a][b] >= s:
            break
          a += D[0]
          b += D[1]
        score *= v
      ans = max(ans, score)
  print(ans)


part1()
part2()
