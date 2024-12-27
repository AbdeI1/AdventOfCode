from functools import *


import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().split('\n')[:-1]


def part1():
  f = reader()
  timers = list(map(int, f[0].split(',')))
  fish = len(timers)
  for i in range(80):
    l = len(timers)
    for i in range(l):
      if (timers[i] == 0):
        timers[i] = 6
        fish += 1
        timers.append(8)
      else:
        timers[i] -= 1
  print(fish)


@cache
def simulate(n, t):
  if t <= 0:
    return 1
  if n == 0:
    return simulate(6, t - 1) + simulate(8, t - 1)
  return simulate(n - 1, t - 1)


s = [0] * 9


@cache
def simulate2(n, t):
  if t <= 0:
    return s[n]
  if n == 6:
    return simulate2(7, t - 1) + simulate2(0, t - 1)
  return simulate2((n + 1) % 9, t - 1)


def part2():
  f = reader()
  timers = list(map(int, f[0].split(',')))
  for t in timers:
    s[t] += 1
  s1 = 0
  for t in timers:
    s1 += simulate(t, 256)
  s2 = 0
  for i in range(9):
    s2 += simulate2(i, 256)
  print(s1)
  print(s2)


part1()
part2()
