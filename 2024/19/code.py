import os
os.chdir(os.path.dirname(__file__))
from functools import cache


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  patterns, designs = '\n'.join(reader()).split('\n\n')
  patterns = patterns.split(', ')
  designs = designs.split('\n')

  @cache
  def test(d, i):
    if i >= len(d):
      return True
    b = False
    for p in patterns:
      if d[i:i + len(p)] == p:
        b = b or test(d, i + len(p))
    return b

  c = 0
  for d in designs:
    if test(d, 0):
      c += 1

  print(c)


def part2():
  patterns, designs = '\n'.join(reader()).split('\n\n')
  patterns = patterns.split(', ')
  designs = designs.split('\n')

  @cache
  def test(d, i):
    if i >= len(d):
      return 1
    c = 0
    for p in patterns:
      if d[i:i + len(p)] == p:
        c += test(d, i + len(p))
    return c

  c = 0
  for d in designs:
    c += test(d, 0)

  print(c)


part1()
part2()
