import os
os.chdir(os.path.dirname(__file__))
from collections import deque
from heapq import heappop, heappush


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = [(l[1:l.find(']')], list(map(lambda x: eval(f'{{{x[1:-1]}}}'), l[l.find('('):l.find('{')-1].split())), eval(f'[{l[l.find('{')+1:-1]}]')) for l in reader()]
  A = 0
  for E, B, _ in f:
    E = tuple(1 if c == '#' else 0 for c in E)
    S = (0,) * len(E)
    Q = deque([(S, 0)])
    V = set()
    while len(Q) > 0:
      s, d = Q.popleft()
      if s in V:
        continue
      V.add(s)
      if s == E:
        A += d
        break
      for b in B:
        ns = tuple(s[i] if i not in b else (1 - s[i]) for i in range(len(s)))
        Q.append((ns, d + 1))
  print(A)


def part2():
  f = [(l[1:l.find(']')], list(map(lambda x: eval(f'{{{x[1:-1]}}}'), l[l.find('('):l.find('{')-1].split())), eval(f'({l[l.find('{')+1:-1]})')) for l in reader()]
  A = 0
  for _, B, E in f:
    print([min(E[i] for i in b) for b in B])
  print(A)


part1()
part2()
