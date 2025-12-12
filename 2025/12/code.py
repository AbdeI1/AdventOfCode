import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def rotate(t):
  return tuple(''.join(t[i][-1 - j] for i in range(len(t))) for j in range(len(t[0])))


def flip(t):
  return tuple(t[i][::-1] for i in range(len(t)))

def part1():
  f = '\n'.join(reader()).split('\n\n')
  P = [tuple(p.splitlines()[1:]) for p in f[:-1]]
  G = [(lambda t: (tuple(map(int, t[0].split('x'))), tuple(map(int, t[2].split()))))(g.partition(': ')) for g in f[-1].splitlines()]
  Ps = []
  for p in P:
    s = {p}
    for _ in range(2):
      for _ in range(4):
        p = rotate(p)
        s.add(p)
      p = flip(p)
    Ps.append(s)

  Pc = []
  for p in P:
    co = 0
    for r in p:
      for c in r:
        if c == '#':
          co += 1
    Pc.append(co)

  A = 0

  for ((h, w), C) in G:
    T = 0
    for i in range(len(C)):
      T += C[i] * Pc[i]
    if T > h * w:
      continue
    if sum(C) <= (h // 3) * (w // 3):
      A += 1
      continue
    
    # here is the only part where we would actually have to sovle puzzle
    # I have no idea what to do here...
    # BUT THE INPUT DOESN'T INCLUDE ANYTHING THAT COMES HERE!! AHHHHHHHHHHHHHHH!
    # I SPENT SO MUCH TIME TRYING TO FIGURE THIS PART OUT (before writing any code) AND IT WAS SO SIMPLE ALL ALONG

  print(A)


def part2():
  pass


part1()
part2()
