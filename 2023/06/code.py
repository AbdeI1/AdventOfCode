import os
os.chdir(os.path.dirname(__file__))
import math


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  times = list(map(int, f[0].split()[1:]))
  dists = list(map(int, f[1].split()[1:]))
  # -dist  + xt - x^2 = 0 => x = t +- sqrt(t^2 - 4*dist)/2
  ans = 1
  for i in range(len(times)):
    t = times[i]
    d = dists[i]
    disc = t * t - 4 * d
    sqrt = math.sqrt(disc)
    mi = math.floor(((t - sqrt) / 2) + 1)
    ma = math.ceil(((t + sqrt) / 2) - 1)
    ans *= (ma - mi + 1)
  print(ans)


def part2():
  f = reader()
  t = int(''.join(f[0].split()[1:]))
  d = int(''.join(f[1].split()[1:]))
  disc = t * t - 4 * d
  sqrt = math.sqrt(disc)
  mi = math.floor(((t - sqrt) / 2) + 1)
  ma = math.ceil(((t + sqrt) / 2) - 1)
  print(ma - mi + 1)


part1()
part2()
