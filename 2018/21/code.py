import os
os.chdir(os.path.dirname(__file__))


def addr(R, A, B, C):
  R[C] = R[A] + R[B]


def addi(R, A, B, C):
  R[C] = R[A] + B


def mulr(R, A, B, C):
  R[C] = R[A] * R[B]


def muli(R, A, B, C):
  R[C] = R[A] * B


def banr(R, A, B, C):
  R[C] = R[A] & R[B]


def bani(R, A, B, C):
  R[C] = R[A] & B


def borr(R, A, B, C):
  R[C] = R[A] | R[B]


def bori(R, A, B, C):
  R[C] = R[A] | B


def setr(R, A, B, C):
  R[C] = R[A]


def seti(R, A, B, C):
  R[C] = A


def gtir(R, A, B, C):
  R[C] = 1 if A > R[B] else 0


def gtri(R, A, B, C):
  R[C] = 1 if R[A] > B else 0


def gtrr(R, A, B, C):
  R[C] = 1 if R[A] > R[B] else 0


def eqir(R, A, B, C):
  R[C] = 1 if A == R[B] else 0


def eqri(R, A, B, C):
  R[C] = 1 if R[A] == B else 0


def eqrr(R, A, B, C):
  R[C] = 1 if R[A] == R[B] else 0


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = [[l.split()[0]] + list(map(int, l.split()[1:])) for l in reader()]
  ip = int(f[0][1])
  f = f[1:]
  R = [0 for _ in range(6)]
  while R[ip] < len(f):
    if R[ip] == 30:
      break
    op, A, B, C = f[R[ip]]
    eval(op)(R, A, B, C)
    R[ip] += 1
  print(max(R))


def part2():
  f = [[l.split()[0]] + list(map(int, l.split()[1:])) for l in reader()]
  f = f[1:]

  # while R[ip] < len(f):
  #   op, A, B, C = f[R[ip]]
  #   eval(op)(R, A, B, C)
  #   R[ip] += 1

  x1, x2 = f[7][1], max(f[11][1:3])

  n = 0
  L = []
  G = set()
  while n not in G:
    G.add(n)
    L.append(n)
    a = n | (1 << 16)
    n = x1
    while (a > 0):
      n = (((n + (a & 255)) & 16777215) * x2) & 16777215
      a >>= 8

  print(L[-1])


part1()
part2()

# A B C D E ip
# C = 123
# C &= 456
# C = (C == 72)
# ip += C
# ip = 0
# C = 9
# B = C | 65536
# C = 1250634
# E = B & 255
# C += E
# C &= 16777215
# C *= 65899
# C &= 16777215
# E = (256 > B)
# ip += E
# ip += 1
# ip = 27
# E = 0
# D = E + 1
# D *= 256
# D = (D > B)
# ip += D
# ip += 1
# ip = 25
# E += 1
# ip = 17
# B = E
# ip = 7
# E = (A == C)
# ip += E
# ip = 5
