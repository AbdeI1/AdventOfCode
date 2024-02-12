import pathlib
import re

def reader():
  f = open(f"{pathlib.Path(__file__).parent.resolve()}/sample.txt", 'r').read()
  f = f.split('\n')
  f = f[:-1]
  return f

def part1():
  f = [[x.split()[0]] + [list(map(int, x.split()[1].split(',')))] for x in reader()]
  ans = 0
  for s, n in f:
    p = s.replace('.', 'a').replace('#', 'b').replace('?','.')
    diff = len(s) - sum(n) - len(n) + 1
    l = [0]*(len(n) + 1)
    t = 0
    def count(i, c):
      nonlocal t
      if i == len(l)-1:
        l[i] = c
        p2 = "a"*l[0]
        for j in range(len(n)-1):
          p2 += "b"*n[j] + "a"
          p2 += "a"*l[j+1]
        p2 += "b"*n[-1] + "a"*l[-1]
        if re.fullmatch(p, p2):
          t += 1
      else:
        for j in range(c+1):
          l[i] = j
          count(i+1, c-j)
    count(0, diff)
    ans += t
  print(ans)

def part2():
  f = [[x.split()[0]] + [list(map(int, x.split()[1].split(',')))] for x in reader()]
  ans = 0
  for s, n in f:
    p = s.replace('.', 'a').replace('#', 'b').replace('?','.')
    diff = len(s) - sum(n) - len(n) + 1
    l = [0]*(len(n) + 1)
    t = 0
    c1, c2 = 0, 0
    def count(i, c):
      nonlocal t, c1, c2
      if i == len(l)-1:
        l[i] = c
        p2 = "a"*l[0]
        for j in range(len(n)-1):
          p2 += "b"*n[j] + "a"
          p2 += "a"*l[j+1]
        p2 += "b"*n[-1] + "a"*l[-1]
        if re.fullmatch(p, p2):
          if p[-1] == "b": c1 += 1
          if p[0] == "b": c2  += 1
          t += 1
      else:
        for j in range(c+1):
          l[i] = j
          count(i+1, c-j)
    count(0, diff)
    t1 = t
    t = 0
    p = "." + p
    count(0, diff+1)
    t2 = t
    print(t2)
    print(t1 * (t2 ** 4))
    ans += t1*(t2 ** 4)
  print(ans)

part1()
part2()
