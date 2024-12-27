import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


class Node:
  def __init__(self, i):
    self.ord = -1
    self.n = i
    self.prev = None
    self.next = None

  def __str__(self):
    return f"{self.ord}: {self.prev.n if self.prev else None} <-- {self.n} --> {self.next.n if self.next else None}"


def part1():
  f = reader()
  f = list(map(int, f))
  M = len(f)
  n = Node(f[0])
  n.ord = 0
  p = n
  for i in range(1, M):
    node = Node(f[i])
    p.next = node
    node.prev = p
    node.ord = i
    p = node
  p.next = n
  n.prev = p
  for i in range(M):
    while n.ord != i:
      n = n.next
    v = n.n
    c = n.next
    c.prev = n.prev
    n.prev.next = c
    M -= 1
    v = ((v % M) + M) % M
    M += 1
    while v > 0:
      v -= 1
      c = c.next
    n.next = c
    n.prev = c.prev
    c.prev.next = n
    c.prev = n
  while n.n != 0:
    n = n.next
  ans = 0
  for _ in range(3):
    for _ in range(1000):
      n = n.next
    ans += n.n
  print(ans)


def part2():
  f = reader()
  decryptionKey = 811589153
  f = list(map(int, f))
  f = list(map(lambda x: x * decryptionKey, f))
  M = len(f)
  n = Node(f[0])
  n.ord = 0
  p = n
  for i in range(1, M):
    node = Node(f[i])
    p.next = node
    node.prev = p
    node.ord = i
    p = node
  p.next = n
  n.prev = p
  for _ in range(10):
    for i in range(M):
      while n.ord != i:
        n = n.next
      v = n.n
      c = n.next
      c.prev = n.prev
      n.prev.next = c
      M -= 1
      v = ((v % M) + M) % M
      M += 1
      while v > 0:
        v -= 1
        c = c.next
      n.next = c
      n.prev = c.prev
      c.prev.next = n
      c.prev = n
  while n.n != 0:
    n = n.next
  ans = 0
  for _ in range(3):
    for _ in range(1000):
      n = n.next
    ans += n.n
  print(ans)


part1()
part2()
