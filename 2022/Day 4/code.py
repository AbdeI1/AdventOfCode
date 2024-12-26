import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().split('\n')[:-1]


def part1():
  f = reader()
  ans = 0
  for l in f:
    a = l.split(',')
    ass1 = list(map(int, list(a[0].split('-'))))
    ass2 = list(map(int, list(a[1].split('-'))))
    if ass1[0] <= ass2[0] and ass1[1] >= ass2[1]:
      ans += 1
    elif ass2[0] <= ass1[0] and ass2[1] >= ass1[1]:
      ans += 1
  print(ans)


def part2():
  f = reader()
  ans = 0
  for l in f:
    a = l.split(',')
    ass1 = list(map(int, list(a[0].split('-'))))
    ass2 = list(map(int, list(a[1].split('-'))))
    if ass1[0] > ass2[0]:
      ass1, ass2 = ass2, ass1
    if ass1[1] >= ass2[0]:
      ans += 1
  print(ans)


part1()
part2()
