import os
os.chdir(os.path.dirname(__file__))
from collections import defaultdict
from math import factorial


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  p = list(map(str.split, reader()))
  R = defaultdict(int)
  R['a'] = 7
  def val(x): return R[x] if x.isalpha() else int(x)
  i = 0
  while i in range(len(p)):
    l = p[i]
    match l[0]:
      case 'cpy':
        R[l[2]] = val(l[1])
      case 'inc':
        R[l[1]] += 1
      case 'dec':
        R[l[1]] -= 1
      case 'jnz':
        if val(l[1]) != 0:
          i += val(l[2])
          continue
      case 'tgl':
        j = i + val(l[1])
        if j in range(len(p)):
          if len(p[j]) == 2:
            p[j][0] = 'dec' if p[j][0] == 'inc' else 'inc'
          elif len(p[j]) == 3:
            p[j][0] = 'cpy' if p[j][0] == 'jnz' else 'jnz'
    i += 1
  print(R['a'])


def part2():
  p = list(map(str.split, reader()))
  a, b = int(p[-7][1]), int(p[-6][1])
  print(factorial(12) + a * b)


part1()
part2()
