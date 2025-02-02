import os
os.chdir(os.path.dirname(__file__))
from sortedcontainers import SortedList


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = list(map(list, reader()))
  C = SortedList(key=lambda x: (x[0][1], x[0][0]))
  for y, r in enumerate(f):
    for x, c in enumerate(r):
      match c:
        case '>':
          C.add(((x, y), (1, 0), 0))
          f[y][x] = '-'
        case '<':
          C.add(((x, y), (-1, 0), 0))
          f[y][x] = '-'
        case '^':
          C.add(((x, y), (0, -1), 0))
          f[y][x] = '|'
        case 'v':
          C.add(((x, y), (0, 1), 0))
          f[y][x] = '|'
  while True:
    Cn = SortedList(key=lambda x: (x[0][1], x[0][0]))
    for (x, y), (dx, dy), i in C:
      match f[y][x]:
        case '-', '|':
          dx, dy = dx, dy
        case '/':
          dx, dy = -dy, -dx
        case '\\':
          dx, dy = dy, dx
        case '+':
          match i % 3:
            case 0:
              dx, dy = dy, -dx
            case 1:
              dx, dy = dx, dy
            case 2:
              dx, dy = -dy, dx
          i += 1
      P = (x + dx, y + dy)
      if P in {p for p, _, _ in C} | {p for p, _, _ in Cn}:
        print(','.join(map(str, P)))
        return
      Cn.add((P, (dx, dy), i))
    C = Cn


def part2():
  f = list(map(list, reader()))
  C = SortedList(key=lambda x: (x[0][1], x[0][0]))
  for y, r in enumerate(f):
    for x, c in enumerate(r):
      match c:
        case '>':
          C.add(((x, y), (1, 0), 0))
          f[y][x] = '-'
        case '<':
          C.add(((x, y), (-1, 0), 0))
          f[y][x] = '-'
        case '^':
          C.add(((x, y), (0, -1), 0))
          f[y][x] = '|'
        case 'v':
          C.add(((x, y), (0, 1), 0))
          f[y][x] = '|'
  while len(C) > 1:
    Cn = SortedList(key=lambda x: (x[0][1], x[0][0]))
    for (x, y), (dx, dy), i in C:
      for (x2, y2), d2, i2 in Cn:
        if (x, y) == (x2, y2):
          Cn.discard(((x2, y2), d2, i2))
          break
      else:
        match f[y][x]:
          case '-', '|':
            dx, dy = dx, dy
          case '/':
            dx, dy = -dy, -dx
          case '\\':
            dx, dy = dy, dx
          case '+':
            match i % 3:
              case 0:
                dx, dy = dy, -dx
              case 1:
                dx, dy = dx, dy
              case 2:
                dx, dy = -dy, dx
            i += 1
        P = (x + dx, y + dy)
        for p2, d2, i2 in Cn:
          if P == p2:
            Cn.discard((p2, d2, i2))
            break
        else:
          Cn.add((P, (dx, dy), i))
    C = Cn
  print(','.join(map(str, C[0][0])))


part1()
part2()
