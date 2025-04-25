import os
os.chdir(os.path.dirname(__file__))
from re import findall


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  ans = 0
  for l in reader():
    s, f = 0, False
    for i in range(len(l) - 3):
      if l[i] == '[':
        f = True
      elif l[i] == ']':
        f = False
      elif l[i] != l[i + 1] and l[i] == l[i + 3] and l[i + 1] == l[i + 2]:
        if f:
          s = 0
          break
        else:
          s = 1
    ans += s
  print(ans)


def part2():
  ans = 0
  for l in reader():
    h = findall(r'\[\w+\]', l)
    for t in h:
      l = l.replace(t, '||')
    h = ''.join(h)
    for i in range(len(l) - 2):
      if l[i] == l[i + 2] and l[i] != l[i + 1] and f'{l[i+1]}{l[i]}{l[i+1]}' in h:
        ans += 1
        break
  print(ans)


part1()
part2()
