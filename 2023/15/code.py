import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  print(sum([sum([(pow(17, len(s) - i, 256) * ord(c)) % 256 for i, c in enumerate(s)]) % 256
             for s in reader()[0].split(',')]))


def part2():
  f = reader()[0].split(',')

  def hash(s):
    return sum([(pow(17, len(s) - i, 256) * ord(c)) % 256 for i, c in enumerate(s)]) % 256

  m = {i: [] for i in range(256)}

  for op in f:
    if op[-1] == '-':
      s = op[:-1]
      h = hash(s)
      for i, (k, _) in enumerate(m[h]):
        if k == s:
          m[h].pop(i)
          break
    else:
      s, num = op.split('=')
      h = hash(s)
      n = int(num)
      for i, (k, _) in enumerate(m[h]):
        if k == s:
          m[h][i] = (s, n)
          break
      else:
        m[h].append((s, n))

  ans = 0

  for i, l in m.items():
    for j, (_, n) in enumerate(l):
      ans += (i + 1) * (j + 1) * n

  print(ans)


part1()
part2()
