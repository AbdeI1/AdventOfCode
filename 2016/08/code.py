import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = [l.split() for l in reader()]
  W, H = 50, 6
  G = [[0 for _ in range(W)] for _ in range(H)]
  for l in f:
    match l[0]:
      case 'rect':
        w, h = map(int, l[1].split('x'))
        for i in range(h):
          for j in range(w):
            G[i][j] = 1
      case 'rotate':
        i = j = int(l[2].split('=')[1])
        d = int(l[4])
        match l[1]:
          case 'row':
            G[i][:] = G[i][-d:] + G[i][:-d]
          case 'column':
            for i, v in enumerate([G[i - d][j] for i in range(H)]):
              G[i][j] = v
  print(sum(sum(r) for r in G))


def part2():
  f = [l.split() for l in reader()]
  W, H = 50, 6
  G = [[0 for _ in range(W)] for _ in range(H)]
  for l in f:
    match l[0]:
      case 'rect':
        w, h = map(int, l[1].split('x'))
        for i in range(h):
          for j in range(w):
            G[i][j] = 1
      case 'rotate':
        i = j = int(l[2].split('=')[1])
        d = int(l[4])
        match l[1]:
          case 'row':
            G[i][:] = G[i][-d:] + G[i][:-d]
          case 'column':
            for i, v in enumerate([G[i - d][j] for i in range(H)]):
              G[i][j] = v
  for r in G:
    print(''.join(['  ', '{}'][i] for i in r))


part1()
part2()
