import os
os.chdir(os.path.dirname(__file__))
from collections import Counter


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  f = list(map(lambda s: (s.split()[0], int(s.split()[1])), f))
  order = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
  val = {l: i for i, l in enumerate(order)}

  def toTuple(h: str):
    v = 0
    b = 1
    for c in reversed(h):
      v += b * val[c]
      b *= len(val)
    s = Counter(h)
    t = 0
    if len(s) == 1:
      t = 6
    elif len(s) == 2:
      if s.most_common(1)[0][1] == 4:
        t = 5
      else:
        t = 4
    elif len(s) == 3:
      if s.most_common(1)[0][1] == 3:
        t = 3
      else:
        t = 2
    elif len(s) == 4:
      t = 1
    else:
      t = 0
    return (t, v)
  hands = sorted(f, key=lambda t: toTuple(t[0]))
  wins = 0
  for i, h in enumerate(hands):
    wins += (i + 1) * h[1]
  print(wins)


def part2():
  f = reader()
  f = list(map(lambda s: (s.split()[0], int(s.split()[1])), f))
  order = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
  val = {l: i for i, l in enumerate(order)}

  def toTuple(h: str):
    v = 0
    b = 1
    for c in reversed(h):
      v += b * val[c]
      b *= len(val)
    s = Counter(h)
    if s['J'] in range(1, 5):
      x = list(filter(lambda y: y[0] != 'J', s.most_common(2)))[0][0]
      s[x] += s['J']
      del s['J']
    t = 0
    if len(s) == 1:
      t = 6
    elif len(s) == 2:
      if s.most_common(1)[0][1] == 4:
        t = 5
      else:
        t = 4
    elif len(s) == 3:
      if s.most_common(1)[0][1] == 3:
        t = 3
      else:
        t = 2
    elif len(s) == 4:
      t = 1
    else:
      t = 0
    return (t, v)
  hands = sorted(f, key=lambda t: toTuple(t[0]))
  wins = 0
  for i, h in enumerate(hands):
    wins += (i + 1) * h[1]
  print(wins)


part1()
part2()
