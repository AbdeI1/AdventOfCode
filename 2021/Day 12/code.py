def reader():
	f = open("Day12input.txt", 'r').read()
	f = f.split('\n')
	f = f[:-1]
	return f

def search1(n, d, v, p):
	if n == 'end':
		return 1
	s = 0
	for n1 in d[n]:
		if n1 == 'start':
			continue
		if n1.islower() and n1 != 'end':
			if n1 not in v:
				s += search1(n1, d, v.union({n1}), p + [n1])
		else:
			s += search1(n1, d, v, p + [n1])
	return s

def part1():
	f = reader()
	d = {}
	for l in f:
		n = l.split('-')
		if n[0] in d:
			d[n[0]].append(n[1])
		else:
			d[n[0]] = [n[1]]
		if n[1] in d:
			d[n[1]].append(n[0])
		else:
			d[n[1]] = [n[0]]
	print(search1('start', d, set(), ['start']))

def search2(n, d, v, p, b):
	if n == 'end':
		return 1
	s = 0
	for n1 in d[n]:
		if n1 == 'start':
			continue
		if n1.islower() and n1 != 'end':
			if n1 not in v:
				s += search2(n1, d, v.union({n1}), p + [n1], b)
			elif not b:
				s += search2(n1, d, v, p + [n1], True)
		else:
			s += search2(n1, d, v, p + [n1], b)
	return s

def part2():
	f = reader()
	d = {}
	for l in f:
		n = l.split('-')
		if n[0] in d:
			d[n[0]].append(n[1])
		else:
			d[n[0]] = [n[1]]
		if n[1] in d:
			d[n[1]].append(n[0])
		else:
			d[n[1]] = [n[0]]
	print(search2('start', d, set(), ['start'], False))

part1()
part2()