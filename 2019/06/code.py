import os
os.chdir(os.path.dirname(__file__))
from itertools import chain


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = list(map(lambda x: x.split(')'), reader()))
  p = {n: None for n in chain(*f)}
  for a, b in f:
    p[b] = a
  P = {n: None for n in chain(*f)}

  def getP(n):
    if P[n] is None:
      P[n] = [p[n]] + getP(p[n]) if p[n] else []
    return P[n]

  c = 0
  for n in p:
    c += len(getP(n))
  print(c)


def part2():
  f = list(map(lambda x: x.split(')'), reader()))
  p = {n: None for n in chain(*f)}
  for a, b in f:
    p[b] = a
  P = {n: None for n in chain(*f)}

  def getP(n):
    if P[n] is None:
      P[n] = [p[n]] + getP(p[n]) if p[n] else []
    return P[n]

  for n in p:
    getP(n)

  p1, p2 = P['YOU'], P['SAN']

  while p1[-1] == p2[-1]:
    p1.pop()
    p2.pop()

  print(len(p1) + len(p2))


part1()
part2()
