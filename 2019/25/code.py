import os
os.chdir(os.path.dirname(__file__))
import sys
sys.path.append('..')
from intcode import compute
from threading import Thread
from time import sleep


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  code = list(map(int, reader()[0].split(',')))

  D = {}

  def dfs(p):
    I, O = list(map(ord, '\n'.join(p) + '\n')), []
    T = Thread(target=compute, args=(code.copy(), I, O), daemon=True)
    T.start()
    sleep(0.1)
    out = ''.join(map(chr, O)).strip()
    k = 'Command?\n\n\n\n'
    if k in out:
      out = out[out.rfind(k) + len(k):]
    out = out[out.find('==') + 3:]
    room = out[:out.find('==') - 1]
    if room in D:
      return
    items = []
    if 'Items here:' in out:
      items = out[out.find('Items here:') + 12:]
      items = items[:items.find('\n\n')]
      items = [i[2:] for i in items.splitlines()]
    D[room] = (p, items)
    dirs = out[out.find('Doors here lead:') + 17:]
    dirs = dirs[:dirs.find('\n\n')]
    dirs = [d[2:] for d in dirs.splitlines()]
    for d in dirs:
      dfs(p + [d])

  opp = {'north': 'south', 'south': 'north', 'east': 'west', 'west': 'east'}

  dfs([])

  I = {i[0]: [] for x, i in D.values() if i}

  for i in I:
    p = next(p for p, items in D.values() if items and items[0] == i)
    I[i] = p
    op = [opp[d] for d in p]
    In, O = list(map(ord,
                     f"{'\n'.join(p)}\ntake {i}\n{'\n'.join(op[::-1])}\n")), []
    T = Thread(target=compute, args=(code.copy(), In, O), daemon=True)
    T.start()
    sleep(0.2)
    out = ''.join(map(chr, O)).strip()
    if out.count('Hull Breach') != 2:
      I[i] = None

  I = {k: v for k, v in I.items() if v}

  for s in range(1 << len(I)):
    take = {p for i, p in enumerate(I) if s & (1 << i)}
    P = ''.join(f"{'\n'.join(I[t])}\ntake {t}\n{'\n'.join([opp[d]
                                                           for d in I[t]][::-1])}\n" for t in take)
    P += '\n'.join(D['Pressure-Sensitive Floor'][0]) + '\n'
    In, O = list(map(ord, P)), []
    T = Thread(target=compute, args=(code.copy(), In, O), daemon=True)
    T.start()
    sleep(1)
    out = ''.join(map(chr, O)).strip()
    if 'Alert!' not in out:
      out = out[out.rfind('typing') + 7:]
      out = out[:out.find(' ')]
      print(out)
      break

  # I, O = list(map(ord, 'west\nwest\n')), []
  # T = Thread(target=compute, args=(code, I, O), daemon=True)
  # T.start()
  # sleep(1)
  # while True:
  #   out = ''
  #   while O:
  #     out += chr(O.pop(0))
  #   print(out)
  #   i = input()
  #   I.extend(map(ord, i + '\n'))
  #   sleep(1)


def part2():
  pass


part1()
part2()
