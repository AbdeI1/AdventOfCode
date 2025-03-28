import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = [l.split() for l in reader()]
  s = list("abcdefgh")
  for l in f:
    if l[0] == "swap" and l[1] == "position":
      x, y = int(l[2]), int(l[5])
      s[x], s[y] = s[y], s[x]
    elif l[0] == "swap" and l[1] == "letter":
      x, y = l[2], l[5]
      i, j = s.index(x), s.index(y)
      s[i], s[j] = y, x
    elif l[0] == "rotate" and l[1] == "left":
      x = int(l[2]) % len(s)
      s = s[x:] + s[:x]
    elif l[0] == "rotate" and l[1] == "right":
      x = int(l[2]) % len(s)
      s = s[-x:] + s[:-x]
    elif l[0] == "rotate" and l[1] == "based":
      x = l[6]
      i = s.index(x)
      r = (1 + i + (1 if i >= 4 else 0)) % len(s)
      s = s[-r:] + s[:-r]
    elif l[0] == "reverse":
      x, y = int(l[2]), int(l[4])
      s = s[:x] + s[x:y + 1][::-1] + s[y + 1:]
    elif l[0] == "move":
      x, y = int(l[2]), int(l[5])
      ll = s.pop(x)
      s.insert(y, ll)
  print(''.join(s))


def part2():
  f = [l.split() for l in reader()]
  s = list("fbgdceah")
  for l in f[::-1]:
    if l[0] == "swap" and l[1] == "position":
      x, y = int(l[2]), int(l[5])
      s[x], s[y] = s[y], s[x]
    elif l[0] == "swap" and l[1] == "letter":
      x, y = l[2], l[5]
      i, j = s.index(x), s.index(y)
      s[i], s[j] = y, x
    elif l[0] == "rotate" and l[1] == "left":
      x = int(l[2]) % len(s)
      s = s[-x:] + s[:-x]
    elif l[0] == "rotate" and l[1] == "right":
      x = int(l[2]) % len(s)
      s = s[x:] + s[:x]
    elif l[0] == "rotate" and l[1] == "based":
      x = l[6]
      i = (s.index(x) - 1) % len(s)
      i = i // 2 + (4 if i % 2 == 1 else 0)
      r = (1 + i + (1 if i >= 4 else 0)) % len(s)
      s = s[r:] + s[:r]
    elif l[0] == "reverse":
      x, y = int(l[2]), int(l[4])
      s = s[:x] + s[x:y + 1][::-1] + s[y + 1:]
    elif l[0] == "move":
      x, y = int(l[2]), int(l[5])
      ll = s.pop(y)
      s.insert(x, ll)
  print(''.join(s))


part1()
part2()
