import pathlib

def reader():
  f = open(f"{pathlib.Path(__file__).parent.resolve()}/Day11input.txt", 'r').read()
  f += '\n'
  f = f.split('\n\n')
  f = f[:-1]
  return f

class Monkey:
  def __init__(self, desc):
    f = desc.split('\n')
    self.items = eval("[" + f[1].split("Starting items: ")[1] + "]")
    def op(x):
      return eval(f[2].split("new = ")[1], {"old": x})
    self.op = op
    def test(x):
      if x % int(f[3].split("divisible by ")[1]) == 0:
        return int(f[4].split("monkey ")[1])
      return int(f[5].split("monkey ")[1])
    self.test = test

def part1():
  f = reader()
  M = list(map(Monkey, f))
  inspects = [0 for _ in range(8)]
  for _ in range(20):
    for i in range(len(M)):
      m = M[i]
      inspects[i] += len(m.items)
      while len(m.items):
        item = m.items.pop(0)
        item = m.op(item)
        item //= 3
        M[m.test(item)].items.append(item)
  print(sorted(inspects)[-1]*sorted(inspects)[-2])

def part2():
  f = reader()
  base = 1
  for l in f:
    base *= int(l.split("divisible by ")[1].split("\n")[0])
  M = list(map(Monkey, f))
  inspects = [0 for _ in range(8)]
  for _ in range(10000):
    for i in range(len(M)):
      m = M[i]
      inspects[i] += len(m.items)
      while len(m.items):
        item = m.items.pop(0)
        item = m.op(item)
        item %= base
        M[m.test(item)].items.append(item)
  print(sorted(inspects)[-1]*sorted(inspects)[-2])

part1()
part2()
