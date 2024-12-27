import math


import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  crabs = list(map(int, f[0].split(',')))
  m = 100000000
  for i in range(min(crabs), max(crabs) + 1):
    f = 0
    for c in crabs:
      f += abs(c - i)
    m = min(m, f)
  print(m)


def part2():
  f = reader()
  crabs = list(map(int, f[0].split(',')))
  m = 1000000000
  for i in range(min(crabs), max(crabs) + 1):
    f = 0
    for c in crabs:
      s = abs(c - i)
      f += (s * (s + 1)) // 2
    m = min(m, f)
  print(m)


def part3():
  f = reader()
  crabs = list(map(int, f[0].split(',')))
  mean = sum(crabs) / len(crabs)
  mean -= 1  # not sure why, but this is needed
  min1 = math.ceil(mean - 0.5)
  min2 = math.floor(mean + 0.5)
  ans1 = 0
  for c in crabs:
    s = abs(c - min1)
    ans1 += (s * (s + 1)) // 2
  ans2 = 0
  for c in crabs:
    s = abs(c - min2)
    ans2 += (s * (s + 1)) // 2
  print(ans1)


part1()
part2()
part3()
