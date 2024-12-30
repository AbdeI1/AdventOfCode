import os
os.chdir(os.path.dirname(__file__))
import sys
sys.path.append('..')
from intcode import compute
from itertools import permutations
from threading import Thread
from time import sleep


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  code = list(map(int, reader()[0].split(',')))
  m = 0
  for p in permutations(range(5)):
    out = 0
    for i in p:
      out = compute(code.copy(), [i, out], [])[0]
    m = max(m, out)
  print(m)


def part2():
  code = list(map(int, reader()[0].split(',')))
  M = {}

  def test(p):
    I = [[i] for i in p]
    I[0].append(0)
    T = [Thread(target=compute, args=(code.copy(), I[i], I[(i + 1) % 5]))
         for i in range(5)]
    for t in T:
      t.start()
    T[-1].join()
    M[p] = I[0][0]
  TT = [Thread(target=test, args=(p,)) for p in permutations(range(5, 10))]
  for t in TT:
    t.start()
  for t in TT:
    t.join()
  print(max(M.values()))


part1()
part2()
