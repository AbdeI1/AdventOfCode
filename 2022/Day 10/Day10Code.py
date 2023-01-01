import pathlib

def reader():
  f = open(f"{pathlib.Path(__file__).parent.resolve()}/Day10input.txt", 'r').read()
  f = f.split('\n')
  f = f[:-1]
  return f

def part1():
  f = reader()
  c = 0 
  x = 1
  signals = []
  def inc():
    nonlocal c
    c += 1
    if c%40 == 20:
      signals.append(c*x)
  for l in f:
    ins = l.split()
    if ins[0] == "noop":
      inc()
    elif ins[0] == "addx":
      inc()
      inc()
      x += int(ins[1])
  print(sum(signals))

def part2():
  f = reader()
  c = -1
  x = 1
  pic = [['  ' for _ in range(40)] for _ in range(6)]
  def inc():
    nonlocal c
    c += 1
    if abs(x - c%40) <= 1:
      pic[c//40][c%40] = '██'
  for l in f:
    ins = l.split()
    if ins[0] == "noop":
      inc()
    elif ins[0] == "addx":
      inc()
      inc()
      x += int(ins[1])
  s = ""
  for i in pic:
    for j in i:
      s += j
    s += '\n'
  print(s)

part1()
part2()
