from math import prod
from time import sleep
from collections import defaultdict


def compute(code: list[int], inp: list[int], out: list[int]):
  code = defaultdict(lambda: 0, {i: c for i, c in enumerate(code)})
  ip = 0
  rb = 0

  def index(i, m):
    if m == 0:
      return i
    elif m == 2:
      return i + rb
    else:
      return i

  def value(i, m):
    if m == 0:
      return code[i]
    elif m == 1:
      return i
    elif m == 2:
      return code[i + rb]
    else:
      return i

  while ip in range(len(code)):
    op = code[ip] % 100
    if op == 99:
      break
    mode = list(map(int, str(code[ip] // 100).zfill(3)))[::-1]
    if op == 1:
      code[index(code[ip + 3], mode[2])] = sum(value(code[ip + i + 1], mode[i])
                                               for i in range(2))
      ip += 4
    elif op == 2:
      code[index(code[ip + 3], mode[2])] = prod(value(code[ip + i + 1], mode[i])
                                                for i in range(2))
      ip += 4
    elif op == 3:
      while not inp:
        sleep(0)
      x = inp.pop(0)
      if x is None:
        break
      code[index(code[ip + 1], mode[0])] = x
      ip += 2
    elif op == 4:
      out.append(value(code[ip + 1], mode[0]))
      ip += 2
    elif op == 5:
      ip = value(code[ip + 2], mode[1]) if value(code[ip + 1],
                                                 mode[0]) != 0 else ip + 3
    elif op == 6:
      ip = value(code[ip + 2], mode[1]) if value(code[ip + 1],
                                                 mode[0]) == 0 else ip + 3
    elif op == 7:
      code[index(code[ip + 3], mode[2])] = 1 if value(code[ip + 1],
                                                      mode[0]) < value(code[ip + 2], mode[1]) else 0
      ip += 4
    elif op == 8:
      code[index(code[ip + 3], mode[2])] = 1 if value(code[ip + 1],
                                                      mode[0]) == value(code[ip + 2], mode[1]) else 0
      ip += 4
    elif op == 9:
      rb += value(code[ip + 1], mode[0])
      ip += 2
    else:
      print(f"Unknown opcode {op}")
      break
  return out
