import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  S = reader()
  v = 0
  i = 1
  M = 10007
  for s in S:
    if s.startswith('deal with increment'):
      i = (i * pow(int(s[s.rfind(' ') + 1:]), -1, M)) % M
    elif s.startswith('cut'):
      v = (v + int(s[s.rfind(' ') + 1:]) * i) % M
    elif s.startswith('deal into new stack'):
      i = -i % M
      v = (v + i) % M
    else:
      print(s)
  print((((2019 - v) % M) * pow(i, -1, M)) % M)


def part2():
  S = reader()
  v = 0
  i = 1
  M = 119315717514047
  I = 101741582076661
  for s in S:
    if s.startswith('deal with increment'):
      i = (i * pow(int(s[s.rfind(' ') + 1:]), -1, M)) % M
    elif s.startswith('cut'):
      v = (v + int(s[s.rfind(' ') + 1:]) * i) % M
    elif s.startswith('deal into new stack'):
      i = -i % M
      v = (v + i) % M
    else:
      print(s)
  v = (v * (pow(i, I, M) - 1) * pow(i - 1, -1, M)) % M
  i = pow(i, I, M)
  print((v + 2020 * i) % M)


part1()
part2()
