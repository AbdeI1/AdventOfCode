import os
os.chdir(os.path.dirname(__file__))
from collections import deque
from typing import Tuple, List


def reader():
  return open(f"input.txt", 'r').read().splitlines()


class Position():
  def __init__(self, i, j):
    self.i = i
    self.j = j

  def adj(self):
    return [Position(self.i + di, self.j + dj) for di, dj in [(-1, 0), (0, -1), (0, 1), (1, 0)]]

  def __lt__(self, other):
    return (self.i, self.j) < (other.i, other.j)

  def __add__(self, other):
    return Position(self.i + other.i, self.j + other.j)

  def __repr__(self):
    return f"{(self.i, self.j)}"

  def __eq__(self, other):
    return self.i == other.i and self.j == other.j

  def __hash__(self):
    return hash((self.i, self.j))


class Unit():
  def __init__(self, p: Position, hp: int, ap: int, t: int, i: int):
    self.position = p
    self.hp = hp
    self.ap = ap
    self.team = t
    self.id = i

  def __repr__(self):
    return f"{[self.team, self.id, self.hp, self.position, self.ap]}"

  def __eq__(self, other):
    if not isinstance(other, Unit):
      return NotImplemented
    return f"{self}" == f"{other}"


class CombatEnd(Exception):
  pass


def play(M, U: Tuple[List[Unit], List[Unit]]):
  for u in sorted(sum(U, []), key=lambda u: u.position):
    if u.hp <= 0: continue
    targets: List[Unit] = list(filter(lambda u: u.hp > 0, U[1 - u.team]))
    if len(targets) == 0:
      raise CombatEnd()
    sq = {p for t in targets for p in t.position.adj()
          if p not in M or p == u.position}
    if u.position not in sq:
      P = set()
      D = -1
      Q = deque([(u.position, 0, [])])
      V = set()
      while Q:
        p, d, path = Q.popleft()
        if D != -1 and d > D:
          break
        if p in V:
          continue
        V.add(p)
        if p in M and M[p] != u:
          continue
        if p in sq:
          P.add((p, path[0]))
          D = d
        for pp in p.adj():
          Q.append((pp, d + 1, path + [pp]))
      if P:
        _, p = min(P)
        del M[u.position]
        u.position = p
        M[p] = u
    opps = [M[p]
            for p in u.position.adj() if p in M and M[p] != '#' and M[p].team == 1 - u.team]
    if opps:
      tar = min(opps, key=lambda u: (u.hp, u.position))
      tar.hp -= u.ap
      if tar.hp <= 0:
        del M[tar.position]
  U = list(filter(lambda u: u.hp > 0, U[0])), list(
    filter(lambda u: u.hp > 0, U[1]))
  return U


def part1():
  f = reader()
  M = {}
  U = [], []
  for i, r in enumerate(f):
    for j, c in enumerate(r):
      p = Position(i, j)
      if c == 'E':
        M[p] = Unit(p, 200, 3, 0, len(U[0]))
        U[0].append(M[p])
      if c == 'G':
        M[p] = Unit(p, 200, 3, 1, len(U[1]))
        U[1].append(M[p])
      if c == '#':
        M[p] = '#'
  R = 0
  try:
    while True:
      U = play(M, U)
      R += 1
  except:
    pass
  print(R * sum(u.hp for u in sum(U, []) if u.hp > 0))


def part2():
  f = reader()

  def test(v):
    M = {}
    U = [], []
    for i, r in enumerate(f):
      for j, c in enumerate(r):
        p = Position(i, j)
        if c == 'E':
          M[p] = Unit(p, 200, v, 0, len(U[0]))
          U[0].append(M[p])
        if c == 'G':
          M[p] = Unit(p, 200, 3, 1, len(U[1]))
          U[1].append(M[p])
        if c == '#':
          M[p] = '#'
    R = 0
    L = len(U[0])
    try:
      while len(U[0]) == L:
        U = play(M, U)
        R += 1
    except:
      pass
    return R * sum(u.hp for u in U[0]) if len(U[0]) == L else 0

  b = 1 << 4
  s = b >> 1

  while s > 0:
    if test(b) == 0:
      b += s
    else:
      b -= s
    s >>= 1
  if test(b) == 0: b += 1

  print(test(b))


part1()
part2()
