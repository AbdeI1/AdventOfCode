import pathlib

def reader():
  f = open(f"{pathlib.Path(__file__).parent.resolve()}/input.txt", 'r').read()
  f = f.split('\n')
  f = f[:-1]
  return f

def part1():
  f = reader()
  ans = 0
  for l in f:
    p1, p2 = l.split(": ")
    ID = int(p1[p1.find(" "):])
    pulls = list(map(lambda l: l.split(", "), p2.split("; ")))
    for p in pulls:
      for c in p:
        num, col = c.split(" ")
        num = int(num)
        match col:
          case 'red':
            if num > 12: break
          case 'green':
            if num > 13: break
          case 'blue':
            if num > 14: break
      else:
        continue
      break
    else:
      ans += ID
  print(ans)

def part2():
  f = reader()
  ans = 0
  for l in f:
    p1, p2 = l.split(": ")
    ID = int(p1[p1.find(" "):])
    pulls = list(map(lambda l: l.split(", "), p2.split("; ")))
    mins = [0, 0, 0]
    for p in pulls:
      for c in p:
        num, col = c.split(" ")
        num = int(num)
        match col:
          case 'red': mins[0] = max(mins[0], num)
          case 'green': mins[1] = max(mins[1], num)
          case 'blue': mins[2] = max(mins[2], num)
    ans += mins[0] * mins[1] * mins[2]
  print(ans)

part1()
part2()
