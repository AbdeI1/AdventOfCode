import os
os.chdir(os.path.dirname(__file__))


def reader():
  return open(f"input.txt", 'r').read().splitlines()


def part1():
  f = reader()
  steps = [[[0] * 2 for _ in range(3)] for _ in range(len(f))]
  power = [False] * len(f)
  for i in range(len(f)):
    l = f[i]
    if l[1] == 'n':
      power[i] = True
    xs = l[l.index('x') + 2:l.index(',')].split('..')
    steps[i][0][0] = int(xs[0])
    steps[i][0][1] = int(xs[1])
    l = l[l.index(',') + 1:]
    ys = l[l.index('y') + 2:l.index(',')].split('..')
    steps[i][1][0] = int(ys[0])
    steps[i][1][1] = int(ys[1])
    l = l[l.index(',') + 1:]
    zs = l[l.index('z') + 2:].split('..')
    steps[i][2][0] = int(zs[0])
    steps[i][2][1] = int(zs[1])
  reactor = [[[False] * 101 for _ in range(101)] for _ in range(101)]
  for i in range(len(steps)):
    step = steps[i]
    for x in range(101):
      for y in range(101):
        for z in range(101):
          if step[0][0] + 50 <= x and x <= step[0][1] + 50 and step[1][0] + 50 <= y and y <= step[1][1] + 50 and step[2][0] + 50 <= z and z <= step[2][1] + 50:
            reactor[x][y][z] = power[i]
  count = 0
  for x in range(101):
    for y in range(101):
      for z in range(101):
        if reactor[x][y][z]:
          count += 1
  print(count)


def intersect(cube1, cube2):
  if cube1[0][0] <= cube2[0][1] and cube1[0][1] >= cube2[0][0] and cube1[1][0] <= cube2[1][1] and cube1[1][1] >= cube2[1][0] and cube1[2][0] <= cube2[2][1] and cube1[2][1] >= cube2[2][0]:
    xs = (max(cube1[0][0], cube2[0][0]), min(cube1[0][1], cube2[0][1]))
    ys = (max(cube1[1][0], cube2[1][0]), min(cube1[1][1], cube2[1][1]))
    zs = (max(cube1[2][0], cube2[2][0]), min(cube1[2][1], cube2[2][1]))
    return (True, (xs, ys, zs))
  return (False, ((1, 0), (1, 0), (1, 0)))


def part2():
  f = reader()
  steps = [[[0] * 2 for _ in range(3)] for _ in range(len(f))]
  power = [False] * len(f)
  for i in range(len(f)):
    l = f[i]
    if l[1] == 'n':
      power[i] = True
    xs = l[l.index('x') + 2:l.index(',')].split('..')
    steps[i][0][0] = int(xs[0])
    steps[i][0][1] = int(xs[1])
    l = l[l.index(',') + 1:]
    ys = l[l.index('y') + 2:l.index(',')].split('..')
    steps[i][1][0] = int(ys[0])
    steps[i][1][1] = int(ys[1])
    l = l[l.index(',') + 1:]
    zs = l[l.index('z') + 2:].split('..')
    steps[i][2][0] = int(zs[0])
    steps[i][2][1] = int(zs[1])
  regions = []
  signs = []
  for i in range(len(steps)):
    step = steps[i]
    xs = step[0]
    ys = step[1]
    zs = step[2]
    if power[i]:
      regions.append(((xs[0], xs[1]), (ys[0], ys[1]), (zs[0], zs[1])))
      signs.append(1)
    cur = ((xs[0], xs[1]), (ys[0], ys[1]), (zs[0], zs[1]))
    for j in range(len(regions) - (1 if power[i] else 0)):
      (b, r) = intersect(cur, regions[j])
      if b:
        regions.append(r)
        signs.append(-signs[j])
  total = 0
  for i in range(len(regions)):
    r = regions[i]
    xs = r[0]
    ys = r[1]
    zs = r[2]
    total += (xs[1] - xs[0] + 1) * (ys[1] - ys[0] + 1) * \
        (zs[1] - zs[0] + 1) * signs[i]
  print(total)


# part1()
part2()


# al = [[], [], []]
# for j in range(3):
# 	for i in range(len(steps)):
# 		step = steps[i]
# 		xr = step[j]
# 		xl = al[j]
# 		if power[i]:
# 			start = 0
# 			while start < len(xl) and xl[start] < xr[0]:
# 				start += 1
# 			end = 0
# 			while end < len(xl) and xl[end] < xr[1]:
# 				end += 1
# 			if start == end:
# 				if start % 2 == 0:
# 					xl = xl[:start] + [xr[0], xr[1]] + xl[end:]
# 			else:
# 				if start % 2 == 0:
# 					xl[start] = xr[0]
# 					start += 1
# 				if end % 2 == 0:
# 					xl[end-1] = xr[1]
# 					end -= 1
# 				if end > start:
# 					xl = xl[:start] + xl[end:]
# 		else:
# 			start = 0
# 			while start < len(xl) and xl[start] < xr[0]:
# 				start += 1
# 			end = 0
# 			while end < len(xl) and xl[end] < xr[1]:
# 				end += 1
# 			if start == end:
# 				if start % 2 == 1:
# 					xl = xl[:start] + [xr[0]-1, xr[1]+1] + xl[end:]
# 			else:
# 				if start % 2 == 1:
# 					xl[start] = xr[0]-1
# 					start += 1
# 				if end % 2 == 1:
# 					xl[end-1] = xr[1]+1
# 					end -= 1
# 				if end > start:
# 					xl = xl[:start] + xl[end:]
# 		al[j] = xl
# counts = [0,0,0]
# for i in range(3):
# 	j = 0
# 	while j < len(al[i]):
# 		counts[i] += (al[i][j+1] - al[i][j] + 1)
# 		j += 2
# print(counts[0]*counts[1]*counts[2])
