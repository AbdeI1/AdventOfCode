import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


D = {
  'A': 0,
  'B': 1,
  'C': 2,
  'X': 1,
  'Y': 2,
  'Z': 3
}


def part1():
  f = reader()
  ans = 0
  for l in f:
    a = l.split(' ')
    ans += D[a[1]]
    if (D[a[0]] + 1) % 3 == (D[a[1]] - 1):
      ans += 6
    elif D[a[0]] == (D[a[1]] - 1):
      ans += 3
  print(ans)


def part2():
  f = reader()
  ans = 0
  for l in f:
    a = l.split(' ')
    if a[1] == 'X':
      ans += (D[a[0]] + 2) % 3 + 1
    elif a[1] == 'Y':
      ans += D[a[0]] + 1 + 3
    else:
      ans += (D[a[0]] + 1) % 3 + 1 + 6
  print(ans)


part1()
part2()
