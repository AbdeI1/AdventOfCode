import os
os.chdir(os.path.dirname(__file__))
from math import prod


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  n = int(reader()[0])
  F = [0 for _ in range(1000000)]
  for i in range(1, len(F)):
    F[i] += i * 10
    if F[i] > n:
      print(i)
      break
    for j in range(i + i, len(F), i):
      F[j] += i * 10


def part2():
  n = int(reader()[0])
  F = [0 for _ in range(1000000)]
  for i in range(1, len(F)):
    F[i] += i * 11
    if F[i] > n:
      print(i)
      break
    for j in range(i + i, min(len(F), 50 * i + 1), i):
      F[j] += i * 11


part1()
part2()
