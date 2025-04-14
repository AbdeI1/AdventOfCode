import os
os.chdir(os.path.dirname(__file__))
from hashlib import md5
from collections import Counter


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()[0]
  f = 'abc'
  C = Counter()
  for i in range(1000):
    s = md5(f'{f}{i}'.encode()).hexdigest()
    for j in range(len(s) - 5):
      if len(set(s[j:j + 5])) == 1:
        C[s[j]] += 1
  i = 1000
  K = []
  while len(K) < 64:
    s1 = md5(f'{f}{i - 1000}'.encode()).hexdigest()
    s2 = md5(f'{f}{i}'.encode()).hexdigest()
    for j in range(len(s2) - 5):
      if len(set(s1[j:j + 5])) == 1:
        C[s1[j]] -= 1
      if len(set(s2[j:j + 5])) == 1:
        C[s2[j]] += 1
    for j in range(len(s1) - 3):
      if len(set(s1[j:j + 3])) == 1:
        if C[s1[j]] > 0:
          K.append(i - 1000)
        break
    i += 1
  print(K)


def part2():
  pass


part1()
part2()
