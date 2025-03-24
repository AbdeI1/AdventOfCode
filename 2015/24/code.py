import os
os.chdir(os.path.dirname(__file__))
from functools import cache
from math import prod


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  W = list(map(int, reader()))
  T = sum(W) // 3

  @cache
  def f(t=T, i=0):
    if i >= len(W):
      return [[]] if t == 0 else []
    if t == 0:
      return [[]]
    if t < 0:
      return []
    return f(t, i + 1) + [[W[i]] + l for l in f(t - W[i], i + 1)]

  L = f()
  l = len(min(L, key=lambda l: len(l)))
  print(
    prod(sorted(filter(lambda x: len(x) == l, L), key=lambda x: prod(x))[0]))


def part2():
  W = list(map(int, reader()))
  T = sum(W) // 4

  @cache
  def f(t=T, i=0):
    if i >= len(W):
      return [[]] if t == 0 else []
    if t == 0:
      return [[]]
    if t < 0:
      return []
    return f(t, i + 1) + [[W[i]] + l for l in f(t - W[i], i + 1)]

  L = f()
  l = len(min(L, key=lambda l: len(l)))
  print(
    prod(sorted(filter(lambda x: len(x) == l, L), key=lambda x: prod(x))[0]))


part1()
part2()
