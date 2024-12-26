import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().split('\n')[:-1]


class Sensor:
  def __init__(self, l):
    self.pos = ((int(l.split("x=")[1].split(",")[0])), int(
      l.split("y=")[1].split(":")[0]))
    self.beacon = ((int(l.split("x=")[2].split(",")[0])), int(l.split("y=")[2]))
    self.dist = abs(self.pos[0] - self.beacon[0]) + \
        abs(self.pos[1] - self.beacon[1])

  def __str__(self):
    return f"({self.pos}, {self.beacon}, {self.dist})"


def part1():
  f = reader()
  sensors = []
  beacons = set()
  for l in f:
    sensors.append(Sensor(l))
  y = 2000000
  ranges = []
  for s in sensors:
    d = abs(s.pos[1] - y)
    beacons.add(s.beacon)
    if d < s.dist:
      diff = s.dist - d
      ranges.append((s.pos[0] - diff, s.pos[0] + diff))
  ranges.sort()
  i = 0
  while i < len(ranges) - 1:
    r1 = ranges[i]
    r2 = ranges[i + 1]
    if max(r1[0], r2[0]) <= min(r1[1], r2[1]):
      ranges[i] = (r1[0], max(r1[1], r2[1]))
      del ranges[i + 1]
    else:
      i += 1
  ans = 0
  for r in ranges:
    ans += len(range(r[0], r[1] + 1))
    for b in beacons:
      if b[0] in range(r[0], r[1] + 1) and b[1] == y:
        ans -= 1
  print(ans)


def part2():
  f = reader()
  sensors = []
  for l in f:
    sensors.append(Sensor(l))
  for y in range(0, 4000001):
    ranges = []
    for s in sensors:
      d = abs(s.pos[1] - y)
      if d < s.dist:
        diff = s.dist - d
        ranges.append((s.pos[0] - diff, s.pos[0] + diff))
    ranges.sort()
    i = 0
    while i < len(ranges) - 1:
      r1 = ranges[i]
      r2 = ranges[i + 1]
      if max(r1[0], r2[0]) <= min(r1[1], r2[1]):
        ranges[i] = (r1[0], max(r1[1], r2[1]))
        del ranges[i + 1]
      else:
        i += 1
    if len(ranges) > 1:
      print((ranges[0][1] + 1) * 4000000 + y)


part1()
part2()
