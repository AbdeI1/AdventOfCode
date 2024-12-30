from math import prod
from time import sleep


def compute(code: list[int], inp: list[int], out: list[int]):
  ip = 0
  def value(i, m): return code[i] if m == 0 else i
  while ip in range(len(code)):
    op = code[ip] % 100
    if op == 99:
      break
    mode = list(map(int, str(code[ip] // 100).zfill(3)))[::-1]
    if op == 1:
      code[code[ip + 3]] = sum(value(code[ip + i + 1], mode[i])
                               for i in range(2))
      ip += 4
    elif op == 2:
      code[code[ip + 3]] = prod(value(code[ip + i + 1], mode[i])
                                for i in range(2))
      ip += 4
    elif op == 3:
      while not inp:
        sleep(0.1)
      x = inp.pop(0)
      if x is None:
        break
      code[code[ip + 1]] = x
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
      code[code[ip + 3]] = 1 if value(code[ip + 1],
                                      mode[0]) < value(code[ip + 2], mode[1]) else 0
      ip += 4
    elif op == 8:
      code[code[ip + 3]] = 1 if value(code[ip + 1],
                                      mode[0]) == value(code[ip + 2], mode[1]) else 0
      ip += 4
    else:
      print(f"Unknown opcode {op}")
      break
  return out
