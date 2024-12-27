import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().split('\n')[:-1]


def part1():
  f = reader()
  ans = 0
  for l in f:
    n = len(l)
    s1 = l[:n // 2]
    s2 = l[n // 2:]
    c = set(list(s1)).intersection(set(list(s2)))
    i = ord(list(c)[0])
    if i > 96:
      ans += i - 96
    else:
      ans += i - 64 + 26
  print(ans)


def part2():
  f = reader()
  ans = 0
  i = 0
  s = set()
  for l in f:
    if i % 3 == 0:
      if i != 0:
        c = ord(list(s)[0])
        if c > 96:
          ans += c - 96
        else:
          ans += c - 64 + 26
      s = set(list(l))
    else:
      s = s.intersection(set(list(l)))
    i += 1
  c = ord(list(s)[0])
  if c > 96:
    ans += c - 96
  else:
    ans += c - 64 + 26
  print(ans)


part1()
part2()
