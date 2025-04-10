import os
os.chdir(os.path.dirname(__file__))
from math import prod


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  D = [(int(l.split()[3]), int(l.split()[-1][:-1])) for l in reader()]
  M = prod(m for m, _ in D)
  B = [((M // m) * pow(M // m, -1, m)) % M for m, _ in D]
  P = [(-(i + 1) - D[i][1]) % D[i][0] for i in range(len(D))]
  print(sum(p * b for p, b in zip(P, B)) % M)


def part2():
  D = [(int(l.split()[3]), int(l.split()[-1][:-1])) for l in reader()]
  D += [(11, 0)]
  M = prod(m for m, _ in D)
  B = [((M // m) * pow(M // m, -1, m)) % M for m, _ in D]
  P = [(-(i + 1) - D[i][1]) % D[i][0] for i in range(len(D))]
  print(sum(p * b for p, b in zip(P, B)) % M)


part1()
part2()
