import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


rfields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
eyecolors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def part1():
  f = ('\n'.join(reader()) + '\n').replace(' ', '\n').split('\n')
  isValid = False
  count = 0
  a = []
  afields = []
  for str in f:
    if len(str) == 0:
      for s in a:
        afields.append(s[0:3])
      if len(a) < 7:
        isValid = False
      elif len(a) > 7:
        isValid = True
      else:
        fcount = 0
        for field in rfields:
          for f in afields:
            if f == field:
              fcount = fcount + 1
          if fcount == 7:
            isValid = True
      if isValid:
        count = count + 1
        isValid = False
      a = []
      afields = []
    else:
      a.append(str)
  print(count)


def part2():
  f = ('\n'.join(reader()) + '\n').replace(' ', '\n').split('\n')
  count = 0
  a = []
  isValid = False
  for str in f:
    if len(str) == 0:
      if len(a) < 7:
        isValid = False
      else:
        validCount = 0
        for line in a:
          if line[0:3] == "byr":
            text = line[4:]
            if 1920 <= int(text) <= 2002:
              validCount = validCount + 1
          elif line[0:3] == "iyr":
            text = line[4:]
            if 2010 <= int(text) <= 2020:
              validCount = validCount + 1
          elif line[0:3] == "eyr":
            text = line[4:]
            if 2020 <= int(text) <= 2030:
              validCount = validCount + 1
          elif line[0:3] == "hgt":
            text = line[4:]
            if len(text) > 2:
              if text[len(text) - 2: len(text)] == "in":
                if 59 <= int(text[:len(text) - 2]) <= 76:
                  validCount = validCount + 1
              elif text[len(text) - 2: len(text)] == "cm":
                if 150 <= int(text[:len(text) - 2]) <= 193:
                  validCount = validCount + 1
          elif line[0:3] == "hcl":
            text = line[4:]
            if text[0] == '#':
              color = text[1:]
              if len(color) == 6:
                try:
                  x = int(color, 16)
                except ValueError:
                  continue
                validCount = validCount + 1
          elif line[0:3] == "ecl":
            text = line[4:]
            if len(text) == 3:
              for color in eyecolors:
                if text == color:
                  validCount = validCount + 1
          elif line[0:3] == "pid":
            text = line[4:]
            if len(text) == 9:
              try:
                x = int(text)
              except ValueError:
                continue
              validCount = validCount + 1
        if validCount == 7:
          isValid = True
      if isValid:
        count = count + 1
        isValid = False
      a = []
      afields = []
    else:
      a.append(str)
  print(count)


part1()
part2()
