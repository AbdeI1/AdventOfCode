import os
os.chdir(os.path.dirname(__file__))
from functools import cache


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  d = 64
  s = (0, 0)
  for i in range(len(f)):
    for j in range(len(f[i])):
      if f[i][j] == 'S':
        s = (i, j)
        break
    else:
      continue
    break
  q = [(s, 0)]
  v = set()
  ans = 0
  while q:
    (i, j), s = q.pop(0)
    if s > d or i not in range(len(f)) or j not in range(len(f[i])) or f[i][j] == '#':
      continue
    if (i, j) in v:
      continue
    v.add((i, j))
    if s % 2 == 0:
      ans += 1
    for d1, d2 in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
      q.append(((i + d1, j + d2), s + 1))
  print(ans)


def part2():
  f = reader()
  s = (0, 0)
  for i in range(len(f)):
    for j in range(len(f[i])):
      if f[i][j] == 'S':
        s = (i, j)
        break
    else:
      continue
    break
  q = [(s, 0)]
  v = [[-1 for _ in range(len(f[i]))] for i in range(len(f))]
  while q:
    (i, j), st = q.pop(0)
    if i not in range(len(f)) or j not in range(len(f[i])) or f[i][j] == '#':
      continue
    if v[i][j] != -1:
      continue
    v[i][j] = st
    for d1, d2 in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
      q.append(((i + d1, j + d2), st + 1))

  d = 26501365
  q = d // len(f)
  r = d % len(f)
  same = sum([sum([1 if n >= 0 and n % 2 == d % 2 else 0 for n in l])
              for l in v])
  same_far = sum(
    [sum([1 if n >= 0 and n % 2 == d % 2 and n > r else 0 for n in l]) for l in v])
  diff = sum([sum([1 if n >= 0 and n % 2 != d % 2 else 0 for n in l])
             for l in v])
  diff_far = sum(
    [sum([1 if n >= 0 and n % 2 != d % 2 and n > r else 0 for n in l]) for l in v])

  ans = pow(q + 1, 2) * same + pow(q, 2) * diff - \
      (q + 1) * same_far + q * diff_far - q * 2
  print(ans)


part1()
part2()
