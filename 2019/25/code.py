import os
os.chdir(os.path.dirname(__file__))
import sys
sys.path.append('..')
from intcode import compute
from threading import Thread
from time import sleep


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  code = list(map(int, reader()[0].split(',')))
  I, O = [], []
  T = Thread(target=compute, args=(code, I, O), daemon=True)


def part2():
  pass


part1()
part2()
