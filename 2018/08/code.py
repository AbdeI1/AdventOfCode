import os
os.chdir(os.path.dirname(__file__))
from functools import cache


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = list(map(int, reader()[0].split()))
  i = 0

  T = {}
  t = 0

  def dfs(n=0):
    nonlocal i, t
    c, m = f[i:i + 2]
    i += 2
    children = []
    for _ in range(c):
      children.append(t + 1)
      dfs(t := t + 1)
    data = f[i:i + m]
    T[n] = (children, data)
    i += m

  dfs()

  print(sum(sum(data) for _, data in T.values()))


def part2():
  f = list(map(int, reader()[0].split()))
  i = 0

  T = {}
  t = 0

  def dfs(n=0):
    nonlocal i, t
    c, m = f[i:i + 2]
    i += 2
    children = []
    for _ in range(c):
      children.append(t + 1)
      dfs(t := t + 1)
    data = f[i:i + m]
    T[n] = (children, data)
    i += m

  dfs()

  @cache
  def value(n=0):
    c, d = T[n]
    if len(c) == 0:
      return sum(d)
    return sum(value(c[i - 1]) for i in d if i in range(1, len(c) + 1))

  print(value())


part1()
part2()
