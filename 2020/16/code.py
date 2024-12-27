import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  rules = f[0:20]
  tickets = f[f.index("nearby tickets:") + 1:]
  srules = []
  for rule in rules:
    srules.append(((int(rule[rule.index(':') + 2: rule.index('-')]), int(rule[rule.index('-') + 1: rule.index(
      " or ")])), (int(rule.split(" or ")[1].split('-')[0]), int(rule.split(" or ")[1].split('-')[1]))))
  sum = 0
  for ticket in tickets:
    values = ticket.split(',')
    for value in values:
      isLegal = False
      for r in srules:
        if r[0][0] <= int(value) <= r[0][1] or r[1][0] <= int(value) <= r[1][1]:
          isLegal = True
      if not isLegal:
        sum += int(value)
  print(sum)


def part2():
  f = reader()
  rules = f[0:20]
  tickets = f[f.index("nearby tickets:") + 1:]
  srules = []
  for rule in rules:
    srules.append(((int(rule[rule.index(':') + 2: rule.index('-')]), int(rule[rule.index('-') + 1: rule.index(
      " or ")])), (int(rule.split(" or ")[1].split('-')[0]), int(rule.split(" or ")[1].split('-')[1]))))
  invalidTickets = []
  i = 0
  while i < len(tickets):
    ticket = tickets[i]
    values = ticket.split(',')
    for value in values:
      isLegal = False
      for r in srules:
        if r[0][0] <= int(value) <= r[0][1] or r[1][0] <= int(value) <= r[1][1]:
          isLegal = True
      if not isLegal:
        if not i in invalidTickets:
          invalidTickets.append(i)
    i += 1
  newTickets = []
  i = 0
  while i < len(tickets):
    if i not in invalidTickets:
      newTickets.append(tickets[i])
    i += 1
  newTickets.append(f[22])
  columns = []
  i = 0
  while i < 20:
    possibleRules = [0, 1, 2, 3, 4, 5, 6, 7, 8,
                     9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    j = 0
    while j < 20:
      rule = srules[j]
      for ticket in newTickets:
        value = int(ticket.split(',')[i])
        if not (rule[0][0] <= value <= rule[0][1] or rule[1][0] <= value <= rule[1][1]):
          possibleRules[j] = -1
          break
      j += 1
    columns.append(possibleRules)
    i += 1
  i = 0
  while i < len(columns):
    new = []
    j = 0
    while j < len(columns[i]):
      if columns[i][j] != -1:
        new.append(columns[i][j])
      j += 1
    columns[i] = new
    i += 1
  cRule = [-1] * 20
  i = 0
  length = 1
  while i < len(columns):
    if len(columns[i]) == length:
      j = 0
      while j < length:
        if columns[i][j] not in cRule:
          cRule[i] = columns[i][j]
        j += 1
      length += 1
      i = -1
    i += 1
  product = 1
  myTicket = f[22].split(',')
  i = 0
  while i < 6:
    product *= int(myTicket[cRule.index(i)])
    i += 1
  print(product)


part1()
part2()
