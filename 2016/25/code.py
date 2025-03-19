import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  B = int(f[1].split()[1])
  C = int(f[2].split()[1])
  s1 = f"{B * C:0b}"
  s2 = "10" * (len(s1) // 2)
  if (int(s1, 2) >= int(s2, 2)):
    s2 += "10"
  print(int(s2, 2) - int(s1, 2))


def part2():
  pass


part1()
part2()
