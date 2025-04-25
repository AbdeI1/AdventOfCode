import os
os.chdir(os.path.dirname(__file__))
from operator import and_, or_, lshift, rshift


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  I = {o: i for i, o in (l.split(' -> ') for l in reader())}
  V = {}

  def val(s: str):
    if s.isdecimal():
      return int(s)
    if s not in V:
      i = I[s].split()
      if len(i) == 1:
        V[s] = val(i[0])
      elif len(i) == 2:
        V[s] = ~val(i[1]) & 0xffff
      else:
        V[s] = {'AND': and_, 'OR': or_, 'LSHIFT': lshift,
                'RSHIFT': rshift}[i[1]](val(i[0]), val(i[2]))
    return V[s]

  print(val('a'))


def part2():
  I = {o: i for i, o in (l.split(' -> ') for l in reader())}
  V = {}

  def val(s: str):
    if s.isdecimal():
      return int(s)
    if s not in V:
      i = I[s].split()
      if len(i) == 1:
        V[s] = val(i[0])
      elif len(i) == 2:
        V[s] = ~val(i[1]) & 0xffff
      else:
        V[s] = {'AND': and_, 'OR': or_, 'LSHIFT': lshift,
                'RSHIFT': rshift}[i[1]](val(i[0]), val(i[2]))
    return V[s]

  V = {'b': val('a')}
  print(val('a'))


part1()
part2()
