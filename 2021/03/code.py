import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().split('\n')[:-1]


def part1():
  f = reader()
  eps = ""
  gam = ""
  for i in range(12):
    c0 = 0
    c1 = 0
    for l in f:
      if l[i] == "1":
        c1 += 1
      else:
        c0 += 1
    if c0 > c1:
      gam += "0"
      eps += "1"
    else:
      gam += "1"
      eps += "0"
  print(int(gam, 2) * int(eps, 2))


def part2():
  f = reader()
  oxy = f.copy()
  co2 = f.copy()
  for i in range(12):
    c0 = 0
    c1 = 0
    for l in oxy:
      if l[i] == "1":
        c1 += 1
      else:
        c0 += 1
    if len(oxy) > 1:
      if c0 > c1:
        oxy = list(filter(lambda x: x[i] == '0', oxy))
      else:
        oxy = list(filter(lambda x: x[i] == '1', oxy))
    c0 = 0
    c1 = 0
    for l in co2:
      if l[i] == "1":
        c1 += 1
      else:
        c0 += 1
    if len(co2) > 1:
      if c0 > c1:
        co2 = list(filter(lambda x: x[i] == '1', co2))
      else:
        co2 = list(filter(lambda x: x[i] == '0', co2))
  print(int(oxy[0], 2) * int(co2[0], 2))


part1()
part2()
