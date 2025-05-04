import os
os.chdir(os.path.dirname(__file__))
from hashlib import md5


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  s = reader()[0]
  i = 0
  while True:
    h = md5(f'{s}{i}'.encode()).hexdigest()
    if h.startswith('00000'):
      print(i)
      break
    i += 1


def part2():
  s = reader()[0]
  i = 0
  while True:
    h = md5(f'{s}{i}'.encode()).hexdigest()
    if h.startswith('000000'):
      print(i)
      break
    i += 1


part1()
part2()
