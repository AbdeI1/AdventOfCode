import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  g = {}
  for l in f:
    n, o = l.split(": ")
    o = o.split(" ")
    if n not in g:
      g[n] = set()
    for n2 in o:
      if n2 not in g:
        g[n2] = set()
      g[n].add(n2)
      g[n2].add(n)

  def num_paths(a, b):
    e = set()
    count = 0
    for n in g[a]:
      s = [(n, a)]
      v = {a}
      p = {}
      while s:
        o, op = s.pop(0)
        if o in v:
          continue
        v.add(o)
        p[o] = op
        if o == b:
          count += 1
          break
        for n2 in g[o]:
          if (o, n2) not in e and (n2, o) not in e:
            s.append((n2, o))
      else:
        continue
      x = b
      while x != a:
        e.add((x, p[x]))
        e.add((p[x], x))
        x = p[x]
    return count

  o = list(g)[0]
  n = 0
  for a in g:
    if num_paths(o, a) == 3:
      n += 1
  print(n * (len(g) - n))


part1()
