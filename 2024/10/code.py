import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  M = reader()
  D = [(1, 0), (-1, 0), (0, 1), (0, -1)]
  c = 0
  for i in range(len(M)):
    for j in range(len(M[i])):
      if M[i][j] == '0':
        q = [(i, j)]
        v = set()
        while q:
          ii, jj = q.pop()
          if (ii, jj) in v:
            continue
          v.add((ii, jj))
          if M[ii][jj] == '9':
            c += 1
          for d in D:
            iii, jjj = ii + d[0], jj + d[1]
            if iii in range(len(M)) and jjj in range(len(M[iii])) and ord(M[iii][jjj]) == ord(M[ii][jj]) + 1:
              q.append((iii, jjj))
  print(c)


def part2():
  M = reader()
  D = [(1, 0), (-1, 0), (0, 1), (0, -1)]
  c = 0
  for i in range(len(M)):
    for j in range(len(M[i])):
      if M[i][j] == '0':
        q = [(i, j)]
        while q:
          ii, jj = q.pop()
          if M[ii][jj] == '9':
            c += 1
          for d in D:
            iii, jjj = ii + d[0], jj + d[1]
            if iii in range(len(M)) and jjj in range(len(M[iii])) and ord(M[iii][jjj]) == ord(M[ii][jj]) + 1:
              q.append((iii, jjj))
  print(c)


part1()
part2()
