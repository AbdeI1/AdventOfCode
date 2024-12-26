import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().split('\n')[:-1]


class Blueprint:
  def __init__(self, desc):
    self.ore = int(desc.split("ore robot costs ")[1].split(" ")[0])
    self.clay = int(desc.split("clay robot costs ")[1].split(" ")[0])
    self.obsidian = (int(desc.split("obsidian robot costs ")[1].split(" ")[
                     0]), int(desc.split("ore and ")[1].split(" ")[0]))
    self.geode = (int(desc.split("geode robot costs ")[1].split(" ")[
                  0]), int(desc.split("ore and ")[2].split(" ")[0]))

  def __str__(self):
    return f"({self.ore}, {self.clay}, {self.obsidian}, {self.geode})"


def part1():
  f = reader()
  B = []
  for l in f:
    B.append(Blueprint(l))
  ans = 0
  i = 1
  for b in B:
    MR = (4, b.obsidian[1], b.geode[1])
    MO = (16, 90, 40)
    DP = {}

    def howMany(R, O, t):
      r1, r2, r3 = R
      ore, clay, obsidian = O
      if t <= 0:
        return 0
      k = (R, O, t)
      if k in DP:
        return DP[k]
      m = 0
      ore += r1
      clay += r2
      obsidian += r3
      if r1 > MR[0] or r2 > MR[1] or r3 > MR[2]:
        return 0
      if ore > MO[0] or clay > MO[1] or obsidian > MO[2]:
        return 0
      if ore - r1 >= b.ore:
        m = max(m, howMany((r1 + 1, r2, r3), (ore - b.ore, clay, obsidian), t - 1))
      if ore - r1 >= b.clay:
        m = max(m, howMany((r1, r2 + 1, r3), (ore - b.clay, clay, obsidian), t - 1))
      if ore - r1 >= b.obsidian[0] and clay - r2 >= b.obsidian[1]:
        m = max(m, howMany((r1, r2, r3 + 1),
                (ore - b.obsidian[0], clay - b.obsidian[1], obsidian), t - 1))
      if ore - r1 >= b.geode[0] and obsidian - r3 >= b.geode[1]:
        m = max(m, howMany((r1, r2, r3),
                (ore - b.geode[0], clay, obsidian - b.geode[1]), t - 1) + t - 1)
      m = max(m, howMany((r1, r2, r3), (ore, clay, obsidian), t - 1))
      DP[k] = m
      return m
    h = howMany((1, 0, 0), (0, 0, 0), 24)
    ans += (i * h)
    i += 1
  print(ans)


def part2():
  f = reader()
  B = []
  for l in f:
    B.append(Blueprint(l))
  B = B[:3]
  ans = 1
  for b in B:
    MR = (4, b.obsidian[1], b.geode[1])
    MO = (16, 90, 40)
    DP = {}

    def howMany(R, O, t):
      r1, r2, r3 = R
      ore, clay, obsidian = O
      if t <= 0:
        return 0
      k = (R, O, t)
      if k in DP:
        return DP[k]
      m = 0
      ore += r1
      clay += r2
      obsidian += r3
      if r1 > MR[0] or r2 > MR[1] or r3 > MR[2]:
        return 0
      if ore > MO[0] or clay > MO[1] or obsidian > MO[2]:
        return 0
      if ore - r1 >= b.ore:
        m = max(m, howMany((r1 + 1, r2, r3), (ore - b.ore, clay, obsidian), t - 1))
      if ore - r1 >= b.clay:
        m = max(m, howMany((r1, r2 + 1, r3), (ore - b.clay, clay, obsidian), t - 1))
      if ore - r1 >= b.obsidian[0] and clay - r2 >= b.obsidian[1]:
        m = max(m, howMany((r1, r2, r3 + 1),
                (ore - b.obsidian[0], clay - b.obsidian[1], obsidian), t - 1))
      if ore - r1 >= b.geode[0] and obsidian - r3 >= b.geode[1]:
        m = max(m, howMany((r1, r2, r3),
                (ore - b.geode[0], clay, obsidian - b.geode[1]), t - 1) + t - 1)
      m = max(m, howMany((r1, r2, r3), (ore, clay, obsidian), t - 1))
      DP[k] = m
      return m
    h = howMany((1, 0, 0), (0, 0, 0), 32)
    ans *= h
  print(ans)


part1()
part2()
