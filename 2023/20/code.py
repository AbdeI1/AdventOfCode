import os
os.chdir(os.path.dirname(__file__))
from math import lcm


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  flip = {s[1:s.find(' ')]: 0 for s in f if s[0] == '%'}
  con = {s[1:s.find(' ')]: {} for s in f if s[0] == '&'}
  modules = {}
  for s in f:
    inp, out = s.split(' -> ')
    inp = inp[1:] if inp != "broadcaster" else inp
    out = out.split(', ')
    modules[inp] = out
    for o in out:
      if o in con:
        con[o][inp] = 0

  def pressButton():
    q = [('broadcaster', '', 0)]
    pulses = [0, 0]
    while q:
      m, s, p = q.pop(0)
      pulses[p] += 1
      if m == 'output':
        continue
      if m == 'broadcaster':
        for o in modules[m]:
          q.append((o, m, p))
      elif m in con:
        con[m][s] = p
        if all(con[m].values()):
          for o in modules[m]:
            q.append((o, m, 0))
        else:
          for o in modules[m]:
            q.append((o, m, 1))
      elif p == 0:
        flip[m] = 1 if flip[m] == 0 else 0
        for o in modules[m]:
          q.append((o, m, flip[m]))
    return pulses

  totalPulses = [0, 0]
  for _ in range(1000):
    lp, hp = pressButton()
    totalPulses[0] += lp
    totalPulses[1] += hp

  print(totalPulses[0] * totalPulses[1])


def part2():
  f = reader()
  flip = {s[1:s.find(' ')]: 0 for s in f if s[0] == '%'}
  con = {s[1:s.find(' ')]: {} for s in f if s[0] == '&'}
  modules = {}
  parent = ''
  for s in f:
    inp, out = s.split(' -> ')
    inp = inp[1:] if inp != "broadcaster" else inp
    if out == 'rx':
      parent = inp
    out = out.split(', ')
    modules[inp] = out
    for o in out:
      if o in con:
        con[o][inp] = 0

  pat = {m: '' for m in modules}

  def pressButton():
    q = [('broadcaster', '', 0)]
    pulses = [0, 0]
    while q:
      m, s, p = q.pop(0)
      if s in pat:
        pat[s] += str(p)
      if m == 'rx' or m == 'output':
        pulses[p] += 1
        continue
      if m == 'broadcaster':
        for o in modules[m]:
          q.append((o, m, p))
      elif m in con:
        con[m][s] = p
        if all(con[m].values()):
          for o in modules[m]:
            q.append((o, m, 0))
        else:
          for o in modules[m]:
            q.append((o, m, 1))
      elif p == 0:
        flip[m] = 1 if flip[m] == 0 else 0
        for o in modules[m]:
          q.append((o, m, flip[m]))
    return pulses

  frq = {'broadcaster': 1}
  for i in range(1, 4002):
    lp, hp = pressButton()
    for m in modules:
      if pat[m] and pat[m].find('1' if pat[m][0] == '0' else '0') >= 0 and m not in frq:
        frq[m] = i

  if parent not in frq:
    frq[parent] = lcm(*[frq[c] for c in con[parent]])
  print(frq[parent])


part1()
part2()
