import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


D = {
  'U': (-1, 0),
  'D': (1, 0),
  'R': (0, 1),
  'L': (0, -1)
}


def part1():
  f = reader()
  B = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
  ]
  i, j = next((i, j) for i in range(len(B))
              for j in range(len(B[i])) if B[i][j] == 5)
  p = ""
  for l in f:
    for c in l:
      di, dj = D[c]
      if i + di in range(len(B)) and j + dj in range(len(B[i + di])):
        i, j = i + di, j + dj
    p += str(B[i][j])
  print(p)


def part2():
  f = reader()
  B = [
    ["", "", "1", "", ""],
    ["", "2", "3", "4", ""],
    ["5", "6", "7", "8", "9"],
    ["", "A", "B", "C", ""],
    ["", "", "D", "", ""]
  ]
  i, j = next((i, j) for i in range(len(B))
              for j in range(len(B[i])) if B[i][j] == '5')
  p = ""
  for l in f:
    for c in l:
      di, dj = D[c]
      if i + di in range(len(B)) and j + dj in range(len(B[i + di])) and B[i + di][j + dj]:
        i, j = i + di, j + dj
    p += B[i][j]
  print(p)


part1()
part2()
