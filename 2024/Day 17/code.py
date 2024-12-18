import pathlib


def reader():
  return open(f"{pathlib.Path(__file__).parent.resolve()}/input.txt", 'r').read().split('\n')[:-1]


def simulate(program, A):
  l = [0, 1, 2, 3, A, 0, 0, -1]
  out = []
  i = 0
  while i < len(program):
    op = program[i]
    operand = program[i + 1]
    if op == 0:
      l[4] = int(l[4] / (2 ** l[operand]))
    elif op == 1:
      l[5] = l[5] ^ operand
    elif op == 2:
      l[5] = l[operand] % 8
    elif op == 3:
      if l[4] != 0:
        i = operand
        continue
    elif op == 4:
      l[5] = l[5] ^ l[6]
    elif op == 5:
      out.append(l[operand] % 8)
    elif op == 6:
      l[5] = int(l[4] / (2 ** l[operand]))
    elif op == 7:
      l[6] = int(l[4] / (2 ** l[operand]))
    i += 2
  return out


def part1():
  f = reader()
  program = list(map(int, f[4][(f[4].find(': ') + 2):].split(',')))
  print(
    ','.join(map(str, simulate(program, int(f[0][(f[0].find(': ') + 2):])))))


def part2():
  f = reader()
  program = list(map(int, f[4][(f[4].find(': ') + 2):].split(',')))

  S = set()

  xor1 = program[3]
  xor2 = program[7]

  def backtrack(A, j):
    if -j > len(program):
      S.add(A >> 3)
      return
    for i in range(8):
      s = (i ^ xor1)
      t = A | i | ((program[j] ^ xor1 ^ xor2 ^ i) << s)
      if simulate(program, t)[j:] == program[j:]:
        backtrack(t << 3, j - 1)
  backtrack(0, -1)

  print(min(S))


part1()
part2()
