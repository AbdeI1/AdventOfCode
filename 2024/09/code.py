import os
os.chdir(os.path.dirname(__file__))
from sortedcontainers import SortedList
from itertools import accumulate


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  n = list(map(int, reader()[0]))
  s = []
  c = 0
  i = 0
  j = len(n) - 1
  while i <= j:
    if i % 2 == 0:
      a = i // 2
      for _ in range(n[i]):
        s.append(a)
        c += 1
    else:
      ii = 0
      while i < j and ii < n[i]:
        if n[j] == 0 or j % 2 != 0:
          j -= 1
        else:
          a = j // 2
          s.append(a)
          c += 1
          n[j] -= 1
          ii += 1
    i += 1
  print(sum(i * n for i, n in enumerate(s)))


def part2():
  n = list(map(int, reader()[0]))
  gaps = [SortedList() for _ in range(10)]
  for i in range(1, len(n), 2):
    gaps[n[i]].add(i)
  pre = list(accumulate(n))
  c = 0
  for i in range(len(n) - 1, 0, -2):
    a = i // 2
    x, k = -1, len(n)
    for j in range(n[i], 10):
      l = gaps[j]
      if len(l) > 0 and l[0] < k:
        x = j
        k = l[0]
    if x >= 0:
      gaps[x].remove(k)
      c += a * n[i] * (2 * (pre[k] - x) + (n[i] - 1)) // 2
      gaps[x - n[i]].add(k)
    else:
      c += a * n[i] * (2 * pre[i - 1] + (n[i] - 1)) // 2
    for l in gaps:
      if l.count(i - 1) > 0:
        l.remove(i - 1)
  print(c)


# slow ~ 1.3s
def original_part2():
  n = list(map(int, reader()[0]))
  gaps = [n[i] for i in range(1, len(n), 2)]
  f = [[] for _ in range(len(gaps))]
  for i in range(len(n) - 1, 0, -2):
    a = i // 2
    s = n[i]
    try:
      j = next(j for j, g in enumerate(gaps) if g >= s and 2 * j + 1 < i)
      gaps[j] -= s
      n[i] = -n[i]
      f[j].extend([a] * s)
    except:
      pass
  s = []
  for i in range(0, len(n), 2):
    if n[i] >= 0:
      s.extend([i // 2] * n[i])
    else:
      s.extend([0] * -n[i])
    if i < len(n) - 1:
      s.extend(f[i // 2] + [0] * gaps[i // 2])
  print(sum(i * n for i, n in enumerate(s)))


part1()
part2()
