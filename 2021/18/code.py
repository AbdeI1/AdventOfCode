from math import *


import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().split('\n')[:-1]


class node():
  def __init__(self, val, lchild, rchild, depth, parent):
    self.v = val
    self.l = lchild
    self.r = rchild
    self.d = depth
    self.p = parent


def split(n):
  if n == None:
    return
  if n.v >= 10:
    lc = node(n.v // 2, None, None, n.d + 1, n)
    rc = node(-(-n.v // 2), None, None, n.d + 1, n)
    n.v = -1
    n.l = lc
    n.r = rc
    return 1
  x = split(n.l)
  if x == 1:
    return 1
  return split(n.r)


def getMagnitude(t):
  if t.v != -1:
    return t.v
  return 3 * getMagnitude(t.l) + 2 * getMagnitude(t.r)


def explode(n):
  if n.v != -1:
    return
  if n.l.v != -1 and n.r.v != -1 and n.d >= 4:
    x = n.l.v
    y = n.r.v
    cur = n
    res = None
    while cur.p != None:
      if cur.p.l is cur:
        cur = cur.p
      else:
        res = cur.p.l
        break
    if res != None:
      while res.v == -1:
        res = res.r
      res.v += x
    cur = n
    res = None
    while cur.p != None:
      if cur.p.r is cur:
        cur = cur.p
      else:
        res = cur.p.r
        break
    if res != None:
      while res.v == -1:
        res = res.l
      res.v += y
    n.v = 0
    n.l = None
    n.r = None
    return 1
  x = explode(n.l)
  if x == 1:
    return 1
  return explode(n.r)


def toNode(n, i, p):
  if type(n) == int:
    new = node(n, None, None, i, p)
  else:
    new = node(-1, toNode(n[0], i + 1, None), toNode(n[1], i + 1, None), i, p)
    new.l.p = new
    new.r.p = new
  return new


def reduce(t):
  if t == None:
    return
  x = explode(t)
  if x == 1:
    return
  split(t)


def toString(t):
  if t.v != -1:
    return str(t.v)
  return '[' + toString(t.l) + ',' + toString(t.r) + ']'


def incDepth(t):
  if t == None:
    return
  t.d += 1
  incDepth(t.l)
  incDepth(t.r)

# def reduce(n):
# 	depth = -1
# 	i = 0
# 	while True:
# 		if i >= len(n):
# 			break
# 		if n[i] != '[' and n[i] != ']' and n[i] != ',' and n[i+1] != '[' and n[i+1] != ']' and n[i+1] != ',':
# 			x = int(n[i] + n[i+1])
# 			st = '[' + str(x//2) + ',' + str(int(ceil(x/2))) + ']'
# 			n = n[:i] + st + n[(i+2):]
# 			continue
# 		if n[i] == '[':
# 			depth += 1
# 		if n[i] == ']':
# 			depth -= 1
# 		if depth >= 4 and n[i] == '[':
# 			while n[i] == '[':
# 				i += 1
# 			i -= 1
# 			if n[i + 3] == '[' or n[i + 3] == ']' or n[i + 3] == ',':
# 				continue
# 			x = int(n[i+1])
# 			back = i
# 			while back >= 0:
# 				if n[back] != '[' and n[back] != ']' and n[back] != ',':
# 					t = str(int(n[back]) + x)
# 					if len(t) > 1:
# 						x = int(t)
# 						st = '[' + str(x//2) + ',' + str(int(ceil(x/2))) + ']'
# 						n = n[:back] + st + n[(back+1):]
# 						i += 4
# 					else:
# 						n = n[:back] + t + n[(back+1):]
# 					break
# 				back -= 1
# 			y = int(n[i+3])
# 			back = i+4
# 			while back < len(n):
# 				if n[back] != '[' and n[back] != ']' and n[back] != ',':
# 					t = str(int(n[back]) + y)
# 					if len(t) > 1:
# 						x = int(t)
# 						st = '[' + str(x//2) + ',' + str(int(ceil(x/2))) + ']'
# 						n = n[:back] + st + n[(back+1):]
# 					else:
# 						n = n[:back] + t + n[(back+1):]
# 					break
# 				back += 1
# 			n = n[:i] + '0' + n[(i+5):]
# 			depth -= 1
# 		i += 1
# 	return n


def part1():
  f = reader()
  inp = list(map(eval, f))
  # t1 = toNode(inp[0],1, None)
  # t2 = toNode(inp[1],1, None)
  # t3 = node(-1, t1, t2, 0, None)
  # t1.p = t3
  # t2.p = t3
  # print(toString(t3))
  # for _ in range(200):
  # 	reduce(t3)
  # print(toString(t3))
  # t1 = t3
  # t2 = toNode(inp[2],1,None)
  # incDepth(t1)
  # t3 = node(-1, t1, t2, 0, None)
  # t1.p = t3
  # t2.p = t3
  # print(toString(t3))
  # for _ in range(200):
  # 	reduce(t3)
  # 	print(toString(t3))

  t = toNode(inp[0], 0, None)
  for i in range(1, len(inp)):
    incDepth(t)
    tn = node(-1, t, toNode(inp[i], 1, None), 0, None)
    tn.l.p = tn
    tn.r.p = tn
    for _ in range(500):
      reduce(tn)
    t = tn
  print(toString(t))
  print(getMagnitude(t))

  # n = f[0]
  # for i in range(1, len(f)):
  # 	n = '[' + n + ',' + f[i] + ']'
  # 	for _ in range(100):
  # 		n = reduce(n)
  # 	print(n)
  # print(n)


def part2():
  f = reader()
  inp = list(map(eval, f))
  ma = 0
  for i in inp:
    for j in inp:
      if i != j:
        t = node(-1, toNode(i, 1, None), toNode(j, 1, None), 0, None)
        t.l.p = t
        t.r.p = t
        for _ in range(500):
          reduce(t)
        ma = max(getMagnitude(t), ma)
  print(ma)


part1()
part2()
