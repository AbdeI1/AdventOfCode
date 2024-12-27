import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  ans = 0
  for l in f:
    s = list(filter(str.isdigit, l))
    ans += int(s[0] + s[-1])
  print(ans)


def part2():
  digits = {
    "one": 1, "1": 1,
    "two": 2, "2": 2,
    "three": 3, "3": 3,
    "four": 4, "4": 4,
    "five": 5, "5": 5,
    "six": 6, "6": 6,
    "seven": 7, "7": 7,
    "eight": 8, "8": 8,
    "nine": 9, "9": 9
  }
  f = reader()
  ans = 0
  for l in f:
    first, last = len(l), -1
    fk, lk = None, None
    for d in digits:
      i = l.find(d)
      if i != -1:
        if i < first:
          first = i
          fk = d
        i = l.rfind(d)
        if i > last:
          last = i
          lk = d
    ans += 10 * digits[fk] + digits[lk]
  print(ans)


part1()
part2()
