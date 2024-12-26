import os
os.chdir(os.path.dirname(__file__))
from functools import cmp_to_key


def reader():
  return open(f"input.txt", 'r').read().split('\n')[:-1]


def compare(l1, l2):
  if isinstance(l1, int) and isinstance(l2, int):
    if l1 < l2:
      return -1
    if l2 < l1:
      return 1
    return 0
  elif isinstance(l1, list) and isinstance(l2, list):
    i = 0
    while True:
      if i == len(l1):
        if i == len(l2):
          return 0
        return -1
      if i == len(l2):
        return 1
      j = compare(l1[i], l2[i])
      if j != 0:
        return j
      i += 1
  else:
    if isinstance(l1, int):
      return compare([l1], l2)
    else:
      return compare(l1, [l2])


def part1():
  f = '\n'.join(reader()).split('\n\n')
  ans = 0
  i = 1
  for p in f:
    p = p.split('\n')
    l1 = eval(p[0])
    l2 = eval(p[1])
    if compare(l1, l2) < 0:
      ans += i
    i += 1
  print(ans)


def part2():
  f = '\n'.join(reader()).split('\n\n')
  packets = []
  for p in f:
    packets += list(map(eval, p.split('\n')))
  packets += [[[2]], [[6]]]
  packets.sort(key=cmp_to_key(compare))
  ans = 1
  for i in range(len(packets)):
    if packets[i] == [[2]] or packets[i] == [[6]]:
      ans *= (i + 1)
  print(ans)


part1()
part2()
