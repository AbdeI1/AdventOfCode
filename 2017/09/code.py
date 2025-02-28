import os
os.chdir(os.path.dirname(__file__))
from re import sub


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = list(sub(r"!.", "", reader()[0]).replace(
    "{", "[").replace("}", "]").replace('"', ""))
  o = False
  for i in range(len(f)):
    if not o and f[i] == '<':
      f[i] = '"'
      o = True
    elif o and f[i] == '>':
      f[i] = '"'
      o = False
  f = ''.join(f)
  s = eval(f)

  def score(l, b=1):
    if type(l) is str:
      return 0
    return b + sum(score(x, b + 1) for x in l)

  print(score(s))


def part2():
  f = list(sub(r"!.", "", reader()[0]).replace(
    "{", "[").replace("}", "]").replace('"', "'"))
  o = False
  for i in range(len(f)):
    if not o and f[i] == '<':
      f[i] = '"'
      o = True
    elif o and f[i] == '>':
      f[i] = '"'
      o = False
  f = ''.join(f)
  s = eval(f)

  def score(l):
    if type(l) is str:
      return len(l)
    return sum(score(x) for x in l)

  print(score(s))


part1()
part2()
