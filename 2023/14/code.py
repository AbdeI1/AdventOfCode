import os
os.chdir(os.path.dirname(__file__))
from collections import Counter


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  ans = 0
  for j in range(len(f[0])):
    l = len(f)
    for i in range(len(f)):
      match f[i][j]:
        case 'O':
          ans += l
          l -= 1
        case '#':
          l = len(f) - i - 1
  print(ans)


def part2():
  f = [list(s) for s in reader()]

  def roll(f, dir='n'):
    match dir:
      case 'n':
        for j in range(len(f[0])):
          k = 0
          for i in range(len(f)):
            match f[i][j]:
              case 'O':
                f[i][j], f[k][j] = f[k][j], f[i][j]
                k += 1
              case '#':
                k = i + 1
      case 'e':
        for i in range(len(f)):
          k = len(f[0]) - 1
          for j in reversed(range(len(f[0]))):
            match f[i][j]:
              case 'O':
                f[i][j], f[i][k] = f[i][k], f[i][j]
                k -= 1
              case '#':
                k = j - 1
      case 's':
        for j in range(len(f[0])):
          k = len(f) - 1
          for i in reversed(range(len(f))):
            match f[i][j]:
              case 'O':
                f[i][j], f[k][j] = f[k][j], f[i][j]
                k -= 1
              case '#':
                k = i - 1
      case 'w':
        for i in range(len(f)):
          k = 0
          for j in range(len(f[0])):
            match f[i][j]:
              case 'O':
                f[i][j], f[i][k] = f[i][k], f[i][j]
                k += 1
              case '#':
                k = j + 1

  def cycle(f):
    roll(f, 'n')
    roll(f, 'w')
    roll(f, 's')
    roll(f, 'e')
    return f

  cycles = 1000000000 - 3
  i = 0

  def hash(state): return ''.join([''.join(l) for l in state])

  states = [hash(f)]
  map = {hash(f): [[c for c in l] for l in f]}
  while True:
    cycle(f)
    h = hash(f)
    if h in map:
      i = states.index(h)
      break
    states.append(h)
    map[h] = [[c for c in l] for l in f]

  def getState(c):
    if c >= len(states):
      c = i + (c % (len(states) - i))
    return states[c]

  f = map[getState(cycles)]

  print(sum([(len(f) - i) * j for i,
        j in enumerate([sum([c == 'O' for c in l]) for l in f])]))


part1()
part2()
