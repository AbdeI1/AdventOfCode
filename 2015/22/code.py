import os
os.chdir(os.path.dirname(__file__))
from heapq import heappush, heappop


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  hp = int(f[0].split()[-1])
  dmg = int(f[1].split()[-1])
  Q = [(0, 50, 0, 500, hp, 0, 0, 0, 0)]
  while Q:
    mana_u, php, parm, mana, bhp, shield, poison, recharge, t = heappop(Q)

    if shield > 0:
      shield -= 1
      if shield == 0:
        parm = 0

    if poison > 0:
      bhp -= 3
      poison -= 1

    if recharge > 0:
      mana += 101
      recharge -= 1

    if bhp <= 0:
      print(mana_u)
      break

    if php <= 0:
      continue

    if t == 0:
      if mana >= 53:
        heappush(Q, (mana_u + 53, php, parm, mana - 53,
                     bhp - 4, shield, poison, recharge, 1))
      if mana >= 73:
        heappush(Q, (mana_u + 73, php + 2, parm, mana -
                     73, bhp - 2, shield, poison, recharge, 1))
      if mana >= 113 and shield == 0:
        heappush(Q, (mana_u + 113, php, 7, mana -
                 113, bhp, 6, poison, recharge, 1))
      if mana >= 173 and poison == 0:
        heappush(Q, (mana_u + 173, php, parm, mana -
                 173, bhp, shield, 6, recharge, 1))
      if mana >= 229 and recharge == 0:
        heappush(Q, (mana_u + 229, php, parm, mana -
                 229, bhp, shield, poison, 5, 1))
    else:
      heappush(Q, (mana_u, php - max(1, dmg - parm), parm,
               mana, bhp, shield, poison, recharge, 0))


def part2():
  f = reader()
  hp = int(f[0].split()[-1])
  dmg = int(f[1].split()[-1])
  Q = [(0, 50, 0, 500, hp, 0, 0, 0, 0)]
  while Q:
    mana_u, php, parm, mana, bhp, shield, poison, recharge, t = heappop(Q)

    if t == 0:
      php -= 1

    if php <= 0:
      continue

    if shield > 0:
      shield -= 1
      if shield == 0:
        parm = 0

    if poison > 0:
      bhp -= 3
      poison -= 1

    if recharge > 0:
      mana += 101
      recharge -= 1

    if bhp <= 0:
      print(mana_u)
      break

    if php <= 0:
      continue

    if t == 0:
      if mana >= 53:
        heappush(Q, (mana_u + 53, php, parm, mana - 53,
                     bhp - 4, shield, poison, recharge, 1))
      if mana >= 73:
        heappush(Q, (mana_u + 73, php + 2, parm, mana -
                     73, bhp - 2, shield, poison, recharge, 1))
      if mana >= 113 and shield == 0:
        heappush(Q, (mana_u + 113, php, 7, mana -
                 113, bhp, 6, poison, recharge, 1))
      if mana >= 173 and poison == 0:
        heappush(Q, (mana_u + 173, php, parm, mana -
                 173, bhp, shield, 6, recharge, 1))
      if mana >= 229 and recharge == 0:
        heappush(Q, (mana_u + 229, php, parm, mana -
                 229, bhp, shield, poison, 5, 1))
    else:
      heappush(Q, (mana_u, php - max(1, dmg - parm), parm,
               mana, bhp, shield, poison, recharge, 0))


part1()
part2()
