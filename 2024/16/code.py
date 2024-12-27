import os
os.chdir(os.path.dirname(__file__))
import heapq


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  M = reader()
  S = next((i, j) for i in range(len(M))
           for j in range(len(M[i])) if M[i][j] == 'S')
  Q = [(0, S, (0, 1))]
  V = set()
  while Q:
    (p, (i, j), (di, dj)) = heapq.heappop(Q)
    if ((i, j), (di, dj)) in V:
      continue
    V.add(((i, j), (di, dj)))
    if M[i][j] == 'E':
      print(p)
      break
    ii = i + di
    jj = j + dj
    if M[ii][jj] != '#':
      heapq.heappush(Q, (p + 1, (ii, jj), (di, dj)))
    heapq.heappush(Q, (p + 1000, (i, j), (-dj, di)))
    heapq.heappush(Q, (p + 1000, (i, j), (dj, -di)))


def part2():
  M = reader()
  S = next((i, j) for i in range(len(M))
           for j in range(len(M[i])) if M[i][j] == 'S')
  E = next((i, j) for i in range(len(M))
           for j in range(len(M[i])) if M[i][j] == 'E')
  Q = [(0, E, (0, 1), [E]), (0, E, (0, -1), [E]),
       (0, E, (1, 0), [E]), (0, E, (-1, 0), [E])]
  D = {}
  while Q:
    (p, (i, j), (di, dj), l) = heapq.heappop(Q)
    if ((i, j), (di, dj)) in D:
      continue
    D[(i, j), (di, dj)] = p
    ii = i + di
    jj = j + dj
    if M[ii][jj] != '#':
      heapq.heappush(Q, (p + 1, (ii, jj), (di, dj), l + [(ii, jj)]))
    heapq.heappush(Q, (p + 1000, (i, j), (-dj, di), l))
    heapq.heappush(Q, (p + 1000, (i, j), (dj, -di), l))
  Q = [(0, S, (0, 1))]
  V = set()
  B = set()
  P = D[(S, (0, 1))]
  while Q:
    (p, (i, j), (di, dj)) = heapq.heappop(Q)
    if p > P:
      break
    if ((i, j), (di, dj)) in V:
      continue
    V.add(((i, j), (di, dj)))
    if p + D[(i, j), (-di, -dj)] == P:
      B.add((i, j))
    ii = i + di
    jj = j + dj
    if M[ii][jj] != '#':
      heapq.heappush(Q, (p + 1, (ii, jj), (di, dj)))
    heapq.heappush(Q, (p + 1000, (i, j), (-dj, di)))
    heapq.heappush(Q, (p + 1000, (i, j), (dj, -di)))
  print(len(B))


part1()
part2()
