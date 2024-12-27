import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  ingredients = [0] * len(f)
  allergens = [0] * len(f)
  i = 0
  while i < len(f):
    ingredients[i] = f[i].split('(')[0].split(' ')[:-1]
    allergens[i] = f[i].split("contains")[1][:-1].split(',')
    i += 1
  totalAllergens = []
  totalIngredients = []
  for a in allergens:
    for i in a:
      if i not in totalAllergens:
        totalAllergens.append(i)
  for f in ingredients:
    for i in f:
      if i not in totalIngredients:
        totalIngredients.append(i)
  total = 0
  for ingredient in totalIngredients:
    i = 0
    t = len(ingredients)
    anotin = []
    while i < len(ingredients):
      if ingredient not in ingredients[i]:
        t -= 1
        for a in allergens[i]:
          if a not in anotin:
            anotin.append(a)
      i += 1
    if len(anotin) == len(totalAllergens):
      total += t
  print(total)


def part2():
  f = reader()
  ingredients = [0] * len(f)
  allergens = [0] * len(f)
  i = 0
  while i < len(f):
    ingredients[i] = f[i].split('(')[0].split(' ')[:-1]
    allergens[i] = f[i].split("contains")[1][:-1].split(',')
    i += 1
  totalAllergens = []
  totalIngredients = []
  for a in allergens:
    for i in a:
      if i not in totalAllergens:
        totalAllergens.append(i)
  for f in ingredients:
    for i in f:
      if i not in totalIngredients:
        totalIngredients.append(i)
  actualIngredients = []
  for ingredient in totalIngredients:
    i = 0
    anotin = []
    while i < len(ingredients):
      if ingredient not in ingredients[i]:
        for a in allergens[i]:
          if a not in anotin:
            anotin.append(a)
      i += 1
    if len(anotin) != len(totalAllergens):
      actualIngredients.append(ingredient)
  d = {}
  for ingredient in actualIngredients:
    d[ingredient] = []
    i = 0
    while i < len(ingredients):
      if ingredient not in ingredients[i]:
        for a in allergens[i]:
          if a not in d[ingredient]:
            d[ingredient].append(a)
      i += 1
  for x in d:
    counter = []
    for a in totalAllergens:
      if a not in d[x]:
        counter.append(a)
    d[x] = counter
  for i in range(8):
    for x in d:
      if len(d[x]) == 1:
        i = d[x][0]
      else:
        continue
      for j in d:
        if j != x and i in d[j]:
          d[j].remove(i)
  final = ""
  for i in sorted(totalAllergens):
    for x in d:
      if d[x][0] == i:
        final += x + ','
  print(final)


part1()
part2()
