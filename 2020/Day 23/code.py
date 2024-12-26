def part1():
  input = "418976235"
  f = list(map(lambda x: int(x), list(input)))
  cc = 0
  for i in range(100):
    label = f[cc]
    temps = []
    for i in range(3):
      if cc == len(f) - 1:
        temps.append(f[0])
        del f[0]
        cc = len(f) - 1
      else:
        temps.append(f[cc + 1])
        del f[cc + 1]
    dc = f[cc] - 1
    while dc not in f:
      if dc == 0:
        dc = 9
      else:
        dc -= 1
    f = f[:f.index(dc) + 1] + temps + f[f.index(dc) + 1 :]
    cc = (f.index(label) + 1)%len(f)
  answer = ""
  cc = f.index(1)
  while len(answer) < 9:
    answer += str(f[cc])
    cc = (cc + 1)%len(f)
  print(answer[1:])

def part2():
  input = "418976235"
  f = list(map(lambda x: int(x), list(input)))
  a = [(-1, -1) for _ in range(1000001)]
  a[f[0]] = (1000000, f[1])
  for i in range(1, len(f)-1):
    a[f[i]] = (f[i-1], f[i+1])
  a[f[-1]] = (f[-2], 10)
  a[10] = (f[-1], 11)
  for i in range(11, 1000001):
    a[i] = (i-1, i+1)
  a[1000000] = (999999, f[0])
  i = f[0]
  for _ in range(10000000):
    l = i-1
    if l <= 0:
      l = 1000000
    n1 = a[i][1]
    n2 = a[n1][1]
    n3 = a[n2][1]
    a[i] = (a[i][0], a[n3][1])
    s = (n1, n2, n3)
    while l in s:
      l -= 1
      if l <= 0:
        l = 1000000
    n = a[l][1]
    a[l] = (a[l][0], n1)
    a[n1] = (l, n2)
    a[n3] = (n2, n)
    i = a[i][1]
  print(a[1][1]*a[a[1][1]][1])

part1()
part2()
