import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  D = eval(reader()[0])

  def ssum(d):
    if type(d) is str:
      return 0
    if type(d) is int:
      return d
    if type(d) is list:
      return sum([ssum(i) for i in d])
    if type(d) is dict:
      return sum([ssum(v) for k, v in d.items()])

  print(ssum(D))


def part2():
  D = eval(reader()[0])

  def ssum(d):
    if type(d) is str:
      return 0
    if type(d) is int:
      return d
    if type(d) is list:
      return sum([ssum(i) for i in d])
    if type(d) is dict:
      x = 0
      for _, v in d.items():
        if v == 'red':
          return 0
        x += ssum(v)
      return x

  print(ssum(D))


part1()
part2()
