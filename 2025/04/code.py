import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  A = 0
  for i in range(len(f)):
    for j in range(len(f[i])):
      if f[i][j] == '@':
        c = 0
        for di in range(-1, 2):
          for dj in range(-1, 2):
            if di == 0 and dj == 0: continue
            ii = i + di
            jj = j + dj
            if ii in range(len(f)) and jj in range(len(f[ii])) and f[ii][jj] == '@':
              c += 1
        if c < 4:
          A += 1
  print(A)


def part2():
  f = [list(r) for r in reader()]

  def rem():
    A = 0
    for i in range(len(f)):
      for j in range(len(f[i])):
        if f[i][j] == '@':
          c = 0
          for di in range(-1, 2):
            for dj in range(-1, 2):
              if di == 0 and dj == 0: continue
              ii = i + di
              jj = j + dj
              if ii in range(len(f)) and jj in range(len(f[ii])) and f[ii][jj] == '@':
                c += 1
          if c < 4:
            f[i][j] = 'x'
            A += 1
    return A
  
  A = a = rem()
  while a != 0:
    A += (a := rem())
  print(A)


part1()
part2()
