import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


class Group:
  def __init__(self, s: str, t: int, i: int):
    l = s.split()
    self.team = t
    self.id = i
    self.units = int(l[0])
    self.hp = int(l[4])
    self.weak = set()
    i = l.index("weak") if "weak" in l else l.index(
      "(weak") if "(weak" in l else -1
    if i > -1:
      i += 2
      while l[i][-1] not in ";)":
        self.weak.add(l[i][:-1])
        i += 1
      self.weak.add(l[i][:-1])
    self.immune = set()
    i = l.index("immune") if "immune" in l else l.index(
      "(immune") if "(immune" in l else -1
    if i > -1:
      i += 2
      while l[i][-1] not in ";)":
        self.immune.add(l[i][:-1])
        i += 1
      self.immune.add(l[i][:-1])
    self.damage = int(l[-6])
    self.dtype = l[-5]
    self.initiative = int(l[-1])

  def __repr__(self):
    return f"{[self.team, self.id, self.units, self.hp, self.weak, self.immune, self.damage, self.dtype, self.initiative]}"

  def __eq__(self, other):
    if not isinstance(other, Group):
      return NotImplemented
    return f"{self}" == f"{other}"

  def effective_power(self):
    return self.units * self.damage


def part1():
  f = '\n'.join(reader()).split('\n\n')
  A = [Group(s, 0, i) for i, s in enumerate(f[0].splitlines()[1:])], [
      Group(s, 1, i) for i, s in enumerate(f[1].splitlines()[1:])]

  def fight(A):
    def k(g): return (-g.effective_power(), -g.initiative)

    T = sorted(A[0] + A[1], key=k)
    S = set()
    Ts = {}
    for t in T:
      D = t.effective_power()
      target = 0, None
      for e in sorted(A[1 - t.team], key=k):
        if (e.team, e.id) in S:
          continue
        d = 0 if t.dtype in e.immune else D * 2 if t.dtype in e.weak else D
        if d > target[0]:
          target = d, e
      Ts[(t.team, t.id)] = target
      if target[1]:
        S.add((target[1].team, target[1].id))

    for t in sorted(A[0] + A[1], key=lambda g: -g.initiative):
      if t.units <= 0:
        continue
      _, e = Ts[(t.team, t.id)]
      if not e:
        continue
      D = t.effective_power()
      d = 0 if t.dtype in e.immune else D * 2 if t.dtype in e.weak else D
      e.units -= (d // e.hp)

    A = list(filter(lambda g: g.units > 0, A[0])), list(
      filter(lambda g: g.units > 0, A[1]))

    return A

  while len(A[0]) > 0 and len(A[1]) > 0:
    A = fight(A)

  print(sum(sum(g.units for g in a) for a in A))


def part2():
  f = '\n'.join(reader()).split('\n\n')

  def test(B):
    A = [Group(s, 0, i) for i, s in enumerate(f[0].splitlines()[1:])], [
        Group(s, 1, i) for i, s in enumerate(f[1].splitlines()[1:])]
    for a in A[0]:
      a.damage += B

    def fight(A):
      def k(g): return (-g.effective_power(), -g.initiative)

      T = sorted(A[0] + A[1], key=k)
      S = set()
      Ts = {}
      for t in T:
        D = t.effective_power()
        target = 0, None
        for e in sorted(A[1 - t.team], key=k):
          if (e.team, e.id) in S:
            continue
          d = 0 if t.dtype in e.immune else D * 2 if t.dtype in e.weak else D
          if d > target[0]:
            target = d, e
        Ts[(t.team, t.id)] = target
        if target[1]:
          S.add((target[1].team, target[1].id))

      for t in sorted(A[0] + A[1], key=lambda g: -g.initiative):
        if t.units <= 0:
          continue
        _, e = Ts[(t.team, t.id)]
        if not e:
          continue
        D = t.effective_power()
        d = 0 if t.dtype in e.immune else D * 2 if t.dtype in e.weak else D
        e.units -= (d // e.hp)

      A = list(filter(lambda g: g.units > 0, A[0])), list(
        filter(lambda g: g.units > 0, A[1]))

      return A

    while len(A[0]) > 0 and len(A[1]) > 0:
      s = f"{A}"
      An = fight(A)
      if s == f"{A}":
        return ([], [])
      A = An

    return A

  b = 1 << 11
  s = b >> 1

  while s > 0:
    if len(test(b)[0]) == 0:
      b += s
    else:
      b -= s
    s >>= 1
  if len(test(b)[0]) == 0: b += 1

  A = test(b)
  print(sum(sum(g.units for g in a) for a in A))


part1()
part2()
