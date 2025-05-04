import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = [sorted(map(int, l.split())) for l in reader()]
  print(len([z for x, y, z in f if x + y > z]))


def part2():
  f = reader()
  T = [sorted(map(int, (f[i:i + 3][k].split()[j] for k in range(3))))
       for i in range(0, len(f), 3) for j in range(3)]
  print(len([z for x, y, z in T if x + y > z]))


part1()
part2()
