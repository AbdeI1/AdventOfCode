import pathlib


def reader():
  return open(f"{pathlib.Path(__file__).parent.resolve()}/input.txt", 'r').read().split('\n')[:-1]


def part1():
  n = list(map(int, reader()[0]))
  s = []
  c = 0
  i = 0
  j = len(n) - 1
  while i <= j:
    if i % 2 == 0:
      a = i // 2
      for _ in range(n[i]):
        s.append(a)
        c += 1
    else:
      ii = 0
      while i < j and ii < n[i]:
        if n[j] == 0 or j % 2 != 0:
          j -= 1
        else:
          a = j // 2
          s.append(a)
          c += 1
          n[j] -= 1
          ii += 1
    i += 1
  print(sum(i * n for i, n in enumerate(s)))


def part2():
  n = list(map(int, reader()[0]))
  gaps = [n[i] for i in range(1, len(n), 2)]
  f = [[] for _ in range(len(gaps))]
  for i in range(len(n) - 1, 0, -2):
    a = i // 2
    s = n[i]
    try:
      j = next(j for j, g in enumerate(gaps) if g >= s and 2 * j + 1 < i)
      gaps[j] -= s
      n[i] = -n[i]
      f[j].extend([a] * s)
    except:
      pass
  s = []
  for i in range(0, len(n), 2):
    if n[i] >= 0:
      s.extend([i // 2] * n[i])
    else:
      s.extend([0] * -n[i])
    if i < len(n) - 1:
      s.extend(f[i // 2] + [0] * gaps[i // 2])
  print(sum(i * n for i, n in enumerate(s)))


part1()
part2()
