import os
os.chdir(os.path.dirname(__file__))
import sys
sys.path.append('..')
from intcode import compute


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  code = list(map(int, reader()[0].split(',')))
  print(compute(code, [1], [])[0])


def part2():
  code = list(map(int, reader()[0].split(',')))
  print(compute(code, [2], [])[0])


part1()
part2()
