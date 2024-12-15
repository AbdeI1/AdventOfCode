import pathlib


def reader():
  return open(f"{pathlib.Path(__file__).parent.resolve()}/input.txt", 'r').read().split('\n')[:-1]


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
  for m in moves:
    di, dj = movements[m]
    i, j = p
    if di == 0:
      while M[i][j] not in {'#', '.'}:
        i, j = i + di, j + dj
      if M[i][j] == '.':
        while M[i][j] != '@':
          M[i][j] = M[i - di][j - dj]
          i, j = i - di, j - dj
        M[i][j] = '.'
        p = i + di, j + dj
    else:
      ps = set()

      def r(x, y):
        if M[x][y] == '#':
          return False
        if M[x][y] == '.':
          return True
        if (x, y) in ps:
          return True
        ps.add((x, y))
        if M[x][y] == '@':
          return r(x + di, y + dj)
        if M[x][y] == '[':
          return r(x, y + 1) and r(x + di, y + dj)
        if M[x][y] == ']':
          return r(x, y - 1) and r(x + di, y + dj)

      if r(i, j):
        for ii, jj in sorted(ps, key=lambda t: -di * t[0]):
          M[ii + di][jj + dj] = M[ii][jj]
          M[ii][jj] = '.'
        p = i + di, j + dj
  print(sum(100 * i + j for i in range(len(M))
        for j in range(len(M[i])) if M[i][j] == '['))


part1()
part2()
