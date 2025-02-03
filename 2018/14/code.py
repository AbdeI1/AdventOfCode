import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  n = int(reader()[0])
  r = [3, 7]
  i1, i2 = 0, 1
  while len(r) < n + 10:
    r.extend(map(int, str(r[i1] + r[i2])))
    i1 = (i1 + r[i1] + 1) % len(r)
    i2 = (i2 + r[i2] + 1) % len(r)
  print(''.join(map(str, r[n:n + 10])))


def part2():
  n = int(reader()[0])
  r = [3, 7]
  i1, i2 = 0, 1
  while True:
    r.extend(map(int, str(r[i1] + r[i2])))
    i1 = (i1 + r[i1] + 1) % len(r)
    i2 = (i2 + r[i2] + 1) % len(r)
    if int(''.join(map(str, r[-6:]))) == n:
      print(len(r) - 6)
      break
    if int(''.join(map(str, r[-7:-1]))) == n:
      print(len(r) - 7)
      break


part1()
part2()
