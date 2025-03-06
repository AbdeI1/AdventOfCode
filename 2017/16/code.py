import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()[0].split(',')
  A = [chr(ord('a') + i) for i in range(16)]
  P = {c: i for i, c in enumerate(A)}
  for i in f:
    match i[0]:
      case 's':
        x = int(i[1:])
        A = A[-x:] + A[:-x]
        P = {c: i for i, c in enumerate(A)}
      case 'x':
        a, b = map(int, i[1:].split("/"))
        A[a], A[b] = A[b], A[a]
        P[A[a]] = a
        P[A[b]] = b
      case 'p':
        a, b = i[1:].split("/")
        P[a], P[b] = P[b], P[a]
        A[P[a]] = a
        A[P[b]] = b
  print(''.join(A))


def part2():
  f = reader()[0].split(',')
  A = [chr(ord('a') + i) for i in range(16)]
  P = {c: i for i, c in enumerate(A)}
  S = {}
  k = 0
  while ''.join(A) not in S:
    S[''.join(A)] = k
    for i in f:
      match i[0]:
        case 's':
          x = int(i[1:])
          A = A[-x:] + A[:-x]
          P = {c: i for i, c in enumerate(A)}
        case 'x':
          a, b = map(int, i[1:].split("/"))
          A[a], A[b] = A[b], A[a]
          P[A[a]] = a
          P[A[b]] = b
        case 'p':
          a, b = i[1:].split("/")
          P[a], P[b] = P[b], P[a]
          A[P[a]] = a
          A[P[b]] = b
    k += 1
  D = S[''.join(A)]
  M = k - D
  t = D + (1000000000 % M)
  print({i: s for s, i in S.items()}[t])


part1()
part2()
