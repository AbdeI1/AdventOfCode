import os
os.chdir(os.path.dirname(__file__))
import re


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = sorted([(tuple(map(int, re.split(r'[-: ]', l.split('] ')[0][1:]))),
               l.split('] ')[1]) for l in reader()])
  G = {}
  g = -1
  t = -1
  for (y, m, d, hh, mm), e in f:
    if e.startswith('Guard #'):
      n = int(e.split(' ')[1][1:])
      g = n
      if g not in G:
        G[g] = [0 for _ in range(60)]
    elif e == 'wakes up':
      for i in range(t, mm):
        G[g][i] += 1
    elif e == 'falls asleep':
      t = mm
    else:
      print(e)
  g, s = sorted(G.items(), key=lambda x: -sum(x[1]))[0]
  mm = max(enumerate(s), key=lambda x: x[1])[0]
  print(g * mm)


def part2():
  f = sorted([(tuple(map(int, re.split(r'[-: ]', l.split('] ')[0][1:]))),
               l.split('] ')[1]) for l in reader()])
  G = {}
  g = -1
  t = -1
  for (y, m, d, hh, mm), e in f:
    if e.startswith('Guard #'):
      n = int(e.split(' ')[1][1:])
      g = n
      if g not in G:
        G[g] = [0 for _ in range(60)]
    elif e == 'wakes up':
      for i in range(t, mm):
        G[g][i] += 1
    elif e == 'falls asleep':
      t = mm
    else:
      print(e)
  g, s = sorted(G.items(), key=lambda x: -max(x[1]))[0]
  mm = max(enumerate(s), key=lambda x: x[1])[0]
  print(g * mm)


part1()
part2()
