import os
os.chdir(os.path.dirname(__file__))
import re


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  rules, parts = '\n'.join(reader()).split('\n\n')
  rules = {r[:r.find("{")]: [s for s in r[r.find("{") + 1:-1].split(",")]
           for r in rules.splitlines()}
  parts = [eval(re.sub(r"([xmas])", r'"\1"', p.replace('=', ':')))
           for p in parts.splitlines()]
  ans = 0
  for p in parts:
    w = 'in'
    while w not in {'A', 'R'}:
      r = rules[w]
      for c in r:
        i = c.find(":")
        w = c
        if i != -1:
          e = c[:i]
          w = c[(i + 1):]
          if eval(e, None, p):
            break
    if w == 'A':
      ans += sum(p.values())
  print(ans)


def part2():
  rules, _ = '\n'.join(reader()).split('\n\n')
  rules = {r[:r.find("{")]: [s for s in r[r.find("{") + 1:-1].split(",")]
           for r in rules.splitlines()}
  ans = 0

  def recurse(p, w):
    nonlocal ans
    if w in {'A', 'R'}:
      if w == 'A':
        a, b, c, d = [y - x + 1 for x, y in p.values()]
        ans += (a * b * c * d)
      return
    r = rules[w]
    for c in r:
      i = c.find(":")
      w = c
      if i != -1:
        e = c[:i]
        w = c[(i + 1):]
        l = e[0]
        cmp = e[1]
        n = int(e[2:])
        v = p[l]
        match cmp:
          case '>':
            if v[0] > n:
              recurse(p, w)
              break
            elif v[1] <= n:
              pass
            else:
              copy = {k: v for k, v in p.items()}
              v1, v2 = [v[0], n], [n + 1, v[1]]
              p[l] = v1
              copy[l] = v2
              recurse(copy, w)
          case '<':
            if v[1] < n:
              recurse(p, w)
              break
            elif v[0] >= n:
              pass
            else:
              copy = {k: v for k, v in p.items()}
              v1, v2 = [v[0], n - 1], [n, v[1]]
              p[l] = v2
              copy[l] = v1
              recurse(copy, w)
      else:
        recurse(p, w)

  recurse({'x': [1, 4000], 'm': [1, 4000],
           'a': [1, 4000], 's': [1, 4000]}, 'in')
  print(ans)


part1()
part2()
