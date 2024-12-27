import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


class Valve:
  def __init__(self):
    self.name = ""
    self.flow = 0
    self.tunnels = set()
    self.paths = {}

  def __str__(self):
    return f"{self.name}: ({self.flow}, {self.tunnels}, {self.paths})"


def part1():
  f = reader()
  V = {}
  for l in f:
    a = l.split()
    v = Valve()
    V[a[1]] = v
    v.name = a[1]
    v.flow = int(a[4].split("ate=")[1][:-1])
    for s in l.split(", "):
      v.tunnels.add(s[-2:])
  for c in V:
    visited = set()
    q = [(c, 0)]
    while q:
      n, d = q.pop(0)
      if n in visited:
        continue
      visited.add(n)
      if V[n].flow > 0:
        V[c].paths[n] = d
      for o in V[n].tunnels:
        q.append((o, d + 1))
  VN = {}
  I = {}
  i = 0
  for c in V:
    if V[c].flow > 0:
      VN[c] = V[c]
      I[c] = i
      i += 1

  def toInt(D):
    ans = 0
    for d in D:
      if D[d]:
        ans += (1 << I[d])
    return ans
  isOpen = {}
  for l in VN:
    isOpen[l] = False
  DP = {}

  def dfs(n, t):
    if t <= 0:
      return 0
    k = (n, t, toInt(isOpen))
    if k in DP:
      return DP[k]
    m = 0
    if not isOpen[n]:
      isOpen[n] = True
      m = max(m, V[n].flow * (t - 1) + dfs(n, t - 1))
      isOpen[n] = False
    for c in VN[n].paths:
      if not isOpen[c] and c != n:
        m = max(m, dfs(c, t - VN[n].paths[c]))
    DP[k] = m
    return m
  ans = 0
  for s in V["AA"].paths:
    ans = max(ans, dfs(s, 30 - V["AA"].paths[s]))
  print(ans)


def part2():
  f = reader()
  V = {}
  for l in f:
    a = l.split()
    v = Valve()
    V[a[1]] = v
    v.name = a[1]
    v.flow = int(a[4].split("ate=")[1][:-1])
    for s in l.split(", "):
      v.tunnels.add(s[-2:])
  for c in V:
    visited = set()
    q = [(c, 0)]
    while q:
      n, d = q.pop(0)
      if n in visited:
        continue
      visited.add(n)
      if V[n].flow > 0:
        V[c].paths[n] = d
      for o in V[n].tunnels:
        q.append((o, d + 1))
  VN = {}
  I = {}
  i = 0
  for c in V:
    if V[c].flow > 0:
      VN[c] = V[c]
      I[c] = i
      i += 1

  def toInt(D):
    ans = 0
    for d in D:
      if D[d]:
        ans += (1 << I[d])
    return ans
  isOpen = {}
  for l in VN:
    isOpen[l] = False
  DP = {}

  def dfs(n, t, p):
    if t <= 0:
      if p >= 1:
        return 0
      else:
        ans = 0
        for s in V["AA"].paths:
          ans = max(ans, dfs(s, 26 - V["AA"].paths[s], 1))
        return ans
    k = (n, t, p, toInt(isOpen))
    if k in DP:
      return DP[k]
    m = 0
    if not isOpen[n]:
      isOpen[n] = True
      m = max(m, V[n].flow * (t - 1) + dfs(n, t - 1, p))
      isOpen[n] = False
    for c in VN[n].paths:
      if not isOpen[c] and c != n:
        m = max(m, dfs(c, t - VN[n].paths[c], p))
    if p == 0:
      for s in V["AA"].paths:
        m = max(m, dfs(s, 26 - V["AA"].paths[s], 1))
    DP[k] = m
    return m
  ans = 0
  for s in V["AA"].paths:
    ans = max(ans, dfs(s, 26 - V["AA"].paths[s], 0))
  print(ans)


part1()
part2()
