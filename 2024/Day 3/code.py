import pathlib
import math
import re


def reader():
  return open(f"{pathlib.Path(__file__).parent.resolve()}/input.txt", 'r').read().split('\n')[:-1]


def part1():
  print(sum(math.prod(map(int, m[4:-1].split(',')))
        for m in re.findall(r'mul\(\d{1,3},\d{1,3}\)', ''.join(reader()))))


def part2():
  print((lambda c: sum(math.prod(map(int, m[4:-1].split(','))) * c if m[0] == 'm' else 0 * (c := 1 if m == "do()" else 0) for m in re.findall(
    r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', ''.join(reader()))))(1))


part1()
part2()
