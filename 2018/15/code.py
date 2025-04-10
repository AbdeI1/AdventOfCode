import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  M: list[list[str]] = list(map(list, reader()))
  G, E = {}, {}
  for y, row in enumerate(M):
    for x, c in enumerate(row):
      if c == 'G':
        n = f'{c}{len(G)}'
        row[x] = n
        G[n] = 200
      elif c == 'E':
        n = f'{c}{len(E)}'
        row[x] = n
        E[n] = 200

  def bfs(p, t):
    V = set()
    Q = [(p, 0, [p])]
    while Q:
      (x, y), d, path = Q.pop(0)
      if (x, y) in V:
        continue
      V.add((x, y))
      if M[y][x][0] == t:
        return M[y][x], d, path
      if (x, y) != p and M[y][x] != '.':
        continue
      for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
        Q.append(((x + dx, y + dy), d + 1, path + [(x + dx, y + dy)]))
    return '.', -1, []

  R = 0
  while len(E) > 0 and len(G) > 0:
    Mo = set()
    for y, r in enumerate(M):
      for x, c in enumerate(r):
        if c[0] in 'GE' and c not in Mo:
          Mo.add(c)
          a, d, p = bfs((x, y), 'G' if c[0] == 'E' else 'E')
          xx, yy = x, y
          if d > 1:
            M[y][x] = '.'
            xx, yy = p[1]
            M[yy][xx] = c
            d -= 1
          if d == 1:
            if c[0] == 'G':
              hp = E[a]
              t = p[-1]
              for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
                if M[yy + dy][xx + dx][0] == 'E' and E[M[yy + dy][xx + dx]] < hp:
                  hp = E[M[yy + dy][xx + dx]]
                  a = M[yy + dy][xx + dx]
                  t = xx + dx, yy + dy
              E[a] -= 3
              if E[a] <= 0:
                del E[a]
                M[t[1]][t[0]] = '.'
            elif c[0] == 'E':
              hp = G[a]
              t = p[-1]
              for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
                if M[yy + dy][xx + dx][0] == 'G' and G[M[yy + dy][xx + dx]] < hp:
                  hp = G[M[yy + dy][xx + dx]]
                  a = M[yy + dy][xx + dx]
                  t = xx + dx, yy + dy
              G[a] -= 3
              if G[a] <= 0:
                del G[a]
                M[t[1]][t[0]] = '.'
    R += 1
  print(R * (sum(E.values()) + sum(G.values())))


def part2():
  def test(ap):
    M: list[list[str]] = list(map(list, reader()))
    G, E = {}, {}
    for y, row in enumerate(M):
      for x, c in enumerate(row):
        if c == 'G':
          n = f'{c}{len(G)}'
          row[x] = n
          G[n] = 200
        elif c == 'E':
          n = f'{c}{len(E)}'
          row[x] = n
          E[n] = 200

    def bfs(p, t):
      V = set()
      Q = [(p, 0, [])]
      while Q:
        (x, y), d, path = Q.pop(0)
        if (x, y) in V:
          continue
        V.add((x, y))
        if M[y][x][0] == t:
          return M[y][x], d, path + [(x, y)]
        if (x, y) != p and M[y][x] != '.':
          continue
        for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
          Q.append(((x + dx, y + dy), d + 1, path + [(x, y)]))
      return '.', -1, []

    R = 0
    el = len(E)
    while len(E) > 0 and len(G) > 0:
      Mo = set()
      for y, r in enumerate(M):
        for x, c in enumerate(r):
          if c[0] in 'GE' and c not in Mo:
            Mo.add(c)
            a, d, p = bfs((x, y), 'G' if c[0] == 'E' else 'E')
            xx, yy = x, y
            if d > 1:
              M[y][x] = '.'
              xx, yy = p[1]
              M[yy][xx] = c
              d -= 1
            if d == 1:
              if c[0] == 'G':
                hp = float('inf')
                t = -1, -1
                for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
                  if M[yy + dy][xx + dx][0] == 'E' and E[M[yy + dy][xx + dx]] < hp:
                    hp = E[M[yy + dy][xx + dx]]
                    a = M[yy + dy][xx + dx]
                    t = xx + dx, yy + dy
                E[a] -= 3
                if E[a] <= 0:
                  del E[a]
                  M[t[1]][t[0]] = '.'
              elif c[0] == 'E':
                hp = float('inf')
                t = -1, -1
                for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
                  if M[yy + dy][xx + dx][0] == 'G' and G[M[yy + dy][xx + dx]] < hp:
                    hp = G[M[yy + dy][xx + dx]]
                    a = M[yy + dy][xx + dx]
                    t = xx + dx, yy + dy
                G[a] -= ap
                if G[a] <= 0:
                  del G[a]
                  M[t[1]][t[0]] = '.'
      R += 1
      # print(R, G, E)
      # for r in M:
      #   print(''.join(c[0] for c in r))
    return R * (sum(E.values())) if len(E) == el else 0

  v = 1 << 7
  s = v >> 1

  while s > 0:
    if test(v):
      v -= s
    else:
      v += s
    s >>= 1

  print(test(v) if test(v) else test(v + 1))


part1()
part2()  # I give up, 62468, can't figure out what's wrong
