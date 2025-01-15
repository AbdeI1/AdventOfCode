import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  W, H = 1000, 1000
  f = [[0 for _ in range(W)] for _ in range(H)]
  R = [(eval(l[l.find('@') + 2:l.find(':')]),
        eval(l[l.find(':') + 2:].replace('x', ','))) for l in reader()]
  for ((l, t), (w, h)) in R:
    for i in range(t, t + h):
      for j in range(l, l + w):
        f[i][j] += 1
  print(sum(len(list(filter(lambda c: c >= 2, r))) for r in f))


def part2():
  W, H = 1000, 1000
  f = [[0 for _ in range(W)] for _ in range(H)]
  R = [(eval(l[l.find('@') + 2:l.find(':')]),
        eval(l[l.find(':') + 2:].replace('x', ','))) for l in reader()]
  for ((l, t), (w, h)) in R:
    for i in range(t, t + h):
      for j in range(l, l + w):
        f[i][j] += 1
  for i, ((l, t), (w, h)) in enumerate(R):
    if sum([len(list(filter(lambda c: c >= 2, r[l:l + w]))) for r in f[t:t + h]]) == 0:
      print(i + 1)
      break


part1()
part2()
