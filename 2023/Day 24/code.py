import pathlib


def reader():
  f = open(f"{pathlib.Path(__file__).parent.resolve()}/input.txt", 'r').read()
  f = f.split('\n')
  f = f[:-1]
  return f


def part1():
  f = [tuple(map(eval, s.split(' @ '))) for s in reader()]
  area = [200000000000000, 400000000000000]
  ans = 0
  for i in range(len(f)):
    p1, v1 = f[i]
    l1 = [-v1[1], v1[0], v1[1] * p1[0] - v1[0] * p1[1]]
    for j in range(i + 1, len(f)):
      p2, v2 = f[j]
      l2 = [-v2[1], v2[0], v2[1] * p2[0] - v2[0] * p2[1]]
      cross = [l1[1] * l2[2] - l1[2] * l2[1], l1[2] *
               l2[0] - l1[0] * l2[2], l1[0] * l2[1] - l1[1] * l2[0]]
      if cross[2] != 0:
        x, y = cross[0] / cross[2], cross[1] / cross[2]
        if x >= area[0] and x <= area[1] and y >= area[0] and y <= area[1]:
          t1 = (x - p1[0]) / v1[0]
          t2 = (x - p2[0]) / v2[0]
          if t1 >= 0 and t2 >= 0:
            ans += 1
  print(ans)


def part2():
  f = [tuple(map(eval, s.split(' @ '))) for s in reader()]
  for i in range(len(f)):
    p1, v1 = f[i]
    l1 = [-v1[1], v1[0], v1[1] * p1[0] - v1[0] * p1[1]]
    for j in range(i + 1, len(f)):
      p2, v2 = f[j]
      l2 = [-v2[1], v2[0], v2[1] * p2[0] - v2[0] * p2[1]]
      cross = [l1[1] * l2[2] - l1[2] * l2[1], l1[2] *
               l2[0] - l1[0] * l2[2], l1[0] * l2[1] - l1[1] * l2[0]]
      if cross[2] != 0:
        x, y = cross[0] / cross[2], cross[1] / cross[2]
        ans += 1
  print(ans)


part1()
part2()
