import os
os.chdir(os.path.dirname(__file__))
from re import findall
from collections import deque
from itertools import combinations, chain, tee
from collections import defaultdict


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  L = [(
    set(
      map(
        lambda s: f'{s[0].upper()}{s[1]}',
        findall(r'\S+ microchip', l)
      )
    ),
    set(
      map(
        lambda s: f'{s[0].upper()}{s[1]}',
        findall(r'\S+ generator', l)
      )
    )
  ) for l in reader()]
  S = str((0, L))
  Q = deque([(S, 0)])
  V = set()
  while Q:
    s, d = Q.popleft()
    i, l = eval(s)
    loc = defaultdict(lambda: (-1, -1))
    for j in range(len(l)):
      M, G = l[j]
      for m in M:
        loc[m] = (j, loc[m][1])
      for g in G:
        loc[g] = (loc[g][0], j)
    K = (i, tuple(sorted(loc.values())))
    if K in V:
      continue
    V.add(K)
    if i == len(l) - 1 and all(len(M) + len(G) == 0 for M, G in l[:-1]):
      print(d)
      break
    M, G = l[i]
    for ni in [i - 1, i + 1]:
      if ni not in range(len(l)):
        continue
      Mn, Gn = l[ni]
      s1, s2 = tee(chain(map(lambda s: f'{s}M', M), map(lambda s: f'{s}G', G)))
      for t in chain(combinations(s1, 1), combinations(s2, 2)):
        aM, aMn, aG, aGn = eval(str((M, Mn, G, Gn)))
        for j in t:
          e, ee = j[:-1], j[-1]
          if ee == 'M':
            aM.remove(e)
            aMn.add(e)
          else:
            aG.remove(e)
            aGn.add(e)
        if (len(aG) == 0 or aM <= aG) and (len(aGn) == 0 or aMn <= aGn):
          l[i], l[ni] = (aM, aG), (aMn, aGn)
          Q.append((str((ni, l)), d + 1))
          l[i], l[ni] = (M, G), (Mn, Gn)


def part2():
  L = [(
    set(
      map(
        lambda s: f'{s[0].upper()}{s[1]}',
        findall(r'\S+ microchip', l)
      )
    ),
    set(
      map(
        lambda s: f'{s[0].upper()}{s[1]}',
        findall(r'\S+ generator', l)
      )
    )
  ) for l in reader()]
  M, G = L[0]
  L[0] = M | {'El', 'Di'}, G | {'El', 'Di'}
  S = str((0, L))
  Q = deque([(S, 0)])
  V = set()
  while Q:
    s, d = Q.popleft()
    i, l = eval(s)
    loc = defaultdict(lambda: (-1, -1))
    for j in range(len(l)):
      M, G = l[j]
      for m in M:
        loc[m] = (j, loc[m][1])
      for g in G:
        loc[g] = (loc[g][0], j)
    K = (i, tuple(sorted(loc.values())))
    if K in V:
      continue
    V.add(K)
    if i == len(l) - 1 and all(len(M) + len(G) == 0 for M, G in l[:-1]):
      print(d)
      break
    M, G = l[i]
    for ni in [i - 1, i + 1]:
      if ni not in range(len(l)):
        continue
      Mn, Gn = l[ni]
      s1, s2 = tee(chain(map(lambda s: f'{s}M', M), map(lambda s: f'{s}G', G)))
      for t in chain(combinations(s1, 1), combinations(s2, 2)):
        aM, aMn, aG, aGn = eval(str((M, Mn, G, Gn)))
        for j in t:
          e, ee = j[:-1], j[-1]
          if ee == 'M':
            aM.remove(e)
            aMn.add(e)
          else:
            aG.remove(e)
            aGn.add(e)
        if (len(aG) == 0 or aM <= aG) and (len(aGn) == 0 or aMn <= aGn):
          l[i], l[ni] = (aM, aG), (aMn, aGn)
          Q.append((str((ni, l)), d + 1))
          l[i], l[ni] = (M, G), (Mn, Gn)


part1()
part2()
