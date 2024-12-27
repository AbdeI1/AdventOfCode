import os
os.chdir(os.path.dirname(__file__))
from functools import cache


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  stones = list(map(int, reader()[0].split()))

  @cache
  def t(n, i):
    if i == 0:
      return 1
    if n == 0:
      return t(1, i - 1)
    s = str(n)
    x = len(s)
    if x % 2 == 0:
      return t(int(s[:(x // 2)]), i - 1) + t(int(s[(x // 2):]), i - 1)
    return t(n * 2024, i - 1)

  print(sum(t(s, 25) for s in stones))


def part2():
  stones = list(map(int, reader()[0].split()))

  @cache
  def t(n, i):
    if i == 0:
      return 1
    if n == 0:
      return t(1, i - 1)
    s = str(n)
    x = len(s)
    if x % 2 == 0:
      return t(int(s[:(x // 2)]), i - 1) + t(int(s[(x // 2):]), i - 1)
    return t(n * 2024, i - 1)

  print(sum(t(s, 75) for s in stones))


part1()
part2()
