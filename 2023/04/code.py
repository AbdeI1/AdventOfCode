import os
os.chdir(os.path.dirname(__file__))
import functools


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  ans = 0
  for l in f:
    wins = set(map(int, filter(lambda s: len(s) > 0,
               l[l.find(":") + 1:l.find("|")].split(" "))))
    nums = list(
      map(int, filter(lambda s: len(s) > 0, l[l.find("|") + 1:].split(" "))))
    c = list(filter(lambda x: x in wins, nums))
    if len(c) > 0:
      ans += 2 ** (len(c) - 1)
  print(ans)


def part2():
  f = reader()
  inp = []
  ans = 0
  for l in f:
    wins = set(map(int, filter(lambda s: len(s) > 0,
               l[l.find(":") + 1:l.find("|")].split(" "))))
    nums = list(
      map(int, filter(lambda s: len(s) > 0, l[l.find("|") + 1:].split(" "))))
    inp.append((wins, nums))

  @functools.cache
  def f(i: int):
    wins, nums = inp[i]
    c = list(filter(lambda x: x in wins, nums))
    return len(c) + sum((f(i + j) for j in range(1, len(c) + 1)))
  ans = sum(f(i) for i in range(len(inp))) + len(inp)
  print(ans)


part1()
part2()
