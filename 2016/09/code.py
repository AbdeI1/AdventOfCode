import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  s = reader()[0]
  d = ""
  i = 0
  while i in range(len(s)):
    if s[i] == '(':
      j = s.find(')', i)
      l, m = map(int, s[i + 1:j].split('x'))
      d += s[j + 1:j + 1 + l] * m
      i = j + l
    else:
      d += s[i]
    i += 1
  print(len(d))


def part2():
  s = reader()[0]

  def L(i, j):
    if i >= j:
      return 0
    if s[i] == '(':
      ii = s.find(')', i)
      l, m = map(int, s[i + 1:ii].split('x'))
      return L(ii + 1, ii + l + 1) * m + L(ii + l + 1, j)
    return 1 + L(i + 1, j)

  print(L(0, len(s)))


part1()
part2()
