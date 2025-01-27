import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  l = reader()[0].split()
  P, M = int(l[0]), int(l[6])

  class Node:
    def __init__(self, v=0, n=None, p=None):
      self.v = v
      self.n = n if n else self
      self.p = p if p else self

    def rm(self):
      self.p.n = self.n
      self.n.p = self.p
      return self

    def next(self, n=1):
      if n == 0:
        return self
      return self.n.next(n - 1)

    def prev(self, n=1):
      if n == 0:
        return self
      return self.p.prev(n - 1)

    def insert_next(self, n):
      n.p = self
      n.n = self.n
      self.n.p = n
      self.n = n

    def insert_prev(self, n):
      self.p.insert_next(n)

  N = Node(0)
  p = [0] * P

  for i in range(1, M + 1):
    if i % 23 == 0:
      p[(i - 1) % P] += i + N.prev(7).v
      N.prev(7).rm()
      N = N.prev(6)
    else:
      N.next().insert_next(Node(i))
      N = N.next(2)

  print(max(p))


def part2():
  l = reader()[0].split()
  P, M = int(l[0]), int(l[6])
  M *= 100

  class Node:
    def __init__(self, v=0, n=None, p=None):
      self.v = v
      self.n = n if n else self
      self.p = p if p else self

    def rm(self):
      self.p.n = self.n
      self.n.p = self.p
      return self

    def next(self, n=1):
      if n == 0:
        return self
      return self.n.next(n - 1)

    def prev(self, n=1):
      if n == 0:
        return self
      return self.p.prev(n - 1)

    def insert_next(self, n):
      n.p = self
      n.n = self.n
      self.n.p = n
      self.n = n

    def insert_prev(self, n):
      self.p.insert_next(n)

  N = Node(0)
  p = [0] * P

  for i in range(1, M + 1):
    if i % 23 == 0:
      p[(i - 1) % P] += i + N.prev(7).v
      N.prev(7).rm()
      N = N.prev(6)
    else:
      N.next().insert_next(Node(i))
      N = N.next(2)

  print(max(p))


part1()
part2()
