import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


class Node:
  def __init__(self, v=0):
    self.v = v
    self.p = self
    self.n = self

  def prev(self, i=1):
    r = self
    for _ in range(i):
      r = r.p
    return r

  def next(self, i=1):
    r = self
    for _ in range(i):
      r = r.n
    return r

  def insertNext(self, v=0):
    n = Node(v)
    n.p = self
    n.n = self.n
    self.n = n
    n.n.p = n
    return n

  def insertPrev(self, v=0):
    self.p.insertNext(v)

  def __repr__(self):
    return f"({self.p.v} <- {self.v} -> {self.n.v})"


def part1():
  s = int(reader()[0])
  n = Node()
  for i in range(1, 2018):
    n = n.next(s).insertNext(i)
  print(n.n.v)


def part2():
  s = int(reader()[0])
  i = 0
  x = -1
  for j in range(1, 50000000):
    i = (i + s) % j
    i += 1
    if i == 1:
      x = j
  print(x)


part1()
part2()
