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
  T.start()
  I.extend(map(ord, """
NOT A J
NOT B T
OR T J
NOT C T
OR T J
AND D J
WALK
""".strip() + '\n'))
  sleep(0.1)
  print(O[-1])


def part2():
  code = list(map(int, reader()[0].split(',')))
  I, O = [], []
  T = Thread(target=compute, args=(code, I, O), daemon=True)
  T.start()
  I.extend(map(ord, """
NOT A J
NOT B T
OR T J
NOT C T
OR T J
AND D J
NOT E T
NOT T T
OR H T
AND T J
RUN
""".strip() + '\n'))
  sleep(1)
  print(O[-1])


part1()
part2()
