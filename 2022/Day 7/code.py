import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().split('\n')[:-1]


class Node:
  def __init__(self):
    self.children = []
    self.name = ""
    self.parent = None
    self.size = -1

  def getSize(self):
    if self.size != -1:
      return self.size
    self.size = 0
    for i in self.children:
      self.size += i.getSize()
    return self.size


def part1():
  f = reader()
  n = Node()
  n.name = "/"
  curNode = n
  i = 0
  while i < len(f):
    l = f[i]
    if l[0] == '$':
      cmd = l[2:].split()
      if cmd[0] == 'ls':
        i += 1
        while i < len(f) and f[i][0] != '$':
          files = f[i].split()
          if files[0] == 'dir':
            d = Node()
            d.name = files[1]
            d.parent = curNode
            curNode.children.append(d)
          else:
            d = Node()
            d.size = int(files[0])
            d.name = files[1]
            d.parent = curNode
            curNode.children.append(d)
          i += 1
        i -= 1
      elif cmd[0] == 'cd':
        dirName = cmd[1]
        if dirName == '..':
          curNode = curNode.parent
        elif dirName == '/':
          curNode = n
        else:
          for c in curNode.children:
            if c.name == dirName:
              curNode = c
              break
    i += 1
  ans = 0

  def dfs(node):
    nonlocal ans
    if len(node.children) == 0:
      return
    if node.getSize() <= 100000:
      ans += node.getSize()
    for i in node.children:
      dfs(i)
  dfs(n)
  print(ans)


def part2():
  f = reader()
  n = Node()
  n.name = "/"
  curNode = n
  i = 0
  while i < len(f):
    l = f[i]
    if l[0] == '$':
      cmd = l[2:].split()
      if cmd[0] == 'ls':
        i += 1
        while i < len(f) and f[i][0] != '$':
          files = f[i].split()
          if files[0] == 'dir':
            d = Node()
            d.name = files[1]
            d.parent = curNode
            curNode.children.append(d)
          else:
            d = Node()
            d.size = int(files[0])
            d.name = files[1]
            d.parent = curNode
            curNode.children.append(d)
          i += 1
        i -= 1
      elif cmd[0] == 'cd':
        dirName = cmd[1]
        if dirName == '..':
          curNode = curNode.parent
        elif dirName == '/':
          curNode = n
        else:
          for c in curNode.children:
            if c.name == dirName:
              curNode = c
              break
    i += 1
  dirs = []

  def dfs(node):
    nonlocal dirs
    if len(node.children) == 0:
      return
    dirs.append(node.getSize())
    for i in node.children:
      dfs(i)
  dfs(n)
  needed = n.getSize() - 40000000
  dirs.sort()
  for i in range(len(dirs)):
    if dirs[i] > needed:
      print(dirs[i])
      break


part1()
part2()
