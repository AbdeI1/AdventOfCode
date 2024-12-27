from functools import *


import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


count = 0
num = 1


def roll():
  global count
  global num
  res = num
  num += 1
  count += 1
  if num > 100:
    num = 1
  return res


def part1():
  f = reader()
  global count
  pos1 = int(f[0][f[0].index(':') + 2:])
  pos2 = int(f[1][f[1].index(':') + 2:])
  score1 = 0
  score2 = 0
  turn = True
  while score1 < 1000 and score2 < 1000:
    if turn:
      s = roll()
      s += roll()
      s += roll()
      pos1 += s
      while pos1 > 10:
        pos1 -= 10
      score1 += pos1
    else:
      s = roll()
      s += roll()
      s += roll()
      pos2 += s
      while pos2 > 10:
        pos2 -= 10
      score2 += pos2
    turn = not turn
  print(count * min(score1, score2))


@cache
def getNum(pos1, pos2, score1, score2, turn):
  if score1 >= 21:
    return [1, 0]
  if score2 >= 21:
    return [0, 1]
  rolls = [3, 4, 5, 4, 5, 6, 5, 6, 7]
  rolls += list(map(lambda x: x + 1, rolls))
  rolls += list(map(lambda x: x + 2, rolls[:9]))
  pos1s = [-1] * 27
  pos2s = [-1] * 27
  for i in range(27):
    pos1s[i] = (pos1 + rolls[i] - 1) % 10 + 1
    pos2s[i] = (pos2 + rolls[i] - 1) % 10 + 1
  res = [0, 0]
  if turn:
    for p in pos1s:
      r = getNum(p, pos2, score1 + p, score2, not turn)
      res[0] += r[0]
      res[1] += r[1]
  else:
    for p in pos2s:
      r = getNum(pos1, p, score1, score2 + p, not turn)
      res[0] += r[0]
      res[1] += r[1]
  return res


def part2():
  f = reader()
  pos1 = int(f[0][f[0].index(':') + 2:])
  pos2 = int(f[1][f[1].index(':') + 2:])
  res = getNum(pos1, pos2, 0, 0, True)
  print(max(res))


part1()
part2()
