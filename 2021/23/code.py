import heapq


import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


costs = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
rooms = {'A': 3, 'B': 5, 'C': 7, 'D': 9}
roomsI = {3: 'A', 5: 'B', 7: 'C', 9: 'D'}


def finished(b):
  for i in {2, 3, 4, 5}:
    for j in {3, 5, 7, 9}:
      if (i, j) not in b:
        return False
      if b[(i, j)] != roomsI[j]:
        return False
  return True


def possibleMoves(b):
  moves = []
  for (i, j) in b:
    c = b[(i, j)]
    if i == 1:
      if j < rooms[c]:
        for k in range(j + 1, rooms[c] + 1):
          if (1, k) in b:
            break
        else:
          for k in range(2, 6):
            if (k, rooms[c]) in b and b[(k, rooms[c])] != c:
              break
          else:
            k = 5
            while (k, rooms[c]) in b:
              k -= 1
            cost = costs[c] * (abs(k - i) + abs(rooms[c] - j))
            moves.append((cost, (i, j), (k, rooms[c])))
      else:
        k = j - 1
        while k > rooms[c]:
          if (1, k) in b:
            break
          k -= 1
        else:
          for k in range(2, 6):
            if (k, rooms[c]) in b and b[(k, rooms[c])] != c:
              break
          else:
            k = 5
            while (k, rooms[c]) in b:
              k -= 1
            cost = costs[c] * (abs(k - i) + abs(rooms[c] - j))
            moves.append((cost, (i, j), (k, rooms[c])))
    else:
      if j == rooms[c]:
        for k in range(2, 6):
          if (k, rooms[c]) in b and b[(k, rooms[c])] != c:
            break
        else:
          continue
      if i >= 3 and (i - 1, j) in b:
        pass
      else:
        for k in range(j + 1, 12):
          if k == 3 or k == 5 or k == 7 or k == 9:
            continue
          (x, y) = (1, k)
          if (x, y) in b:
            break
          cost = costs[c] * (abs(x - i) + abs(y - j))
          moves.append((cost, (i, j), (x, y)))
        k = j - 1
        while k > 0:
          if k == 3 or k == 5 or k == 7 or k == 9:
            k -= 1
            continue
          (x, y) = (1, k)
          if (x, y) in b:
            break
          cost = costs[c] * (abs(x - i) + abs(y - j))
          moves.append((cost, (i, j), (x, y)))
          k -= 1
  return moves


def move(b, m):
  start = m[1]
  end = m[2]
  nb = b.copy()
  nb[end] = b[start]
  del nb[start]
  return nb


def toString(b):
  res = ""
  for i in range(7):
    for j in range(13):
      if (i, j) in b:
        res += b[(i, j)]
      elif i == 1 and 0 < j and j < 12:
        res += '.'
      elif 2 <= i and i <= 5 and j in {3, 5, 7, 9}:
        res += '.'
      elif i in {3, 4, 5, 6} and j in {0, 1, 11, 12}:
        res += ' '
      else:
        res += '#'
    res += '\n'
  return res


def fromString(s):
  f = s.split('\n')
  board = {}
  for i in range(len(f)):
    for j in range(len(f[i])):
      if f[i][j] != ' ' and f[i][j] != '.' and f[i][j] != '#':
        board[(i, j)] = f[i][j]
  return board


def part1():
  f = reader()
  # done by hand


def part2():
  f = reader()
  board = {}
  for i in range(len(f)):
    for j in range(len(f[i])):
      if f[i][j] != ' ' and f[i][j] != '.' and f[i][j] != '#':
        board[(i, j)] = f[i][j]
  q = [(0, toString(board))]
  visited = set()
  while len(q) > 0:
    (cost, s) = heapq.heappop(q)
    b = fromString(s)
    if s in visited:
      continue
    visited.add(s)
    if finished(b):
      print("finished: ", cost)
      break
    moves = possibleMoves(b)
    for m in moves:
      nb = move(b, m)
      heapq.heappush(q, (m[0] + cost, toString(nb)))


part1()
part2()
