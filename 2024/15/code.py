import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  M, moves = '\n'.join(reader()).split('\n\n')
  M = list(map(list, M.split('\n')))
  moves = moves.replace('\n', '')
  p = next((i, j) for i in range(len(M))
           for j in range(len(M[i])) if M[i][j] == '@')
  movements = {
    '<': (0, -1),
    '>': (0, 1),
    '^': (-1, 0),
    'v': (1, 0)
  }
  for m in moves:
    di, dj = movements[m]
    i, j = p
    while M[i][j] not in {'#', '.'}:
      i, j = i + di, j + dj
    if M[i][j] == '.':
      while M[i][j] != '@':
        M[i][j] = M[i - di][j - dj]
        i, j = i - di, j - dj
      M[i][j] = '.'
      p = i + di, j + dj
  print(sum(100 * i + j for i in range(len(M))
        for j in range(len(M[i])) if M[i][j] == 'O'))


def part2():
  M, moves = '\n'.join(reader()).split('\n\n')
  M = list(map(lambda s: list(s.replace('#', '##').replace(
    'O', '[]').replace('.', '..').replace('@', '@.')), M.split('\n')))
  moves = moves.replace('\n', '')
  p = next((i, j) for i in range(len(M))
           for j in range(len(M[i])) if M[i][j] == '@')
  movements = {
    '<': (0, -1),
    '>': (0, 1),
    '^': (-1, 0),
    'v': (1, 0)
  }

  def search(x, y, di=0, dj=0, V=set()):
    if M[x][y] == '#':
      return False
    if M[x][y] == '.' or (x, y) in V:
      return True
    V.add((x, y))
    b = search(x + di, y + dj, di, dj, V)
    return b if M[x][y] == '@' or M[x][y] == 'O' else b and (search(x, y + 1, di, dj, V) if M[x][y] == '[' else search(x, y - 1, di, dj, V))

  for m in moves:
    di, dj = movements[m]
    i, j = p
    ps = set()
    if search(i, j, di, dj, ps):
      for ii, jj in sorted(ps, key=lambda t: (-di * t[0], -dj * t[1])):
        M[ii + di][jj + dj] = M[ii][jj]
        M[ii][jj] = '.'
      p = i + di, j + dj
  print(sum(100 * i + j for i in range(len(M))
        for j in range(len(M[i])) if M[i][j] == '['))


part1()
part2()
