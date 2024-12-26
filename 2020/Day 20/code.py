import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().split('\n')[:-1]


def part1():
  f = '\n'.join(reader()).split('\n\n')
  tileIds = []
  tiles = []
  for s in f:
    x = s.split('\n')
    tileIds.append(int(x[0][5: -1]))
    tiles.append([list(l) for l in x[1:]])
  d = {}
  j = 0
  while j < 144:
    d[j] = []
    i = 0
    while i < len(tiles):
      if i != j:
        if checkUp(tiles[j], tiles[i]):
          d[j].append(i)
        if checkDown(tiles[j], tiles[i]):
          d[j].append(i)
        if checkRight(tiles[j], tiles[i]):
          d[j].append(i)
        if checkLeft(tiles[j], tiles[i]):
          d[j].append(i)
      i += 1
    j += 1
  print(d)
  # corners are: 5, 16, 72, 143
  t = tiles[16]
  t = rotate(rotate(t))
  print(checkRightNums(t, tiles[67]))
  print(checkDownNums(t, tiles[98]))
  print(checkRightNums(t, tiles[98]))
  print(checkDownNums(t, tiles[67]))


def tester():
  f = reader()
  tileIds = []
  tiles = []
  for s in f:
    x = s.split('\n')
    tileIds.append(int(x[0][5: -1]))
    tiles.append([list(l) for l in x[1:]])
  print(checkDownNums(rotate(rotate(tiles[16])), tiles[98]))


def part2():
  f = '\n'.join(reader()).split('\n\n')
  tileIds = []
  tiles = []
  for s in f:
    x = s.split('\n')
    tileIds.append(int(x[0][5: -1]))
    tiles.append([list(l) for l in x[1:]])
  d = {}
  j = 0
  while j < 144:
    d[j] = [-1] * 4
    i = 0
    while i < len(tiles):
      if i != j:
        if checkUp(tiles[j], tiles[i]):
          d[j][0] = i
        if checkDown(tiles[j], tiles[i]):
          d[j][2] = i
        if checkRight(tiles[j], tiles[i]):
          d[j][1] = i
        if checkLeft(tiles[j], tiles[i]):
          d[j][3] = i
      i += 1
    j += 1
  print(d)
  puzzle = []
  [puzzle.append([-1] * 12) for i in range(12)]
  puzzle[0][0] = [16, 0, 2]
  puzzle[0][1] = [67, 0, 1]
  puzzle[1][0] = [98, 0, 0]
  j = 2
  while j < len(puzzle[0]):
    adj = puzzle[0][j - 1]
    p = tiles[adj[0]]
    index = 1
    if adj[1] == 1:
      index = 3
      p = flip(p)
    i = 0
    while i < adj[2]:
      p = rotate(p)
      if index == 0:
        index = 3
      else:
        index = index - 1
      i += 1
    print(adj)
    print(index)
    n = d[adj[0]][index]
    pos = checkRightNums(p, tiles[n])
    print(pos)
    puzzle[0][j] = [n, pos[1], pos[2]]
    # for n in d[adj[0]]:
    # 	if n != -1:
    # 		if not inPuzzle(n, puzzle):
    # 			if len(d[n]) < 4:
    # 				piece = tiles[adj[0]]
    # 				if adj[1] == 1:
    # 					piece = flip(piece)
    # 				i = 0
    # 				while i < adj[2]:
    # 					piece = rotate(piece)
    # 					i += 1
    # 				pos = [-1, -11, -11]
    # 				if adj[1] == 0:
    # 					pos = checkRightNums(piece, tiles[n])
    # 				elif adj[1] == 1:
    # 					pos = checkLeftNums(piece, tiles[n])
    # 				puzzle[0][j] = [n, pos[1], pos[2]]
    j += 1
  print(puzzle[0])
  j = 2
  while j < len(puzzle):
    adj = puzzle[j - 1][0]
    for n in d[adj[0]]:
      if not inPuzzle(n, puzzle):
        if len(d[n]) < 4:
          piece = tiles[adj[0]]
          if adj[1] == 1:
            piece = flip(piece)
          i = 0
          while i < adj[2]:
            piece = rotate(piece)
            i += 1
          pos = checkDownNums(piece, tiles[n])
          puzzle[j][0] = [n, pos[1], pos[2]]
    j += 1
  i = 1
  while i < 12:
    j = 1
    while j < 12:
      adjL = puzzle[i][j - 1]
      adjU = puzzle[i - 1][j]
      for n in d[adjL[0]]:
        if (not inPuzzle(n, puzzle)) and adjU[0] in d[n]:
          piece = tiles[adjL[0]]
          if adjL[1] == 1:
            piece = flip(piece)
          k = 0
          while k < adjL[2]:
            piece = rotate(piece)
            k += 1
          pos = [-1, -11, -11]
          if adjL[1] == 0:
            pos = checkRightNums(piece, tiles[n])
          elif adjL[1] == 1:
            pos = checkLeftNums(piece, tiles[n])
          puzzle[i][j] = [n, pos[1], pos[2]]
      j += 1
    i += 1
  i = 0
  print(puzzle)
  while i < len(puzzle):
    j = 0
    while j < len(puzzle[i]):
      nums = puzzle[i][j]
      piece = tiles[nums[0]]
      k = 0
      while k < nums[1]:
        piece = flip(piece)
        k += 1
      k = 0
      while k < nums[2]:
        piece = rotate(piece)
        k += 1
      puzzle[i][j] = piece
      j += 1
    i += 1
  i = 0
  while i < len(puzzle):
    j = 0
    while j < len(puzzle[i]):
      puzzle[i][j] = cutBorder(puzzle[i][j])
      j += 1
    i += 1
  i = 0
  while i < len(puzzle):
    puzzle[i] = combine(puzzle[i])
    i += 1
  fullPic = []
  for a in puzzle:
    for r in a:
      fullPic.append(r)
  print(len(fullPic))
  print(len(fullPic[0]))
  print(countKraken(fullPic))
  rpic = rotate(fullPic)
  i = 0
  while i < 3:
    print(countKraken(rpic))
    rpic = rotate(rpic)
    i += 1
  rpic = flip(fullPic)
  i = 0
  while i < 4:
    print(countKraken(rpic))
    rpic = rotate(rpic)
    i += 1
  print(counthashtags(fullPic))


def counthashtags(pic):
  total = 0
  for row in pic:
    for col in row:
      if col == '#':
        total += 1
  return total


def checkRightNums(a, b):
  return checkDownNums(rotate(a), rotate(b))
  # x = rotate(a)
  # y = rotate(b)
  # if x[0] == y[9]:
  # 	return [True, 0, 0]
  # n = rotate(y)
  # i = 1
  # while i < 4:
  # 	if x[0] == n[9]:
  # 		return [True, 0, i]
  # 	n = rotate(n)
  # 	i += 1
  # n = flip(y)
  # n = rotate(rotate(n))
  # i = 0
  # while i < 4:
  # 	if x[0] == n[9]:
  # 		return [True, 1, i]
  # 	n = rotate(n)
  # 	i += 1
  # return [False, -1, -1]


def checkLeftNums(a, b):
  return checkUpNums(rotate(a), rotate(b))
  # x = rotate(a)
  # y = rotate(b)
  # if x[9] == y[0]:
  # 	return [True, 0, 0]
  # n = rotate(y)
  # i = 1
  # while i < 4:
  # 	if x[9] == n[0]:
  # 		return [True, 0, i]
  # 	n = rotate(n)
  # 	i += 1
  # n = flip(y)
  # n = rotate(rotate(n))
  # i = 0
  # while i < 4:
  # 	if x[9] == n[0]:
  # 		return [True, 1, i]
  # 	n = rotate(n)
  # 	i += 1
  # return [False, -1, -1]


def checkUpNums(a, b):
  if a[0] == b[9]:
    return [True, 0, 0]
  n = rotate(b)
  i = 1
  while i < 4:
    if a[0] == n[9]:
      return [True, 0, i]
    n = rotate(n)
    i += 1
  n = flip(b)
  i = 0
  while i < 4:
    if a[0] == n[9]:
      return [True, 1, i]
    n = rotate(n)
    i += 1
  return [False, -1, -1]


def checkDownNums(a, b):
  if a[9] == b[0]:
    return [True, 0, 0]
  n = rotate(b)
  i = 1
  while i < 4:
    if a[9] == n[0]:
      return [True, 0, i]
    n = rotate(n)
    i += 1
  n = flip(b)
  # n = rotate(rotate(n))
  i = 0
  while i < 4:
    if a[9] == n[0]:
      return [True, 1, 0]
    n = rotate(n)
    i += 1
  return [False, -1, -1]


def countKraken(pic):
  total = 0
  i = 1
  while i < len(pic) - 1:
    j = 19
    while j < len(pic[i]):
      if isKraken(i, j, pic):
        total += 1
      j += 1
    i += 1
  return total


def isKraken(row, column, pic):
  i = row
  j = column
  return pic[i][j] == '#' and pic[i - 1][j - 1] == '#' and pic[i][j - 1] == '#' and pic[i][j - 2] == '#' and pic[i + 1][j - 3] == '#' and pic[i + 1][j - 6] == '#' and pic[i][j - 7] == '#' and pic[i][j - 8] == '#' and pic[i + 1][j - 9] == '#' and pic[i + 1][j - 12] == '#' and pic[i][j - 13] == '#' and pic[i][j - 14] == '#' and pic[i + 1][j - 15] == '#' and pic[i + 1][j - 18] == '#' and pic[i][j - 19] == '#'


def combine(tiles):
  bigTile = []
  j = 0
  while j < len(tiles[0]):
    bigTile.append(tiles[0][j])
    i = 1
    while i < len(tiles):
      bigTile[j] += tiles[i][j]
      i += 1
    j += 1
  return bigTile


def cutBorder(tile):
  newTile = []
  i = 1
  while i < len(tile) - 1:
    newTile.append(tile[i][1:len(tile[i]) - 1])
    i += 1
  return newTile


def rotate(tile):
  newTile = []
  [newTile.append([0] * len(tile)) for i in range(len(tile))]
  i = 0
  while i < len(tile):
    j = 0
    while j < len(tile):
      newTile[j][len(tile) - 1 - i] = tile[i][j]
      j += 1
    i += 1
  return (newTile)


def flip(tile):
  newTile = []
  [newTile.append([0] * len(tile)) for i in range(len(tile))]
  i = 0
  while i < len(tile):
    j = 0
    while j < len(tile):
      newTile[i][len(tile) - 1 - j] = tile[i][j]
      j += 1
    i += 1
  return (newTile)


def checkUp(a, b):
  if a[0] == b[9]:
    return True
  n = rotate(b)
  i = 1
  while i < 4:
    if a[0] == n[9]:
      return True
    n = rotate(n)
    i += 1
  n = flip(b)
  i = 0
  while i < 4:
    if a[0] == n[9]:
      return True
    n = rotate(n)
    i += 1
  return False


def checkDown(a, b):
  if a[9] == b[0]:
    return True
  n = rotate(b)
  i = 0
  while i < 3:
    if a[9] == n[0]:
      return True
    n = rotate(n)
    i += 1
  n = flip(b)
  i = 0
  while i < 4:
    if a[9] == n[0]:
      return True
    n = rotate(n)
    i += 1
  return False


def checkRight(a, b):
  return checkDown(rotate(a), rotate(b))


def checkLeft(a, b):
  return checkUp(rotate(a), rotate(b))


def inPuzzle(i, p):
  result = False
  for r in p:
    for l in r:
      if l != -1 and l[0] == i:
        result = True
  return result


part1()
part2()
# answer should be 2409 with 29 krakens
