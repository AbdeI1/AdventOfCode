def reader():
	f = open("Day5input.txt", 'r').read()
	f = f.split('\n')
	f = f[:-1]
	return f

def part1():
	f = reader()
	d = {}
	for l in f:
		ps = l.split(' -> ')
		p1 = list(map(int, ps[0].split(',')))
		p2 = list(map(int, ps[1].split(',')))
		if p1[0] == p2[0]:
			i = p1[0]
			for j in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1):
				d[(i,j)] = 2 if (i,j) in d else 1
		elif p1[1] == p2[1]:
			j = p1[1]
			for i in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):
				d[(i,j)] = 2 if (i,j) in d else 1
	count = 0
	for di in d:
		if d[di] != 1:
			count += 1
	print(count)


def part2():
	f = reader()
	d = {}
	for l in f:
		ps = l.split(' -> ')
		p1 = list(map(int, ps[0].split(',')))
		p2 = list(map(int, ps[1].split(',')))
		if p1[0] == p2[0]:
			i = p1[0]
			for j in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1):
				d[(i,j)] = 2 if (i,j) in d else 1
		else:
			slope = (p1[1]-p2[1])/(p1[0]-p2[0])
			j = p1[1] if p1[0] < p2[0] else p2[1]
			for i in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):
				d[(i,j)] = 2 if (i,j) in d else 1
				j += slope
	count = 0
	for di in d:
		if d[di] != 1:
			count += 1
	print(count)

part1()
part2()
