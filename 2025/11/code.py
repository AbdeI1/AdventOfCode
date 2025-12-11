import os
os.chdir(os.path.dirname(__file__))
from functools import cache


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = {l[:l.find(':')]: l[l.find(':') + 2:].split() for l in reader()}
  
  @cache
  def count(l):
    if l == "out":
      return 1
    return sum(count(x) for x in f[l])
  
  print(count("you"))


def part2():
  f = {l[:l.find(':')]: l[l.find(':') + 2:].split() for l in reader()}
  
  @cache
  def count(l, vdac = False, vfft = False):
    if l == "out":
      return 1 if vdac and vfft else 0
    if l == "dac":
      vdac = True
    if l == "fft":
      vfft = True
    return sum(count(x, vdac, vfft) for x in f[l])
  
  print(count("svr"))


part1()
part2()
