import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  v = set()

  s = [(0, 0, 'e')]

  while s:
    i, j, d = s.pop()
    if i not in range(len(f)) or j not in range(len(f[i])):
      continue
    if (i, j, d) in v:
      continue
    v.add((i, j, d))
    match d:
      case 'n':
        match f[i][j]:
          case '\\':
            s.append((i, j - 1, 'w'))
          case '/':
            s.append((i, j + 1, 'e'))
          case '-':
            s.append((i, j + 1, 'e'))
            s.append((i, j - 1, 'w'))
          case _:
            s.append((i - 1, j, 'n'))
      case 'e':
        match f[i][j]:
          case '\\':
            s.append((i + 1, j, 's'))
          case '/':
            s.append((i - 1, j, 'n'))
          case '|':
            s.append((i - 1, j, 'n'))
            s.append((i + 1, j, 's'))
          case _:
            s.append((i, j + 1, 'e'))
      case 's':
        match f[i][j]:
          case '\\':
            s.append((i, j + 1, 'e'))
          case '/':
            s.append((i, j - 1, 'w'))
          case '-':
            s.append((i, j + 1, 'e'))
            s.append((i, j - 1, 'w'))
          case _:
            s.append((i + 1, j, 's'))
      case 'w':
        match f[i][j]:
          case '\\':
            s.append((i - 1, j, 'n'))
          case '/':
            s.append((i + 1, j, 's'))
          case '|':
            s.append((i - 1, j, 'n'))
            s.append((i + 1, j, 's'))
          case _:
            s.append((i, j - 1, 'w'))

  print(len({(i, j) for (i, j, d) in v}))


def part2():
  f = reader()

  def simulate(start):
    v = set()
    s = [start]

    while s:
      i, j, d = s.pop()
      if i not in range(len(f)) or j not in range(len(f[i])):
        continue
      if (i, j, d) in v:
        continue
      v.add((i, j, d))
      match d:
        case 'n':
          match f[i][j]:
            case '\\':
              s.append((i, j - 1, 'w'))
            case '/':
              s.append((i, j + 1, 'e'))
            case '-':
              s.append((i, j + 1, 'e'))
              s.append((i, j - 1, 'w'))
            case _:
              s.append((i - 1, j, 'n'))
        case 'e':
          match f[i][j]:
            case '\\':
              s.append((i + 1, j, 's'))
            case '/':
              s.append((i - 1, j, 'n'))
            case '|':
              s.append((i - 1, j, 'n'))
              s.append((i + 1, j, 's'))
            case _:
              s.append((i, j + 1, 'e'))
        case 's':
          match f[i][j]:
            case '\\':
              s.append((i, j + 1, 'e'))
            case '/':
              s.append((i, j - 1, 'w'))
            case '-':
              s.append((i, j + 1, 'e'))
              s.append((i, j - 1, 'w'))
            case _:
              s.append((i + 1, j, 's'))
        case 'w':
          match f[i][j]:
            case '\\':
              s.append((i - 1, j, 'n'))
            case '/':
              s.append((i + 1, j, 's'))
            case '|':
              s.append((i - 1, j, 'n'))
              s.append((i + 1, j, 's'))
            case _:
              s.append((i, j - 1, 'w'))
    return len({(i, j) for (i, j, _) in v})

  m = -1

  for i in range(len(f)):
    m = max(m, simulate((i, 0, 'e')), simulate((i, len(f[i]) - 1, 'w')))
  for j in range(len(f[0])):
    m = max(m, simulate((0, j, 's')), simulate((len(f[0]) - 1, j, 'n')))

  print(m)


part1()
part2()
