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


OPs = [addr, addi, mulr, muli, banr, bani, borr, bori,
       setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]


def part1():
  f, p = '\n'.join(reader()).split('\n\n\n\n')
  f = [(lambda a, b, c: [tuple(eval(a[a.find(': ') + 2:])), tuple(map(int, b.split())),
        tuple(eval(c[c.find(': ') + 2:]))])(*s.splitlines()) for s in f.split('\n\n')]
  p = [tuple(map(int, l.split())) for l in p.splitlines()]
  t = 0
  for b, (_, A, B, C), a in f:
    c = 0
    for op in OPs:
      R = list(b)
      op(R, A, B, C)
      if tuple(R) == a:
        c += 1
    if c >= 3:
      t += 1
  print(t)


def part2():
  global OPs
  f, p = '\n'.join(reader()).split('\n\n\n\n')
  f = [(lambda a, b, c: [tuple(eval(a[a.find(': ') + 2:])), tuple(map(int, b.split())),
        tuple(eval(c[c.find(': ') + 2:]))])(*s.splitlines()) for s in f.split('\n\n')]
  p = [tuple(map(int, l.split())) for l in p.splitlines()]
  M = [set(range(16)) for _ in range(16)]
  for b, (o, A, B, C), a in f:
    c = 0
    for i, op in enumerate(OPs):
      R = list(b)
      op(R, A, B, C)
      if tuple(R) != a:
        M[o].discard(i)
  while any(len(s) > 1 for s in M):
    for i, s in enumerate(M):
      if len(s) == 1:
        for j, t in enumerate(M):
          if i != j:
            t -= s
  OPs = [OPs[list(i)[0]] for i in M]
  R = [0, 0, 0, 0]
  for o, A, B, C in p:
    OPs[o](R, A, B, C)
  print(R[0])


part1()
part2()
