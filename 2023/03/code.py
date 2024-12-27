import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = list(map(list, reader()))
  ans = 0
  for i in range(len(f)):
    for j in range(len(f[i])):
      if f[i][j] != '.' and not f[i][j].isdigit():
        for D in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
          if f[i + D[0]][j + D[1]].isdigit():
            s, e = j + D[1], j + D[1]
            while s >= 0 and f[i + D[0]][s].isdigit():
              s -= 1
            s += 1
            while e < len(f[i + D[0]]) and f[i + D[0]][e].isdigit():
              e += 1
            num = int(''.join(f[i + D[0]][s:e]))
            for k in range(s, e):
              f[i + D[0]][k] = '.'
            ans += num
  print(ans)


def part2():
  f = list(map(list, reader()))
  ans = 0
  for i in range(len(f)):
    for j in range(len(f[i])):
      if f[i][j] == '*':
        nums = []
        for D in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
          if f[i + D[0]][j + D[1]].isdigit():
            s, e = j + D[1], j + D[1]
            while s >= 0 and f[i + D[0]][s].isdigit():
              s -= 1
            s += 1
            while e < len(f[i + D[0]]) and f[i + D[0]][e].isdigit():
              e += 1
            num = int(''.join(f[i + D[0]][s:e]))
            for k in range(s, e):
              f[i + D[0]][k] = '.'
            nums.append(num)
        if len(nums) == 2:
          ans += nums[0] * nums[1]
  print(ans)


part1()
part2()
