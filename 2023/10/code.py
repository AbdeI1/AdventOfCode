import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  s = (-1, -1)
  for i in range(len(f)):
    for j in range(len(f[i])):
      if f[i][j] == "S":
        s = (i, j)
  hist = [s]
  if f[s[0] - 1][s[1]] in {"|", "7", "F"}:
    hist.append((s[0] - 1, s[1]))
  elif f[s[0] + 1][s[1]] in {"|", "J", "L"}:
    hist.append((s[0] + 1, s[1]))
  elif f[s[0]][s[1] - 1] in {"-", "L", "F"}:
    hist.append((s[0], s[1] - 1))
  elif f[s[0]][s[1] + 1] in {"-", "J", "7"}:
    hist.append((s[0], s[1] + 1))
  while hist[-1] != s:
    p = hist[-1]
    dirs = []
    match f[p[0]][p[1]]:
      case "|": dirs = [(1, 0), (-1, 0)]
      case "-": dirs = [(0, 1), (0, -1)]
      case "7": dirs = [(1, 0), (0, -1)]
      case "F": dirs = [(1, 0), (0, 1)]
      case "J": dirs = [(-1, 0), (0, -1)]
      case "L": dirs = [(-1, 0), (0, 1)]
    d = (0, 0)
    if hist[-2] == (p[0] + dirs[0][0], p[1] + dirs[0][1]):
      d = dirs[1]
    else:
      d = dirs[0]
    hist.append((p[0] + d[0], p[1] + d[1]))
  print(len(hist) // 2)


def part2():
  f = reader()
  s = (-1, -1)
  for i in range(len(f)):
    for j in range(len(f[i])):
      if f[i][j] == "S":
        s = (i, j)
  hist = [s]
  if f[s[0] - 1][s[1]] in {"|", "7", "F"}:
    hist.append((s[0] - 1, s[1]))
  elif f[s[0] + 1][s[1]] in {"|", "J", "L"}:
    hist.append((s[0] + 1, s[1]))
  elif f[s[0]][s[1] - 1] in {"-", "L", "F"}:
    hist.append((s[0], s[1] - 1))
  elif f[s[0]][s[1] + 1] in {"-", "J", "7"}:
    hist.append((s[0], s[1] + 1))
  while hist[-1] != s:
    p = hist[-1]
    dirs = []
    match f[p[0]][p[1]]:
      case "|": dirs = [(1, 0), (-1, 0)]
      case "-": dirs = [(0, 1), (0, -1)]
      case "7": dirs = [(1, 0), (0, -1)]
      case "F": dirs = [(1, 0), (0, 1)]
      case "J": dirs = [(-1, 0), (0, -1)]
      case "L": dirs = [(-1, 0), (0, 1)]
    d = (0, 0)
    if hist[-2] == (p[0] + dirs[0][0], p[1] + dirs[0][1]):
      d = dirs[1]
    else:
      d = dirs[0]
    hist.append((p[0] + d[0], p[1] + d[1]))
  h = set(hist)
  ans = 0
  for i in range(len(f)):
    x = 0
    r = ''
    for j in range(len(f[i])):
      if (i, j) in h:
        if f[i][j] == "-":
          continue
        if f[i][j] == 'F' or f[i][j] == 'L':
          r = f[i][j]
        if (f[i][j] == 'J' and r == 'F') or (f[i][j] == '7' and r == 'L'):
          x -= 1
        x += 1
      else:
        ans += x % 2
  print(ans)


part1()
part2()
