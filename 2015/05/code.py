import os
os.chdir(os.path.dirname(__file__))
from re import findall, search


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  print(len([l for l in reader() if len(findall(r'[aeiou]', l)) >=
             3 and search(r'(.)\1', l) != None and search(r'ab|cd|pq|xy', l) == None]))


def part2():
  print(len([l for l in reader() if search(r'(..).*\1', l)
        != None and search(r'(.).\1', l) != None]))


part1()
part2()
