import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  result = 0
  for i in range(len(f)):
    a = f[i].split(':')
    policy = a[0]
    password = a[1][1:]
    pChar = policy[len(policy) - 1]
    pMin = int(policy[0:policy.find('-')])
    pMax = int(policy[policy.find('-') + 1: len(policy) - 2])
    count = password.count(pChar)
    if pMin <= count <= pMax:
      result = result + 1
  print(result)


def part2():
  f = reader()
  result = 0
  for i in range(len(f)):
    a = f[i].split(':')
    policy = a[0]
    password = a[1][1:]
    pChar = policy[len(policy) - 1]
    pFirst = int(policy[0:policy.find('-')]) - 1
    pSecond = int(policy[policy.find('-') + 1: len(policy) - 2]) - 1
    if bool(password[pFirst] == pChar) != bool(password[pSecond] == pChar):
      result = result + 1
  print(result)


part1()
part2()
