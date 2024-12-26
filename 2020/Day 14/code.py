import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().split('\n')[:-1]


def part1():
  f = reader()
  d = {}
  mask = ""
  for s in f:
    if s[0:3] == "mas":
      mask = s[s.index('=') + 2:]
    elif s[0:3] == "mem":
      key = s[s.index('[') + 1: s.index(']')]
      value = bin(int(s[s.index('=') + 2:]))[2:]
      value = binStringToArray(value)
      maskValue = []
      i = 0
      while i < len(mask):
        if mask[i] == '0':
          maskValue.append(0)
        elif mask[i] == '1':
          maskValue.append(1)
        elif mask[i] == 'X':
          maskValue.append(value[i])
        i += 1
      maskValue = binArrayToString(maskValue)
      d[key] = maskValue
  sum = 0
  for x in d:
    sum += int(d[x], 2)
  print(sum)


def part2():
  f = reader()
  d = {}
  mask = ""
  for s in f:
    if s[0:3] == "mas":
      mask = s[s.index('=') + 2:]
    elif s[0:3] == "mem":
      key = bin(int(s[s.index('[') + 1: s.index(']')]))[2:]
      key = binStringToArray(key)
      value = int(s[s.index('=') + 2:])
      keysNum = 1
      maskKey = []
      i = 0
      while i < len(mask):
        if mask[i] == '0':
          maskKey.append(key[i])
        elif mask[i] == '1':
          maskKey.append(1)
        elif mask[i] == 'X':
          maskKey.append('X')
          keysNum *= 2
        i += 1
      keys = [0] * keysNum
      i = 0
      while i < keysNum:
        bString = format(i, "0" + str(len(bin(keysNum)[2:]) - 1) + "b")
        keys[i] = []
        j = 0
        k = 0
        while j < len(maskKey):
          if maskKey[j] == 0:
            keys[i].append(0)
          elif maskKey[j] == 1:
            keys[i].append(1)
          elif maskKey[j] == 'X':
            keys[i].append(int(bString[k]))
            k += 1
          j += 1
        keys[i] = binArrayToString(keys[i])
        i += 1
      for k in keys:
        d[k] = value
  sum = 0
  for x in d:
    sum += d[x]
  print(sum)


def binStringToArray(s):
  a = []
  i = 36
  while i > len(s):
    a.append(0)
    i -= 1
  for c in s:
    a.append(int(c))
  return a


def binArrayToString(a):
  s = ""
  for i in a:
    s = s + str(i)
  return s


part1()
part2()
