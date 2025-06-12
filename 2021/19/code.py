import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().split('\n')[:-1]


possibleOrientations = [([0, 1, 2], [1, 1, 1]), ([0, 2, 1], [-1, 1, 1]),
                        ([1, 2, 0], [1, 1, 1]), ([1, 0, 2], [-1, 1, 1]),
                        ([2, 0, 1], [1, 1, 1]), ([2, 1, 0], [-1, 1, 1]),
                        ([0, 1, 2], [
                            1, -1, -1]), ([0, 2, 1], [1, -1, 1]),
                        ([1, 2, 0], [
                            1, -1, -1]), ([1, 0, 2], [1, -1, 1]),
                        ([2, 0, 1], [
                            1, -1, -1]), ([2, 1, 0], [1, -1, 1]),
                        ([0, 1, 2], [-1, 1, -1]), ([
                            0, 2, 1], [1, 1, -1]),
                        ([1, 2, 0], [-1, 1, -1]), ([
                            1, 0, 2], [1, 1, -1]),
                        ([2, 0, 1], [-1, 1, -1]), ([
                            2, 1, 0], [1, 1, -1]),
                        ([0, 1, 2], [-1, -1, 1]), ([
                            0, 2, 1], [-1, -1, -1]),
                        ([1, 2, 0], [-1, -1, 1]), ([
                            1, 0, 2], [-1, -1, -1]),
                        ([2, 0, 1], [-1, -1, 1]), ([
                            2, 1, 0], [-1, -1, -1]),
                        ]


def getMap(sc):
  m = set()
  for coords in sc:
    x = coords[0]
    y = coords[1]
    z = coords[2]
    m.add((x, y, z))
  return m


def getPos(basep, p):
  return [basep[0] + p[0], basep[1] + p[1], basep[2] + p[2]]


def getOrient(base, o):
  res1 = [-1] * 3
  res2 = [0] * 3
  res1[base[0][0]] = o[0][0]
  res2[0] = o[1][0]
  res1[base[0][1]] = o[0][1]
  res2[1] = o[1][1]
  res1[base[0][2]] = o[0][2]
  res2[2] = o[1][2]
  res2[0] *= base[1][0]
  res2[1] *= base[1][1]
  res2[2] *= base[1][2]
  return (res1, res2)


def getPoint(p, position, orientation):
  x = p[orientation[0][0]] * orientation[1][0] + position[0]
  y = p[orientation[0][1]] * orientation[1][1] + position[1]
  z = p[orientation[0][2]] * orientation[1][2] + position[2]
  return (x, y, z)


def getPoints(sc, p, o):
  res = set()
  for p1 in sc:
    res.add(getPoint(p1, p, o))
  return res


def overlappingPoints(sc1, sc2):
  res = set()
  for x in sc1:
    if x in sc2:
      res.add(x)
  return res


def countOverlap(sc1, sc2):
  count = 0
  for x in sc1:
    if x in sc2:
      count += 1
  return count


def countMaxOverlap(sc1, sc2, maps, i):
  points = set()
  mp = [0, 0, 0]
  mo = possibleOrientations[0]
  u = getPoints(sc1, [0, 0, 0], possibleOrientations[0])
  for o in possibleOrientations:
    t = getPoints(sc2, [0, 0, 0], o)
    for (a, b, c) in u:
      for (x, y, z) in t:
        pos = [a - x, b - y, c - z]
        t2 = getPoints(t, pos, possibleOrientations[0])
        count = countOverlap(u, t2)
        if count >= 12:
          maps[i] = getPoints(sc2, pos, o)
          return (count, points, pos, o)
  return (0, points, mp, mo)


def part1():
  f = '\n'.join(reader()).split('\n\n')
  sc = list(map(lambda x: x.split('\n')[1:], f))
  sc = list(map(lambda y: list(map(lambda x: x.split(','), y)), sc))
  sc = list(map(lambda y: list(map(lambda x: list(map(int, x)), y)), sc))
  maps = list(map(lambda x: getMap(x), sc))
  positions = [[0] * 3 for _ in range(len(maps))]
  orientations = [([0, 1, 2], [1, 1, 1]) for _ in range(len(maps))]
  cur = 0
  fin = [False] * len(maps)
  fin[0] = True
  for _ in range(len(maps)):
    for cur in range(len(maps)):
      if fin[cur]:
        for i in range(len(maps)):
          if not fin[i]:
            (count, p, po, o) = countMaxOverlap(maps[cur], maps[i], maps, i)
            if count >= 12:
              cur = i
              fin[cur] = True
              break
  points = set()
  for i in range(len(maps)):
    points = points.union(getPoints(maps[i], positions[0], orientations[0]))
  print(len(points))


def getManhatt(p1, p2):
  return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1]) + abs(p2[2] - p1[2])


def part2():
  f = '\n'.join(reader()).split('\n\n')
  sc = list(map(lambda x: x.split('\n')[1:], f))
  sc = list(map(lambda y: list(map(lambda x: x.split(','), y)), sc))
  sc = list(map(lambda y: list(map(lambda x: list(map(int, x)), y)), sc))
  maps = list(map(lambda x: getMap(x), sc))
  positions = [[0] * 3 for _ in range(len(maps))]
  orientations = [([0, 1, 2], [1, 1, 1]) for _ in range(len(maps))]
  cur = 0
  fin = [False] * len(maps)
  fin[0] = True
  for _ in range(len(maps)):
    for cur in range(len(maps)):
      if fin[cur]:
        for i in range(len(maps)):
          if not fin[i]:
            (count, p, po, o) = countMaxOverlap(maps[cur], maps[i], maps, i)
            if count >= 12:
              cur = i
              positions[i] = po
              fin[cur] = True
              break
  dist = -1
  for i in positions:
    for j in positions:
      dist = max(dist, getManhatt(i, j))
  print(dist)


part1()
part2()
