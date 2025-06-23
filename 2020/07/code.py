import os
os.chdir(os.path.dirname(__file__))
from functools import cache


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = {k: v for k, v in map(
    lambda t: (t[0], {c: n for n, c in [(lambda l: (int(l[0]), " ".join(l[1:-1])))(s.split()) for s in t[1].split(", ")]} if t[1] != "no other bags." else {}), [tuple(s.split(" bags contain ")) for s in reader()])}

  @cache
  def containsGold(c):
    if c == "shiny gold": return True
    return any(containsGold(cc) for cc in f[c])

  print(sum(containsGold(c) for c in f) - 1)


def part2():
  f = {k: v for k, v in map(
    lambda t: (t[0], {c: n for n, c in [(lambda l: (int(l[0]), " ".join(l[1:-1])))(s.split()) for s in t[1].split(", ")]} if t[1] != "no other bags." else {}), [tuple(s.split(" bags contain ")) for s in reader()])}

  @cache
  def howMany(c):
    return sum(n + n * howMany(cc) for cc, n in f[c].items())

  print(howMany("shiny gold"))


part1()
part2()
