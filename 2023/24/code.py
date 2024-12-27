import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


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

  def add(l1, l2):
    return [l1[i] + l2[i] for i in range(len(l1))]

  def mul(l1, s):
    return [s * l1[i] for i in range(len(l1))]

  def dot(l1, l2):
    return sum([l1[i] * l2[i] for i in range(len(l1))])

  def cross(l1, l2):
    return [l1[1] * l2[2] - l1[2] * l2[1], l1[2] *
            l2[0] - l1[0] * l2[2], l1[0] * l2[1] - l1[1] * l2[0]]

  p1, v1 = (add(f[0][0], mul(f[2][0], -1)), add(f[0][1], mul(f[2][1], -1)))
  p2, v2 = (add(f[1][0], mul(f[2][0], -1)), add(f[1][1], mul(f[2][1], -1)))

  t1 = -dot(cross(p1, p2), v2) // \
      dot(cross(v1, p2), v2)
  t2 = -dot(cross(p1, p2), v1) // \
      dot(cross(p1, v2), v1)
  c1 = add(f[0][0], mul(f[0][1], t1))
  c2 = add(f[1][0], mul(f[1][1], t2))
  p = add(c1, mul(mul(add(c2, mul(c1, -1)), 1 / (t2 - t1)), -t1))
  print(round(sum(p)))


part1()
part2()
