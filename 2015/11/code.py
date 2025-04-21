import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()

# just do both parts of this problem in your head, below code might not work for all


def part1():
  s = list(map(ord, reader()[0]))
  if s[4] <= s[3] <= ord('x') and s[3] not in range(ord('i') - 2, ord('p')) and s[3:] != [s[3], s[3], s[3] + 1, s[3] + 2, s[3] + 2]:
    s[3:] = [s[3], s[3], s[3] + 1, s[3] + 2, s[3] + 2]
  elif s[4] <= s[3] <= ord('x') and s[3:] != [s[3], s[3], s[3] + 1, s[3] + 2, s[3] + 2]:
    s[3:] = [ord('p'), ord('p'), ord('q'), ord('r'), ord('r')]
  else:
    s[2:] = [s[2] + (2 if s[2] in {ord('h'), ord('k'), ord('n')}
                     else 1), ord('a'), ord('a'), ord('b'), ord('c'), ord('c')]
  print(''.join(map(chr, s)))


def part2():
  s = list(map(ord, reader()[0]))

  def f(s):
    if s[4] <= s[3] <= ord('x') and s[3] not in range(ord('i') - 2, ord('p')) and s[3:] != [s[3], s[3], s[3] + 1, s[3] + 2, s[3] + 2]:
      s[3:] = [s[3], s[3], s[3] + 1, s[3] + 2, s[3] + 2]
    elif s[4] <= s[3] <= ord('x') and s[3:] != [s[3], s[3], s[3] + 1, s[3] + 2, s[3] + 2]:
      s[3:] = [ord('p'), ord('p'), ord('q'), ord('r'), ord('r')]
    else:
      s[2:] = [s[2] + (2 if s[2] in {ord('h'), ord('k'), ord('n')}
                       else 1), ord('a'), ord('a'), ord('b'), ord('c'), ord('c')]

  f(s)
  f(s)
  print(''.join(map(chr, s)))


part1()
part2()
