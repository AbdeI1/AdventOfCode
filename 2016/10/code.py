import os
os.chdir(os.path.dirname(__file__))
from collections import defaultdict


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = [l.split() for l in reader()]
  I = {}
  B = defaultdict(list)
  O = defaultdict(list)
  for l in f:
    if l[0] == 'bot':
      I[int(l[1])] = ((l[5], int(l[6])), (l[10], int(l[11])))
    else:
      B[int(l[5])].append(int(l[1]))

  def r(i):
    if len(B[i]) == 2:
      v1, v2 = sorted(B[i])
      if (v1, v2) == (17, 61):
        print(i)
      (I1d, I1n), (I2d, I2n) = I[i]
      if I1d == 'bot':
        B[I1n].append(v1)
        r(I1n)
      else:
        O[I1n].append(v1)
      if I2d == 'bot':
        B[I2n].append(v2)
        r(I2n)
      else:
        O[I2n].append(v2)
      B[i] = []

  s = -1
  for n in B:
    if len(B[n]) == 2:
      s = n
  r(s)


def part2():
  f = [l.split() for l in reader()]
  I = {}
  B = defaultdict(list)
  O = defaultdict(list)
  for l in f:
    if l[0] == 'bot':
      I[int(l[1])] = ((l[5], int(l[6])), (l[10], int(l[11])))
    else:
      B[int(l[5])].append(int(l[1]))

  def r(i):
    if len(B[i]) == 2:
      v1, v2 = sorted(B[i])
      (I1d, I1n), (I2d, I2n) = I[i]
      if I1d == 'bot':
        B[I1n].append(v1)
        r(I1n)
      else:
        O[I1n].append(v1)
      if I2d == 'bot':
        B[I2n].append(v2)
        r(I2n)
      else:
        O[I2n].append(v2)
      B[i] = []

  s = -1
  for n in B:
    if len(B[n]) == 2:
      s = n
  r(s)

  print(O[0][0] * O[1][0] * O[2][0])


part1()
part2()
