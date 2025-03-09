import os
os.chdir(os.path.dirname(__file__))
from collections import defaultdict
from time import sleep
from threading import Thread


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = [l.split() for l in reader()]
  R = defaultdict(int)
  def val(x): return R[x] if x.isalpha() else int(x)
  i = 0
  F = None
  while True:
    l = f[i]
    match l[0]:
      case 'snd':
        F = val(l[1])
      case 'set':
        R[l[1]] = val(l[2])
      case 'add':
        R[l[1]] += val(l[2])
      case 'mul':
        R[l[1]] *= val(l[2])
      case 'mod':
        R[l[1]] %= val(l[2])
      case 'rcv':
        if val(l[1]) != 0:
          break
      case 'jgz':
        if val(l[1]) > 0:
          i += val(l[2])
          continue
    i += 1
  print(F)


def part2():
  f = [l.split() for l in reader()]

  def run(pid, f, I, O, C):
    R = defaultdict(int)
    R['p'] = pid
    def val(x): return R[x] if x.isalpha() else int(x)
    i = 0
    while True:
      l = f[i]
      match l[0]:
        case 'snd':
          C[0] += 1
          O.append(val(l[1]))
        case 'set':
          R[l[1]] = val(l[2])
        case 'add':
          R[l[1]] += val(l[2])
        case 'mul':
          R[l[1]] *= val(l[2])
        case 'mod':
          R[l[1]] %= val(l[2])
        case 'rcv':
          w = 0
          while len(I) == 0:
            sleep(0.01)
            w += 1
            if w >= 100:
              return C
          R[l[1]] = I.pop(0)
        case 'jgz':
          if val(l[1]) > 0:
            i += val(l[2])
            continue
      i += 1

  Q0, Q1 = [], []
  C0, C1 = [0], [0]
  T0 = Thread(target=run, args=[0, f, Q1, Q0, C0])
  T1 = Thread(target=run, args=[1, f, Q0, Q1, C1])

  T0.start()
  T1.start()

  T0.join()
  T1.join()

  print(C1[0])


part1()
part2()
