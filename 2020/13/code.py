import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  f[1] = f[1].split(',')
  n = int(f[0])
  m = 0
  i = 0
  for x in f[1]:
    if x != 'x':
      if max(m, n % int(x)) != m:
        m = n % int(x)
        i = int(x)
  print(i * (i - m))


def part2():
  f = reader()
  f = f[1].split(',')
  i = 0
  while i < len(f):
    if f[i] == 'x':
      f[i] = 0
    else:
      f[i] = int(f[i])
    i += 1
  t = []
  for x in f:
    if x != 0:
      t.append((x, f.index(x)))
  time = 0
  i = 0
  iterator = 1
  while i < len(t):
    time += iterator
    if (time + t[i][1]) % t[i][0] == 0:
      iterator *= t[i][0]
      i += 1
  print(time)


part1()
part2()
