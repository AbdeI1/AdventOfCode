import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().split('\n')[:-1]


D = {
  "4": 4,
  "3": 3,
  "2": 2,
  "1": 1,
  "0": 0,
  "-": -1,
  "=": -2
}

ᗡ = {v: k for k, v in D.items()}


def SNAFUToDec(s):
  ans = 0
  b = 1
  for i in range(1, len(s) + 1):
    ans += b * D[s[-i]]
    b *= 5
  return ans


def DecToSNAFU(x):
  s = ""
  while x:
    s = str(x % 5) + s
    x //= 5
  a = list(s)
  i = 0
  while i < len(a):
    while i >= 0 and (a[i] == "3" or a[i] == "4"):
      a[i - 1] = ᗡ[D[a[i - 1]] + 1]
      a[i] = ᗡ[D[a[i]] - 5]
      i -= 1
    i += 1
  return "".join(a)


def part1():
  f = reader()
  x = 0
  for l in f:
    x += SNAFUToDec(l)
  print(DecToSNAFU(x))


part1()
