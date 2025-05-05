import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  print(sum(map(lambda t: 2 * t[0] * t[1] + 2 * t[1] * t[2] + 2 *
        t[0] * t[2] + min(t[0] * t[1], t[1] * t[2], t[0] * t[2]), (eval(l.replace('x', ',')) for l in reader()))))


def part2():
  print(sum(map(lambda t: 2 * min(t[0] + t[1], t[1] + t[2], t[0] + t[2]) +
        t[0] * t[1] * t[2], (eval(l.replace('x', ',')) for l in reader()))))


part1()
part2()
