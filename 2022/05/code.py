import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = '\n'.join(reader()).split('\n\n')
  stacks = [[] for _ in range(9)]
  i = 1
  st = f[0].split('\n')
  for j in range(9):
    r = 7
    while r >= 0 and st[r][i] != ' ':
      stacks[j].append(st[r][i])
      r -= 1
    i += 4
  ins = f[1].split('\n')
  for l in ins:
    st = l.split(' ')
    n1 = int(st[1])
    n2 = int(st[3]) - 1
    n3 = int(st[5]) - 1
    for _ in range(n1):
      c = stacks[n2].pop()
      stacks[n3].append(c)
  ans = ""
  for i in range(9):
    ans += stacks[i].pop()
  print(ans)


def part2():
  f = '\n'.join(reader()).split('\n\n')
  stacks = [[] for _ in range(9)]
  i = 1
  st = f[0].split('\n')
  for j in range(9):
    r = 7
    while r >= 0 and st[r][i] != ' ':
      stacks[j].append(st[r][i])
      r -= 1
    i += 4
  ins = f[1].split('\n')
  for l in ins:
    st = l.split(' ')
    n1 = int(st[1])
    n2 = int(st[3]) - 1
    n3 = int(st[5]) - 1
    a = []
    for _ in range(n1):
      c = stacks[n2].pop()
      a.append(c)
    for i in range(len(a)):
      stacks[n3].append(a[len(a) - i - 1])
  ans = ""
  for i in range(9):
    ans += stacks[i].pop()
  print(ans)


part1()
part2()
