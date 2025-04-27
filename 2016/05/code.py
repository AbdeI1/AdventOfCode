import os
os.chdir(os.path.dirname(__file__))
from hashlib import md5


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  s = reader()[0]
  i = 0
  p = ""
  while len(p) < 8:
    h = md5(f'{s}{i}'.encode()).hexdigest()
    if h.startswith('00000'): p += h[5]
    i += 1
  print(p)


def part2():
  s = reader()[0]
  i = 0
  p = [None for _ in range(8)]
  while None in p:
    h = md5(f'{s}{i}'.encode()).hexdigest()
    if h.startswith('00000'):
      pi = int(h[5], base=16)
      if pi in range(len(p)) and p[pi] == None:
        p[pi] = h[6]
    i += 1
  print(''.join(p))


part1()
part2()
