import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  code = list(map(int, reader()[0].split(',')))
  code[1] = 12
  code[2] = 2
  for i in range(0, len(code), 4):
    op, i1, i2, i3 = code[i:i + 4]
    if op == 99:
      break
    elif op == 1:
      code[i3] = code[i1] + code[i2]
    elif op == 2:
      code[i3] = code[i1] * code[i2]
    else:
      print(f"Unknown opcode {op}")
  print(code[0])


def part2():
  init_code = list(map(int, reader()[0].split(',')))
  for noun in range(100):
    for verb in range(100):
      code = init_code.copy()
      code[1] = noun
      code[2] = verb
      for i in range(0, len(code), 4):
        op, i1, i2, i3 = code[i:i + 4]
        if op == 99:
          break
        elif op == 1:
          code[i3] = code[i1] + code[i2]
        elif op == 2:
          code[i3] = code[i1] * code[i2]
        else:
          print(f"Unknown opcode {op}")
          break
      if code[0] == 19690720:
        print(100 * noun + verb)


part1()
part2()
