import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  cardKey, doorKey = map(int, reader())
  subjectNum = 7
  value = 1
  cardLoop = 0
  while True:
    if value == cardKey:
      break
    value = value * subjectNum
    value = value % 20201227
    cardLoop += 1
  value = 1
  subjectNum = doorKey
  for i in range(cardLoop):
    value = value * subjectNum
    value = value % 20201227
  print(value)


part1()
