import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  n1, n2 = map(int, reader()[0].split('-'))
  c = 0
  for n in range(n1, n2 + 1):
    s = str(n)
    if s != ''.join(sorted(s)):
      continue
    if len(set(s)) == len(s):
      continue
    c += 1
  print(c)


def part2():
  n1, n2 = map(int, reader()[0].split('-'))
  c = 0
  for n in range(n1, n2 + 1):
    s = str(n)
    if s != ''.join(sorted(s)):
      continue
    if 2 not in [s.count(d) for d in s]:
      continue
    c += 1
  print(c)


part1()
part2()
