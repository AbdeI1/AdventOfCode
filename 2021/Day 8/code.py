import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().split('\n')[:-1]


def part1():
  f = reader()
  sum = 0
  for l in f:
    ls = l.split('|')
    patterns = ls[0].split(' ')
    output = ls[1].split(' ')
    for o in output:
      if len(o) == 2 or len(o) == 4 or len(o) == 3 or len(o) == 7:
        sum += 1
  print(sum)


def getDigit(m):
  if m[0] == 1 and m[1] == 1 and m[2] == 1 and m[3] == 1 and m[4] == 1 and m[5] == 1 and m[6] == 1:
    return 8
  elif m[0] == 1 and m[1] == 1 and m[2] == 1 and m[4] == 1 and m[5] == 1 and m[6] == 1 and m[3] == 0:
    return 0
  elif m[0] == 1 and m[1] == 1 and m[3] == 1 and m[4] == 1 and m[5] == 1 and m[6] == 1 and m[2] == 0:
    return 6
  elif m[0] == 1 and m[1] == 1 and m[3] == 1 and m[2] == 1 and m[5] == 1 and m[6] == 1 and m[4] == 0:
    return 9
  elif m[0] == 1 and m[2] == 1 and m[3] == 1 and m[4] == 1 and m[6] == 1 and m[1] == 0 and m[5] == 0:
    return 2
  elif m[0] == 1 and m[2] == 1 and m[3] == 1 and m[5] == 1 and m[6] == 1 and m[1] == 0 and m[4] == 0:
    return 3
  elif m[0] == 1 and m[1] == 1 and m[3] == 1 and m[5] == 1 and m[6] == 1 and m[2] == 0 and m[4] == 0:
    return 5
  elif m[1] == 1 and m[2] == 1 and m[3] == 1 and m[5] == 1 and m[0] == 0 and m[4] == 0 and m[6] == 0:
    return 4
  elif m[0] == 1 and m[2] == 1 and m[5] == 1 and m[1] == 0 and m[3] == 0 and m[4] == 0 and m[6] == 0:
    return 7
  elif m[2] == 1 and m[5] == 1 and m[0] == 0 and m[1] == 0 and m[3] == 0 and m[4] == 0 and m[6] == 0:
    return 1
  else:
    return -1


def mapC(c):
  if c == 'a':
    return 0
  elif c == 'b':
    return 1
  elif c == 'c':
    return 2
  elif c == 'd':
    return 3
  elif c == 'e':
    return 4
  elif c == 'f':
    return 5
  else:
    return 6


def part2():
  f = reader()
  sum = 0
  for l in f:
    ls = l.split(' | ')
    patterns = ls[0].split(' ')
    output = ls[1].split(' ')
    m = [-1] * 7
    s = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
    one = ''
    seven = ''
    four = ''
    for p in patterns:
      if len(p) == 2:
        one = p
      if len(p) == 3:
        seven = p
      if len(p) == 4:
        four = p
    s = set()
    for c in seven:
      s.add(c)
    for c in one:
      s.remove(c)
      m[mapC(c)] = 25
    for n in s:
      m[mapC(n)] = 0
    for c in four:
      if m[mapC(c)] == -1:
        m[mapC(c)] = 13
    for i in range(7):
      if m[i] == -1:
        m[i] = 46
    for p in patterns:
      if len(p) == 6:
        su = 0
        for c in p:
          if m[mapC(c)] == 46:
            su += 1
        if su == 1:
          for c in p:
            if m[mapC(c)] == 46:
              m[mapC(c)] = 6
          break
    for i in range(7):
      if m[i] == 46:
        m[i] = 4
    for p in patterns:
      if len(p) == 6:
        su = 0
        for c in p:
          if m[mapC(c)] == 13:
            su += 1
        if su == 1:
          for c in p:
            if m[mapC(c)] == 13:
              m[mapC(c)] = 1
          break
    for i in range(7):
      if m[i] == 13:
        m[i] = 3
    for p in patterns:
      if len(p) == 6:
        su = 0
        for c in p:
          if m[mapC(c)] >= 10:
            su += 1
        if su == 1:
          for c in p:
            if m[mapC(c)] == 25:
              m[mapC(c)] = 5
          break
    for i in range(7):
      if m[i] == 25:
        m[i] = 2
    digits = []
    for o in output:
      ma = [0] * 7
      for c in o:
        ma[m[mapC(c)]] = 1
      digits.append(getDigit(ma))
    sum += digits[0] * 1000 + digits[1] * 100 + digits[2] * 10 + digits[3]
  print(sum)


part1()
part2()
