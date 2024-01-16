import pathlib

def reader():
  f = open(f"{pathlib.Path(__file__).parent.resolve()}/input.txt", 'r').read()
  f = f.split('\n')
  f = f[:-1]
  return f

class RangeMap:
  def __init__(self):
    self.ranges = []

  def __setitem__(self, key, value):
    self.ranges.append((key, value))

  def __getitem__(self, key):
    if isinstance(key, int):
      for r, v in self.ranges:
        if key in r:
          return v
      return 0
    if isinstance(key, list):
      res = []
      for r, v in self.ranges:
      return res

def part1():
  f = '\n'.join(reader()).split('\n\n')
  seeds = list(map(int, f[0][f[0].find(':')+2:].split(" ")))
  maps = []
  for m in f[1:]:
    r = RangeMap()
    for l in m.split('\n')[1:]:
      nums =  list(map(int, l.split(" ")))
      r[range(nums[1], nums[1] + nums[2])] = nums[0] - nums[1]
    maps.append(r)
  ans = float('inf')
  for s in seeds:
    n = s
    for m in maps:
      n = n + m[n]
    ans = min(ans, n)
  print(ans)
  

def part2():
  f = '\n'.join(reader()).split('\n\n')
  seeds = list(map(int, f[0][f[0].find(':')+2:].split(" ")))
  maps = []
  for m in f[1:]:
    r = RangeMap()
    for l in m.split('\n')[1:]:
      nums =  list(map(int, l.split(" ")))
      r[range(nums[1], nums[1] + nums[2])] = nums[0] - nums[1]
    maps.append(r)
  ans = float('inf')
  for s in seeds:
    n = s
    for m in maps:
      n = n + m[n]
    ans = min(ans, n)
  print(ans)

part1()
part2()
