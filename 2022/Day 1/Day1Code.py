import pathlib

def reader():
  f = open(f"{pathlib.Path(__file__).parent.resolve()}/Day1input.txt", 'r').read()
  f = f.split('\n')
  f = f[:-1]
  return f

def part1():
  f = reader()
  ans = -1
  s = 0
  for i in f:
    if i == '':
      ans = max(ans, s)
      s = 0
      continue
    s += int(i)
  print(ans)

def part2():
  f = reader()
  l = []
  s = 0
  for i in f:
    if i == '':
      l.append(s)
      s = 0
      continue
    s += int(i)
  l.sort()
  print(l[-1] + l[-2] + l[-3])

part1()
part2()
