import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


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
      for r2 in key:
        ints = []
        for r1, v in self.ranges:
          start = max(r1.start, r2.start)
          stop = min(r1.stop, r2.stop)
          if stop > start:
            ints.append(range(start, stop))
            res.append(range(start + v, stop + v))
        ints.sort(key=lambda r: r.start)
        start = r2.start
        for i in ints:
          if i.start > start:
            res.append(range(start, i.start))
          start = i.stop
        if r2.stop > start:
          res.append(range(start, r2.stop))
      return sorted(res, key=lambda r: r.start)


def part1():
  f = '\n'.join(reader()).split('\n\n')
  seeds = list(map(int, f[0][f[0].find(':') + 2:].split(" ")))
  maps = []
  for m in f[1:]:
    r = RangeMap()
    for l in m.split('\n')[1:]:
      nums = list(map(int, l.split(" ")))
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
  seeds = list(map(int, f[0][f[0].find(':') + 2:].split(" ")))
  maps = []
  for m in f[1:]:
    r = RangeMap()
    for l in m.split('\n')[1:]:
      nums = list(map(int, l.split(" ")))
      r[range(nums[1], nums[1] + nums[2])] = nums[0] - nums[1]
    maps.append(r)
  ans = float('inf')
  ranges = []
  for i in range(0, len(seeds), 2):
    ranges.append(range(seeds[i], seeds[i] + seeds[i + 1]))
  ranges.sort(key=lambda r: r.start)
  for m in maps:
    ranges = m[ranges]
  print(ranges[0].start)


part1()
part2()
