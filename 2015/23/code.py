import os
os.chdir(os.path.dirname(__file__))
from collections import defaultdict


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  p = list(map(lambda s: s.replace(",", "").split(), reader()))
  R = defaultdict(int)
  i = 0
  while i in range(len(p)):
    l = p[i]
    match l[0]:
      case 'hlf':
        R[l[1]] //= 2
      case 'tpl':
        R[l[1]] *= 3
      case 'inc':
        R[l[1]] += 1
      case 'jmp':
        i += int(l[1])
        continue
      case 'jie':
        if R[l[1]] % 2 == 0:
          i += int(l[2])
          continue
      case 'jio':
        if R[l[1]] == 1:
          i += int(l[2])
          continue
    i += 1
  print(R['b'])


def part2():
  p = list(map(lambda s: s.replace(",", "").split(), reader()))
  R = defaultdict(int)
  R['a'] = 1
  i = 0
  while i in range(len(p)):
    l = p[i]
    match l[0]:
      case 'hlf':
        R[l[1]] //= 2
      case 'tpl':
        R[l[1]] *= 3
      case 'inc':
        R[l[1]] += 1
      case 'jmp':
        i += int(l[1])
        continue
      case 'jie':
        if R[l[1]] % 2 == 0:
          i += int(l[2])
          continue
      case 'jio':
        if R[l[1]] == 1:
          i += int(l[2])
          continue
    i += 1
  print(R['b'])


part1()
part2()
