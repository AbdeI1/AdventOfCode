import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  M = reader()
  n = {}
  for i in range(len(M)):
    for j in range(len(M[i])):
      if M[i][j] != '.':
        c = M[i][j]
        if c not in n:
          n[c] = []
        n[c].append((i, j))
  A = set()
  for k in n:
    l = n[k]
    for i in range(len(l)):
      for j in range(i + 1, len(l)):
        x1, y1 = l[i]
        x2, y2 = l[j]
        a1 = (x1 - (x2 - x1), y1 - (y2 - y1))
        a2 = (x2 + (x2 - x1), y2 + (y2 - y1))
        if a1[0] in range(len(M)) and a1[1] in range(len(M[a1[0]])):
          A.add(a1)
        if a2[0] in range(len(M)) and a2[1] in range(len(M[a2[0]])):
          A.add(a2)
  print(len(A))


def part2():
  M = reader()
  n = {}
  for i in range(len(M)):
    for j in range(len(M[i])):
      if M[i][j] != '.':
        c = M[i][j]
        if c not in n:
          n[c] = []
        n[c].append((i, j))
  A = set()
  for k in n:
    l = n[k]
    for i in range(len(l)):
      for j in range(i + 1, len(l)):
        x1, y1 = l[i]
        x2, y2 = l[j]
        dx, dy = x2 - x1, y2 - y1
        a1 = x1, y1
        while a1[0] in range(len(M)) and a1[1] in range(len(M[a1[0]])):
          A.add(a1)
          a1 = a1[0] - dx, a1[1] - dy
        a2 = x2, y2
        while a2[0] in range(len(M)) and a2[1] in range(len(M[a2[0]])):
          A.add(a2)
          a2 = a2[0] + dx, a2[1] + dy
  print(len(A))


part1()
part2()
