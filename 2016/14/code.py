import os
os.chdir(os.path.dirname(__file__))
from hashlib import md5
from collections import Counter
from functools import cache


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()[0]
  C = Counter()
  for i in range(1000):
    s = md5(f'{f}{i}'.encode()).hexdigest()
    for j in range(len(s) - 4):
      if len(set(s[j:j + 5])) == 1:
        C[s[j]] += 1
  i = 1000
  K = []
  while len(K) < 64:
    s1 = md5(f'{f}{i - 1000}'.encode()).hexdigest()
    s2 = md5(f'{f}{i}'.encode()).hexdigest()
    for j in range(len(s2) - 4):
      if len(set(s1[j:j + 5])) == 1:
        C[s1[j]] -= 1
      if len(set(s2[j:j + 5])) == 1:
        C[s2[j]] += 1
    for j in range(len(s1) - 2):
      if len(set(s1[j:j + 3])) == 1:
        if C[s1[j]] > 0:
          K.append(i - 1000)
        break
    i += 1
  print(K[-1])


def part2():
  f = reader()[0]
  C = Counter()

  @cache
  def hash(s: str):
    for _ in range(2017):
      s = md5(s.encode()).hexdigest()
    return s

  for i in range(1000):
    s = hash(f'{f}{i}')
    for j in range(len(s) - 4):
      if len(set(s[j:j + 5])) == 1:
        C[s[j]] += 1
  i = 1000
  K = []
  while len(K) < 64:
    s1 = hash(f'{f}{i - 1000}')
    s2 = hash(f'{f}{i}')
    for j in range(len(s2) - 4):
      if len(set(s1[j:j + 5])) == 1:
        C[s1[j]] -= 1
      if len(set(s2[j:j + 5])) == 1:
        C[s2[j]] += 1
    for j in range(len(s1) - 2):
      if len(set(s1[j:j + 3])) == 1:
        if C[s1[j]] > 0:
          K.append(i - 1000)
        break
    i += 1
  print(K[-1])


part1()
part2()
