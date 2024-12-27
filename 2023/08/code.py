import os
os.chdir(os.path.dirname(__file__))
from functools import reduce


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  dirs = f[0]
  m = {s.split(" = ")[0]: tuple(s.split(" = ")[1][1:-1].split(', '))
       for s in f[2:]}
  s = "AAA"
  i = 0
  while s != "ZZZ":
    d = dirs[i % len(dirs)]
    s = m[s][0 if d == "L" else 1]
    i += 1
  print(i)


def gcd(a, b):
  return a if b == 0 else gcd(b, a % b)


def lcm(a, b):
  return (a * b) // gcd(a, b)


def part2():
  f = reader()
  dirs = f[0]
  m = {s.split(" = ")[0]: tuple(s.split(" = ")[1][1:-1].split(', '))
       for s in f[2:]}
  n = []
  for l in m:
    if l[-1] == "A":
      s = l
      i = 0
      while s[-1] != "Z":
        d = dirs[i % len(dirs)]
        s = m[s][0 if d == "L" else 1]
        i += 1
      j = 0
      while j < 1 or s[-1] != "Z":
        d = dirs[i % len(dirs)]
        s = m[s][0 if d == "L" else 1]
        i += 1
        j += 1
      i -= j
      n.append(i)
  print(reduce(lcm, n))


part1()
part2()
