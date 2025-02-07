import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


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


def part1():
  f = [[l.split()[0]] + list(map(int, l.split()[1:])) for l in reader()]
  ip = int(f[0][1])
  f = f[1:]
  R = [0 for _ in range(6)]
  while R[ip] < len(f):
    op, A, B, C = f[R[ip]]
    eval(op)(R, A, B, C)
    R[ip] += 1
  print(R[0])


def part2():
  f = [[l.split()[0]] + list(map(int, l.split()[1:])) for l in reader()]
  ip = int(f[0][1])
  f = f[1:]
  R = [0 for _ in range(6)]
  R[0] = 1
  while R[ip] != 1:
    op, A, B, C = f[R[ip]]
    eval(op)(R, A, B, C)
    R[ip] += 1
  N = max(R)
  print(sum([i for i in range(1, N + 1) if N % i == 0]))


part1()
part2()
