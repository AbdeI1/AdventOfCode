import os
os.chdir(os.path.dirname(__file__))
from collections import defaultdict
from functools import cache


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = [l.split() for l in reader()]
  R = defaultdict(int)
  def val(x): return R[x] if x.isalpha() else int(x)
  i = 0
  while i in range(len(f)):
    l = f[i]
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
    i += 1
  print(R['a'])


def part2():
  f = [l.split() for l in reader()]
  R = defaultdict(int)

  def fib(n):
    return 1 if n <= 1 else fib(n - 1) + fib(n - 2)

  print(fib(eval(f'{f[2][1]}+{f[5][1]}+1')) + eval(f'{f[16][1]}*{f[17][1]}'))


part1()
part2()
