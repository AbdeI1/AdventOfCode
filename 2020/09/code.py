import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  i = 0
  while i < len(f):
    f[i] = int(f[i])
    i += 1
  i = 25
  while i < len(f):
    a = f[i - 25: i]
    if not checkSum(a, f[i]):
      print(f[i])
    i += 1


def checkSum(a, x):
  i = 0
  while i < len(a):
    first = a[i]
    j = i + 1
    while j < len(a):
      second = a[j]
      if first != second and first + second == x:
        return True
      j += 1
    i += 1
  return False


def part2():
  f = reader()
  i = 0
  invalidNum = 393911906
  while i < len(f):
    f[i] = int(f[i])
    i += 1
  i = 0
  while i < len(f):
    sum = 0
    a = []
    j = i
    while sum < invalidNum:
      sum += f[j]
      a.append(f[j])
      j += 1
    if sum == invalidNum and len(a) > 1:
      print(min(a) + max(a))
    i += 1


part1()
part2()
