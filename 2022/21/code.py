import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  D = {}
  for l in f:
    a = l.split(": ")
    if len(a[1].split(" ")) == 1:
      D[a[0]] = int(a[1])
    else:
      D[a[0]] = a[1]

  def getNum(i):
    if isinstance(D[i], int) or isinstance(D[i], float):
      return D[i]
    v1 = D[i].split(" ")[0]
    v2 = D[i].split(" ")[2]
    n = eval(D[i], {v1: getNum(v1), v2: getNum(v2)})
    D[i] = n
    return D[i]
  print(int(getNum("root")))


def part2():
  f = reader()
  D = {}
  for l in f:
    a = l.split(": ")
    if len(a[1].split(" ")) == 1:
      D[a[0]] = int(a[1])
    else:
      D[a[0]] = a[1]
  v1 = D["root"].split(" ")[0]
  v2 = D["root"].split(" ")[2]

  def getNum(i):
    if i == "humn":
      return "humn"
    if isinstance(i, int) or isinstance(i, float):
      return i
    if isinstance(D[i], int) or isinstance(D[i], float):
      return D[i]
    v1 = D[i].split(" ")[0]
    v2 = D[i].split(" ")[2]
    n = eval(D[i], {v1: getNum(v1), v2: getNum(v2)})
    D[i] = n
    return n
  n = 0
  try:
    n = getNum(v1)
    v1 = None
  except:
    pass
  try:
    n = getNum(v2)
    v2 = None
  except:
    pass
  x = v1 if v1 else v2

  def dfs(i, v):
    if i == "humn":
      D[i] = v
    else:
      v1 = D[i].split(" ")[0]
      op = D[i].split(" ")[1]
      v2 = D[i].split(" ")[2]
      try:
        v1 = getNum(v1)
      except:
        pass
      try:
        v2 = getNum(v2)
      except:
        pass
      if isinstance(v1, int) or isinstance(v1, float):
        if op == "+":
          dfs(v2, v - v1)
        elif op == "-":
          dfs(v2, v1 - v)
        elif op == "*":
          dfs(v2, v / v1)
        elif op == "/":
          dfs(v2, v1 / v)
      else:
        if op == "+":
          dfs(v1, v - v2)
        elif op == "-":
          dfs(v1, v2 + v)
        elif op == "*":
          dfs(v1, v / v2)
        elif op == "/":
          dfs(v1, v2 * v)
  dfs(x, n)
  print(int(D["humn"]))


part1()
part2()
