import pathlib

def reader():
  f = open(f"{pathlib.Path(__file__).parent.resolve()}/Day17input.txt", 'r').read()
  f = f.split('\n')
  f = f[:-1]
  return f

ROCKS = [
  [['#', '#', '#', '#']],
  [['.', '#', '.'],
   ['#', '#', '#'],
   ['.', '#', '.']],
  [['.', '.', '#'],
   ['.', '.', '#'],
   ['#', '#', '#']],
  [['#'],
   ['#'],
   ['#'],
   ['#']],
  [['#', '#'],
   ['#', '#']]
]

def part1():
  f = reader()
  M = f[0]
  n = -1
  grid = [['.' for _ in range(7)] for _ in range(10000)]
  h = 0
  for c in range(2022):
    r = ROCKS[c%len(ROCKS)]
    i, j = len(grid)-(h+3+len(r)), 2
    while True:
      n += 1
      n %= len(M)
      if M[n] == '>':
        if j + len(r[0]) < len(grid[i]):
          j += 1
          for x in range(len(r)):
            for y in range(len(r[x])):
              if r[x][y] == '#' and grid[i+x][j+y] == '#':
                j -= 1
                break
            else:
              continue
            break
      else:
        if j > 0:
          j -= 1
          for x in range(len(r)):
            for y in range(len(r[x])):
              if r[x][y] == '#' and grid[i+x][j+y] == '#':
                j += 1
                break
            else:
              continue
            break
      done = False
      if i + len(r) < len(grid):
        i += 1
        for x in range(len(r)):
            for y in range(len(r[x])):
              if r[x][y] == '#' and grid[i+x][j+y] == '#':
                i -= 1
                done = True
                break
            else:
              continue
            break
      else:
        done = True
      if done:
        h = max(h, len(grid) - i)
        for x in range(len(r)):
          for y in range(len(r[x])):
            if r[x][y] == '#': grid[i+x][j+y] = '#'
        break
  print(h)

def part2():
  f = reader()
  M = f[0]
  n = -1
  grid = [['.' for _ in range(7)] for _ in range(100000)]
  H = [0]
  h = 0
  for c in range(6000):
    r = ROCKS[c%len(ROCKS)]
    i, j = len(grid)-(h+3+len(r)), 2
    while True:
      n += 1
      n %= len(M)
      if M[n] == '>':
        if j + len(r[0]) < len(grid[i]):
          j += 1
          for x in range(len(r)):
            for y in range(len(r[x])):
              if r[x][y] == '#' and grid[i+x][j+y] == '#':
                j -= 1
                break
            else:
              continue
            break
      else:
        if j > 0:
          j -= 1
          for x in range(len(r)):
            for y in range(len(r[x])):
              if r[x][y] == '#' and grid[i+x][j+y] == '#':
                j += 1
                break
            else:
              continue
            break
      done = False
      if i + len(r) < len(grid):
        i += 1
        for x in range(len(r)):
            for y in range(len(r[x])):
              if r[x][y] == '#' and grid[i+x][j+y] == '#':
                i -= 1
                done = True
                break
            else:
              continue
            break
      else:
        done = True
      if done:
        h = max(h, len(grid) - i)
        H.append(h)
        for x in range(len(r)):
          for y in range(len(r[x])):
            if r[x][y] == '#': grid[i+x][j+y] = '#'
        break
  Hd = []
  for i in range(1, len(H)):
    Hd.append(H[i] - H[i-1])
  def findRepeat(arr):
    for l in range(20, len(arr)//2):
      for i in range(len(arr)-2*l):
        for j in range(l):
          if arr[i+j] != arr[i+l+j]:
            break
        else:
          return (i, l)
  (i, l) = findRepeat(Hd)
  T = 1000000000000
  h = 0
  h += sum(Hd[:i])
  T -= i
  h += sum(Hd[i:(i+l)]) * (T//l)
  T %= l
  h += sum(Hd[i:(i+T)])
  print(h)

part1()
part2()
