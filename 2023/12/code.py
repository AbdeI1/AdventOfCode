import os
os.chdir(os.path.dirname(__file__))
import re
from functools import cache


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = [[x.split()[0]] + [list(map(int, x.split()[1].split(',')))]
       for x in reader()]
  ans = 0
  for s, n in f:
    p = s.replace('.', 'a').replace('#', 'b').replace('?', '.')
    diff = len(p) - sum(n) - len(n) + 1
    l = [0] * (len(n) + 1)
    t = 0

    def count(i, c):
      nonlocal t
      if i == len(l) - 1:
        l[i] = c
        p2 = "a" * l[0]
        for j in range(len(n) - 1):
          p2 += "b" * n[j] + "a"
          p2 += "a" * l[j + 1]
        p2 += "b" * n[-1] + "a" * l[-1]
        if re.fullmatch(p, p2):
          t += 1
      else:
        for j in range(c + 1):
          l[i] = j
          count(i + 1, c - j)
    count(0, diff)
    ans += t
  print(ans)


def part2():
  f = [[x.split()[0]] + [list(map(int, x.split()[1].split(',')))]
       for x in reader()]
  ans = 0
  for s, n in f:
    rep = 5
    s = '?'.join([s for _ in range(rep)])
    n = n * rep

    @cache
    def count(i, j):
      if i >= len(s):
        return 1 if j >= len(n) else 0
      if j >= len(n):
        return count(i + 1, j) if s[i] in {'.', '?'} else 0
      match s[i]:
        case '.':
          return count(i + 1, j)
        case '#':
          c2 = 0
          c = 0
          while c < n[j] and i + c < len(s) and s[i + c] in {'#', '?'}:
            c += 1
          if c == n[j] and (i + c >= len(s) or s[i + c] in {'.', '?'}):
            c2 = count(i + c + 1, j + 1)
          return c2
        case '?':
          c1 = count(i + 1, j)
          c2 = 0
          c = 0
          while c < n[j] and i + c < len(s) and s[i + c] in {'#', '?'}:
            c += 1
          if c == n[j] and (i + c >= len(s) or s[i + c] in {'.', '?'}):
            c2 = count(i + c + 1, j + 1)
          return c1 + c2
    t = count(0, 0)
    ans += t
  print(ans)


part1()
part2()
